---
layout: page
title: "Part 2 — 200 OK, and Nothing Was Created"
---

# Part 2 — 200 OK, and nothing was created

*Series: Homelab Automation Skills.*

{% include homelab-disclaimer.html %}

Part 1 was about tools that cannot reach: no Terraform resource for vCenter, a
provider that connects too early, a resource that plans cleanly and never works,
a summit that is not a vSphere object at all. Four tools, four kinds of gap.

Those are the comfortable failures. They announce themselves.

This part is about the other kind — where the tool reaches fine, the call
succeeds, the apply is green, and nothing you asked for exists. The skill cannot
warn you off a tool here, because the tool is working. It has to teach you what
to go and look at instead.

> **If you don't do this for a living.** When software asks another system to do
> something, it gets a reply — usually a number meaning "fine" or "not fine."
> This post is about four situations where the reply was "fine" and the work had
> not been done. The reply was not a lie: each system answered a narrower
> question than the one I thought I was asking.

---

## Why this happens at all, and why it is not a bug

A modern infrastructure API almost never does the work while you wait. You send
a request; it records what you want and returns. Something else makes it true,
afterwards, somewhere you are not looking.

So there are two separate facts in play — **what you asked for** and **what is
actually running** — and the response you get describes the first one.

NSX is unusually honest about this, in that it will show you both if you ask:

```
policy   /policy/api/v1/infra/ip-pools/<id>/ip-subnets   <- what I declared
realized /api/v1/pools/ip-pools/<id>                     <- what exists
```

Two URLs, two answers, and they are allowed to disagree indefinitely. Most
systems have the same split and only expose one side of it.

Once you see that, the four failures below stop looking like four bugs and start
looking like one shape with four edges.

| # | Category | The reply means | Instance |
|---|---|---|---|
| 1 | Accepted is not realized | "I recorded your intent" | NSX IP pool |
| 2 | Created is not working | "The object exists" | NSX Edge transport node |
| 3 | Stuck is not slow | "Still in progress" | NSX-to-vCenter sync record |
| 4 | The record outlived the thing | "State says it exists" | Terraform state, post-rebuild |

---

## 1. Accepted is not realized

The lab's NSX tunnel endpoints draw from a small pool, `.30–.39`. One of those
addresses collided with something the router had already handed out, so the
obvious fix was to shrink the pool to `.33–.39` and move on.

Terraform agreed. Clean in-place update. **0 to destroy.** No warning, no retry,
no sign of trouble.

The pool never changed:

```
policy   /policy/api/v1/infra/ip-pools/<id>/ip-subnets  -> .33-.39
realized /api/v1/pools/ip-pools/<id>                    -> .30-.39
```

NSX will not realize a range that excludes an address it has already allocated.
It accepted the intent, failed to apply it, recorded `consolidated_status =
ERROR` on the policy object — and told nobody. Terraform asked whether the
intent matched what was declared. It did. Green.

The actual fix was not in NSX at all: move the *host* via a DHCP reservation, so
the existing allocation becomes valid again. Zero NSX changes. The pool was
never the problem; it was just the thing I could see.

> **In plain terms.** You file a change request and the clerk stamps it
> RECEIVED. The stamp is honest — they genuinely received it. Whether anyone
> acts on it is a different question, tracked on a different form, and nobody
> posts you the rejection.
>
> This category is dangerous because **your automation is checking the stamp.**
> It compares what you asked for against what is on file, and both agree. Being
> declarative is not the same as being true, and the tool is only ever reading
> one of the two.

## 2. Created is not working

The NSX Edge is deployed by NSX itself: Terraform registers a transport node,
NSX deploys the appliance into vSphere. That registration takes vSphere object
IDs — a cluster, a datastore, a host, a network.

After a vCenter rebuild, those IDs pointed at objects that no longer existed.

The transport node **registered successfully**. The API object is real; you can
fetch it. In the background, the OVF deploy failed immediately, against a
cluster reference that was meaningless.

Nothing said so. The failure surfaced later, on a *different resource*:

```
Error: Failed to create Edge Cluster ... Edge node ... has config status 'PENDING'
```

Which reads exactly like "still booting, give it a minute" — and the module's
own inline comment said as much. It is not. The real message was one API call
away, on the object itself:

```
GET /api/v1/transport-nodes/<id>/state

VM_DEPLOYMENT_FAILED
Ovf deploy for vm nsx-edge-01 failed ... Compute id doesnt exist :
The object 'vim.ClusterComputeResource:domain-c10' has already been deleted
or has not been completely created
```

> **In plain terms.** The delivery is marked complete because the van left the
> depot. Whether the parcel arrived is recorded somewhere else — and when it
> doesn't, the complaint comes in about a different order entirely.
>
> This category costs the most, for two compounding reasons: **the error is
> delayed, and it arrives attached to the wrong thing.** You debug the resource
> that reported the problem, which is genuinely fine, while the broken one sits
> quietly upstream reporting success.

## 3. Stuck is not slow

Supervisor enablement kept failing on a requirement I could not satisfy:
`vcenter.wcp.service.cidr.required`. A service CIDR, apparently missing. I was
passing one.

So I went looking for the right field name, properly rather than by guesswork.
I read `govmomi`'s own wire-format structs — the bindings vCenter's own tooling
uses. Then I pulled a complete, pre-indexed OpenAPI spec for vCenter 9.1 and
checked every candidate schema exhaustively: `Workloads`, `WorkloadNetwork`,
`VpcNetwork`. All three matched the bindings exactly.

**There was no service CIDR field.** Not misspelled, not nested somewhere
unexpected, not missing from the docs — not reachable from that request at all.

That result is worth sitting with, because it is the opposite of the usual
lesson. Reading the source instead of the documentation is the technique that
solved most of Part 1. Here I did it thoroughly, and it was still the wrong
question. The request shape was never the problem.

The answer was in runtime state. NSX keeps an internal record for syncing a
Transit Gateway into vCenter's namespace-management layer, and that record said:

```
RealizedTgwObject
  runtime_status  : IN_PROGRESS
  publish_status  : UNINITIALIZED
  _last_modified_time : unchanged across a 20-second poll
```

`IN_PROGRESS` reads as "working on it." It had not moved. It was not converging
slowly; it was stuck — plausibly left dangling by one of the earlier interrupted
enable attempts in that same debugging session.

vCenter derives the CIDR data it wants from that sync. The sync never completed,
so the data was never populated, and the enable call reported it the only way it
knew how: as a missing requirement. The error named a **field**. The cause was
**state**.

> **In plain terms.** A tracking page that has said "in progress" since Tuesday
> is not telling you it is nearly done. It is telling you nobody has updated it.
> The two look identical until you check the timestamp.
>
> This category is nasty because **the misleading status is on a different
> object than the error.** The thing that failed reported a plausible problem
> with your input; the thing that was actually broken reported a reassuring
> word. And "in progress" is the single most expensive status in
> infrastructure, because it is the one that makes waiting feel like
> diagnosis.

## 4. The record outlived the thing

vCenter was rebuilt — not upgraded, replaced. Terraform did not know that.

Its state file still described a module's worth of resources, tracked against a
vCenter instance that no longer existed. The old NSX Manager and Edge addresses
returned nothing at all — not a timeout, nothing. The infrastructure was
genuinely gone. The record was intact, detailed and completely wrong.

What makes this worth a section rather than a footnote is how differently two
resource types in the *same provider* handled the identical staleness:

- `vsphere_virtual_machine` noticed the object had vanished and planned a
  recreate — *"Objects have changed outside of Terraform."* Graceful, correct,
  and easy to accept without thinking.
- `vsphere_folder` threw a hard error and blocked the entire plan:
  `cannot locate folder: ServerFaultCode: ... has already been deleted or has
  not been completely created`.

Same cause. One looks like normal drift. The other looks like a broken config.
Neither says "your state predates a rebuild."

The fix was `terraform state rm`, not `terraform destroy`. There was nothing
left to destroy, and asking Terraform to try would have meant waiting on
endpoints that no longer answer.

> **In plain terms.** The inventory system says the warehouse holds four
> pallets. The warehouse burned down last month. Every query you run against
> the inventory is fast, confident and internally consistent — because it is
> answering from the record, which is the only thing it has.
>
> Automation is especially exposed here, because **a state file is a cache of
> the world, and nothing invalidates it when the world is replaced.** The
> practical rule that came out of it: after any rebuild of a platform other
> resources depend on, a `plan` against an existing module is the real test —
> and a hard refresh error, not just "will be created," is the signal there are
> more of these to find.

## What went into the skill

Not the four stories. A change to what a verification step is allowed to be.

Every stage gate in this build now names **an object and a state**, never a
command and an exit code:

```
Stage 2    GET /policy/api/v1/infra/tier-0s/<id>/static-routes  ->  result_count: 1
Stage 2    realized pool  /api/v1/pools/ip-pools/<id>  ->  matches the declared range
Stage 2.5  host transport node  ->  state = success, AND a TEP IP assigned
```

Each exists because the corresponding step once reported success while being
untrue. "Terraform applied cleanly" is not in that list, and cannot be, because
every failure above happened on a clean apply.

There is a fourth that is a habit rather than a line of output: after any
rebuild of something other resources depend on, run a `plan` against an
existing module *before* trusting the state file. A hard refresh error is the
signal; "will be created" on something you know exists is the quieter one.

The second thing the skill records is which greens are worthless. An entry that
says *this tool returns success for the request, not the result* is worth more
than another procedure step — it tells you where not to spend your trust. A
runbook has nowhere to put that, because a procedure step reads as equally
trustworthy whether or not anyone has checked.

> **In plain terms.** The instinct is to write down *what to do*. What actually
> prevents this class of problem is writing down *what to go and look at
> afterwards, and what the answer should be* — which is more work, less
> satisfying, and the part everyone skips.

## What's next

Four categories, one underlying split: what you asked for, and what is actually
running. Everything here came from trusting the first as though it were the
second.

So far the consequences have been wasted days. Coming up, they get more
expensive: a deployment that destroyed more than it built, and said so in the
plan output in a way I nearly missed; a host I bricked by acting on a theory I
had not tested; and the point where the real constraint on the lab turned out
not to be CPU, RAM, or any provider at all, but temperature.

The thread is getting harder to ignore: **check the object, not the exit code.**

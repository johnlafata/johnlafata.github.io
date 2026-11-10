---
layout: page
title: "Part 6 — Nothing to Store It On"
published: false
---

# Part 6 — Nothing to store it on

*Series: Homelab Automation Skills.*

{% include homelab-disclaimer.html %}

> **DRAFT — `published: false`.** Flip the flag in the front matter when
> this is ready to go live.

A registry would not install. Its four storage claims sat pending until the
deployment timed out, which is an ordinary enough Tuesday.

What that turned out to mean was that **no persistent storage had ever been
created on this platform.** Not once, in its entire life. The Supervisor had
enabled cleanly, passed every gate, run applications and served traffic for
days, and could not have stored a byte if anything had asked.

Nothing had asked. That is the whole problem.

> **If you don't do this for a living.** Some software needs to remember things
> between restarts — a database, a registry, a backup. That requires the
> platform to hand it a piece of disk. This platform could not, had never been
> able to, and reported itself healthy throughout, because nothing had
> requested disk yet and so nothing had failed.

---

## The error, and three layers of lying

```
failed to provision volume with StorageClass "...":
  InvalidArgument{ InvalidProperty: "createSpecs.profile" }
  "A specified parameter was not correct: createSpecs.profile"
```

`createSpecs.profile` is the storage policy. So I spent a long time proving the
storage policy was fine — which it was, in increasingly specific ways: the
policy ID existed, it resolved to real datastores, the per-host variant
correctly narrowed to exactly one, the same policy already served the
Supervisor's own storage, the namespace had a quota for it, every relevant
service was healthy, and a disk created with *no* policy succeeded on that
datastore.

Having thoroughly established that nothing was wrong, I was clearly reading the
wrong error.

**Two measurements broke it open.**

A timestamp. The driver logged the create call at `57.517` and the fault at
`57.558` — **41 milliseconds**. Nothing had gone looking for a datastore. This
was argument validation, refusing synchronously before any work began.

An operation ID. The driver logs one per call, and vCenter carries the same id
through its own logs:

```
grep <opId> /var/log/vmware/vsan-health/vsanvcmgmtd.log   # a SOAP 500
grep <opId> /var/log/vmware/vmware-sps/sps.log            # the real reason
```

The storage service was answering two callers within seconds of each other:

```
one caller  (works, 7ms): Hubs: [datastore-1056, datastore-1011]
                          reqs: [CapabilityProfileRequirement{...}]

the other   (fails):      Hubs: null
                          reqs: [(ZoneTopologyRequirement){ clusters = [...] }]
  -> No PlacementHub found for given ZoneTopologyRequirement
```

A zone-scoped request demands a datastore valid for the **whole cluster**. Both
datastores here are local, one per host. Nothing qualified, so the request was
rejected — and the layer above reported *its own* argument as the invalid one.

Three components, each describing its local view honestly, composing into an
answer that pointed at the one thing that was healthy.

> **In plain terms.** You ask a shop for a part. The clerk asks the warehouse,
> the warehouse says "no such shelf," and the clerk tells you your order form
> was filled in wrong. Nobody lied. Nobody was in a position to tell you what
> actually happened.

## The wrong turn, which is the real lesson

"No shared storage" was my first hypothesis, formed in about ten minutes.

I abandoned it for two days, because the obvious compatibility check returned
compatible datastores for every policy.

That check is real and it is also irrelevant. It asks *can this profile be
satisfied by this datastore?* Zone placement asks *is this datastore reachable
from the whole zone?* Nothing in the first question touches the second. The
tool returned green to a question nobody had asked.

So: a correct hypothesis, tested with an instrument structurally incapable of
falsifying it, discarded on the strength of the result.

> **In plain terms.** The useful habit is not "test your hypothesis" — I did
> that. It is **ask whether the test you are about to run can return no.** If
> it cannot, a green result carries no information, and treating it as
> disconfirming evidence is worse than not testing at all.

## The fix, and four ways it silently un-fixes itself

One export mounted on both hosts. A claim bound in thirty seconds, on the
Supervisor and inside a guest cluster — the first persistent volume this
platform had ever held.

The error moved on the way:

```
before : InvalidArgument / createSpecs.profile    (no placement candidate)
after  : NoPermission                             (transient)
then   : Successfully provisioned
```

That middle state lasted about three minutes while the platform propagated a
storage grant to its own service account. Read literally it says permissions
are missing. Comparing the new datastore against a working one showed it
carrying *more* grants — 57 against 56, the extra being precisely the storage
role. Nothing was missing. Waiting was the fix.

Then four distinct ways to undo the repair while appearing to have done nothing
wrong, each reproducing the **original** misleading error:

1. **Mount it on one host.** Still no cluster-wide candidate. Identical failure.
2. **Mount it but don't tag it.** The policy is tag-based; an untagged
   datastore satisfies nothing.
3. **Tag it but don't assign the policy to the namespace.** A policy that
   matches a datastore is still unusable from a namespace it is not assigned to.
4. **Run the automation.** The datastore resource manages a `tags` attribute.
   The tag was applied out-of-band, so the tool saw an undeclared attribute and
   set it to null — **silently removing the tag during an unrelated disk
   resize.** Clean plan. Successful apply. Tag gone.

The fourth is self-inflicted and the most instructive: the automation built to
maintain the platform became a way to break it, with no error anywhere.

> **In plain terms.** A repair with four quiet reversals is not really fixed
> until each reversal has a guard. Three of these were things I could do
> wrong; the fourth was something my own tooling would do *for* me, on a day I
> was changing something unrelated.

## What went into the skill

**The correlation technique, first.** The operation ID is the thread that
connects a driver's error to the service that actually refused. That one
paragraph replaces the two days.

**A warning about a specific green.** The compatibility check answers a
different question than the one you are asking. Written as a trap, because the
tool is not wrong and will keep saying yes.

**Both halves of the fix, with the reversals.** Mount on every host, tag it,
assign the policy to the namespace — and an `ignore_changes` with a stated
reason so the tooling stops removing the tag.

**The transient, named as transient.** A permission error immediately after
granting permissions is propagation, not absence. Wait and retry before
granting anything by hand.

And the entry carries its own history: hypothesis formed, recorded as weak,
then confirmed. A version written at the end would show only the answer and
lose the misleading green that cost the two days.

## What's next

This is the last of the failures. What remains is the question the whole series
has been circling: what the skill actually became, whether it is repeatable,
and what any of it is worth to someone whose stack is not this one.

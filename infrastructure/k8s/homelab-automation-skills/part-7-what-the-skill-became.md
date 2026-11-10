---
layout: page
title: "Part 7 — What the Skill Became"
published: false
---

# Part 7 — What the skill became

*Series: Homelab Automation Skills.*

{% include homelab-disclaimer.html %}

> **DRAFT — `published: false`.** Flip the flag in the front matter when this
> is ready to go live. Two numbers near the end are deliberately left open:
> whether the rebuild test has been run, and what it showed.

The goal was never to build a homelab. It was to write a skill that could build
one, and then rebuild it, from bare metal, without me remembering anything.

Six parts later the lab runs: a Supervisor, two guest clusters, shared storage,
a registry, ingress. That is the least interesting outcome. The question this
part is about is whether the **artifact** is any good — and the honest answer
has one part proven and one part still outstanding.

> **If you don't do this for a living.** The usual output of a project like
> this is a step-by-step guide. This one produced something different: a
> document meant to be read and acted on by software, which means every gap a
> human would paper over had to be written down. This is what that turned out
> to contain, and what it is worth.

---

## The two documents

The project produced two descriptions of the same platform, and they can be
compared directly.

| | lines | encodes |
|---|---|---|
| the runbook | ~630 | the path — do this, then this, with a check at each stage |
| the skill | ~3,600, 23 entries | the terrain — what each step is for, how it fails silently, which diagnoses are dead ends |

Plus a dozen infrastructure modules and about thirty scripts carrying the same
reasoning in their comments, so the knowledge sits next to the thing it
governs.

The runbook is better for a first build. It is ordered, it is shorter, and a
competent person can follow it. The skill is close to unreadable front-to-back
and is not meant to be read that way.

**The runbook's own closing line is the honest summary of its limit:** six of
the traps it lists *produce no error at the point of the mistake*. A document
organised as a sequence has nowhere to put "this will look fine now and fail
three stages later, in a different subsystem, blaming something else."

## What six parts of failure actually produced

Not procedures. Looking back at what went into the skill from each part, the
reusable content falls into four kinds — and none of them is a step.

**Where a tool cannot reach, stated so nobody searches.** *No resource exists
for this. Stop looking.* Cheap to write, and it removes a day.

**Diagnostic order.** *Read the host's own log first; the manager only ever
says "timeout."* *The operation ID connects the driver's error to the service
that actually refused.* These replace entire afternoons, and they are the
single highest-value category.

**Traps, stated as traps.** *An empty identity file does not mean there is no
stale identity.* *The compatibility check answers a different question than the
one you are asking.* Each exists because a correct hypothesis was nearly, or
actually, abandoned on bad evidence.

**Ordering constraints with their window.** *Unprepare the hosts before
destroying the manager — once it is gone, repair stops being possible.* Not
"do this first," but what becomes impossible if you don't.

What is *not* in there: "read the plan carefully," "watch your temperatures,"
"check your work." Those are wishes. The test I ended up applying is whether an
entry would change what a reader does in the next ten minutes.

## The gates are the part that transfers

Every stage check in this build names **an object and a state**, never a
command and an exit code:

```
static routes on the gateway   ->  result_count: 1
host transport node            ->  state = success, AND an endpoint IP assigned
a test claim in the namespace  ->  Bound, within about 30 seconds
```

"The automation applied cleanly" does not appear and cannot, because several of
the worst failures in this series happened on a clean apply.

This is the part I would hand to someone whose stack looks nothing like mine.
Any environment with an infrastructure-as-code engine, a pipeline that runs it,
a layer that attests to the result, and increasingly an agent reading all three
has the same exposure: **an attestation that every step succeeded is a claim
about the steps, not about the system.**

The platform in this series enabled successfully, passed every gate it had, and
could not create a unit of persistent storage. A pipeline checking exit codes
would have certified that build. So would a compliance report asserting every
stage completed. Neither would have been lying.

Knowing which greens are trustworthy is not in the pipeline, the policy engine,
or the vendor's documentation. It is in whatever artifact records *why* a check
means what it claims to mean — and that artifact has to be written during the
work, by whoever is doing it, because afterwards nobody remembers which greens
were load-bearing.

## The test, and its current status

The claim this series rests on is falsifiable, and it is not "did it build."

> **Did it rebuild, after the environment changed underneath it?**

Partly proven. The lower stages have been rebuilt several times — vCenter
replaced, hosts reinstalled, state orphaned and recovered, a host added to a
running cluster. Each rebuild audited both documents against reality, and the
runbook is the one that failed quietly: a section describing the storage
situation stayed confidently wrong for hours after the storage situation
changed. Nothing broke. It simply became untrue.

Not proven: the newest automation has never run clean from zero. The shared
storage stage took three correction cycles to get right — a missing virtual
CD-ROM, a configuration system overwriting its own network settings, a disk
that needed resizing. All three fixes are in the code. **The fixed code has
never been applied to an empty environment.**

That is the open item, and it is deliberately stated rather than glossed:

> _[pending: result of a clean Stage 3 rebuild — did the three fixes compose,
> or does the first run still need hands?]_

I would rather publish with that gap visible than imply a test I have not run.
The whole argument is that an admitted gap costs less credibility than a
confident claim that turns out to be untested.

## What I would do differently

**Split the skill earlier.** It interleaves two kinds of fact — things true of
the product anywhere, and things true of this lab's addresses and hostnames.
Only the first half transfers. Separating them is mechanical and I left it too
late.

**Write the gate when the failure happens, not after.** Every gate in that list
exists because something reported success while being untrue. Several were
added weeks after the incident, from memory, and are weaker for it.

**Record the wrong turn in the same session.** The most valuable entries carry
their own history — hypothesis formed, recorded as weak, then confirmed. The
ones written at the end show only the answer, and the answer alone is the least
reusable part.

**Stop trusting remembered numbers.** A host was ruled out of a role for months
on a figure nobody had measured. Sixty seconds of checking would have changed
the architecture.

## The thread, one last time

**Check the object, not the exit code.**

The tools were right every time. A status code describes a request. A plan
summary describes a diff. A manager's view of a host describes what the manager
observed. A compatibility check answers the question it was built to answer.
None of them describe the thing itself — and the thing itself was almost always
one command away.

The skill is, in the end, mostly a list of which object to go and look at, and
what the answer should be. That is a duller artifact than I expected to produce
and a more useful one than the guide I set out to write.

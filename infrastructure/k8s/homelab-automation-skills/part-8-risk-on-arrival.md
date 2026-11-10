---
layout: page
title: "Part 8 — Risk on Arrival"
published: false
---

# Part 8 — Risk on arrival

*Series: Homelab Automation Skills.*

{% include homelab-disclaimer.html %}

> **DRAFT — `published: false`.** Flip the flag in the front matter when this
> is ready to go live.

Seven parts about one homelab invites a fair question: so what?

The honest answer is that none of it was ever about the homelab, and the proof
is that the series' central lesson turned out to be **buildable**. Not written
down as advice — built, as a small instrument you can point at someone else's
migration and get a table of answers back.

This part is about that instrument, what it found, and what it cannot tell you.

> **If you don't do this for a living.** Moving applications from one platform
> to another, the instinct is to study what you have. The tool described here
> does the opposite: it sends deliberately awkward sample workloads to the
> *destination* and records exactly how each one is refused, mangled, or
> quietly ignored — before anything real is moved.

---

## Risk is on arrival, not departure

The customer already runs the old platform. They understand it, they have run
it for years, and it works. Nothing about the source is mysterious.

What nobody knows is which of their manifests the **destination** will refuse,
silently ignore, or leave half-working.

That is a different question from the one migration projects usually ask, and
it reorders the work. Inventorying the source is the comfortable task — it is
knowable, it produces a spreadsheet, and it feels like progress. It also tells
you almost nothing about what will break, because breakage happens where the
new platform's opinions differ from the old one's, and those opinions are only
discoverable by provoking them.

So the harness probes the destination's **enforcement surface** rather than the
customer's manifests.

That choice has a practical consequence worth more than the theory: it needs
**no source environment and no customer artifacts**. No cluster backups, no
exported manifests, no access to production. Early in an engagement, when
sharing any of that is weeks of paperwork away, you can still produce a real
break/fix table.

> **In plain terms.** You do not learn whether your furniture fits by measuring
> your furniture. You measure the doorway.

## It has controls, which is the whole reason to trust it

Nineteen specimens, each isolating **one hazard**, so that a result is
unambiguous. And two of them — `00` and `10` — are controls that must pass.

From the harness's own notes: *if `00` fails, no other row is trustworthy.*

This is the lesson from Part 6 built into hardware rather than written as
advice. That part ended on the habit I had failed to apply: **ask whether the
test you are about to run can return "no."** A green from an instrument
structurally incapable of returning red carries no information, and I lost two
days to exactly that.

A control answers the inverse and equally necessary question: can this
instrument return *yes*? If a compliant, boring, obviously-fine workload does
not run, then every "this was rejected" below it is the harness being broken,
not the platform being strict.

> **In plain terms.** Before you trust a smoke alarm's silence, press the test
> button. Two of the nineteen probes exist purely to be the test button, and
> they are the reason the other seventeen mean anything.

## What it found

Eleven specimens have measured results against a real VKS guest cluster:

| specimen | hazard | result |
|---|---|---|
| 00 | compliant workload | **control — runs** |
| 01 | no `securityContext` | accepted, **zero pods** |
| 02 | runs as root | accepted, **zero pods** |
| 08 | hostPath + hostNetwork | accepted, **zero pods** |
| 03 | image names its user | pod created, **will not start** |
| 04 | `ncp/*` annotations | applied, retained, **inert** |
| 05 | Ingress resource | created, **no address** |
| 06 | default-deny NetworkPolicy | **enforced** |
| 07 | PVC, old platform's StorageClass | **Pending**, never binds |
| 09 | egress identity, two namespaces | **one shared source IP** |
| 10 | NodePort | **control — allocated** |

Read that column again, because the shape of it is the point.

**Every single finding is a green that lies.** `kubectl apply` returns success
for all of them. Three separate hazards produce "accepted" with *zero pods
ever created* — the Deployment exists, the ReplicaSet exists, and the only
record of the rejection lives on an object most people never describe. One
produces a pod that is created and will never start. One retains six
annotations faithfully and acts on none of them, with nothing anywhere warning
that the intent was dropped.

That is the whole series, arriving in someone else's environment on a schedule.

The egress finding is the one I would lead with in a customer conversation.
Two namespaces that the old platform would have given distinct network
identities share **one source IP** on arrival. Nothing fails. Nothing warns.
Every workload keeps running — and any downstream firewall rule, audit trail,
or allowlist keyed on that identity is now wrong, silently, from the moment of
cutover.

> **In plain terms.** The dangerous outcomes here are not the ones that break.
> They are the ones that *keep working while meaning something different* —
> and those are invisible to any check that asks "did it deploy?"

## What it cannot tell you

The report states its own limit in its second paragraph, and I would rather
quote it than paraphrase: every result is **measured** on the cluster named in
the report; expected old-platform behaviour is **asserted from documentation**,
with no source environment observed.

That matters. The harness proves what the destination does. It *assumes* what
the source did. For the findings above that gap is mostly harmless — "restricted
pod security rejects a root container" does not need a control group — but
anywhere the claim is "this used to work differently," the evidence is a
document, not a measurement.

A real engagement closes that by running the same specimens against the
customer's actual source platform. Same instrument, both ends, two measured
columns instead of one measured and one assumed.

Eight of the nineteen specimens also have no results yet. The harness is
committed as a draft and I am not going to describe it as more finished than it
is.

## What transfers

Nothing above depends on the specific platforms involved, and that is the part
worth taking away.

Before migrating anything, build a small instrument that probes the
destination's enforcement surface:

- **one hazard per probe**, so a result is unambiguous
- **controls that must pass**, so a broken instrument is distinguishable from a
  real finding
- **run against the destination**, so it needs nothing from the source and can
  happen on day one
- **record what was measured versus what was assumed**, separately, every time

The specimens are not the asset. The asset is having asked the destination
instead of assuming from the source — which is the same move the whole series
has been making, one layer up.

## Where this leaves it

The lab was built to prove a skill could build a lab. The skill turned out to
be mostly a catalogue of greens that lie. And the catalogue, pointed outward,
is an instrument for finding which greens will lie in an environment I have
never seen.

That is a more useful ending than the one I set out to write, and it is the
first part of this project that was never about my homelab at all.

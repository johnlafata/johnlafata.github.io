---
layout: page
title: "Part 5 — The Number Nobody Measured"
---

# Part 5 — The number nobody measured

*Series: Homelab Automation Skills.*

{% include homelab-disclaimer.html %}

Every constraint in this series so far has lived in a file. A missing resource,
a stale record, a dependency graph, a certificate. Things you can reason about
from a desk, at any hour, with a terminal.

This one is a heatsink.

It had been shaping results for weeks before I measured it, and when I finally
did, the thing I had been treating as the lab's capacity turned out to be a
number I had never looked at.

> **If you don't do this for a living.** Servers are usually described by two
> numbers: how many processor cores they have, and how much memory. Both of
> mine looked fine. Neither is the number that was actually running out — and
> the one that was does not appear on any spec sheet or in any management
> screen I was using.

---

## The sizing that looked fine

Here is how I had been thinking about the host running the platform:

```
esxi-sm   8 cores   127.9 GB RAM
```

Eight cores and 128 GB, for a management plane. That reads as comfortable. The
virtual machines on it are not enormous and their memory totals fit with room
to spare. I checked that arithmetic more than once and it kept being fine.

The platform is not trimmable, which I also knew:

| component | vCPU |
|---|---|
| NSX Manager | 6 |
| Supervisor control plane (3 VMs, fixed) | 6 |
| NSX Edge | 4 |
| vCenter | 4 |

Twenty vCPU on eight cores is over-subscription, but over-subscription is
normal — that is most of the point of virtualization. vCPU counts do not tell
you whether a host is actually keeping up.

So I looked at CPU ready times, which is the number that does. They were mostly
healthy: 0.8–1.6% per vCPU, one Supervisor VM at 5.1%. Saturated but coping.

Everything I measured said the host was fine, and the host was not fine.

## The number I was not looking at

Not cores. Not RAM. Not ready time. **Clock budget.**

```
platform demand   ~18.3 GHz
esxi-sm provides   16.8 GHz
```

The host is being asked for more cycles per second than it physically has. Not
80% utilised, not tight — **over**. It reported 109% CPU and stayed there,
because the work does not go away; it queues, runs flat out, and never catches
up.

That number is trivially derivable and appears nowhere by default. You get
cores and you get a percentage. The percentage above 100 is the tell, and I had
read it as "busy."

> **In plain terms.** A removal van rated for a one-bedroom flat is not "busy"
> when you ask it to move a house — it is the wrong van, and no amount of
> careful packing fixes it. Core count is how many people you have. Clock
> budget is how fast they can actually work. I had counted the people.

## The heat was the symptom

Running flat out continuously has a physical consequence, and that is where it
finally became visible:

```
sustained full-platform load  ->  CPU 96 C, flagged RED by ESXi
Xeon D-1541 throttle point    ->  ~100-105 C
```

Four degrees of margin, sustained, with no guest cluster running at all.

It is worth being precise about the causality, because I had it backwards at
first and the framing matters. The heat is not an independent problem competing
with CPU for attention. **The host is thermally stressed because it is
computationally over-committed.** One cause, two readouts, and I had been
reading the one that looked survivable.

## Measuring to a convenient reading

I got the measurement itself wrong first, and this is the part most worth
copying.

After a round of remediation I ran a load ramp, watched the temperature, and
reported it fixed:

```
[ 780s] load= 87%  cpu=86C [Green]    <- called this the answer
[1080s] load=107%  cpu=89C [Green]
[1200s] load=107%  cpu=93C [Yellow]
[1380s] load=102%  cpu=96C [Red]      <- actual equilibrium
[1620s] load= 91%  cpu=96C [Red]      <- sustained
```

86°C at thirteen minutes. Green. Out of the critical band. Exactly the result I
was hoping for, arriving at exactly the moment I was ready to stop.

The chassis takes more than twenty minutes to heat-soak. Any thermal conclusion
drawn before equilibrium is worthless, and mine was drawn at thirteen.

> **In plain terms.** You take someone's temperature thirty seconds after they
> swallow a cold drink.
>
> What makes this expensive is not impatience — it is that **the premature
> reading agreed with me.** A measurement that confirms what you want is the
> one you are least likely to repeat, which means the bias is strongest exactly
> where the cost of being wrong is highest.

## The experiment that actually isolated it

The one thing I did well here was the next step, so it is worth recording as
the counterexample.

Rather than guessing between "the room is too warm," "the fans are failing" and
"the heatsink is bad," I cleaned the dust out and measured **every sensor**
before and after:

| sensor | before | after |
|---|---|---|
| idle CPU | 65 C | 56 C |
| DIMMs | 51–56 C | 41–42 C |
| MB_10G | 64 C | 53 C |
| Peripheral | 57 C | 48 C |
| **sustained-load CPU** | **96 C RED** | **96 C RED** |

Every ambient sensor improved by 5–14 degrees. The CPU under load landed in
*exactly* the same place.

That is a clean isolation. Airflow demonstrably improved and the CPU did not
benefit, which puts the fault at the CPU-to-heatsink interface — dried thermal
paste or seating — rather than anywhere in the chassis. The fan data agrees:
FAN2 pins at 6100 RPM under load, so the fan is working and the heat is not
reaching the fins for it to move.

> **In plain terms.** Changing one thing and measuring everything beats
> changing several things and measuring the one you care about. The sensors
> that improved are what let you trust the sensor that didn't.

## Why there is no software answer

The reflex is to reduce the footprint. There is nothing to reduce.

The Supervisor control plane is three VMs and fixed — an etcd quorum
requirement, not a setting. NSX Manager at 6 vCPU is already the documented
minimum. The Edge's form factor cannot be changed after creation. Dropping a
guest-cluster worker saves 2 vCPU and, measurably, **nothing thermally**.

This is also why an earlier evaluation of a lighter networking architecture
mattered less than it looked: the best case traded the Edge for a smaller
appliance, saving perhaps 2 vCPU, and would not have moved the thermal picture
at all.

The levers are all physical: reseat the heatsink with fresh paste, populate the
two empty fan headers, park the lab when idle — or move the work.

## The dismissal, on a number nobody measured

The real fix is to move the platform to the other host, and the reason it took
so long to see is the most uncomfortable part of this post.

| | esxi-sm (Xeon D-1541) | esxi-mini (Ryzen 9 9955HX) |
|---|---|---|
| CPU | 8 cores / **16.8 GHz** | 16 cores / **39.9 GHz** |
| RAM | **127.9 GB** | 93.7 GB |
| thermals under platform load | **96 C RED** | idle |

The platform needs ~18.3 GHz and about 77 GB. That is *more clock than esxi-sm
physically has*, and **46% of esxi-mini**, whose 93.7 GB fits the 77 GB at
around 82%.

So the CPU-heavy platform belongs on the CPU-rich host, and the RAM-hungry
guest clusters belong on the RAM-rich one. The lab had it exactly backwards.

And esxi-mini had been ruled out as a platform host months earlier — **on RAM
grounds**. That judgement was never checked against a live figure. When it
finally was, the platform fit comfortably and the clock advantage was 2.4×.

> **In plain terms.** A whole architecture was built around an assumption that
> would have taken sixty seconds to verify, and the verification never happened
> because the assumption was never contentious.
>
> This is the thread of the series arriving from a direction I did not expect.
> Parts 1 to 4 were about trusting a system's *report* instead of checking the
> object. This is the same mistake with no system involved at all: **I trusted
> my own recollection of a number, and recollection is a report too.**

## What went into the skill

**A derived figure, written down.** The platform's clock demand and each host's
clock budget, as numbers, because neither appears in any console and the
comparison is the whole decision.

**A measurement protocol.** *Measure to equilibrium, not to a convenient
reading. Heat soak on this chassis takes more than twenty minutes.* With the
ramp table attached, because the shape of that curve is what makes the rule
believable.

**The failed fix, kept.** Dust cleaning improved every ambient sensor and did
nothing for the CPU. That negative result is what isolates the fault, and
deleting it would leave the next person re-running it.

**The dismissal, recorded as an error.** In as many words: dismissing a host on
a number nobody measured is how this went unaddressed for as long as it did.

What is *not* in there is "watch your temperatures." That is a sentiment. The
useful content is the specific derived number, the time-to-equilibrium for this
chassis, and the one experiment that distinguishes an airflow problem from an
interface problem.

## What's next

Five parts in, every failure has been something the system could in principle
have told me, if I had asked the right object: a plan's JSON, a host's log, a
realized-state API, a thermal sensor at equilibrium.

The last one in this stretch is the worst of them, because the system was
asked, answered clearly, and the answer was wrong in a way that took three
layers of software to produce. A platform that enabled perfectly, passed every
gate, ran applications — and could not create a single unit of persistent
storage, which nobody noticed because nothing had asked for one yet.

---
title: "Homelab Automation Skills, Part 5: The Number Nobody Measured"
date: 2026-11-10
tags: [Skills, Automation, Homelab, VKS]
excerpt: "Eight cores, 128 GB, healthy CPU ready times. Everything I measured said the host was fine, and the host was not fine — the number that was running out appears on no spec sheet."
---

{% include homelab-disclaimer.html %}

Every constraint in this series so far has lived in a file — a missing resource, a stale record, a dependency graph, a certificate. Things you can reason about from a desk. This one is a heatsink.

The host running the platform has eight cores and 128 GB of RAM, which reads as comfortable for a management plane. The memory arithmetic worked with room to spare. CPU ready times — the number that actually tells you whether a host is keeping up — were mostly healthy. Everything I measured said it was fine.

The number I was not looking at was clock budget. The platform demands about 18.3 GHz; the host provides 16.8. Not tight — *over*. It reported 109% CPU and stayed there, because the work does not go away. Core count is how many people you have; clock budget is how fast they can actually work. I had counted the people.

Running flat out continuously has a physical consequence, and that is where it became visible: 96°C under sustained load, flagged RED, against a throttle point around 100–105, with no guest cluster running at all. The causality matters and I had it backwards at first — the heat is not a separate problem competing for attention. The host is thermally stressed *because* it is computationally over-committed. One cause, two readouts, and I was reading the survivable one.

I also got the measurement wrong before I got it right. Thirteen minutes into a load ramp the CPU read 86°C, green, out of the critical band — exactly the result I wanted, arriving exactly when I was ready to stop. The chassis takes more than twenty minutes to heat-soak. Equilibrium was 96°C. A measurement that confirms what you hoped is the one you are least likely to repeat.

The one thing I did well was the next step: rather than guessing between airflow, fans and heatsink, I cleaned the dust and measured every sensor before and after. Every ambient sensor improved 5–14 degrees. The CPU under load landed in exactly the same place. That is a clean isolation — the fault is the CPU-to-heatsink interface, not the chassis.

There is no software answer. The Supervisor control plane is fixed at three VMs, NSX Manager is already at its documented minimum, and dropping a guest worker saves 2 vCPU and measurably nothing thermally. The real fix is to move the platform to the other host — which has 2.4× the clock and enough RAM, and which I had ruled out months earlier on RAM grounds, in a judgement never checked against a live figure.

That last part is the series' own thread arriving from an unexpected direction. Parts 1 through 4 were about trusting a system's report instead of checking the object. This is the same mistake with no system involved: I trusted my own recollection of a number, and recollection is a report too.

**Full technical notes:** [Part 5 — The number nobody measured](/infrastructure/k8s/homelab-automation-skills/part-5-the-number-nobody-measured.html)

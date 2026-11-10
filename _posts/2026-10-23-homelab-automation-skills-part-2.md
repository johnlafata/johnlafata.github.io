---
title: "Homelab Automation Skills, Part 2: 200 OK, and Nothing Was Created"
date: 2026-10-23
tags: [Skills, Automation, Homelab, VKS]
excerpt: "Four times the call succeeded and the work had not been done. None of the replies were lies — each system answered a narrower question than the one I thought I was asking."
---

{% include homelab-disclaimer.html %}

Part 1 was about tools that cannot reach the thing you need. Those are the comfortable failures — they announce themselves, and a skill can warn you off the tool.

This one is harder to write down. The tool reaches fine, the call succeeds, the apply is green, and nothing you asked for exists.

It happens because a modern infrastructure API almost never does the work while you wait. You send a request, it records what you want, and something else makes it true afterwards, somewhere you are not looking. So there are always two facts in play — what you asked for, and what is actually running — and the reply you get describes the first one. NSX is unusually honest about this and will show you both if you ask; most systems have the same split and only expose one side.

Four instances, which stopped looking like four bugs once I saw the shape. NSX accepted a change to an address pool, failed to apply it, and recorded the error on an object Terraform never reads — clean in-place update, 0 to destroy, pool unchanged. An Edge transport node registered successfully while the appliance deploy failed in the background, surfacing later as a `PENDING` status on a *different* resource that was itself fine. Supervisor enablement demanded a service CIDR that, after reading govmomi's structs and checking a full vCenter OpenAPI spec, turned out not to exist as a field at all — the real cause was a sync record frozen at `IN_PROGRESS`, which reads like progress and means nobody updated it. And a Terraform state file confidently described a module's worth of resources belonging to a vCenter that had been rebuilt out from under it.

The third one is the one I keep coming back to, because it inverts Part 1's lesson. Reading the source instead of the documentation is what solved most of Part 1. Here I did it thoroughly and correctly, and it was still the wrong question — the request shape was never the problem.

What came out of this was not four more procedure steps. It was a rule about what a verification step is allowed to be: every stage gate now names an object and a state, never a command and an exit code. "Terraform applied cleanly" cannot appear in that list, because every failure above happened on a clean apply.

**Full technical notes:** [Part 2 — 200 OK, and nothing was created](/infrastructure/k8s/homelab-automation-skills/part-2-200-ok-nothing-created.html)

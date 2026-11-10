---
title: "Homelab Automation Skills, Part 3: Three to Destroy"
date: 2026-10-30
tags: [Skills, Automation, Homelab, VKS]
excerpt: "The plan told me exactly what it was about to do. I read it, approved it, and would have destroyed a working NSX Manager — because the warning was in a place I was not reading."
---

{% include homelab-disclaimer.html %}

Part 2 was about replies that meant less than they appeared to. This one is worse, because the tool was not quiet at all. It told me precisely what it intended to do, I read the output, and I would still have destroyed a working NSX Manager — twice.

The mechanism is ordinary once you see it. Some attributes cannot be changed in place; altering one means destroy and rebuild. What is less obvious is that a resource can be scheduled for replacement without anything about it changing: when something it depends on has an unapplied diff, the values flowing from that dependency become unknown, and if an unknown lands on one of those un-changeable attributes, the dependent resource gets replaced. Nothing changed. It is being rebuilt because its neighbour has pending paperwork.

It happened four times, from four unrelated causes, each more remote from the damage than the last. A refreshed certificate fingerprint on the ESXi host planned a rebuild of NSX Manager. A field NSX populates and then clears planned a rebuild of the distributed switch — which would have detached the host's only physical NIC, removing the path you would use to fix it. vCenter re-issuing a host certificate on join made that first one guaranteed rather than occasional. And then, with nothing in the repository changed at all, a DHCP lease moved, the software depot's URL no longer matched, and the cascade reached NSX Manager again.

That last one is why this is its own post. The summary read `3 to add, 4 to change, 3 to destroy`. The rendered plan above it listed three actions, all expected, none of them NSX Manager. The two replacements appeared only in `terraform show -json`.

The tool did not hide anything — that is exactly why the detail was in the JSON. But I had been reading the summary line as though it were the plan, because it had been accurate every previous time. This is the first failure in the series that is mine rather than the platform's, and the most likely to repeat: the habit that caused it is the same habit that makes you quick the rest of the week.

The fix was not to protect NSX Manager. It was to stop the drift at the source, where it is inert, with a stated reason and a recorded cost for each one. Measured on a live plan: `3 to add, 4 to change, 3 to destroy` became `0 to add, 1 to change, 0 to destroy`.

**Full technical notes:** [Part 3 — Three to destroy](/infrastructure/k8s/homelab-automation-skills/part-3-three-to-destroy.html)

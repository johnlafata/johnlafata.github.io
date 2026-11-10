---
title: "Homelab Automation Skills, Part 4: Check the Object, Not the Exit Code"
date: 2026-11-06
tags: [Skills, Automation, Homelab, VKS]
excerpt: "I rebuilt NSX Manager and kept the ESXi install underneath it. That seemed obviously safe. It cost me the host — not the configuration on it, the installation."
---

{% include homelab-disclaimer.html %}

I rebuilt NSX Manager and kept the ESXi install underneath it. The manager is a virtual appliance, the host is a hypervisor, one is clearly above the other — so this seemed obviously safe. It cost me the host.

Host preparation failed with a timeout, which sends you straight to connectivity, and connectivity was fine. That message is NSX Manager's view of the host: it waited, nothing came. Accurate, and useless. The host's own log said what was actually wrong, 326 times — `NET1111`, certificate validation failed, couldn't find the new manager's thumbprint. It was not failing to reach the manager. It was reaching it, being offered a certificate, and refusing it, because it still trusted the one issued by the manager I had deleted.

Then I nearly talked myself out of the correct answer. Looking for where that trust lived, I checked a file that should have held the old manager's identity. It was empty — which reads unambiguously as *there is no stale identity here*. The file was empty and the problem was real; the identity simply lives somewhere else. Checking the wrong object and getting a clean answer is more dangerous than not checking at all, because now you have evidence.

What followed was four repair attempts in ninety seconds-ish succession, each a plausible theory about which file held the credential, none of them tested first, while the error count climbed from 1560 to 1579. Unpreparing the host removed the transport node server-side and left the host's credentials untouched. Deleting the host's certificate and private key turned out to target the host's *own* identity, not the manager's. Deleting the appliance info file produced a file that was never regenerated. The API action I expected to exist did not. Verdict: unfixable in place, reinstall the host.

The rule that came out is about ordering, not repair: if NSX Manager is rebuilt, the prepared hosts must be reinstalled too — so unprepare them *before* destroying the manager, because once the issuer is gone the window has closed.

The more useful part came days later, when a host looked broken in a very similar way and every instinct — including my own freshly-written note — said reinstall. It needed one file deleted and a reboot. Spherelet and every other VIB survived, all of which a reinstall would have destroyed. Two problems that present almost identically; the difference is only visible in which object is actually holding the stale state.

Four parts in, it is the same shape every time, so it is worth naming: **check the object, not the exit code.** The tools were right every time. They answered the question they were asked, which was almost never the question I needed answered.

**Full technical notes:** [Part 4 — Check the object, not the exit code](/infrastructure/k8s/homelab-automation-skills/part-4-check-the-object.html)

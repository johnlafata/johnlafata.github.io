---
title: "Homelab Automation Skills, Part 1: Four Tools, One Skill"
date: 2026-10-16
tags: [Skills, Automation, Homelab, VKS]
excerpt: "The goal was to write a skill that could build the lab and rebuild it on demand. The first discovery: four tools, and four different kinds of gap between them."
---

{% include homelab-disclaimer.html %}

Context: I keep a homelab to keep my skills sharp, but I often need to tear it down and rebuild it with different configurations for different potential client engagements.   I wanted a set of skills that could reliably rebuild the lab from scratch quickly and consistently.

I wanted to create automation to "build and rebuild my homelab for different scenarios".  After using Claude code Skills to accelerate application deployments, my first thought was to write a Claude Code skill that could build this lab configuration from bare metal as one of many possible labs, then rebuild it in the configuration I needed.  

The goal was to write a skill, so that Claude could execute it using all the potential tools it needed. A skill is the artifact that encodes the knowledge and users uses that knowledge and the tools it references something with no memory of what's been done before.

The first task was to identify the tools needed. VCF 9.1.1 with vSphere Kubernetes Service needs four different provisioning tools, not one. vCenter has no Terraform resource at all — the `vsphere` provider is a client of the thing it would have to bootstrap. The `nsxt` provider connects eagerly at configure time, so a missing NSX Manager fails `terraform plan` for the entire root module rather than just the NSX resources. `vsphere_supervisor_v2` exists, plans cleanly, and is a dead end — the working path is PowerCLI's `Enable-WMCluster`, and switching to it forced an architecture change, not a small patch. And the guest cluster isn't a vSphere object at all; it's a Cluster API resource applied with `kubectl`.

Which led to the first rule that went into the skill, and it wasn't a procedure. The ordered list of steps is the cheap half — reconstructible from the code, stale the moment a provider version bumps. What costs days to rediscover is the shape of the gaps — and there are four kinds: where a tool can't reach, where it fails misleadingly, where it appears to work and doesn't, and where the boundary is a different system entirely.

**Full technical notes:** [Part 1 — Four tools, one skill](/infrastructure/k8s/homelab-automation-skills/part-1-skills-and-tools.html)

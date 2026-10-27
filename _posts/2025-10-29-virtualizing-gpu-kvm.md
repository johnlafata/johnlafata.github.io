---
title: "Hosting a GPU in a Hypervisor Using Linux with KVM"
date: 2025-10-29
tags: [GPU, Virtualization]
excerpt: "Notes on NVIDIA vGPU for Linux KVM hosts: version compatibility rules, the move to the NVIDIA License System, and why sharing a physical GPU across VMs matters for AI and rendering workloads."
---

Sharing a single physical GPU across multiple virtual machines used to be a VMware-only trick. NVIDIA's vGPU software now does the same thing on Linux with KVM — letting several VMs share one card's acceleration for AI, data science and graphics workloads instead of pinning a whole GPU to a single guest.

This note captures the parts that actually bite in practice: which vGPU Manager and guest driver versions are compatible with each other, why mixing branches breaks things, and why every release now depends on the NVIDIA License System instead of the older on-prem license server.

**Full technical notes:** [Hosting a GPU in a hypervisor using Linux with KVM](/infrastructure/virtualizing-gpu.html)

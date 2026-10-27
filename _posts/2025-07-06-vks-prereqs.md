---
title: "Pre-Requisites for On-Premises Kubernetes with vSphere Kubernetes Service (VKS)"
date: 2025-07-06
tags: [Kubernetes, VMware]
excerpt: "Highlights from two separate projects deploying Kubernetes on a vSAN stretched cluster with vSphere Kubernetes Service — high availability, cross-site networking, storage and disaster recovery."
---

Running Kubernetes on a vSAN stretched cluster adds a layer most VKS write-ups skip past: the control plane and etcd need to stay highly available across sites, not just across nodes, and the networking has to support cross-site communication cleanly.

This note pulls together what mattered across two separate VKS deployments on stretched clusters — availability, networking, storage, and the disaster-recovery posture that stretched clusters are supposed to buy you in the first place.

**Full technical notes:** [vSphere Kubernetes deployments on a vSAN stretched cluster](/infrastructure/k8s/tanzukubernetes/1.README-VKS-PREREQS.html)

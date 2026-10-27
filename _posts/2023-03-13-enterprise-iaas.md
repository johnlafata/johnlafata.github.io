---
title: "Enterprise Infrastructure as a Service: Implementation Thoughts"
date: 2023-03-13
tags: [DevOps, AWS]
excerpt: "Design thoughts for a self-service enterprise deployment tool: developers request capacity or consumption-based resources, and the system provisions across Kubernetes, AWS Fargate, Azure or Google Cloud without routing through operations."
---

The assumption behind this one: developers deploying applications to the cloud shouldn't need to open a ticket with an operations team to get there. This note works through what a self-service enterprise deployment tool looks like when it has to support both capacity-based and consumption-based requests, stay flexible across Kubernetes, AWS, Azure and Google Cloud, and still keep security built in rather than bolted on.

**Full write-up:** [Enterprise Infrastructure as a Service project](/doc/devops/DevSecOps-scalableCICD-2023-03-13.html)

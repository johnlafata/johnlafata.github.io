---
title: "Deploying Letta on AWS Fargate"
date: 2025-09-24
tags: [AWS, AI]
excerpt: "A quick-start guide to running Letta, the conversational-agent framework, on AWS Fargate — ECS cluster, task definition, ALB and an RDS PostgreSQL backend for persistence."
---

Letta is built for the cloud, so running it there shouldn't require much ceremony. This is the short path: stand up an ECS cluster, define a Fargate task on the `letta/letta` image, wire in the environment variables it needs, put an ALB in front for production traffic, and connect it to RDS PostgreSQL for persistence.

The goal was to spend the setup time once and get back to building agents instead of babysitting infrastructure.

**Full write-up:** [Deploying Letta on AWS Fargate](/tools/code/frameworks/letta/blog-post-2025-09-24.html)

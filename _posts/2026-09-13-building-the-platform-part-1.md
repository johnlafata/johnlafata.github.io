---
title: "Building the Platform, Part 1: Extend an existing Pipeline to develop a Platform"
date: 2026-09-13
tags: [AWS, Terraform, DevOps]
excerpt: "After working with a GitHub Actions pipeline built to deploy an application to Fargate.  We decided to see if we could use it as the basis for claude skills to automate and generalize the deployment process."
---

We started from an existing deployment pipeline:
GitHub Actions, hand-rolled Terraform, Vault for secrets, Kafka, all of it
built commit by commit to get one  application onto
AWS Fargate   Reading the commit log is reading
a single application come up, one fix at a time — database host corrections,
Kafka debugging, Vault path adjustments — and every fix was correct and also
only true about that one app.

The question that actually mattered wasn't whether the pipeline worked. It
was what happens to the *next* application. There was no seam to cut: the
generic Terraform and the application-specific resources had grown into each
other, and onboarding anything else meant forking the whole repo and
renaming it.

So we split the repo's two jobs apart. The generic half — modules, stacks, a
build/deploy pipeline that doesn't know whose code it's building — became a
real platform. The procedural half — the knowledge of how to actually drive
it, previously living in whoever had done it most recently — became a new
repo, `platform_skills`, written as Claude Code Skills: thin command
wrappers over a CLI, which is itself a thin wrapper over plain functions.

The split also surfaced a risk that had been invisible with only one AWS
account in play: a default CLI profile that silently resolves to a different AWS account from the account planned for the platform. That got three independent
guards instead of a README note — a lesson worth its own section.

**Full technical notes:** [Part 1 — Extend an Pipeline to support a Platform](/infrastructure/aws/fargate/platform-skills-migration/part-1-extend-existing-pipeline-for-a-platform.html)

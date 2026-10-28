---
title: "Building the Platform, Part 3: Retiring AWS Copilot"
date: 2026-09-15
tags: [AWS, Security, Platform]
excerpt: "Six applications were already running on Fargate, deployed by AWS Copilot. Adoption turned out to be mostly deletion — one app.yaml replacing a copilot/ directory — except for the one gap we wrote down instead of faking, and the three names two stacks can't both own."
---

Six small applications showed up already running on Fargate, each deployed
by typing `copilot init`, `svc init`, `env init`, and `deploy` from a
laptop. One of them was the exact app an earlier post on this site walked
through deploying — a Gradio chatbot, Cognito wired in by hand at the ALB.
Copilot wasn't broken. The question was what happens once there's a platform
that has to run all of these the same way, from CI, without six people each
remembering their own procedure.

Adoption turned out to be mostly deletion: one `app.yaml` and two Terraform
roots, in place of a `copilot/` directory and its own CI. The rule that kept
it honest rather than guessy — read the target's existing deployment config
first. The Copilot manifest is authoritative for the port, the health check,
the build context; derive the new manifest from it, never assume.

Not everything ported cleanly, and the gap that didn't got written down
instead of worked around. Our subscription service's earlier Copilot
deployment used a hand-written CloudFormation addon to attach two DynamoDB
Global Secondary Indexes — something our own Terraform module doesn't
support yet. Rather than hand-port the addon and reintroduce exactly the
bespoke infrastructure we were trying to eliminate, the gap is now a
recorded blocker, the same way an unfinished offering already gets recorded
elsewhere in the marketplace.

The Cognito wiring fared better — it didn't get reinvented, it got
generalized into the `user-registry` marketplace offering from yesterday's
post, so the ALB does the same `authenticate-cognito` dance for any
application that asks, instead of each one hand-wiring its own listener
rule. And retiring the CLI itself stayed safe because the two stacks coexist
by construction — new resources, new names — except for three things that
are genuinely global: a DNS record, an ACM validation CNAME, and any
globally-unique S3 bucket name. Those three have to move in order; nothing
else does.

**Full technical notes:** [Part 3 — Retiring AWS Copilot](/infrastructure/aws/fargate/platform-skills-migration/part-3-retiring-aws-copilot.html)

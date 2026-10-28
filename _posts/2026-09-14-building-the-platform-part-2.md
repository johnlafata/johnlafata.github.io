---
title: "Building the Platform, Part 2: A Catalog, a Marketplace, and a Broker"
date: 2026-09-14
tags: [AWS, Platform, Terraform]
excerpt: "A platform that can deploy an application isn't yet a platform that knows which applications it can deploy, or what any of them actually need. We built a deployment catalog, then generalized three hardcoded dependencies into a marketplace with a broker."
---

A platform that can deploy *an* application isn't yet a platform that knows
*which* applications it can deploy, or what any one of them actually needs
from it. Yesterday's split left us with a reusable deployment platform and a
front end to drive it. Today's question was concrete: what goes in the
catalog, and what does a listed application actually get?

The deployment catalog turned out to need separating from a second,
unrelated catalog we kept conflating — the *runtime* catalog of tenants and
subscribers living behind our subscription service. One is a file in git,
always available; the other is a database, only available while that
service is up. The rule that falls out of keeping them apart: a deploy must
never depend on a running service, or that service being down would block
deploying the fix for it being down.

The more interesting rewrite was underneath: three dependencies — database,
Kafka, auth — had been wired directly into the platform, which worked until
an application needed a second database, or a cache, or a bucket. We
generalized them into a marketplace: an application requests a service
*logically* (an offering and a plan), and a broker resolves it, provisions
it, and binds the credentials in — three Terraform stages, same discipline
as the account guard from Part 1, just one layer up. The best proof it
works: an application's code suggested it needed Redis; a grep found zero
Redis calls anywhere. The offering it actually needed was `keyvalue`, which
on this platform's posture resolves to DynamoDB — no idle node, no secret to
rotate, nothing running at all until something asks for it.

app1 was the first thing that went up through all of it end to end —
both services healthy behind a shared ALB, Cognito registration working,
database migrations running as a release task.

**Full technical notes:** [Part 2 — A Catalog, a Marketplace, and a Broker](/infrastructure/aws/fargate/platform-skills-migration/part-2-a-catalog-a-marketplace-and-a-broker.html)

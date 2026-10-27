---
title: "Typical Gen AI Application Architecture and Infrastructure"
date: 2025-02-13
tags: [AI, Platform]
excerpt: "A baseline reference architecture for Gen AI applications, plus the development infrastructure basics most teams skip: repo secret scanning and sane .env-based credential handling."
---

Before an LLM feature ships, there's a baseline shape most Gen AI applications share — and a few infrastructure basics that are easy to skip in the rush to a demo. This note lays out a typical Gen AI application architecture alongside the development-infrastructure foundation underneath it: secret scanning on the repo, and a clean pattern for keeping credentials in a `.env` file instead of the codebase.

**Full write-up:** [Gen AI Application Infrastructure](/README-ARCH-INFRA.html)

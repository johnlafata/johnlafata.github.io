---
layout: page
title: "Part 3 — Three to Destroy"
---

# Part 3 — Three to destroy

*Series: Homelab Automation Skills.*

{% include homelab-disclaimer.html %}

Part 2 was about replies that meant less than they appeared to: accepted but not
realized, created but not working, in progress but frozen, recorded but no
longer true. In every one of those, the tool told me nothing was wrong.

This one is different, and worse. **The tool told me exactly what it was about
to do.** I read the output, approved it, and would have destroyed a working NSX
Manager — twice — because the warning was in a place I was not reading.

> **If you don't do this for a living.** Before this kind of automation changes
> anything, it shows you a preview: what it will create, change, and delete. The
> preview is trustworthy. The problem in this post is that the summary at the
> bottom of the preview and the detail above it do not always agree, and the
> expensive part is only in the detail — which, in one case, was not printed at
> all.

---

## The mechanism, once

Terraform resources have attributes that cannot be changed in place. Change one
and the resource must be destroyed and rebuilt. The provider calls this
**ForceNew**, and the plan marks it `# forces replacement`.

That much is well known. The part that cost me is what happens upstream.

When resource B depends on resource A — whether through a real reference or an
explicit `depends_on` — and A has *any* pending change, Terraform cannot know
what A's outputs will be until A is applied. So values flowing from A into B
become `(known after apply)`. And if one of those values lands on a ForceNew
attribute of B, Terraform plans to **replace B**.

Nothing about B changed. Nothing in the configuration changed. B is slated for
destruction because something it depends on has an unapplied diff.

In this lab, B was usually NSX Manager — a virtual machine that takes
twenty-two minutes to deploy and that everything above it depends on.

> **In plain terms.** You ask the builder to repaint a windowsill. The quote
> comes back including demolition of the extension, because the extension's
> paperwork references the windowsill and the paperwork now has to be reissued.
> Every individual step is defensible. The total is insane.

## Four triggers, same mechanism

What makes this worth a whole post is that it happened four times, from four
unrelated causes, each less visible than the last.

| # | Trigger | What it would have destroyed | How visible |
|---|---|---|---|
| 1 | ESXi host thumbprint refreshed | NSX Manager VM | `# forces replacement` in the plan |
| 2 | A field NSX clears server-side | the DVS — **detaching a physical NIC** | in the plan, if you read the right resource |
| 3 | vCenter re-issuing a host certificate | NSX Manager VM, 22 minutes after deploying it | guaranteed on every first plan |
| 4 | A DHCP lease moving | NSX Manager VM | **not in the rendered plan at all** |

### 1. A certificate fingerprint

A routine thumbprint refresh on the ESXi host in one module made NSX Manager in
*another* module show:

```
datacenter_id = (known after apply)  # forces replacement
```

A plan to destroy and redeploy NSX Manager because a certificate fingerprint
string changed.

### 2. A field the server clears

Long-standing, harmless drift on the Edge cluster — a `member.description` field
NSX populates then clears, which the configuration never set — made the host
preparation module plan its distributed switch as destroy-and-recreate.

That one would have **detached the host's physical NIC mid-flight**. On a
single-NIC host, the path you would use to fix it is the path you just removed.

### 3. Not occasional — guaranteed

On a later rebuild it became clear this was not bad luck. **vCenter's certificate
authority re-issues an ESXi host's certificate when the host joins**, so the
thumbprint attribute *always* differs on the first plan after the inventory
stage. Not sometimes. Every time.

It again planned to destroy and recreate the NSX Manager VM that had just spent
twenty-two minutes deploying.

### 4. A DHCP lease

The last one arrived during a routine regression plan, with nothing in the repo
changed at all.

The offline software depot's URL contains this workstation's address. The
workstation's DHCP lease had moved. State held `192.168.86.2`, the variables file
said `.86.5`, and the depot's `location` is ForceNew — so the depot planned a
replacement, and that pending diff cascaded into `(known after apply)` on two
more ForceNew attributes, both belonging to NSX Manager.

A DHCP lease expiring was, in Terraform's view, sufficient reason to rebuild the
network management plane.

> **In plain terms.** Each trigger is more remote from the damage than the last:
> a fingerprint, a field nobody set, a certificate renewal that happens by
> design, and finally a router handing out a different address overnight.
>
> The pattern worth internalising is that **the severity of the consequence
> tells you nothing about the significance of the cause.** There is no
> proportionality here to use as an alarm.

## The part I nearly missed

Trigger 4 is the reason this is Part 3 and not a footnote in the skill.

Here is what the terminal showed:

```
Plan: 3 to add, 4 to change, 3 to destroy
```

Three to destroy. The rendered plan above it listed **three actions**, all of
them expected, none of them NSX Manager.

The two NSX Manager replacements were visible only in `terraform show -json`.

I want to be careful about the claim here, because it would be convenient to say
the tool hid something. It did not. The information was in the plan — that is
precisely why it is in the JSON. But the human-readable rendering and the
summary count did not line up in a way I would have noticed at the speed I was
reading, and I had approved plans with similar-looking summaries all week.

The honest version: **I was reading the summary line as though it were the
plan.** It is a count. It had been accurate every previous time, which is
exactly what made it load-bearing.

> **In plain terms.** The receipt total is correct. The itemised list above it
> is correct. You have been checking the total for a month, because it has
> always matched — and this is the day it includes something you did not put in
> the basket.
>
> This is the only failure in the series so far that is **mine rather than the
> platform's.** It is also the one most likely to repeat, because the habit that
> caused it — skimming a familiar output — is the habit that makes you
> productive the other ninety-nine times.

## Why the obvious diagnostic makes it worse

The instinct, on seeing a plan propose something alarming, is to narrow it:
`terraform plan -target=<the resource I care about>`.

That does not help here, and it is actively misleading. `-target` does not
resolve the upstream diff either — it produces **the same bogus replacement**,
now with the surrounding context stripped out, which reads as confirmation that
the resource itself is genuinely broken.

The diagnostic that does work is the opposite: apply the *upstream* change in
isolation first, then re-plan. The cascade clears once nothing upstream is
pending.

## The fix is upstream, not downstream

The reflex is to protect the victim — put `ignore_changes` or `prevent_destroy`
on NSX Manager. That treats the symptom and leaves the mechanism live, ready to
point at whatever depends on the next drifting resource.

The fix is to stop the drift at the source, **where it is inert**:

- the depot's `location` — ignored, because the URL only matters while the depot
  is registered and the cluster image pinned; vCenter never re-fetches it
- the Edge cluster's `member[0].description` — ignored, scoped to the single
  attribute so cluster membership stays tracked
- the host's `thumbprint` and `services` — ignored, because a thumbprint is a
  join-time credential with no effect once the host is connected

Each of these is safe to ignore for a *specific, stated* reason. That matters:
`ignore_changes` is a loaded weapon, and an entry without a reason is
indistinguishable from one added to make a plan quiet.

There is a real cost, recorded alongside each one. Ignoring the depot's
`location` means changing depots for real now requires an explicit `-replace=`.
That is a worse day for someone later, and it is written down precisely because
nothing in the code will tell them.

Measured on a live plan, before and after:

```
before:  3 to add, 4 to change, 3 to destroy      (two hidden NSX Manager replacements)
after :  0 to add, 1 to change, 0 to destroy
```

## What went into the skill

Three things, none of them a procedure.

**A rule about reading plans.** Before applying anything that proposes
replacing infrastructure you did not touch, check whether the replacement is
upstream drift leaking through a dependency. The question is not *"why is this
resource being replaced?"* but *"what does it depend on that has a pending
change?"*

**A warning about the diagnostic.** `-target` is not safe here. Written down
explicitly, because it is the first thing anyone reaches for and it produces a
confident wrong answer.

**A reason attached to every `ignore_changes`.** Including its cost. The entry
for the depot URL says, in as many words, that changing depots now needs
`-replace=`.

What is *not* in the skill is "read the plan carefully." That is not knowledge;
it is a wish. The transferable part is knowing which specific attribute in this
stack drifts without anyone touching it, and what each one takes down with it.

## What's next

Everything so far has been a machine telling me something — accurately,
misleadingly, or too quietly. In each case the information existed and I could
have gone and read it.

Next is the one where I did not go and read it: a host I bricked by acting on a
theory I had not tested. After that, the point where the real constraint on this
lab turned out not to be CPU, RAM, or any provider at all, but temperature.

The thread, now hard to avoid: **check the object, not the exit code.**

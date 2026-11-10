---
layout: page
title: "Part 4 — Check the Object, Not the Exit Code"
---

# Part 4 — Check the object, not the exit code

*Series: Homelab Automation Skills.*

{% include homelab-disclaimer.html %}

I rebuilt NSX Manager and kept the ESXi install underneath it. That seemed
obviously safe. The manager is a virtual appliance; the host is a hypervisor;
one is clearly above the other.

It cost me the host. Not the configuration on it — the installation.

This is the part where the thing running through the whole series finally got a
name, because it is the first time ignoring it cost something I could not undo
with a command.

> **If you don't do this for a living.** Two machines had to trust each other,
> the way a phone and a car do after you pair them. I replaced one of them and
> assumed the pairing would simply redo itself. It did not — the other machine
> still remembered the old one, refused the new one, and had no way to be told
> otherwise. Everything below is me trying four different ways to make it
> forget.

---

## The symptom, and the first lie

Host preparation failed like this:

```
Fabric-node installation failure. Time out waiting for host to join NSX Manager.
```

A timeout. Which sends you to connectivity, and connectivity was fine — ports
1234, 1235 and 443 all open, the host plainly reaching the manager.

That message is NSX Manager's view of the host. It is the only thing NSX will
tell you, and it describes what the manager observed: it waited, nothing came.
Accurate, and useless.

The host's own log says what is actually wrong, 326 times:

```
/var/log/nsx-syslog.log
  errorCode="NET1111"  Certificate validation failed: 18-self-signed certificate
  Certificate validation: couldn't find SHA256 digest '<new manager thumbprint>'
  CcpConnectionV2: connection fail with reason 4
```

The host is not failing to reach the manager. It is reaching it, being offered a
certificate, and **refusing it** — because it still trusts the one issued by the
manager I deleted.

Two systems, two accounts of the same event. One says *timeout*. One says
*I do not trust you*. Only one of them was in the room.

> **In plain terms.** The report that reaches you is written by whichever
> component is still working. The broken one is not filing reports; that is
> what being broken means. So you get an accurate description of the symptom
> from a healthy neighbour, and you spend your afternoon investigating the
> neighbour.

## The empty file that nearly won

Having formed the right hypothesis — stale trust from the old manager — I went
looking for where that trust lived, and checked `/etc/vmware/nsx/controller-info.xml`.

It was empty.

Which reads, unambiguously, as *there is no stale identity here*. The hypothesis
appeared disproven, by direct inspection, on the host itself.

It was not. The file was empty and the trust problem was real; the identity
simply lives elsewhere. An empty file is not evidence of absence unless you know
that file is where the thing would be — and I did not know that. I had checked
*a* object, decided it answered the question, and nearly abandoned the only
correct theory I had.

> **In plain terms.** You look in the drawer where the spare key should be. It
> is empty, so you conclude there is no spare key. There is; it is in a
> different drawer, in a house whose layout you do not actually know.
>
> This is the subtler half of "check the object." Checking the *wrong* object
> and getting a clean answer is more dangerous than not checking at all,
> because now you have evidence.

## Four repairs, four wrong objects

| attempt | theory | what actually happened |
|---|---|---|
| unprepare the host via NSX | removing host prep clears its credentials | transport node removed server-side; **host credentials survived**, still dated to the old manager |
| delete `host-cert.pem` + `host-privkey.pem` | this is the trust material | wrong target — that is the host's **own** identity, not the manager's. NSX regenerated the key; `NET1111` continued |
| delete `appliance-info.xml` + restart the agents | this holds the manager's embedded certificate | file was **not** regenerated. Trust never re-established |
| NSX `?action=resolve` | there is a supported repair action | not a valid action on 9.1.1 — the API accepts only the maintenance-mode verbs |

Four theories. Each one plausible, each one acted on immediately, none of them
tested first. `NET1111` climbed from 1560 to 1579 in ninety seconds throughout —
the host telling me, continuously, that nothing I was doing had changed its mind.

The honest summary is that I was deleting files to see what would happen. That
is a legitimate technique on a disposable lab host, right up until the moment
you need a reason to stop — and I had no criterion for when to give up, because
I had never established where the credential actually lived.

**Verdict: unfixable in place. The host was reinstalled.**

> **In plain terms.** Four guesses, each cheap on its own, with no test between
> them to say whether the last one helped. That is not debugging; it is
> shuffling. The expensive part was not any single wrong guess — it was never
> pausing to find out which object held the thing I was trying to change.

## The rule that came out of it

Short, and it is about ordering rather than repair:

> **If NSX Manager is rebuilt, the prepared hosts must be reinstalled too.**
> Unprepare the hosts *before* destroying the manager — once the manager that
> issued their trust is gone, the window has closed.

There is no clever recovery. The repair has to happen while both parties still
exist. I did the steps in the wrong order and the cost was fixed from that
moment, before any of the four attempts.

## The correction, which matters more than the rule

Days later a host looked broken in a very similar way: stranded, an orphaned
distributed switch holding its physical NIC, nothing obviously able to release
it. Every instinct said reinstall — it had worked, it was known, and the earlier
rule was sitting right there in my own notes.

It did not need a reinstall. It needed one file deleted:

```
1. esxcli network ip interface remove --interface-name=vmk10   # TEP
2. esxcli network ip interface remove --interface-name=vmk50   # hyperbus
3. rm -f /etc/vmware/dvsdata.db
4. maintenance mode, then reboot
```

The orphaned switch was gone, the physical NIC released, and **spherelet and
every other VIB survived** — all of which a reinstall would have destroyed.

Two problems that present almost identically. One genuinely requires the
nuclear option; the other is one file. The difference is not visible in the
symptom, only in which object is actually holding the stale state — trust
material issued by a manager that no longer exists, versus a local database of
switch configuration.

The skill now says both, with the newer one explicitly marked as superseding the
older advice. That correction is the single most valuable line in the file,
because the earlier version of me would have confidently reinstalled a host that
did not need it, citing my own documentation.

> **In plain terms.** The dangerous moment is not when you lack a rule. It is
> when you have one that worked before, applied to a situation that merely
> resembles the last one.

## Naming the thread

Four parts in, it is the same shape every time.

- **Part 1** — a resource that plans cleanly and cannot work. The plan is a
  report; the enablement is the object.
- **Part 2** — accepted, created, in progress, recorded. Four replies that
  described a request while the world stayed unchanged.
- **Part 3** — a summary line that said `3 to destroy` while the rendered plan
  showed three unrelated actions. The count was a report; the JSON was the
  object.
- **Part 4** — a timeout reported by a healthy manager, about a host that was
  saying `NET1111` to anyone who opened its log.

**Check the object, not the exit code.**

Not "do not trust tools." The tools were right every time — they answered the
question they were asked, which was almost never the question I needed answered.
A status code describes a *request*. A plan summary describes a *diff*. A
manager's view of a host describes *what the manager observed*. None of them
describe the thing itself, and the thing itself is almost always available if
you are willing to go to it.

The corollary, which Part 4 taught specifically: **going to the wrong object and
getting a clean answer counts as not checking.** Before an empty file disproves
a theory, establish that the file is where the thing would be.

## What went into the skill

Three entries, and the shape of them is the point.

**A diagnostic order, not a fix.** *Read `/var/log/nsx-syslog.log` on the host
first. NSX Manager's transport-node state only ever says "timeout."* That one
line removes the entire afternoon I spent on connectivity.

**A trap, stated as a trap.** *Do not conclude from an empty
`controller-info.xml` that there is no stale identity.* Written because the
correct hypothesis was nearly abandoned on that evidence — and because nothing
in the system will ever warn you that you looked in the wrong place.

**An ordering constraint, with its window.** Unprepare before destroying. The
cost of getting it wrong is not a longer repair; it is that repair stops being
possible.

What is *not* in there is the list of four things that did not work — except as
a table of wrong targets, which is the only part with reuse value. Nobody needs
my sequence of deletions. They need to know that host identity and manager trust
are different objects in different files, because that is the fact that would
have stopped all four.

## What's next

So far every constraint has been logical: a missing resource, a stale record, a
dependency, a certificate. Things that live in files and APIs and can be
reasoned about from a desk.

The last one in this stretch is not like that. After weeks of treating CPU and
memory as the limits that mattered, the real constraint on this lab turned out
to be **temperature** — and it had been shaping the results for longer than I
noticed.

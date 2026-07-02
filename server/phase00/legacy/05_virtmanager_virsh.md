# Linux Server Administration
## Phase 00 — Session 05
# virt-manager vs virsh

## Objective

Understand:

- the difference between GUI and CLI VM management
- why server administrators often prefer virsh
- why remote administration favors CLI tools
- why CLI tools are easier to automate
- how virtualization management fits into Linux administration

---

## Previous Architecture

```text
virt-manager      virsh
      │             │
      └──────┬──────┘
             ▼
          libvirt
             ▼
           QEMU
             ▼
            KVM
             ▼
         Hardware
```

Session 04 focused on:

```text
virt-manager
=
GUI
```

```text
virsh
=
CLI
```

This session focuses on the practical implications of that difference.

---

# Two Ways To Manage A VM

Example task:

```text
View virtual machines
```

GUI:

```text
Open virt-manager
↓
View VM list
```

CLI:

```bash
virsh list --all
```

Both accomplish the same goal.

The difference is how they scale.

---

# virt-manager

Mental model:

```text
Convenience-focused
```

Advantages:

- visual
- beginner friendly
- easy VM creation
- easy hardware configuration
- easy console access

Common usage:

```text
Personal workstation
Learning environment
Small lab
```

---

# virsh

Mental model:

```text
Automation-focused
```

Advantages:

- works over SSH
- requires no GUI
- scriptable
- lightweight
- suitable for remote servers

Examples:

```bash
virsh list --all
```

```bash
virsh start ubuntu-web
```

```bash
virsh shutdown ubuntu-web
```

```bash
virsh reboot ubuntu-web
```

---

# Remote Administration

Suppose:

```bash
ssh admin@server
```

The server is:

```text
Ubuntu Server
```

with no graphical environment.

In that situation:

```text
virt-manager
```

may not even be installed.

However:

```bash
virsh list --all
```

still works.

This is why CLI management is common in server environments.

---

# GUI vs CLI

Many beginners assume:

```text
GUI
=
Advanced
```

and

```text
CLI
=
Inconvenient
```

Server administration often views them differently.

GUI:

```text
Convenience
```

CLI:

```text
Automation
Repeatability
Remote Management
Scalability
```

---

# Scaling Problem

Suppose there is:

```text
1 server
```

Using a GUI is easy.

---

Suppose there are:

```text
100 servers
```

Now consider:

```text
Open GUI
Click
Click
Click
...
```

versus

```bash
for server in ...
do
    command
done
```

The CLI becomes dramatically more efficient.

---

# Automation

Suppose a user manually executes:

```bash
virsh start ubuntu-web
```

This is a manual task.

---

Now place the same command inside:

```bash
#!/bin/bash

virsh start ubuntu-web
```

This becomes the beginning of automation.

---

Automation allows:

```text
Repeatability
Consistency
Speed
```

---

Example Growth

Simple script:

```bash
virsh start ubuntu-web
```

Later:

```bash
virsh start ubuntu-web
sleep 5
virsh domstate ubuntu-web
virsh domifaddr ubuntu-web
```

Eventually:

```text
Start VM
↓
Verify VM
↓
Check Network
↓
Prepare Access
```

A management procedure has been created.

---

# Linux Administration Philosophy

A common progression:

```text
Learn with GUI
```

↓

```text
Operate with CLI
```

↓

```text
Automate with scripts
```

The goal is not:

```text
Avoid GUI
```

The goal is:

```text
Be capable without GUI
```

---

# Core Mental Models

### virt-manager

```text
GUI Management
```

Optimized for convenience.

---

### virsh

```text
CLI Management
```

Optimized for automation and remote administration.

---

### Server Reality

```text
SSH Available
```

is common.

```text
GUI Available
```

is not guaranteed.

---

### Automation

```text
One command
↓
Script
↓
Workflow
↓
Automation
```

---

# Example Workflow

Human:

```bash
virsh start ubuntu-web
```

Automation:

```bash
#!/bin/bash

virsh start ubuntu-web
sleep 5
virsh domstate ubuntu-web
```

Same building blocks.

Different scale.

---

# Session Summary

```text
virt-manager
=
Convenient GUI
```

```text
virsh
=
Automation-friendly CLI
```

```text
Most servers are managed remotely through SSH.
```

```text
CLI tools work even when no GUI exists.
```

```text
CLI scales better than GUI.
```

```text
Automation begins when commands become repeatable procedures.
```

```text
Learn with GUI.
Operate with CLI.
Automate with scripts.
```

---

# QA

<details>
<summary>Q1. What is the primary difference between virt-manager and virsh?</summary>

A:

</details>

<details>
<summary>Q2. Why is virsh commonly used on Linux servers?</summary>

A:

</details>

<details>
<summary>Q3. Why might virt-manager not be available on a server?</summary>

A:

</details>

<details>
<summary>Q4. Which tool is generally easier to automate: virt-manager or virsh?</summary>

A:

</details>

<details>
<summary>Q5. Why does CLI scale better than GUI when managing many systems?</summary>

A:

</details>

<details>
<summary>Q6. What role does SSH play in server administration?</summary>

A:

</details>

<details>
<summary>Q7. Why is repeatability important in administration?</summary>

A:

</details>

<details>
<summary>Q8. When does a command begin to become automation?</summary>

A:

</details>

<details>
<summary>Q9. Complete the progression:</summary>

```text
GUI
↓
CLI
↓
?
```

A:

</details>

<details>
<summary>Q10. What is the most important mindset from this session?</summary>

A:

</details>

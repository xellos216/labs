# Linux Server Administration
## Phase 00 — Session 03
# QEMU and KVM Relationship

## Objective

Understand:

- what QEMU does
- what KVM does
- why both are commonly used together
- the difference between virtualization and acceleration
- the relationship between User Space and Kernel Space

---

## Mental Model

At first glance:

```text
Physical Hardware
        │
        ▼
Arch Linux
        │
        ▼
Ubuntu VM
```

appears sufficient.

However, in practice:

```text
Physical Hardware
        │
        ▼
Arch Linux
        │
        ▼
QEMU + KVM
        │
        ▼
Ubuntu VM
```

is the common architecture.

---

# QEMU

QEMU is responsible for creating virtual hardware.

Examples:

```text
Virtual CPU
Virtual RAM
Virtual Disk
Virtual Network Card
```

Guest operating systems see these devices as if they were real hardware.

---

## QEMU Mental Model

```text
QEMU
=
Virtual Computer Builder
```

Responsibilities:

```text
Create virtual devices
Expose hardware to the guest
Manage virtual machine execution
Provide emulated hardware
```

---

## Guest Perspective

The guest operating system believes:

```text
I have a CPU.
I have RAM.
I have a disk.
I have a network card.
```

However:

```text
These devices are virtual.
```

QEMU creates the illusion of a complete computer.

---

# The Performance Problem

Suppose KVM does not exist.

The guest executes:

```bash
ls
```

```bash
python app.py
```

```bash
apt update
```

All of these eventually generate CPU instructions.

Examples:

```text
MOV
ADD
CMP
JMP
```

Without KVM:

```text
Guest Instruction
        │
        ▼
QEMU interprets instruction
        │
        ▼
Host CPU executes
```

This process works.

However:

```text
Interpretation introduces overhead.
```

---

# KVM

KVM stands for:

```text
Kernel-based Virtual Machine
```

KVM is a Linux kernel module.

Purpose:

```text
Allow guest code to execute
directly on the host CPU
when possible.
```

---

## KVM Mental Model

```text
KVM
=
CPU Accelerator
```

KVM does not create virtual hardware.

QEMU already does that.

Instead:

```text
KVM accelerates execution.
```

---

# QEMU Only

Execution flow:

```text
Guest
        │
        ▼
QEMU
(interprets instructions)
        │
        ▼
CPU
```

Result:

```text
Works
But slower
```

---

# QEMU + KVM

Execution flow:

```text
Guest
        │
        ▼
QEMU
(virtual hardware)
        │
        ▼
KVM
(kernel acceleration)
        │
        ▼
CPU
```

Result:

```text
Works
And much faster
```

---

# User Space vs Kernel Space

QEMU:

```text
User Space
```

Examples:

```bash
ps aux | grep qemu
```

QEMU appears as a normal process.

---

KVM:

```text
Kernel Space
```

Examples:

```bash
lsmod | grep kvm
```

KVM exists inside the Linux kernel.

---

# Important Observation

A virtual machine can still run without KVM.

Reason:

```text
QEMU alone can provide virtualization.
```

Example:

```text
QEMU
✓ VM Creation
✓ Virtual Hardware
```

However:

```text
No KVM
=
Less Performance
```

---

# Virtualization vs Acceleration

Virtualization:

```text
Creating a virtual computer
```

Handled primarily by:

```text
QEMU
```

---

Acceleration:

```text
Executing guest code efficiently
```

Handled primarily by:

```text
KVM
```

---

# Looking Ahead

As environments become larger:

```text
QEMU
KVM
Multiple VMs
Networks
Snapshots
Storage
```

must all be managed.

This leads to:

```text
libvirt
```

which provides a unified management layer.

---

## Core Mental Models

### QEMU

```text
Virtual Computer Builder
```

---

### KVM

```text
CPU Accelerator
```

---

### QEMU Only

```text
Guest
↓
QEMU
↓
CPU
```

Works, but slower.

---

### QEMU + KVM

```text
Guest
↓
QEMU
↓
KVM
↓
CPU
```

Works and performs much better.

---

## Session Summary

```text
QEMU
=
Virtual hardware provider
```

```text
KVM
=
Kernel-level CPU acceleration
```

```text
QEMU lives in User Space
```

```text
KVM lives in Kernel Space
```

```text
QEMU can run without KVM
```

```text
KVM improves performance
but is not responsible for creating VMs
```

```text
Virtualization
≠
Acceleration
```

---

# QA

<details>
<summary>Q1. What is the primary responsibility of QEMU?</summary>

A:

</details>

<details>
<summary>Q2. What virtual hardware can QEMU provide to a guest operating system?</summary>

A:

</details>

<details>
<summary>Q3. Why can a virtual machine still run without KVM?</summary>

A:

</details>

<details>
<summary>Q4. What problem does KVM solve?</summary>

A:

</details>

<details>
<summary>Q5. Explain the difference between virtualization and acceleration.</summary>

A:

</details>

<details>
<summary>Q6. Which component is responsible for creating virtual hardware: QEMU or KVM?</summary>

A:

</details>

<details>
<summary>Q7. Which component lives in User Space?</summary>

A:

</details>

<details>
<summary>Q8. Which component lives in Kernel Space?</summary>

A:

</details>

<details>
<summary>Q9. Complete the execution flow:</summary>

```text
Guest
↓
?
↓
KVM
↓
CPU
```

A:

</details>

<details>
<summary>Q10. Why is QEMU + KVM typically preferred over QEMU alone?</summary>

A:

</details>

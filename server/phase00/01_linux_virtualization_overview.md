# Linux Server Administration
## Phase 00 — Session 01
# Linux Virtualization Overview

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 01
Title: Linux Virtualization Overview
Status:
Review:
ArchiveVersion: 2
Date:
```

## Objective

Understand:

- why virtualization exists
- Host vs Guest
- what a hypervisor does
- how a VM relates to physical hardware
- why server administrators learn inside virtual machines

---

## Mental Model

Physical machine:

```text
CPU
RAM
Disk
NIC
│
└── Arch Linux
```

Virtualized machine:

```text
CPU
RAM
Disk
NIC
│
└── Arch Linux (Host)
        │
        └── Hypervisor
                │
                └── Ubuntu Server (Guest)
```

---

## Host and Guest

Host:

```text
The operating system running directly on physical hardware.
```

Example:

```text
Arch Linux
```

Guest:

```text
An operating system running inside a virtual machine.
```

Example:

```text
Ubuntu Server VM
```

---

## Important Observation

From the Host perspective:

```text
The VM is just another process.
```

Example:

```bash
ps aux | grep qemu
```

You may see:

```text
qemu-system-x86_64
```

running like any other application.

---

## Guest Perspective

The Guest does not think:

```text
"I am a virtual machine."
```

Instead it sees:

```text
CPU
RAM
Disk
Network Card
```

and behaves as though it were a real computer.

---

## Virtual Hardware

A VM usually receives:

```text
vCPU
vRAM
Virtual Disk
Virtual NIC
```

These are virtualized resources.

Example:

```text
4 vCPU
8 GB RAM
```

does not mean:

```text
4 physical CPUs
8 GB dedicated hardware RAM
```

It means:

```text
The Host allows the Guest
to use those resources.
```

---

## Why Use Virtual Machines?

### Isolation

Mistakes remain inside the VM.

Examples:

- firewall mistakes
- package mistakes
- service failures
- authentication failures

Host system remains unaffected.

---

### Recovery

VMs can be restored quickly.

```text
Snapshot
→ Experiment
→ Break
→ Restore
```

---

### Repeatability

The same environment can be rebuilt repeatedly.

Useful for:

- training
- testing
- documentation
- troubleshooting

---

### Remote Administration Practice

VMs allow realistic workflows.

Example:

```text
Host
│
└── SSH
        │
        └── Ubuntu Server VM
```

This resembles real server administration.

---

## Networking Preview

A VM may have its own:

```text
IP address
```

even though the Host only has one physical network card.

Typical flow:

```text
VM
→ Virtual NIC
→ Virtual Network
→ Host NIC
→ Internet
```

Multiple VMs can share a single physical NIC.

---

## Key Concepts

### Hypervisor

Software that allows virtual machines to run.

Responsibilities:

- create virtual hardware
- schedule CPU usage
- manage memory
- provide virtual devices

---

### QEMU

Provides virtual hardware emulation.

Example:

```text
Virtual CPU
Virtual Disk
Virtual NIC
```

---

### KVM

Linux kernel virtualization support.

Purpose:

```text
Run guest code directly on the CPU
when possible.
```

Result:

```text
Much faster virtualization.
```

---

## Core Mental Model

```text
Physical Hardware
        │
        ▼
Host OS
(Arch Linux)
        │
        ▼
QEMU + KVM
        │
        ▼
Guest OS
(Ubuntu Server)
```

---

## Session Summary

```text
Host = Real operating system

Guest = Virtual operating system

Hypervisor = Creates virtual hardware

QEMU = Virtual machine process

KVM = Hardware-assisted acceleration

VM = A process from the Host perspective

VM = A complete computer from the Guest perspective
```

---

# QA

### Q1. What is the difference between a Host OS and a Guest OS?

<details>
<summary>A</summary>

</details>

### Q2. From the Host perspective, what is a virtual machine?

<details>
<summary>A</summary>

</details>

### Q3. From the Guest perspective, what hardware does it believe it owns?

<details>
<summary>A</summary>

</details>

### Q4. Why does assigning 4 vCPUs not mean giving the VM four physical CPUs?

<details>
<summary>A</summary>

</details>

### Q5. Why are snapshots valuable during administration training?

<details>
<summary>A</summary>

</details>

### Q6. Why are virtual machines safer than experimenting directly on the Host?

<details>
<summary>A</summary>

</details>

### Q7. Explain the relationship between QEMU and KVM.

<details>
<summary>A</summary>

</details>

### Q8. Complete the model:

```text
Physical Hardware
        │
        ▼
?
        │
        ▼
?
        │
        ▼
Guest OS
```

<details>
<summary>A</summary>

</details>

### Q9. Why can multiple VMs use the internet even when the Host only has one physical NIC?

<details>
<summary>A</summary>

</details>

### Q10. What is the most important mental model from this session?

<details>
<summary>A</summary>

</details>

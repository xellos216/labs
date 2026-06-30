# Linux Server Administration
## Phase 00 — Session 04
# libvirt Architecture

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 04
Title: libvirt Architecture
Status:
Review:
ArchiveVersion: 2
Date:
```

## Objective

Understand:

- why QEMU/KVM alone becomes difficult to manage
- what libvirt does
- what virsh does
- what virt-manager does
- where VM configuration is stored
- the difference between VM execution and VM management

---

## Starting Mental Model

Previous sessions built this model:

```text
Guest VM
        │
        ▼
QEMU
        │
        ▼
KVM
        │
        ▼
CPU
```

This is enough to run a VM.

However, it is not convenient for managing many VMs.

---

## The Management Problem

Direct QEMU usage may require long commands.

Example:

```bash
qemu-system-x86_64 \
  -m 4096 \
  -smp 2 \
  -drive file=ubuntu.qcow2 \
  -netdev ...
```

This becomes difficult when managing:

```text
ubuntu-web
ubuntu-db
ubuntu-test
ubuntu-backup
ubuntu-monitoring
```

Problems:

- remembering each VM name
- remembering CPU and RAM settings
- remembering disk paths
- remembering network settings
- starting and stopping VMs consistently
- managing snapshots
- managing autostart behavior
- recovering configuration after reboot

---

# VM Definitions

VM settings must survive reboot.

Therefore, they cannot exist only in:

```text
QEMU process memory
```

because process memory disappears when the process exits.

Instead, VM definitions are stored as persistent configuration.

Common form:

```text
XML configuration
```

Example:

```xml
<domain>
  <name>ubuntu-web</name>
  <memory>4096</memory>
  <vcpu>2</vcpu>
</domain>
```

This allows the same VM to be recreated later.

---

# libvirt

libvirt is a virtualization management layer.

Mental model:

```text
libvirt
=
VM management platform
```

It manages:

- VM definitions
- VM start
- VM shutdown
- VM deletion
- storage
- networks
- snapshots
- autostart
- status queries

libvirt does not replace QEMU or KVM.

It manages them.

---

## libvirt Role

```text
libvirt
=
Manager above QEMU/KVM
```

It stores and controls VM configuration, then asks QEMU to run the VM with the correct settings.

---

# virsh

`virsh` is a CLI tool for controlling libvirt.

Mental model:

```text
virsh
=
libvirt command-line interface
```

Examples:

```bash
virsh list --all
virsh start ubuntu-web
virsh shutdown ubuntu-web
```

`virsh` is not QEMU itself.

It sends management requests to libvirt.

---

# virt-manager

`virt-manager` is a GUI tool for controlling libvirt.

Mental model:

```text
virt-manager
=
libvirt graphical interface
```

It allows users to manage VMs visually.

Tasks:

- create VM
- start VM
- stop VM
- attach ISO
- configure CPU/RAM
- configure disk
- configure network
- view console

---

## Important Distinction

Deleting virt-manager does not necessarily delete:

```text
VM definitions
VM disk images
libvirt
QEMU
KVM
```

Reason:

```text
virt-manager is only a management interface.
```

Existing VMs may still be managed with:

```bash
virsh
```

---

# Full Architecture

```text
virt-manager      virsh
     │              │
     └──────┬───────┘
            ▼
         libvirt
            ▼
          QEMU
            ▼
           KVM
            ▼
        Hardware
```

---

# Layer Responsibilities

## virt-manager

```text
GUI management tool
```

Used by humans for visual VM management.

---

## virsh

```text
CLI management tool
```

Used by humans or scripts for VM management.

---

## libvirt

```text
Persistent management layer
```

Stores VM definitions and controls virtualization backends.

---

## QEMU

```text
VM execution and virtual hardware provider
```

Creates virtual hardware and runs the guest VM.

---

## KVM

```text
Kernel-level CPU acceleration
```

Allows guest CPU instructions to run efficiently on real hardware.

---

# Execution vs Management

VM execution:

```text
QEMU + KVM
```

VM management:

```text
libvirt + virsh + virt-manager
```

These are related but not the same.

---

## Example Flow

When a user runs:

```bash
virsh start ubuntu-web
```

the flow is:

```text
virsh
↓
libvirt
↓
Read VM definition
↓
Start QEMU with correct settings
↓
Use KVM acceleration
↓
Guest VM runs
```

---

# Core Mental Model

```text
VM execution layer
=
QEMU + KVM
```

```text
VM management layer
=
libvirt + virsh + virt-manager
```

---

# Session Summary

```text
QEMU/KVM can run VMs directly.
```

```text
Direct QEMU commands become hard to manage.
```

```text
VM settings must be stored persistently.
```

```text
libvirt manages VM definitions and lifecycle.
```

```text
virsh is the CLI interface to libvirt.
```

```text
virt-manager is the GUI interface to libvirt.
```

```text
Deleting virt-manager does not necessarily delete VMs.
```

```text
VM execution and VM management are different layers.
```

---

# QA

### Q1. Why does direct QEMU usage become inconvenient when managing many VMs?

<details>
<summary>A</summary>

</details>

### Q2. Why should VM configuration not exist only in QEMU process memory?

<details>
<summary>A</summary>

</details>

### Q3. What is libvirt?

<details>
<summary>A</summary>

</details>

### Q4. What is virsh?

<details>
<summary>A</summary>

</details>

### Q5. What is virt-manager?

<details>
<summary>A</summary>

</details>

### Q6. Does deleting virt-manager necessarily delete existing VMs?

<details>
<summary>A</summary>

</details>

### Q7. Which layer is responsible for VM execution?

<details>
<summary>A</summary>

</details>

### Q8. Which layer is responsible for VM management?

<details>
<summary>A</summary>

</details>

### Q9. Complete the architecture:

```text
virt-manager / virsh
        ↓
?
        ↓
?
        ↓
?
        ↓
Hardware
```

<details>
<summary>A</summary>

</details>

### Q10. What is the most important distinction from this session?

<details>
<summary>A</summary>

</details>

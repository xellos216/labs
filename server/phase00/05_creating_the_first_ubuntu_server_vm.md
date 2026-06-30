# Creating the First Ubuntu Server VM

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 05
Title: Creating the First Ubuntu Server VM
Status: Draft
Review: Pending
ArchiveVersion: 2
Date: 2026-07-01
```

---

## Objective

Build a mental model for creating the first Ubuntu Server VM as an isolated Linux administration lab.

Connect the ISO, virtual disk, QEMU, KVM, and libvirt concepts from earlier sessions to one coherent VM creation flow without treating the process as a sequence of GUI clicks.

---

## Learning Summary

Creating a VM means defining a virtual computer, attaching installation media, and giving an installer a persistent virtual disk on which to create the Guest operating system.

The main flow is:

```text
VM Definition
↓
Virtual CPU / RAM / Disk / NIC
↓
Attach Ubuntu Server ISO
↓
Boot Installer
↓
Install Ubuntu onto the Virtual Disk
↓
Detach or stop booting from the ISO
↓
Boot the Installed Guest OS
```

libvirt stores and manages the VM definition. QEMU presents the configured virtual hardware, and KVM accelerates Guest CPU execution. The Ubuntu installer runs inside that virtual machine and writes the operating system to the virtual disk.

The VM is being created to provide a reproducible environment for later administration work such as networking, SSH, service management, troubleshooting, and recovery.

---

## Key Concepts

- VM definition
- Ubuntu Server ISO
- Virtual CPU
- Virtual RAM
- Virtual disk
- Virtual NIC
- Guest installer
- First boot
- Clean-install snapshot

### Resource Choices

CPU and RAM determine how much Host capacity the Guest may use. They should be sufficient for the lab without unnecessarily exhausting Host resources.

The virtual disk provides persistent Guest storage. Its configured capacity is what the Guest sees, while a thin-provisioned disk image may consume less space on the Host until data is written.

The virtual network setting determines which virtual network the Guest NIC joins. It creates network connectivity for the VM but does not itself install Ubuntu or assign all network configuration.

### Installation Media and Installed System

```text
ISO
=
Bootable installation media
```

```text
Virtual disk
=
Persistent destination for the installed Guest OS
```

The installer boots from the ISO, partitions or prepares the virtual disk, copies operating-system files, and creates bootable Guest storage. After installation, the virtual disk contains the Guest OS; the ISO remains only installation media.

### First Boot Mental Model

The first normal boot should use the installed virtual disk rather than restarting the installer from the ISO.

```text
Before installation:
ISO → Installer → Empty Virtual Disk

After installation:
Virtual Disk → Ubuntu Server
```

A snapshot taken after a verified clean installation can preserve a known baseline before later configuration experiments. It supports recovery without replacing ordinary backups or careful change records.

---

## Practical Observations

### Suggested Observation 1: VM Definition

Observation target:

- the selected vCPU and memory values
- the virtual disk path and capacity
- the attached ISO path
- the selected virtual network

Compare the intended settings with the VM definition before installation begins.

### Suggested Observation 2: Installation Destination

Observation target:

- the installer boots from the ISO
- the installer identifies a virtual disk as its destination
- the ISO and virtual disk serve different roles

Do not record an installation result until it has actually been observed.

### Suggested Observation 3: First Boot

Observation target:

- the VM boots from its installed virtual disk
- the installer does not restart unexpectedly
- the Ubuntu Server login environment becomes available

### Suggested Observation 4: Clean Baseline

After verifying a successful first boot, consider recording the VM state and creating a clean-install snapshot before beginning later administration changes.

---

## Commands / Code

```bash
virsh list --all
```

Lists VM definitions known to libvirt and their current state.

```bash
virsh dominfo <vm-name>
```

Shows high-level information about a VM definition, including state, vCPU count, and configured memory.

```bash
virsh domblklist <vm-name>
```

Shows the storage devices and backing paths attached to a VM.

```bash
virsh snapshot-list <vm-name>
```

Lists snapshots already associated with a VM. It does not create a snapshot.

---

## Connections

```text
ISO and qcow2
↓
QEMU and KVM
↓
libvirt VM Definition
↓
Ubuntu Installation
↓
First Boot
↓
VM Hardware Observation
```

Session 05 turns the components from earlier sessions into a usable Guest system. Session 06 then observes the virtual hardware from inside that Guest and relates it back to the Host-side definition.

---

## Common Misconceptions

### Incorrect

```text
The ISO is the installed Ubuntu system.
```

Correct:

```text
The ISO provides installation media. The installed system is written to the virtual disk.
```

### Incorrect

```text
Choosing a 40 GB virtual disk always consumes 40 GB on the Host immediately.
```

Correct:

```text
A thin-provisioned disk image can grow as data is written, up to its configured capacity.
```

### Incorrect

```text
Creating a VM definition means Ubuntu is already installed.
```

Correct:

```text
The definition creates the virtual computer. The installer still has to create the Guest OS on its disk.
```

---

## Key Takeaways

- A VM definition describes the virtual computer; it is not the installed operating system.
- The ISO supplies the installer, while the virtual disk stores the installed Guest OS.
- CPU, RAM, disk, and network choices connect Host resources to Guest-visible hardware.
- QEMU presents virtual hardware, KVM accelerates execution, and libvirt manages the definition and lifecycle.
- A verified clean-install snapshot provides a useful recovery baseline for later lab work.

---

## Review Questions

### Q1. What distinct roles do the Ubuntu Server ISO and virtual disk serve during installation?

<details>
<summary>A</summary>

</details>

---

### Q2. How do libvirt, QEMU, and KVM contribute to creating and running the VM?

<details>
<summary>A</summary>

</details>

---

### Q3. Why does creating a VM definition not mean that Ubuntu Server is already installed?

<details>
<summary>A</summary>

</details>

---

### Q4. What should be considered when choosing CPU, RAM, disk, and network settings for a lab VM?

<details>
<summary>A</summary>

</details>

---

### Q5. What should change in the boot mental model after the installer finishes?

<details>
<summary>A</summary>

</details>

---

### Q6. Why is a snapshot useful after a clean installation has been verified?

<details>
<summary>A</summary>

</details>

---

## Next Session

```text
Next:
Phase 00
Session 06

Topic:
VM Hardware Observation
```

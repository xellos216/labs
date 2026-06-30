# VM Hardware Observation

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 06
Title: VM Hardware Observation
Status: Draft
Review: Pending
ArchiveVersion: 2
Date: 2026-07-01
```

---

## Objective

Learn how to observe CPU, memory, disk, and network devices inside an Ubuntu Server Guest and relate that Guest-visible hardware to the Host-side libvirt configuration.

The goal is to build an evidence-based model of virtual hardware without assuming specific command output in advance.

---

## Learning Summary

The Host and Guest describe the same VM from different viewpoints.

```text
Host / libvirt view
VM definition and backing resources
↓
QEMU presents virtual devices
↓
KVM accelerates Guest CPU execution
↓
Guest view
CPU, RAM, block devices, and network interfaces
```

From the Host, libvirt records configuration such as vCPU count, memory allocation, disk backing paths, and virtual network interfaces. From inside the Guest, Linux discovers those resources as usable hardware.

The Guest does not normally manage the Host's physical devices directly. It sees a virtual hardware interface provided by the virtualization stack.

---

## Key Concepts

- Host view
- Guest view
- VM definition
- vCPU
- Guest-visible memory
- Virtual block device
- Virtual NIC
- Hardware discovery
- QEMU device presentation
- KVM acceleration
- libvirt management

### vCPU Observation

The configured vCPU count describes how many virtual processors are exposed to the Guest. Guest tools report the processors available inside the VM, while the Host schedules their execution on physical CPU resources.

### Memory Observation

The Guest treats assigned memory as its available system RAM. Host-side configuration defines the allocation, while Guest tools show how Linux recognizes and uses that memory.

### Disk Observation

The Guest sees block devices rather than Host file paths. A Guest disk such as `/dev/vda` may be backed by a qcow2 image stored elsewhere on the Host.

```text
Guest block device
↓
Virtual storage controller
↓
QEMU
↓
Host disk image or storage volume
```

### Network Interface Observation

The Guest sees a network interface with its own link state and MAC address. On the Host, libvirt and QEMU connect that Virtual NIC to a virtual network.

---

## Practical Observations

### Suggested Observation 1: CPU

Observation target:

- compare the configured vCPU count with the processors visible inside the Guest
- distinguish virtual processors from physical CPU ownership
- inspect architecture and virtualization-related fields without assuming their values

### Suggested Observation 2: Memory

Observation target:

- compare configured memory with memory reported by the Guest
- distinguish total memory from currently available or used memory
- note that reporting units and reserved memory may affect displayed values

### Suggested Observation 3: Block Devices

Observation target:

- identify the Guest's disks and partitions
- relate a Guest block device to its Host-side backing path
- distinguish the configured virtual capacity from current Host storage consumption

### Suggested Observation 4: Network Interface

Observation target:

- identify the Guest's interfaces and MAC addresses
- relate the Guest Virtual NIC to the Host-side libvirt interface definition
- defer IP-assignment reasoning to the later DHCP session

---

## Commands / Code

### Guest Commands

```bash
lscpu
```

Shows the CPU architecture and logical processors visible to the Guest.

```bash
cat /proc/cpuinfo
```

Shows per-processor information exposed by the Guest kernel.

```bash
free -h
```

Summarizes Guest memory totals and current usage in human-readable units.

```bash
cat /proc/meminfo
```

Provides detailed memory information reported by the Guest kernel.

```bash
lsblk
```

Shows Guest block devices, partitions, and their relationships.

```bash
ip addr
```

Shows Guest network interfaces and any assigned addresses.

```bash
hostnamectl
```

Shows the Guest hostname and operating-system information, with environment details when available.

### Host Commands

```bash
virsh dominfo <vm-name>
```

Shows configured VM-level CPU and memory information from libvirt's perspective.

```bash
virsh domblklist <vm-name>
```

Maps Guest storage targets to Host-side backing sources.

```bash
virsh domiflist <vm-name>
```

Shows virtual network interfaces attached to the VM from the Host side.

---

## Connections

```text
VM Creation
↓
libvirt Definition
↓
QEMU Virtual Hardware
↓
Guest Hardware Discovery
↓
Virtual Network Fundamentals
```

This session verifies the hardware model prepared during VM creation. The observed Virtual NIC becomes the starting point for Session 07's virtual networking model and Session 08's DHCP reasoning.

---

## Common Misconceptions

### Incorrect

```text
The Guest sees the Host's physical hardware exactly as it exists.
```

Correct:

```text
The Guest sees hardware interfaces presented by the virtualization stack.
```

### Incorrect

```text
A Guest disk name reveals the Host path of its qcow2 file.
```

Correct:

```text
The Guest sees a block device. Host-side tools are needed to identify its backing source.
```

### Incorrect

```text
If the Guest reports multiple CPUs, it owns that many physical CPUs.
```

Correct:

```text
The Guest sees vCPUs whose execution is scheduled on Host CPU resources.
```

---

## Key Takeaways

- Host configuration and Guest observation are two views of the same VM.
- The Guest sees vCPUs, memory, block devices, and Virtual NICs as usable hardware.
- QEMU presents virtual devices, KVM accelerates CPU execution, and libvirt manages configuration.
- Guest block-device names do not directly reveal Host backing paths.
- Hardware commands provide evidence; their actual output must be observed rather than invented.

---

## Review Questions

### Q1. How do the Host view and Guest view of VM hardware differ?

<details>
<summary>A</summary>

</details>

---

### Q2. Why does a Guest-visible vCPU not represent exclusive ownership of a physical CPU?

<details>
<summary>A</summary>

</details>

---

### Q3. How can Guest and Host tools be combined to relate a block device to its backing storage?

<details>
<summary>A</summary>

</details>

---

### Q4. What evidence should be compared when checking the VM's configured and Guest-visible memory?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does the Guest see a network interface even though it does not own a physical NIC?

<details>
<summary>A</summary>

</details>

---

### Q6. What roles do libvirt, QEMU, and KVM play in the hardware observed by the Guest?

<details>
<summary>A</summary>

</details>

---

## Next Session

```text
Next:
Phase 00
Session 07

Topic:
Virtual Network Fundamentals
```

# Linux Server Administration
## Phase 00 — Session 02
# Installing the Lab Environment

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 02
Title: Installing the Lab Environment
Status:
Review:
ArchiveVersion: 2
Date:
```

## Objective

Understand:

- what components are required to build a virtual machine
- what an ISO file actually is
- where a VM disk exists
- how a virtual disk differs from a physical disk
- how disk image growth works

---

## Mental Model

A virtual machine typically requires:

```text
CPU
RAM
Disk
Network
ISO
```

Each component serves a different purpose.

---

## VM Components

### CPU

Provides computational resources.

Guest perspective:

```text
4 CPUs
```

Host perspective:

```text
4 vCPUs
```

These are scheduled onto the physical CPU by the Host.

---

### RAM

Temporary working memory.

Used for:

- running processes
- kernel memory
- caches
- application data

Guest sees it as physical RAM.

---

### Disk

Persistent storage.

Used for:

- operating system files
- user data
- logs
- packages
- configuration files

Guest sees it as a normal SSD or HDD.

---

### Network

Provides communication.

Allows the Guest to:

- access the internet
- communicate with the Host
- communicate with other machines
- receive SSH connections

Guest typically sees a normal network interface.

Example:

```text
eth0
ens3
```

---

### ISO

An installation medium.

Think of it as:

```text
Installation DVD
stored as a file
```

It usually contains:

- boot environment
- installer
- packages required for installation

It is not an installed operating system.

---

## What Is An ISO?

Example:

```text
ubuntu-24.04-live-server-amd64.iso
```

This is similar to:

```text
Windows installation USB
```

but stored as a single file.

Purpose:

```text
Boot
→ Install
→ Configure
→ Create Operating System
```

---

## VM Disk Mental Model

When creating a VM:

```text
Disk = 30 GB
```

many people assume:

```text
30 GB partition created immediately
```

but that is usually not what happens.

Instead:

```text
Host Filesystem
        │
        ▼
ubuntu-server.qcow2
```

The disk often exists as a file.

---

## qcow2

A common virtual disk format.

Mental model:

```text
qcow2
=
Virtual SSD
```

Example:

```text
~/VMs/
└── ubuntu-server.qcow2
```

Guest perspective:

```text
I have a 30 GB SSD.
```

Host perspective:

```text
I have a disk image file.
```

---

## Deleting The Disk Image

Suppose:

```bash
rm ubuntu-server.qcow2
```

and that file contains the VM disk.

Result:

```text
Guest storage disappears.
```

In practice:

```text
VM cannot boot
```

or

```text
Entire operating system is lost
```

because the virtual disk itself was removed.

---

## Thin Provisioning

Suppose:

```text
VM Disk Size
=
100 GB
```

This does not necessarily mean:

```text
100 GB immediately consumed
```

Instead:

```text
100 GB maximum capacity
```

is reserved conceptually.

Actual usage grows as data is written.

Example:

```text
Initial Install
≈ 4 GB
```

Later:

```text
4 GB
→ 8 GB
→ 15 GB
→ 30 GB
```

as files are added.

---

## Important Distinction

```text
Guest Visible Disk Size
≠
Host Consumed Disk Size
```

Example:

```text
Guest sees:
100 GB SSD
```

while

```text
Host actually stores:
4 GB qcow2 file
```

until more data is written.

---

## Core Mental Models

### Installation Flow

```text
ISO
↓
Boot Installer
↓
Install Ubuntu
↓
Write Files
↓
Virtual Disk
```

---

### Virtual Disk

```text
Guest SSD
=
Host File
```

---

### Thin Provisioning

```text
Maximum Size
≠
Current Usage
```

---

## Session Summary

```text
ISO
=
Installation media
```

```text
qcow2
=
Virtual disk image
```

```text
Guest SSD
=
Host file
```

```text
Deleting qcow2
=
Destroying the virtual disk
```

```text
100 GB virtual disk
≠
100 GB immediately consumed
```

```text
Disk image grows
as data is written
```

---

# QA

### Q1. What are the five common components configured when creating a VM?

<details>
<summary>A</summary>

</details>

### Q2. What is the purpose of an ISO file?

<details>
<summary>A</summary>

</details>

### Q3. Why is an ISO not considered an installed operating system?

<details>
<summary>A</summary>

</details>

### Q4. What does the Guest believe the virtual disk to be?

<details>
<summary>A</summary>

</details>

### Q5. What is a qcow2 file?

<details>
<summary>A</summary>

</details>

### Q6. Why can deleting a qcow2 file prevent a VM from booting?

<details>
<summary>A</summary>

</details>

### Q7. Explain the difference between Guest disk size and Host disk usage.

<details>
<summary>A</summary>

</details>

### Q8. What is Thin Provisioning?

<details>
<summary>A</summary>

</details>

### Q9. A VM is configured with a 100 GB disk but the qcow2 file is only 5 GB. Why is this possible?

<details>
<summary>A</summary>

</details>

### Q10. Complete the model:

```text
ISO
↓
?
↓
?
↓
Virtual Disk
```

<details>
<summary>A</summary>

</details>

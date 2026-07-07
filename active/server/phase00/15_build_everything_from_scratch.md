# Linux Server Administration
## Phase 00 — Session 15
# Build Everything From Scratch

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 15
Title: Build Everything From Scratch
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-07
```

---

# Objective

Integrate the complete Phase 00 lab model from VM creation to networking, SSH administration, snapshot safety, and failure recovery.

The goal is to explain how the major components fit together:

```text
QEMU / KVM / libvirt
↓

virtual disk / virtual NIC
↓

DHCP / DNS / route
↓

netplan / systemd-networkd
↓

SSH
↓

snapshot / recovery
```

---

# Learning Summary

Phase 00 builds a complete Linux administration lab inside a virtual machine.

The stack begins on the physical machine and Host operating system:

```text
Physical Hardware
↓

Arch Linux Host
↓

virt-manager / virsh
↓

libvirt
↓

QEMU
↓

KVM
↓

Ubuntu Server Guest
```

The roles are distinct:

```text
QEMU
=
VM execution layer and virtual hardware provider
```

```text
KVM
=
Linux kernel hardware virtualization acceleration
```

```text
libvirt
=
VM management layer
```

```text
virt-manager
=
GUI frontend for libvirt
```

```text
virsh
=
CLI tool for libvirt
```

A key correction from the session is that KVM is not a virtual kernel. It is a Linux kernel feature that helps QEMU use CPU virtualization efficiently. Another correction is that virt-manager and virsh are not package managers. They are VM management tools that control libvirt.

The VM disk model is also layered:

```text
ISO
=
installation media
```

```text
qcow2
=
Host-side virtual disk file used by the Guest as a disk
```

After installation, the Guest writes its system state to the qcow2 disk image.

Networking is also perspective-dependent:

```text
Guest view
↓

ens3
```

```text
Host view
↓

vnet0
```

`ens3` is the Guest-side virtual network interface. `vnet0` is the Host-side connection point that links the VM into the Host's virtual network.

The Guest receives network configuration through DHCP:

```text
Guest ens3
↓

DHCP Discover / Request
↓

libvirt virtual network
↓

dnsmasq DHCP server
↓

DHCP Offer / Ack
↓

IP / Gateway / DNS received
```

Inside Ubuntu Server, netplan declares the intended network configuration:

```yaml
network:
  version: 2
  ethernets:
    ens3:
      dhcp4: true
```

This means that `ens3` should use DHCP for IPv4 configuration. The YAML file does not perform DHCP by itself. The runtime application path is:

```text
netplan configuration
↓

netplan apply
↓

systemd-networkd
↓

DHCP request and runtime interface state
```

SSH then uses the working network to provide remote administration:

```text
Host terminal
↓

ssh client
↓

TCP/IP network
↓

VM port 22
↓

sshd
↓

authentication
↓

remote shell
```

SSH failure should be diagnosed by layer. DHCP and netplan are not normally checked after `sshd` in the SSH flow. They are lower-layer causes to inspect when the VM has no IP address or network configuration.

A better diagnostic order is:

```text
VM alive?
↓

Guest has IP?
↓

Host can reach VM IP?
↓

Route / virtual network OK?
↓

TCP 22 reachable?
↓

sshd running?
↓

Firewall allows SSH?
↓

Authentication succeeds?
↓

Shell opens?
```

If the Guest does not have an IP, then investigate:

```text
netplan correct?
↓

dhcp4: true?
↓

systemd-networkd running?
↓

libvirt DHCP working?
```

Snapshots provide the recovery structure for risky experiments:

```text
Known Good State
↓

Snapshot
↓

Risky Change
↓

Failure
↓

Rollback or manual repair
↓

Verification
```

Without a snapshot, recovery usually requires console access, configuration repair, reapplying network settings, checking runtime service state, and verifying IP, route, DNS, and SSH again. With a snapshot, the VM can return to the known good state more quickly.

---

# Key Concepts

- QEMU
- KVM
- libvirt
- virt-manager
- virsh
- ISO
- qcow2
- virtual NIC
- Guest-side interface
- Host-side vnet interface
- DHCP
- DNS
- netplan
- systemd-networkd
- SSH
- snapshot
- rollback
- failure recovery

---

# Practical Observations

## Observation 1

```text
Prediction

↓

QEMU, KVM, libvirt, virt-manager, and virsh occupy different layers.

↓

Observation

↓

QEMU runs the VM and provides virtual hardware. KVM accelerates CPU virtualization. libvirt manages VM definitions and lifecycle. virt-manager and virsh control libvirt.

↓

Explanation

Virtualization is not one component. It is a layered system with execution, acceleration, management, and user-interface layers.
```

---

## Observation 2

```text
Prediction

↓

qcow2 is the VM's disk, not the installer ISO.

↓

Observation

↓

The ISO is used to install the operating system. The installed Guest system is stored in the qcow2 virtual disk.

↓

Explanation

Installation media and persistent virtual disk state solve different problems.
```

---

## Observation 3

```text
Prediction

↓

ens3 and vnet0 are different perspectives of the virtual network path.

↓

Observation

↓

The Guest sees ens3. The Host sees vnet0.

↓

Explanation

The same virtual network connection appears differently depending on whether it is observed from inside the Guest or from the Host.
```

---

## Observation 4

```text
Prediction

↓

The VM receives IP, gateway, and DNS through DHCP.

↓

Observation

↓

The Guest sends a DHCP request through ens3 into the libvirt virtual network and receives configuration from the Host-side DHCP service.

↓

Explanation

The Guest does not invent its own address. The virtual network provides configuration.
```

---

## Observation 5

```text
Prediction

↓

netplan declares DHCP use, but systemd-networkd performs runtime network behavior.

↓

Observation

↓

The YAML file records desired state. Runtime services apply it and update kernel network state.

↓

Explanation

Configuration declaration and runtime application are separate layers.
```

---

## Observation 6

```text
Prediction

↓

SSH failure should be diagnosed in network and service layers.

↓

Observation

↓

Failure can occur at VM power state, IP assignment, route, TCP port 22, sshd, firewall, authentication, or shell startup.

↓

Explanation

End-to-end remote administration depends on multiple layers working together.
```

---

## Observation 7

```text
Prediction

↓

Snapshots make risky experiments safer.

↓

Observation

↓

Without a snapshot, the learner must repair the broken configuration manually. With a snapshot, the learner can rollback to a known good state.

↓

Explanation

Recoverability makes failure-driven learning practical and repeatable.
```

---

# Commands / Code

```bash
virt-manager
```

Starts the GUI frontend for managing libvirt VMs.

---

```bash
virsh list --all
```

Lists libvirt-managed VMs from the command line.

---

```bash
ip addr
```

Shows current interface and address state inside the Host or Guest.

---

```bash
ip route
```

Shows the runtime routing table.

---

```bash
cat /etc/netplan/*.yaml
```

Shows declared netplan configuration inside Ubuntu Server.

---

```bash
sudo netplan apply
```

Applies declared netplan configuration.

---

```bash
networkctl status
```

Shows systemd-networkd-managed interface state.

---

```bash
systemctl status systemd-networkd
```

Checks the runtime network manager service state.

---

```bash
ssh user@VM_IP
```

Starts an SSH client connection to the VM by direct IP.

---

```bash
systemctl status ssh
```

Checks SSH service state on Ubuntu systems where the service is named `ssh`.

---

```bash
ss -tulpen | grep ':22'
```

Checks whether TCP port 22 is listening.

---

```bash
virsh snapshot-list VM_NAME
```

Lists snapshots for a VM when supported by the VM and storage configuration.

---

# Connections

```text
Physical Hardware
↓

Host OS
↓

QEMU / KVM / libvirt
↓

Ubuntu Server Guest
```

---

```text
Guest ens3
↓

Host vnet0
↓

libvirt virtual network
↓

DHCP / DNS / NAT
```

---

```text
netplan YAML
↓

systemd-networkd
↓

kernel network state
↓

IP / route / DNS
```

---

```text
IP / route
↓

TCP 22
↓

sshd
↓

authentication
↓

shell
```

---

```text
Risky change
↓

Failure
↓

Manual repair or snapshot rollback
↓

Verification
```

---

# Common Misconceptions

## Incorrect

```text
KVM is a virtual kernel.
```

Correct:

```text
KVM is a Linux kernel hardware virtualization acceleration feature.
```

---

## Incorrect

```text
virt-manager and virsh are package managers.
```

Correct:

```text
virt-manager and virsh are tools for controlling libvirt-managed VMs.
```

---

## Incorrect

```text
qcow2 is the same thing as the installation ISO.
```

Correct:

```text
The ISO is installation media. qcow2 is the VM's virtual disk file.
```

---

## Incorrect

```text
ens3 and vnet0 are unrelated interfaces.
```

Correct:

```text
ens3 is the Guest-side interface, while vnet0 is the Host-side connection point for the same VM network path.
```

---

## Incorrect

```text
The netplan YAML file performs DHCP by itself.
```

Correct:

```text
The YAML file declares DHCP use. systemd-networkd performs the runtime behavior.
```

---

## Incorrect

```text
DHCP/netplan should be checked after sshd in the SSH troubleshooting chain.
```

Correct:

```text
DHCP/netplan are lower-layer causes to check when the VM lacks IP configuration. They are not later than sshd in the SSH workflow.
```

---

# Key Takeaways

- Phase 00 is a complete VM lab foundation, not a list of independent tools.
- QEMU, KVM, libvirt, virt-manager, and virsh each occupy different roles.
- ISO and qcow2 represent different stages of VM installation and persistence.
- Guest-side and Host-side network interfaces provide different views of the same virtual network path.
- DHCP, DNS, and route configuration make the VM usable on the network.
- netplan declares desired network state; systemd-networkd applies runtime network behavior.
- SSH depends on IP reachability, TCP port 22, sshd, firewall, authentication, and shell availability.
- Snapshots make failure-driven learning reversible and repeatable.

---

# Review Questions

### Q1. Explain the roles of QEMU, KVM, libvirt, virt-manager, and virsh.

<details>
<summary>A</summary>

</details>

---

### Q2. What is the difference between an installation ISO and a qcow2 virtual disk?

<details>
<summary>A</summary>

</details>

---

### Q3. How are `ens3` and `vnet0` related in the virtual network path?

<details>
<summary>A</summary>

</details>

---

### Q4. How does a Guest VM receive IP, gateway, and DNS configuration through DHCP?

<details>
<summary>A</summary>

</details>

---

### Q5. What does `dhcp4: true` mean in netplan, and which component performs the runtime DHCP behavior?

<details>
<summary>A</summary>

</details>

---

### Q6. Why should SSH failure be investigated layer by layer?

<details>
<summary>A</summary>

</details>

---

### Q7. If a VM has no IP address, which lower-layer causes should be checked before blaming SSH?

<details>
<summary>A</summary>

</details>

---

### Q8. Compare manual repair and snapshot rollback after a broken network configuration.

<details>
<summary>A</summary>

</details>

---

### Q9. Complete the full Phase 00 flow:

```text
Host OS
↓

?
↓

Ubuntu Server Guest
↓

?
↓

DHCP / DNS / route
↓

?
↓

SSH administration
↓

?
```

<details>
<summary>A</summary>

</details>

---

### Q10. Why is Phase 00 useful before studying users, services, logs, security controls, and recovery in later phases?

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 01
Session 01

Topic:
Users, Groups, and Identity

How Linux represents users and groups, and how identity becomes the basis for access control.
```

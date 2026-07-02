# Linux Server Administration
## Phase 00 — Session 07
# Virtual Network Fundamentals

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 07
Title: Virtual Network Fundamentals
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-06-26
```

---

# Objective

Understand how a virtual machine communicates with the Host, other virtual machines, and the Internet.

Build a mental model of virtual network interfaces and the relationship between the Guest network stack and the Host network stack.

---

# Learning Summary

A virtual machine does not own a physical network interface.

Instead, it is given a **Virtual Network Interface Card (Virtual NIC)** by QEMU. This Virtual NIC connects to a virtual network managed by the Host operating system.

When a Guest sends a packet, it first leaves through its Virtual NIC, enters the Host's virtual networking layer, and is then either:

- forwarded to another VM,
- delivered to the Host,
- or forwarded to the Host's physical NIC toward the Internet.

Although a VM runs inside the Host, it behaves as an independent computer from the network's perspective because it owns its own IP address and network interface.

An important realization is that communication between VMs does not necessarily require the Internet. If they are attached to the same virtual network, packets may never leave the Host.

---

# Key Concepts

- Virtual NIC
- Virtual Network
- Host Network Stack
- Physical NIC
- vnet Interface
- Linux Bridge
- Guest Networking
- Host Networking

---

# Practical Observations

### Observation 1

```text
Prediction

↓

A VM uses the Host to access the Internet.

↓

Observation

↓

The VM owns only a Virtual NIC.
The Host forwards packets through its Physical NIC.

↓

Explanation

The Host acts as the bridge between the virtual network and the physical network.
```

---

### Observation 2

```text
Prediction

↓

VMs on the same Host may communicate without using the Internet.

↓

Observation

↓

Packets can remain inside the Host's virtual network.

↓

Explanation

The virtual networking layer forwards traffic directly between VMs.
```

---

### Observation 3

```text
Prediction

↓

A VM appears to be a separate machine on the network.

↓

Observation

↓

The VM has its own IP address and Virtual NIC.

↓

Explanation

Although implemented inside the Host, the Guest behaves like an independent network device.
```

---

# Commands / Code

```bash
ip link
```

Shows network interfaces on the Host, including interfaces such as `vnet0`, `vnet1`, etc.

---

```bash
ip addr
```

Displays IP addresses assigned to Host interfaces.

---

```bash
ping <ip-address>
```

Tests connectivity between the Host, Guest, or other machines.

---

# Connections

```text
Virtual NIC
↓

Virtual Network

↓

Linux Bridge / NAT

↓

Physical NIC

↓

Router

↓

Internet
```

---

```text
Virtual Networking

↓

DHCP

↓

IP Address Assignment
```

---

# Common Misconceptions

### Incorrect

```text
A VM owns a physical network card.
```

Correct:

```text
A VM owns a Virtual NIC provided by QEMU.
```

---

### Incorrect

```text
VM-to-VM communication must go through the Internet.
```

Correct:

```text
VMs attached to the same virtual network can communicate entirely inside the Host.
```

---

### Incorrect

```text
Because a VM runs inside the Host, it is the same computer from the network's perspective.
```

Correct:

```text
A VM has its own network interface and IP address, so it behaves as a separate computer on the network.
```

---

# Key Takeaways

- A VM does not directly use a physical NIC.
- The Host forwards Guest traffic to the physical network.
- Virtual NICs connect Guests to the Host's virtual network.
- VM-to-VM communication may remain entirely inside the Host.
- Network behavior and implementation location are different concepts.

---

# Review Questions

### Q1. Why does a virtual machine not require its own physical network card?

<details>
<summary>A</summary>

</details>

### Q2. Describe the path a packet takes from a Guest VM to the Internet.

<details>
<summary>A</summary>

</details>

### Q3. What is a Virtual NIC?

<details>
<summary>A</summary>

</details>

### Q4. What is the role of the Host in Guest networking?

<details>
<summary>A</summary>

</details>

### Q5. Can two VMs communicate without using the Internet? Explain why.

<details>
<summary>A</summary>

</details>

### Q6. What does a <code>vnet</code> interface represent?

<details>
<summary>A</summary>

</details>

### Q7. Why is a VM considered a separate computer from the network's perspective?

<details>
<summary>A</summary>

</details>

### Q8. Complete the packet flow:

```text
Guest
↓

Virtual NIC
↓

?

↓

Physical NIC

↓

Internet
```

<details>
<summary>A</summary>

</details>

### Q9. What command can be used to observe <code>vnet</code> interfaces on the Host?

<details>
<summary>A</summary>

</details>

### Q10. Explain the difference between where a VM runs and how it behaves on the network.

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 00
Session 08

Topic:
DHCP Observation

How a virtual machine automatically receives its IP address during boot.
```

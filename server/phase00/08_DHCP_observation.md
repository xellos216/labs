# Linux Server Administration
## Phase 00 — Session 08
# DHCP Observation

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 08
Title: DHCP Observation
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-06-30
```

---

# Objective

Understand how a virtual machine receives an IP address automatically when it joins a virtual network.

The goal is to distinguish:

```text
Virtual NIC
```

from:

```text
DHCP Server
```

and understand why the Guest does not create its own IP address.

---

# Learning Summary

A virtual machine does not invent its own IP address.

When the Guest boots, it already has a Virtual NIC. That Virtual NIC gives the Guest a network interface and a MAC address, but it does not assign an IP address.

The Guest sends a DHCP request into the virtual network. The Host-side virtual network service, commonly managed by libvirt and backed by dnsmasq, answers the request and assigns network configuration.

Typical DHCP-provided information includes:

- IP address
- subnet information
- default gateway
- DNS server

The key distinction is:

```text
Virtual NIC
=
Network device
```

```text
DHCP
=
Network configuration provider
```

---

# Key Concepts

- DHCP
- DHCP Discover
- DHCP Offer
- Virtual NIC
- MAC Address
- IP Address
- Broadcast
- dnsmasq
- libvirt default network
- Gateway
- DNS assignment

---

# Practical Observations

## Observation 1

```text
Prediction

↓

The Host gives the VM an IP address.

↓

Observation

↓

The Guest receives an IP address after joining the virtual network.

↓

Explanation

The Host-side virtual network provides DHCP service, usually through libvirt-managed dnsmasq.
```

---

## Observation 2

```text
Prediction

↓

The Virtual NIC provides the IP address.

↓

Correction

↓

The Virtual NIC provides the network interface and MAC address, not the IP address.

↓

Explanation

IP configuration is assigned by DHCP or configured manually.
```

---

## Observation 3

```text
Prediction

↓

A VM can request an IP even before it owns one.

↓

Explanation

DHCP is designed to work before the client has an IP address.

The client can send a broadcast request using:

Source IP:

```text
0.0.0.0
```

Destination IP:

```text
255.255.255.255
```
```

---

# Commands / Code

```bash
ip addr
```

Shows IP addresses assigned to interfaces inside the Guest or Host.

---

```bash
ip link
```

Shows network interfaces, including interfaces that may not have an IP address.

---

```bash
virsh net-list
```

Lists libvirt virtual networks.

---

```bash
virsh net-dhcp-leases default
```

Shows DHCP leases assigned by the libvirt default network.

---

# Connections

```text
Guest Boot
↓

Virtual NIC Exists
↓

Guest Sends DHCP Discover
↓

Host-side DHCP Server Responds
↓

Guest Receives IP Configuration
```

---

```text
Virtual NIC
↓

MAC Address
↓

DHCP Request
↓

IP Address
↓

Routing / DNS / SSH
```

---

# Common Misconceptions

## Incorrect

```text
The Virtual NIC gives the VM its IP address.
```

Correct:

```text
The Virtual NIC gives the VM a network interface and MAC address.
DHCP gives the VM its IP address.
```

---

## Incorrect

```text
A machine cannot communicate at all before it has an IP address.
```

Correct:

```text
DHCP uses broadcast behavior so a client can request configuration before owning a normal IP address.
```

---

## Incorrect

```text
The Guest should provide DHCP because the IP belongs to the Guest.
```

Correct:

```text
The DHCP server belongs on the network-management side.
In a libvirt virtual network, that role is usually handled by the Host.
```

---

# Key Takeaways

- A VM receives its IP from the network, not from itself.
- A Virtual NIC provides network presence, not full IP configuration.
- DHCP allows a machine with no IP address to request one.
- In a libvirt NAT-style virtual network, the Host commonly provides DHCP.
- Without DHCP, IP, gateway and DNS settings would need to be configured manually.
- DHCP reduces repeated manual configuration and prevents common mistakes such as IP conflicts.

---

# Review Questions

### Q1. What problem does DHCP solve?

<details>
<summary>A</summary>

</details>

---

### Q2. What does a Virtual NIC provide to a Guest VM?

<details>
<summary>A</summary>

</details>

---

### Q3. Why is it incorrect to say that the Virtual NIC assigns the IP address?

<details>
<summary>A</summary>

</details>

---

### Q4. How can a Guest request an IP address before it already has one?

<details>
<summary>A</summary>

</details>

---

### Q5. What is the role of the Host-side DHCP server in a libvirt virtual network?

<details>
<summary>A</summary>

</details>

---

### Q6. What information can DHCP provide besides an IP address?

<details>
<summary>A</summary>

</details>

---

### Q7. What would need to be configured manually if DHCP did not exist?

<details>
<summary>A</summary>

</details>

---

### Q8. Complete the flow:

```text
Guest
↓

?
↓

Virtual Network
↓

?
↓

DHCP Offer
↓

Guest receives IP
```

<details>
<summary>A</summary>

</details>

---

### Q9. Why is DHCP naturally provided by the network-management side rather than by each Guest?

<details>
<summary>A</summary>

</details>

---

### Q10. How does DHCP prepare the VM for later SSH administration?

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 00
Session 09

Topic:
DNS Observation

How the VM resolves domain names after receiving network configuration.
```

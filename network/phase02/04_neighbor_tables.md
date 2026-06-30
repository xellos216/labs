# Phase 02 - Session 04

## Metadata

```yaml
Roadmap: Networking
Phase: 02
Session: 04
Title: Neighbor Tables
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-06-26
```

---

# Objective

Understand why Linux maintains a Neighbor Table, how it maps IP addresses to MAC addresses, and why each entry has a state that changes over time.

---

# Learning Summary

A Linux system cannot transmit an Ethernet frame using only an IP address. Before sending traffic on a local network, it must determine the destination MAC address.

The Neighbor Table stores recently learned IP-to-MAC mappings so Linux does not need to perform ARP for every packet.

An important realization is that the Neighbor Table stores more than just IP and MAC addresses. Each entry also has a state representing how trustworthy or recent the information is.

Because network devices, interfaces, and topology can change, Linux periodically reevaluates cached entries instead of trusting them forever.

---

# Key Concepts

- Neighbor Table
- ARP Cache
- IP Address
- MAC Address
- Neighbor State
- REACHABLE
- STALE
- Dynamic Cache

---

# Practical Observations

### Prediction

Neighbor information cannot remain valid forever because devices and network conditions may change.

↓

### Observation

Neighbor entries changed state automatically over time.

↓

### Explanation

Linux gradually reduces its confidence in cached information instead of assuming it is permanently correct.

---

### Prediction

Communicating with a stale neighbor should cause Linux to verify the entry again.

↓

### Observation

An entry changed from `STALE` back to `REACHABLE` after communication resumed.

↓

### Explanation

Successful communication refreshed Linux's confidence in the cached IP-to-MAC mapping without requiring a new permanent entry.

---

# Commands / Code

```bash
ip neigh
```

Displays the current Neighbor Table, including IP addresses, MAC addresses, network interfaces, and entry states.

---

```bash
ping <destination-ip>
```

Generates network traffic that may refresh a stale Neighbor Table entry.

---

# Connections

```text
IP Address
        ↓
Neighbor Table
        ↓
MAC Address
        ↓
Ethernet Frame
        ↓
Packet Transmission
```

This session provides the foundation for the next topic, where Linux first decides **where** to send a packet (Routing Table) before determining **how** to reach the next hop (Neighbor Table). :contentReference[oaicite:0]{index=0}

---

# Common Misconceptions

- The Neighbor Table is not simply an IP-to-MAC lookup table.
- Neighbor entries are not permanent.
- Linux does not blindly trust cached MAC addresses forever.
- `STALE` does not mean the entry is invalid; it means Linux has not verified it recently.

---

# Key Takeaways

- Linux uses the Neighbor Table to map IP addresses to MAC addresses.
- Neighbor entries include both address information and a confidence state.
- Cached information becomes less trusted over time.
- Communication can refresh an entry from `STALE` to `REACHABLE`.
- The Neighbor Table reduces unnecessary ARP traffic while remaining adaptive to network changes.

---

# Review Questions

### Q1. Why does Linux maintain a Neighbor Table instead of sending an ARP request for every packet?

<details>
<summary>A</summary>

</details>

---

### Q2. Why is storing only an IP-to-MAC mapping insufficient for Linux?

<details>
<summary>A</summary>

</details>

---

### Q3. What does the `STALE` state indicate about a Neighbor Table entry?

<details>
<summary>A</summary>

</details>

---

### Q4. Why can a `STALE` entry become `REACHABLE` again?

<details>
<summary>A</summary>

</details>

---

### Q5. How does the Neighbor Table support Ethernet communication after a routing decision has been made?

<details>
<summary>A</summary>

</details>

---

### Q6. Why doesn't Linux trust Neighbor Table entries forever?

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Next:
Phase 02
Session 05

Topic:
Routing Tables
```

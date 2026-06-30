# Phase 02 - Session 05

## Metadata

```yaml
Roadmap: Networking
Phase: 02
Session: 05
Title: Routing Tables
Status: Completed
Review: Pending
Date: 2026-06-30
```

---

# Objective

Understand how Linux uses the routing table to decide where to send packets, which interface to use, and which next hop should receive the Ethernet frame.

---

# Learning Summary

Routing Tables answer the question:

```text
Where should this destination IP be sent next?
```

Before Linux can resolve a MAC address with the Neighbor Table, it must first decide which route applies to the destination IP.

The routing table determines:

```text
Destination IP
        ↓
Matching Route
        ↓
Outgoing Interface
        ↓
Next Hop
```

For external destinations such as `8.8.8.8`, Linux uses a `default` route when no more specific route matches.

For local-link destinations such as `192.168.0.1` or `175.208.176.254`, Linux uses the directly connected network route, not the default route.

---

# Key Concepts

- Routing Table
- Default Route
- Directly Connected Route
- Next Hop
- Gateway
- Interface Selection
- Metric
- Longest Prefix Match
- Neighbor Table Relationship

---

# Practical Observations

### Observation 1 — Default Route Selection

Routing table:

```text
default via 175.208.176.254 dev enp85s0 proto dhcp src 175.208.176.64 metric 100
default via 192.168.0.1 dev wlp86s0 proto dhcp src 192.168.0.104 metric 600
```

Prediction:

```text
8.8.8.8 is not inside a directly connected LAN.
Therefore Linux should use the default route.
```

Explanation:

```text
8.8.8.8
        ↓
No match for 175.208.176.0/24
No match for 192.168.0.0/24
        ↓
Use default route
        ↓
Two default routes exist
        ↓
Choose lower metric
        ↓
enp85s0 via 175.208.176.254
```

---

### Observation 2 — Directly Connected Wi-Fi Route

Routing table:

```text
192.168.0.0/24 dev wlp86s0 proto kernel scope link src 192.168.0.104 metric 600
```

Destination:

```text
192.168.0.1
```

Explanation:

```text
192.168.0.1
        ↓
Matches 192.168.0.0/24
        ↓
Use wlp86s0 directly
```

Important correction:

```text
192.168.0.1 is the Wi-Fi gateway,
but the reason wlp86s0 is selected is not because Linux is using the default route.

The reason is that 192.168.0.1 belongs to the directly connected
192.168.0.0/24 network.
```

Linux sends the frame directly to the gateway device because the gateway is on the same local link.

---

### Observation 3 — Directly Connected Ethernet Route

Routing table:

```text
175.208.176.0/24 dev enp85s0 proto kernel scope link src 175.208.176.64 metric 100
```

Destination:

```text
175.208.176.254
```

Explanation:

```text
175.208.176.254
        ↓
Matches 175.208.176.0/24
        ↓
Use enp85s0 directly
```

This means:

```text
175.208.176.0/24
        ↓
Do not send through another gateway.
Send directly on enp85s0.
```

The gateway itself is reachable because it is on the same local Ethernet link.

---

# Commands / Code

```bash
ip route
```

Shows the routing table.

Useful for observing:

- destination routes
- default routes
- gateway addresses
- outgoing interfaces
- source addresses
- route metrics

---

```bash
ip route get 8.8.8.8
```

Asks the kernel which route it would use for a specific destination.

This is useful because `ip route` shows the table, while `ip route get <IP>` shows the actual routing decision.

---

```bash
ip route get 192.168.0.1
```

Shows how Linux handles a destination on the Wi-Fi local network.

---

```bash
ip route get 175.208.176.254
```

Shows how Linux handles a destination on the Ethernet local network.

---

```bash
ip neigh
```

Shows the Neighbor Table.

After the routing decision chooses the next hop, Linux uses the Neighbor Table or ARP to find the next hop's MAC address.

---

# Routing Decision Model

Linux does not always use the default route first.

Routing decision order:

```text
1. Find the most specific route matching the destination IP.

2. If multiple routes have the same specificity, compare metric.

3. If no specific route matches, use the default route.
```

The `default` route is effectively:

```text
0.0.0.0/0
```

It matches all IPv4 destinations, but it is the least specific route.

---

# Routing Table and Neighbor Table Relationship

Routing Table:

```text
Destination IP
        ↓
Outgoing Interface
        ↓
Next Hop IP
```

Neighbor Table:

```text
Next Hop IP
        ↓
Next Hop MAC
```

Combined packet flow:

```text
Destination IP
        ↓
Routing Table
        ↓
Outgoing Interface + Next Hop IP
        ↓
Neighbor Table / ARP
        ↓
Next Hop MAC
        ↓
Ethernet Frame
        ↓
Transmission
```

---

# Important Distinction

For Internet destinations:

```text
Destination IP
        ↓
Gateway IP
        ↓
Gateway MAC
```

Not:

```text
Destination IP
        ↓
Destination MAC
```

Example:

```text
8.8.8.8
        ↓
Routing Table
        ↓
Next Hop = 175.208.176.254
        ↓
Neighbor Table
        ↓
MAC = 70:30:5d:09:50:f7
        ↓
Ethernet frame sent through enp85s0
```

ARP does not find the MAC address of `8.8.8.8`.

ARP finds the MAC address of the next hop on the local network.

---

# Connections

```text
Application
        ↓
Socket
        ↓
Destination IP
        ↓
Routing Table
        ↓
Outgoing Interface + Next Hop IP
        ↓
Neighbor Table
        ↓
Next Hop MAC
        ↓
Ethernet Frame
        ↓
Network Transmission
```

This session connects directly to:

```text
Session 03 — ARP
        ↓
Session 04 — Neighbor Tables
        ↓
Session 05 — Routing Tables
        ↓
Session 06 — Default Gateway
```

---

# Common Misconceptions

- Incorrect: Linux always uses the lowest-metric interface.
- Correct: Linux first chooses the most specific matching route, then compares metric if needed.

---

- Incorrect: The default route is used for all traffic.
- Correct: The default route is used only when no more specific route matches.

---

- Incorrect: ARP finds the MAC address of the final Internet destination.
- Correct: For off-LAN destinations, ARP finds the MAC address of the next hop gateway.

---

- Incorrect: A gateway is reached through another gateway.
- Correct: A gateway must itself be reachable on a directly connected local network.

---

# Key Takeaways

- Routing Tables decide where a packet should go next.
- Directly connected network routes are more specific than the default route.
- `default` is used only when no more specific route matches.
- Metric is used when multiple candidate routes have comparable specificity.
- Routing decides the next hop before the Neighbor Table is used.
- For Internet traffic, Ethernet frames are usually addressed to the gateway MAC, not the final destination MAC.

---

# Review Questions

### Q1. What question does the routing table answer?

<details>
<summary>A</summary>

</details>

---

### Q2. What does the `default` route mean?

<details>
<summary>A</summary>

</details>

---

### Q3. Why does `8.8.8.8` use the default route in this session?

<details>
<summary>A</summary>

</details>

---

### Q4. Why does `192.168.0.1` use `wlp86s0` instead of the lower-metric `enp85s0`?

<details>
<summary>A</summary>

</details>

---

### Q5. What does this route mean?

```text
175.208.176.0/24 dev enp85s0 proto kernel scope link src 175.208.176.64 metric 100
```

<details>
<summary>A</summary>

</details>

---

### Q6. When are route metrics used?

<details>
<summary>A</summary>

</details>

---

### Q7. What does `ip route get <destination>` show that `ip route` alone does not show directly?

<details>
<summary>A</summary>

</details>

---

### Q8. For traffic to `8.8.8.8`, does ARP resolve the MAC address of `8.8.8.8` or the gateway?

<details>
<summary>A</summary>

</details>

---

### Q9. Why must the gateway be on a directly connected local network?

<details>
<summary>A</summary>

</details>

---

### Q10. Complete the packet flow:

```text
Destination IP
        ↓
?
        ↓
Outgoing Interface + Next Hop IP
        ↓
?
        ↓
Next Hop MAC
        ↓
Ethernet Frame
```

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Next:
Phase 02
Session 06

Topic:
Default Gateway
```

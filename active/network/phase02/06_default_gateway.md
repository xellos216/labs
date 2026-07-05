# Phase 02 - Session 06

## Metadata

```yaml
Roadmap: Networking
Phase: 02
Session: 06
Title: Default Gateway
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-07-02
```

---

# Objective

Understand what a default gateway is, why Linux sends off-LAN traffic to it, and how routing, ARP, neighbor tables, and traceroute evidence show the gateway's role.

---

# Learning Summary

A default gateway is the first router that receives packets from the local machine when the destination is outside the local network.

The default gateway is not DNS. DNS resolves names into IP addresses. The default gateway forwards packets toward networks that the local host cannot reach directly.

For a destination such as `8.8.8.8`, Linux first checks whether the destination belongs to a directly connected network. Since `8.8.8.8` is outside the local LAN, Linux uses the default route.

In this session, the routing decision showed:

```text
8.8.8.8 via 203.0.113.1 dev eth0 src 203.0.113.10
```

This means packets for `8.8.8.8` are sent first to the gateway `203.0.113.1` through `eth0`.

The neighbor table then showed:

```text
203.0.113.1 dev eth0 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

This means Linux knows the gateway's MAC address and can build an Ethernet frame addressed to that gateway.

Finally, `traceroute 8.8.8.8` confirmed that the first hop was:

```text
_gateway (203.0.113.1)
```

This directly confirmed that the default gateway is the first router on the path toward the external destination.

---

# Key Concepts

- Default Gateway
- Gateway
- Router
- Off-LAN Destination
- Local Network
- Routing Table
- Neighbor Table
- ARP
- Next Hop
- First Hop
- DNS vs Gateway
- Traceroute

---

# Practical Observations

## Observation 1 - External Destination

Prediction:

```text
8.8.8.8 is outside the local LAN.
```

Observation:

```text
ip route get 8.8.8.8

8.8.8.8 via 203.0.113.1 dev eth0 src 203.0.113.10 uid 1000
    cache
```

Explanation:

```text
8.8.8.8
        ↓
Not in local LAN
        ↓
Use default route
        ↓
Send to 203.0.113.1
        ↓
Use eth0
```

Linux does not try to reach `8.8.8.8` directly at Layer 2. It sends the packet to the default gateway.

---

## Observation 2 - Gateway MAC Resolution

Prediction:

```text
After routing chooses the gateway IP, Linux must know the gateway MAC address.
```

Observation:

```text
ip neigh show 203.0.113.1

203.0.113.1 dev eth0 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

Explanation:

```text
Gateway IP:
203.0.113.1

Gateway MAC:
aa:bb:cc:dd:ee:ff
```

The routing table chooses the next-hop IP. The neighbor table provides the next-hop MAC address.

---

## Observation 3 - First Hop in Traceroute

Prediction:

```text
The first hop toward 8.8.8.8 should be the default gateway.
```

Observation:

```text
traceroute 8.8.8.8

1  _gateway (203.0.113.1)  1.491 ms  *  *
2  * * *
3  198.51.100.23 ...
...
8  dns.google (8.8.8.8) ...
```

Explanation:

```text
Local Host
203.0.113.10
        ↓
First Hop
_gateway / 203.0.113.1
        ↓
ISP / Internet Routers
        ↓
8.8.8.8
```

The traceroute output confirms that the default gateway is the first router on the path to the external destination.

---

## Observation 4 - Tracepath No Reply

Observation:

```text
tracepath 8.8.8.8

1?: [LOCALHOST] pmtu 1500
1:  _gateway  2.507ms
1:  no reply
2:  no reply
3:  198.51.100.22  2.943ms
...
```

Explanation:

Some routers do not send traceroute or tracepath replies. `no reply` does not necessarily mean traffic stopped. It means that hop did not return the expected diagnostic response.

The important point is that `tracepath` still showed `_gateway` as the first hop.

---

# Commands / Code

```bash
ip route
```

Shows the system's routing table.

Useful for identifying:

- default routes
- directly connected routes
- gateway addresses
- outgoing interfaces
- metrics

---

```bash
ip route get 8.8.8.8
```

Asks the kernel which route it would use for a specific destination.

In this session, it showed that traffic to `8.8.8.8` would go through:

```text
203.0.113.1 dev eth0
```

---

```bash
ip neigh show 203.0.113.1
```

Shows the neighbor table entry for the gateway.

In this session, it showed:

```text
203.0.113.1 → aa:bb:cc:dd:ee:ff
```

---

```bash
traceroute 8.8.8.8
```

Shows the hop-by-hop path toward a destination.

In this session, the first hop was:

```text
_gateway (203.0.113.1)
```

---

```bash
tracepath 8.8.8.8
```

Another path tracing tool.

It also showed `_gateway` as the first hop, though some later hops returned `no reply`.

---

# Default Gateway Mental Model

A default gateway is used when the destination is outside the local network.

```text
Destination IP
        ↓
Is it inside my local LAN?
        │
        ├─ Yes
        │     ↓
        │   ARP for destination MAC
        │     ↓
        │   Send directly
        │
        └─ No
              ↓
            Use default gateway
              ↓
            ARP for gateway MAC
              ↓
            Send Ethernet frame to gateway
```

---

# DNS vs Default Gateway

DNS and the default gateway solve different problems.

```text
DNS
= Converts a name into an IP address.

Example:
google.com → 142.250.x.x
```

```text
Default Gateway
= Forwards packets from the local LAN toward other networks.

Example:
Send packet for 8.8.8.8 to 203.0.113.1 first.
```

In this session, DNS was not the main issue because the destination was already an IP address:

```text
8.8.8.8
```

---

# IP Packet vs Ethernet Frame

For traffic to an external destination, the IP destination and Ethernet destination are different.

```text
IP Packet:
source IP      = 203.0.113.10
destination IP = 8.8.8.8
```

```text
Ethernet Frame:
source MAC      = local eth0 MAC
destination MAC = gateway MAC
```

In this session:

```text
Gateway IP:
203.0.113.1

Gateway MAC:
aa:bb:cc:dd:ee:ff
```

So the local Ethernet frame is sent to the gateway, while the IP packet still targets `8.8.8.8`.

---

# Connections

```text
Session 03 - ARP
        ↓
How Linux finds a MAC address for a local IP

Session 04 - Neighbor Tables
        ↓
How Linux caches and tracks IP-to-MAC mappings

Session 05 - Routing Tables
        ↓
How Linux chooses the next hop and outgoing interface

Session 06 - Default Gateway
        ↓
Why off-LAN traffic is sent to the first router
```

Combined model:

```text
Application
        ↓
Socket
        ↓
Destination IP
        ↓
Routing Table
        ↓
Default Gateway selected
        ↓
Neighbor Table / ARP
        ↓
Gateway MAC
        ↓
Ethernet Frame
        ↓
First Hop Router
        ↓
External Network
```

---

# Common Misconceptions

- Incorrect: The default gateway sends traffic to DNS.
- Correct: The default gateway forwards packets to other networks. DNS only resolves names to IP addresses.

---

- Incorrect: ARP finds the MAC address of `8.8.8.8`.
- Correct: For off-LAN traffic, ARP finds the MAC address of the gateway.

---

- Incorrect: `no reply` in traceroute or tracepath means the route is broken.
- Correct: It often means that an intermediate router did not send a diagnostic reply.

---

- Incorrect: The final destination IP and Ethernet destination MAC are always the same machine.
- Correct: For off-LAN traffic, the IP destination is remote, but the Ethernet destination is the local gateway.

---

# Key Takeaways

- A default gateway is the first router used for destinations outside the local LAN.
- Linux uses the default route only when no more specific route matches.
- The routing table selects the gateway IP.
- The neighbor table provides the gateway MAC address.
- For external traffic, Ethernet frames are sent to the gateway MAC, not the final destination's MAC.
- `traceroute` confirmed that `_gateway (203.0.113.1)` was the first hop toward `8.8.8.8`.
- DNS and default gateways solve different problems.

---

# Review Questions

### Q1. What problem does a default gateway solve?

<details>
<summary>A</summary>

</details>

---

### Q2. Why can't the local host ARP directly for `8.8.8.8`?

<details>
<summary>A</summary>

</details>

---

### Q3. What is the difference between DNS and a default gateway?

<details>
<summary>A</summary>

</details>

---

### Q4. What did this command show?

```bash
ip route get 8.8.8.8
```

<details>
<summary>A</summary>

</details>

---

### Q5. What did this command show?

```bash
ip neigh show 203.0.113.1
```

<details>
<summary>A</summary>

</details>

---

### Q6. For traffic to `8.8.8.8`, what is the IP destination and what is the Ethernet destination?

<details>
<summary>A</summary>

</details>

---

### Q7. Why was `_gateway (203.0.113.1)` the first hop in `traceroute 8.8.8.8`?

<details>
<summary>A</summary>

</details>

---

### Q8. What does `no reply` in `tracepath` or `traceroute` usually mean?

<details>
<summary>A</summary>

</details>

---

### Q9. Complete the flow for off-LAN traffic:

```text
Destination IP
        ↓
Routing Table
        ↓
?
        ↓
Neighbor Table / ARP
        ↓
?
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
Session 07

Topic:
DHCP
```

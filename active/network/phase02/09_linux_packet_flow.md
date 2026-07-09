# Phase 02 - Session 09

## Metadata

```yaml
Roadmap: Networking
Phase: 02
Session: 09
Title: Linux Packet Flow
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-10
```

---

# Objective

Understand the outbound and inbound packet flow through Linux networking
components and connect earlier Phase 02 topics into one observable model.

This session focused on the relationship between application traffic, sockets,
routing, neighbor resolution, link-layer frames, default gateways, and NAT.

---

# Learning Summary

Linux packet flow is not a single flat operation. A packet moves through several
layers and decisions before it leaves the host.

For outbound traffic to an off-LAN destination, Linux first creates or sends
through a socket, builds an IP packet, consults the routing table, selects a
next hop, resolves the next hop's link-layer address through the neighbor table
or ARP, and transmits a frame through the chosen interface.

The session confirmed that the IP-layer destination and link-layer destination
can be different.

```text
IP destination:
8.8.8.8

Frame destination:
default gateway MAC
```

This is expected for off-LAN traffic. The IP packet is still addressed to the
remote destination, while the local frame is addressed to the next hop on the
local link.

The session also clarified where NAT occurs. In the observed Wi-Fi path, NAT was
not performed inside the Linux host. The Linux host sent the packet to the
Wi-Fi gateway. The gateway or router then handled NAT before forwarding traffic
toward the Internet.

---

# Key Concepts

- Linux packet flow
- Application
- Socket
- IP packet
- Routing table
- Default gateway
- Next hop
- Neighbor table
- ARP
- Link-layer frame
- Interface transmission
- NAT router
- `tcpdump -e`
- ICMP echo request / reply

---

# Practical Observations

## Observation 1 - ICMP Over the Wi-Fi Interface

Prediction:

```text
A ping forced through the Wi-Fi interface should create ICMP packets with the
local Wi-Fi IP as source and 8.8.8.8 as destination.
```

Observation:

```text
PING 8.8.8.8 from 192.168.0.10 wlan0: 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=114 time=37.8 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=114 time=37.8 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=114 time=37.9 ms
```

The packet capture showed matching ICMP request and reply traffic.

```text
192.168.0.10 > 8.8.8.8: ICMP echo request
8.8.8.8 > 192.168.0.10: ICMP echo reply
```

Explanation:

The ping process generated ICMP traffic. At the IP layer, the local Wi-Fi
address was the source and the remote address was the destination.

```text
ping process
        ↓
socket / ICMP
        ↓
IP packet
src IP = 192.168.0.10
dst IP = 8.8.8.8
```

---

## Observation 2 - Link-Layer Destination Differs From IP Destination

Prediction:

```text
For an off-LAN destination, the frame should be sent to the gateway MAC even
though the IP destination remains 8.8.8.8.
```

Observation with link-layer headers enabled:

```text
bb:bb:bb:bb:bb:bb > aa:aa:aa:aa:aa:aa, ethertype IPv4,
    192.168.0.10 > 8.8.8.8: ICMP echo request

aa:aa:aa:aa:aa:aa > bb:bb:bb:bb:bb:bb, ethertype IPv4,
    8.8.8.8 > 192.168.0.10: ICMP echo reply
```

Explanation:

The packet contains different destinations at different layers.

```text
Outbound frame:
source MAC      = local Wi-Fi MAC
destination MAC = gateway MAC

Outbound IP packet:
source IP      = local Wi-Fi IP
destination IP = 8.8.8.8
```

The routing table selected the default gateway as the next hop. The neighbor
table or ARP provided the gateway MAC. Linux then sent the frame to the gateway
while keeping the IP destination as the remote host.

---

## Observation 3 - NAT Happens After the Host Sends to the Gateway

Prediction:

```text
In the Wi-Fi path, NAT should happen at the gateway or router, not inside the
local Linux host.
```

Observation:

The local capture on the Wi-Fi interface showed the internal LAN-side packet
view.

```text
192.168.0.10 > 8.8.8.8: ICMP echo request
8.8.8.8 > 192.168.0.10: ICMP echo reply
```

Explanation:

The Linux host sent a frame to the gateway. NAT occurred later on the gateway or
router. From the host-side capture, the internal IP address was still visible
because the capture was taken before or after NAT on the internal LAN side.

```text
Linux host
        ↓
frame to gateway MAC
        ↓
Wi-Fi gateway / NAT router
        ↓
source translation toward Internet
```

---

## Observation 4 - Complete Outbound Flow

The outbound packet flow can be modeled as:

```text
Application / ping
        ↓
Socket / ICMP
        ↓
IP packet creation
src IP = 192.168.0.10
dst IP = 8.8.8.8
        ↓
Routing table lookup
        ↓
Next hop = default gateway
        ↓
Neighbor table / ARP
        ↓
Gateway MAC resolved
        ↓
Link-layer frame creation
src MAC = local Wi-Fi MAC
dst MAC = gateway MAC
        ↓
wlan0 transmission
        ↓
Gateway / NAT router
        ↓
NAT and external forwarding
        ↓
Internet
```

---

## Observation 5 - Complete Inbound Flow

The inbound return path can be modeled as:

```text
Internet reply
        ↓
Gateway / NAT router
        ↓
NAT table restores internal destination
        ↓
Frame to local host
src MAC = gateway MAC
dst MAC = local Wi-Fi MAC
        ↓
wlan0 receives frame
        ↓
IP layer
src IP = 8.8.8.8
dst IP = 192.168.0.10
        ↓
ICMP handling
        ↓
ping process receives reply
```

---

# Commands / Code

```bash
ip route get 8.8.8.8
```

Shows the route Linux would use for a specific destination.

---

```bash
ip neigh show 192.168.0.1
```

Shows the neighbor table entry for the default gateway on the Wi-Fi network.

---

```bash
sudo tcpdump -ni wlan0 icmp
```

Captures ICMP traffic on the Wi-Fi interface without link-layer addresses.

---

```bash
sudo tcpdump -eni wlan0 'icmp and host 8.8.8.8'
```

Captures ICMP traffic with link-layer headers. The `-e` option is important
because it shows source and destination MAC addresses.

---

```bash
ping -c 3 -I wlan0 8.8.8.8
```

Sends three ICMP echo requests through the Wi-Fi interface.

---

# Connections

```text
Session 03 - ARP
        ↓
How Linux resolves a local next-hop MAC

Session 04 - Neighbor Tables
        ↓
How Linux caches and tracks next-hop reachability

Session 05 - Routing Tables
        ↓
How Linux selects the route and next hop

Session 06 - Default Gateway
        ↓
Why off-LAN traffic is sent to the first router

Session 08 - NAT
        ↓
How the gateway may translate internal IP:Port to external IP:Port

Session 09 - Linux Packet Flow
        ↓
How these parts combine during real packet transmission
```

Combined model:

```text
Application
        ↓
Socket
        ↓
IP packet
        ↓
Routing table
        ↓
Next hop
        ↓
Neighbor table / ARP
        ↓
Link-layer frame
        ↓
Interface
        ↓
Gateway / NAT router
        ↓
External network
```

---

# Common Misconceptions

- Incorrect: The frame destination and IP destination are always the same host.
- Correct: For off-LAN traffic, the frame destination is the next-hop gateway,
  while the IP destination remains the remote host.

---

- Incorrect: ARP resolves the MAC address of the final Internet destination.
- Correct: ARP resolves the MAC address of the next hop on the local link.

---

- Incorrect: NAT happened inside the Linux host during the Wi-Fi observation.
- Correct: The local host sent the packet to the gateway. NAT occurred later at
  the gateway or router.

---

- Incorrect: `tcpdump` without link-layer headers shows the complete frame
  picture.
- Correct: `tcpdump -e` is needed to observe Ethernet or Wi-Fi frame source and
  destination addresses.

---

# Key Takeaways

- Linux first determines the route before resolving a link-layer destination.
- The routing table selects the outgoing path and next hop.
- The neighbor table or ARP resolves the next-hop MAC address.
- For off-LAN traffic, the IP destination remains the remote host, but the frame
  destination is the gateway MAC.
- NAT in the observed Wi-Fi path occurred at the gateway or router, not inside
  the Linux host.
- `tcpdump -e` provides evidence that IP-layer and link-layer destinations can
  differ.
- Packet flow is a chain of decisions across application, socket, IP, routing,
  neighbor resolution, link-layer transmission, and gateway forwarding.

---

# Review Questions

### Q1. What is the first major kernel decision after an outbound packet has a destination IP?

<details>
<summary>A</summary>

</details>

---

### Q2. Why does Linux consult the routing table before the neighbor table?

<details>
<summary>A</summary>

</details>

---

### Q3. For traffic to `8.8.8.8`, why does ARP resolve the gateway MAC instead of the MAC for `8.8.8.8`?

<details>
<summary>A</summary>

</details>

---

### Q4. What did `tcpdump -e` show that ordinary IP-only capture did not show?

<details>
<summary>A</summary>

</details>

---

### Q5. Why can the frame destination MAC and IP destination address differ?

<details>
<summary>A</summary>

</details>

---

### Q6. In the observed Wi-Fi path, where did NAT occur relative to the Linux host?

<details>
<summary>A</summary>

</details>

---

### Q7. What does the outbound flow look like from application to interface transmission?

<details>
<summary>A</summary>

</details>

---

### Q8. What does the inbound return flow look like from gateway to ping process?

<details>
<summary>A</summary>

</details>

---

### Q9. Why is observing packet flow stronger evidence than only describing it conceptually?

<details>
<summary>A</summary>

</details>

---

### Q10. Complete the flow:

```text
Application
        ↓
Socket
        ↓
?
        ↓
Routing table
        ↓
?
        ↓
Neighbor table / ARP
        ↓
?
        ↓
Interface transmission
```

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Next:
Phase 02
Session 10

Topic:
iptables Fundamentals
```

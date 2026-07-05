# Network Phase 02 — Session 03
# ARP (Address Resolution Protocol)

## Metadata

```yaml
Roadmap: Networking
Phase: 02
Session: 03
Title: ARP
Status:
Review:
ArchiveVersion: 2
Date:
```

## Notes

### The Problem

Routing tells Linux **which interface** should be used.

However, Ethernet cannot deliver packets using IP addresses alone.

Question:

```text
How does Linux find the correct Ethernet destination?
```

---

### IP vs MAC

IP addresses identify devices at Layer 3.

Ethernet uses MAC addresses at Layer 2.

Therefore, before creating an Ethernet frame, Linux must determine the destination MAC address.

Mental model:

```text
Destination IP
↓
ARP
↓
Destination MAC
↓
Ethernet Frame
```

---

### What Is ARP?

ARP (Address Resolution Protocol) translates an IPv4 address into a MAC address on the local network.

Example:

```text
192.168.0.1

↓

aa:bb:cc:dd:ee:11
```

ARP answers the question:

```text
"I know the destination IP.

What is its MAC address?"
```

---

### Observing the Neighbor Table

Command:

```bash
ip neigh
```

Example:

```text
192.168.0.1 dev wlan0 lladdr aa:bb:cc:dd:ee:11 REACHABLE

203.0.113.1 dev eth0 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

Fields:

```text
IP
→ Destination IPv4 address

dev
→ Network interface

lladdr
→ Link-layer address (MAC address)

State
→ Neighbor cache state
```

---

### What Does "lladdr" Mean?

```text
lladdr
=
Link-Layer Address
```

In Ethernet, the link-layer address is the MAC address.

Example:

```text
192.168.0.1
↓

aa:bb:cc:dd:ee:11
```

The neighbor table stores the mapping between IP addresses and MAC addresses.

---

### ARP Cache

Linux does not perform ARP for every packet.

Instead, it stores previous ARP results in the Neighbor Table (ARP cache).

Process:

```text
Destination IP
↓
Neighbor Table Lookup
├─ Entry exists
│      ↓
│   Use cached MAC
│
└─ No entry
       ↓
   Send ARP Request
       ↓
   Receive ARP Reply
       ↓
   Store mapping
```

---

### Neighbor States

Common states:

```text
REACHABLE
```

The MAC address has been recently confirmed and is trusted.

```text
STALE
```

The MAC address is still stored, but it has not been used recently.

Linux may verify it again when needed.

Important:

```text
STALE
≠ deleted
```

The entry remains in the cache.

---

### Why Cache ARP Results?

Without caching:

```text
Every packet
↓

ARP Request

↓

ARP Reply

↓

Frame transmission
```

With caching:

```text
Destination IP
↓

Neighbor Table

↓

MAC Address

↓

Frame transmission
```

Benefits:

- Faster packet transmission
- Fewer ARP broadcasts
- Reduced network traffic

---

### Complete Packet Flow

```text
Application
↓
Socket
↓
Destination IP
↓
Routing Table
↓
Interface
↓
ARP
↓
Destination MAC
↓
Ethernet Frame
↓
Transmission
```

---

### Session Mental Model

Routing decides **where** to send a packet.

ARP decides **who** should receive the Ethernet frame.

```text
Destination IP
↓

Routing
↓

Interface
↓

ARP
↓

Destination MAC
↓

Ethernet Frame
```

---

# Review Questions

### Q1. Why can't Linux create an Ethernet frame using only the destination IP address?

<details>
<summary>A</summary>

</details>

---

### Q2. What problem does ARP solve?

<details>
<summary>A</summary>

</details>

---

### Q3. Complete the transformation:

```text
Destination IP
↓

?

↓

Destination MAC
```

<details>
<summary>A</summary>

</details>

---

### Q4. What command displays the neighbor table?

<details>
<summary>A</summary>

</details>

---

### Q5. What does `lladdr` stand for?

<details>
<summary>A</summary>

</details>

---

### Q6. In the neighbor table, what does each field represent?

- IP
- dev
- lladdr
- State

<details>
<summary>A</summary>

</details>

---

### Q7. Why does Linux cache ARP results?

<details>
<summary>A</summary>

</details>

---

### Q8. What is the difference between `REACHABLE` and `STALE`?

<details>
<summary>A</summary>

</details>

---

### Q9. Does `STALE` mean the MAC address has been deleted?

<details>
<summary>A</summary>

</details>

---

### Q10. Complete the packet flow:

```text
Application
↓
Socket
↓
Destination IP
↓
Routing Table
↓
Interface
↓
?
↓
Destination MAC
↓
Ethernet Frame
```

<details>
<summary>A</summary>

</details>

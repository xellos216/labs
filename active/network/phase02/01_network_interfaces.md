# Network Phase 02 — Session 01
# Network Interfaces

## Metadata

```yaml
Roadmap: Networking
Phase: 02
Session: 01
Title: Network Interfaces
Status:
Review:
ArchiveVersion: 2
Date:
```

## Notes

### What Is a Network Interface?

A network interface is the connection point between Linux and a network.

Examples:

- loopback interface
- Ethernet interface
- Wi-Fi interface
- VPN interface

Linux sends packets through interfaces.

Mental model:

```text
Application
↓
Socket
↓
IP
↓
Routing Table
↓
Interface
↓
Packet
```

---

### Observing Interfaces

Command:

```bash
ip link
```

Observed interfaces:

```text
lo
enp85s0
wlp86s0
```

Interpretation:

```text
lo
→ loopback interface
→ communication with self

enp85s0
→ Ethernet interface
→ wired networking

wlp86s0
→ Wireless interface
→ Wi-Fi networking
```

---

### Interfaces and IP Addresses

Observation:

```bash
ip a
```

Important concept:

```text
IP addresses belong to interfaces.
```

Not:

```text
Computer
→ one IP address
```

Instead:

```text
Computer
├─ Interface A → IP A
├─ Interface B → IP B
└─ Interface C → IP C
```

An interface may have one or more IP addresses.

---

### Routing and Interface Selection

Observation:

```bash
ip route
```

Example:

```text
default via 59.9.228.126 dev enp85s0 metric 100

default via 192.168.0.1 dev wlp86s0 metric 600
```

Linux does not immediately send packets through the lowest-metric interface.

Decision process:

```text
Destination IP
↓
Routing Table Lookup
↓
Matching Route?
├─ Yes → Use matching interface
└─ No → Use default route
```

---

### Example

Destination:

```text
192.168.0.50
```

Route:

```text
192.168.0.0/24 dev wlp86s0
```

Decision:

```text
192.168.0.50
↓
Matches 192.168.0.0/24
↓
Use wlp86s0
```

---

### Loopback Routing

Destination:

```text
127.0.0.1
```

Decision:

```text
127.0.0.1
↓
Loopback Network
↓
lo
```

Important:

```text
127.0.0.1
```

is not the only loopback address.

Loopback network:

```text
127.0.0.0/8
```

Examples:

```text
127.0.0.1
127.0.0.2
127.1.1.1
127.42.42.42
```

All belong to the loopback network.

---

### Session Mental Model

```text
IP
↓
Routing Table
↓
Interface
↓
Packet
```

Linux chooses an interface by consulting the routing table.

---

# Review Questions

### Q1. What is a network interface?

<details>
<summary>A</summary>

</details>

---

### Q2. What command can be used to list network interfaces?

<details>
<summary>A</summary>

</details>

---

### Q3. Do IP addresses belong to the computer or to interfaces?

<details>
<summary>A</summary>

</details>

---

### Q4. How does Linux decide which interface to use for a packet?

<details>
<summary>A</summary>

</details>

---

### Q5. What is the role of the routing table?

<details>
<summary>A</summary>

</details>

---

### Q6. If the destination is 192.168.0.50 and a route exists for 192.168.0.0/24, which interface is selected?

<details>
<summary>A</summary>

</details>

---

### Q7. When is the default route used?

<details>
<summary>A</summary>

</details>

---

### Q8. Which interface is typically used for 127.0.0.1?

<details>
<summary>A</summary>

</details>

---

### Q9. Is 127.0.0.1 the only loopback address?

<details>
<summary>A</summary>

</details>

---

### Q10. Complete the model:

```text
IP
↓
?
↓
?
↓
Packet
```

<details>
<summary>A</summary>

</details>

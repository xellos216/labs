# Network Phase 02 — Session 02
# Loopback Interface

## Metadata

```yaml
Roadmap: Networking
Phase: 02
Session: 02
Title: Loopback Interface
Status:
Review:
ArchiveVersion: 2
Date:
```

## Notes

### What Is the Loopback Interface?

The loopback interface is a virtual network interface used for communication with the local machine.

Unlike Ethernet or Wi-Fi interfaces, packets sent through the loopback interface never leave the operating system.

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
lo
↓
Application
```

---

### Observing Loopback

Command:

```bash
ping 127.0.0.1
```

Observation:

```text
Packets are transmitted and received successfully.
```

Important:

The packets are processed entirely inside the Linux kernel.

They are **not** transmitted through:

- Ethernet
- Wi-Fi
- Switch
- Router
- Default Gateway

---

### Loopback Address

Command:

```bash
ip a show lo
```

Example:

```text
lo
inet 127.0.0.1/8
```

Important concept:

```text
127.0.0.1
```

is only one address inside the loopback network.

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

All belong to the loopback interface.

---

### Routing to Loopback

When the destination is:

```text
127.0.0.1
```

Linux performs:

```text
Destination IP
↓
Routing Table Lookup
↓
127.0.0.0/8
↓
lo
↓
Kernel Internal Delivery
```

No physical network device is involved.

---

### Why Does Loopback Exist?

Loopback allows applications on the same machine to communicate using the normal networking stack.

Without loopback, local communication and remote communication would require different programming models.

Instead, Linux provides a unified interface.

Example:

```text
Client
↓
Socket
↓
TCP/IP
↓
lo
↓
Socket
↓
Server
```

The same application can later communicate with another computer simply by changing the destination IP address.

---

### Practical Example

Start a local HTTP server:

```bash
python -m http.server 8000
```

Access it:

```bash
curl http://127.0.0.1:8000
```

Although HTTP and TCP are used, no packet leaves the machine.

The Linux networking stack processes the communication internally through the loopback interface.

---

### Why This Design Matters

Linux treats local communication and remote communication almost identically.

Instead of creating a separate mechanism for processes on the same machine, Linux reuses the existing networking stack.

Benefits:

- One programming model
- Same socket API
- Same TCP/IP behavior
- Easier application development
- Consistent networking architecture

---

### Session Mental Model

```text
Application
↓
Socket
↓
IP
↓
Routing Table
↓
lo
↓
Application
```

Loopback is not a shortcut around networking.

It is a virtual network interface that allows the full networking stack to communicate with the local machine.

---

# Review Questions

### Q1. What is the purpose of the loopback interface?

<details>
<summary>A</summary>

</details>

---

### Q2. Which interface is typically used for communication with the local machine?

<details>
<summary>A</summary>

</details>

---

### Q3. Do packets sent to 127.0.0.1 leave the physical network interface?

<details>
<summary>A</summary>

</details>

---

### Q4. What network does 127.0.0.1 belong to?

<details>
<summary>A</summary>

</details>

---

### Q5. Which component selects the loopback interface?

<details>
<summary>A</summary>

</details>

---

### Q6. Complete the packet flow:

```text
Application
↓
Socket
↓
?
↓
?
↓
Application
```

<details>
<summary>A</summary>

</details>

---

### Q7. Why does Linux use the same networking stack for both local and remote communication?

<details>
<summary>A</summary>

</details>

---

### Q8. Does loopback bypass the TCP/IP stack?

<details>
<summary>A</summary>

</details>

---

### Q9. Why can a program listening on `127.0.0.1:8000` later communicate with another computer without changing its socket logic?

<details>
<summary>A</summary>

</details>

---

### Q10. Complete the statement:

```text
Loopback is not a shortcut around networking.

It is a _______________________________.
```

<details>
<summary>A</summary>

</details>

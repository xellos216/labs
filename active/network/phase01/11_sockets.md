# Sockets

## Metadata

```yaml
Roadmap: Networking
Phase: 01
Session: 11
Title: Sockets
Status:
Review:
ArchiveVersion: 2
Date:
```

## Objective

By the end of this session, you should be able to explain:

- Why sockets exist
- What problem sockets solve
- How applications interact with the network stack
- Why ports are associated with sockets
- How networking concepts become usable by programs

## Why Sockets Exist

So far we have learned:

```text
DNS
↓
Find Address

IP
↓
Find Machine

Routing
↓
Find Path

Port
↓
Find Application

TCP
↓
Reliable Delivery

HTTP
↓
Request / Response

TLS
↓
Protect Contents
```

Question:

```text
How does a program actually use
all of these networking features?
```

Consider:

```text
Firefox
curl
Python
nginx
SSH
```

These are normal applications.

They cannot directly manipulate:

```text
Packets
TCP
IP
Routing Tables
```

Instead, they communicate with the operating system.

Sockets exist to provide that interface.

## Core Problem

Applications need a way to say:

```text
I want to connect to a server.

I want to listen for connections.

I want to send data.

I want to receive data.
```

The kernel manages the networking stack.

Applications need a bridge to that stack.

Sockets solve this problem.

## Mental Model

Think:

```text
Socket
=
Network Handle
```

or

```text
Socket
=
Network Doorway
```

Applications do not directly talk to:

```text
Ethernet
IP
TCP
```

Instead:

```text
Application
↓
Socket
↓
Kernel
↓
Network Stack
```

## Example

When Firefox opens a website:

```text
Firefox
↓
Socket
↓
Kernel
↓
TCP Connection
↓
Server
```

Firefox does not build packets itself.

The kernel does that work.

Firefox communicates through sockets.

## Socket and Port

Remember:

```text
IP
=
Which Machine?

Port
=
Which Application?
```

Sockets are how applications claim and use ports.

Example:

```text
nginx
↓
Socket
↓
Port 80
```

When data arrives:

```text
IP:Port
↓
Socket
↓
Application
```

The kernel delivers the data to the correct socket.

## Observation Principle

Before memorizing socket functions, ask:

```text
Why do applications need sockets?
```

Answer:

```text
Applications need a way to use
the networking stack without
managing networking internals directly.
```

---

# Review Questions

### Q1. What problem do sockets solve?

<details>
<summary>A</summary>

Sockets provide an interface between applications and the kernel networking stack.

</details>

---

### Q2. Why can't applications directly use TCP and IP?

<details>
<summary>A</summary>

Applications rely on the kernel to manage TCP and IP operations..

</details>

---

### Q3. What is a socket?

<details>
<summary>A</summary>

Network doorway

</details>

---

### Q4. Why are sockets often described as an interface between applications and the network stack?

<details>
<summary>A</summary>

Because socket can connect each of them

</details>

---

### Q5. What is the relationship between sockets and ports?

<details>
<summary>A</summary>

Ports identify applications.

Sockets are the kernel objects application use to communicate through those ports.

</details>

---

### Q6. Why might a web server create a listening socket?

<details>
<summary>A</summary>

They have to be ready for accepting the data

</details>

---

### Q7. How does incoming network data reach the correct application?

<details>
<summary>A</summary>

Ports and sockets lead them

</details>

---

### Q8. How do sockets relate to DNS, IP, Routing, TCP, HTTP, and TLS?

<details>
<summary>A</summary>

DNS = finding address

IP = which machine

Routing = which path

TCP = three-way-handshake

HTTP = rules of request and response

TLS = secure envelope

sockets = network door

</details>

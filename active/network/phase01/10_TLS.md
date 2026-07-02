# TLS

## Metadata

```yaml
Roadmap: Networking
Phase: 01
Session: 10
Title: TLS
Status:
Review:
ArchiveVersion: 2
Date:
```

## Objective

By the end of this session, you should be able to explain:

- Why TLS exists
- What problem TLS solves
- Why HTTP is insufficient for secure **communication[**
- What encryption provides
- Why HTTPS exists
- How TLS relates to previous networking concepts

---

## Why TLS Exists

In Session 09:

```text
Browser
↓
HTTP
↓
Server
```

The browser can request resources.

The server can respond.

Communication works.

A new problem appears.

Imagine:

```text
Laptop
↓
Home Router
↓
ISP
↓
Internet
↓
Server
```

Question:

```text
Who can see the data traveling between them?
```

Potentially:

- Home router
- ISP
- Intermediate networks
- Attackers on the same network

Suppose you submit:

```text
username=alice
password=secret123
```

using plain HTTP.

Anyone who can observe the traffic may be able to read it.

HTTP solves communication.

It does NOT solve privacy.

TLS exists to solve that problem.

---

## Core Problem

Without TLS:

```text
Client
↓
HTTP
↓
Server
```

Data travels as plain text.

With TLS:

```text
Client
↓
TLS
↓
HTTP
↓
Server
```

Data is encrypted before transmission.

---

## Mental Model

Think:

```text
HTTP
=
Conversation Rules
```

Think:

```text
TLS
=
Locked Envelope
```

Example:

Without TLS:

```text
Postcard
```

Anyone handling it can read it.

With TLS:

```text
Sealed Envelope
```

People can carry it.

People can route it.

People cannot easily read the contents.

---

## HTTPS

HTTPS is simply:

```text
HTTP
+
TLS
```

HTTP:

```text
Request / Response
```

TLS:

```text
Encryption
```

Together:

```text
Secure Request / Response
```

---

## Observation Principle

Before memorizing TLS terms, ask:

```text
What problem is being solved?
```

Answer:

```text
Protecting communication from observers.
```

# Review Questions

### Q1. What problem does TLS solve?

<details>
<summary>A</summary>

TLS provides privacy by encrypting communication.

</details>

---

### Q2. Why is HTTP insufficient for secure communication?

<details>
<summary>A</summary>

HTTP defines communication rules but does not protect the contents from observers.

</details>

---

### Q3. What could happen if sensitive information is sent over plain HTTP?

<details>
<summary>A</summary>

The attacker or anyone can observe it and read it.

</details>

---

### Q4. What is the relationship between HTTP and HTTPS?

<details>
<summary>A</summary>

HTTPS is HTTP running through TLS encryption.

</details>


---

### Q5. Why is TLS often compared to a sealed envelope?

<details>
<summary>A</summary>

TLS is compared to a sealed envelope because observers can carry it but cannot easily read its contents

</details>

---

### Q6. Why can routers still forward encrypted traffic?

<details>
<summary>A</summary>

Router can still forward encrypted traffic because they do not need to read the encrypted application data. They only need routing information such as the destination IP address, which remains visible in the IP header. TLS encrypts the HTTP/application content, but the outet network-layer information needed for packet forwarding is still readable by routers.

</details>

---

### Q7. What problem would exist if TLS did not exist?

<details>
<summary>A</summary>

Anyone who is in same network can observe and read the data

</details>

---

### Q8. How does TLS relate to DNS, IP, Routing, TCP, and HTTP?

<details>
<summary>A</summary>

DNS - translator
IP - destination
Routing - path selection
Port - application identifier
TCP - reliable delivery
HTTP - request/response rules
TLS - sealed envelope protecting the contents

</details>

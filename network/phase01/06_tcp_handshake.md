# Session 06 — TCP Three-Way Handshake

## Metadata

```yaml
Roadmap: Networking
Phase: 01
Session: 06
Title: TCP Three-Way Handshake
Status:
Review:
ArchiveVersion: 2
Date:
```

## Why the Handshake Exists

Reliable communication requires both systems to verify that communication is possible before data transfer begins.

## Core Problem

Before sending data:

- Is the other side alive?
- Can it receive data?
- Can it send data back?
- Is the communication path working?

The handshake exists to answer these questions.

## Mental Model

Step 1:

Client:
"I want to communicate."

Step 2:

Server:
"I received your message and I am ready."

Step 3:

Client:
"I received your reply."

After this process, both sides know communication is possible.

## Three-Way Handshake

Conceptually:

SYN

→ I want to communicate.

SYN-ACK

→ I received your request and I am ready.

ACK

→ I received your reply.

## Observation Principle

Do not memorize:

SYN
SYN-ACK
ACK

First ask:

Why must both sides confirm communication before reliable data transfer can begin?

# Review Questions

### Q1. Why does TCP use a Three-Way Handshake?

<details>
<summary>A</summary>

TCP uses a Three-way handshake to verify that both sides can communicate before data transfer begins.

</details>

---

### Q2. What problem does the handshake solve?

<details>
<summary>A</summary>

The handshake verifies that both systems are reachable, can send and receive data, and have a working communication path.

</details>

---

### Q3. Why can't TCP immediately begin sending data?

<details>
<summary>A</summary>

Without a handshake, neither side can know whether the other side is ready to communicate.

</details>

---

### Q4. What does the first handshake message conceptually mean?

<details>
<summary>A</summary>

The first message means, "I want to communicate with you."

</details>

---

### Q5. What does the second handshake message conceptually mean?

<details>
<summary>A</summary>

The second message means, "I received your request and I am ready to communicate."

</details>

---

### Q6. What does the third handshake message conceptually mean?

<details>
<summary>A</summary>

The third message means, "I received your reply and communication can begin."

</details>

---

### Q7. Why must both sides prove they can communicate?

<details>
<summary>A</summary>

Both sides must prove they can communicate so that reliable data transfer is possible.

</details>

---

### Q8. What is the relationship between TCP reliability and the Three-Way Handshake?

<details>
<summary>A</summary>

The Three-Way handshake establishes the connection that TCP uses to provide reliable communication.

</details>

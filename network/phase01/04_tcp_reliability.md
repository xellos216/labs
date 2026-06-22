# TCP Reliability

## Why TCP Exists

TCP exists to provide reliable communication between systems.

IP can identify a destination.

Ports can identify an application.

Neither guarantees successful delivery.

## Core Problem

Networks are imperfect.

Data may:

- be lost
- arrive late
- arrive out of order
- be duplicated

TCP exists to handle these problems.

## Mental Model

IP = Which machine?

Port = Which application?

TCP = How can data be delivered reliably?

## Reliability

Reliability means:

- detecting loss
- detecting missing data
- confirming delivery
- preserving correct order

## Observation Principle

Before memorizing TCP mechanisms, ask:

- What failure is possible?
- How would the sender detect it?
- How would the receiver recover from it?

# QA

**Q1.**
What problem does TCP solve?

<details>
<summary><strong>A1.</strong></summary>

TCP solves the problem of providing reliable communication between systems.

</details>

---

**Q2.**
Why are IP addresses and ports insufficient for reliable communication?

<details>
<summary><strong>A2.</strong></summary>

IP addresses and ports identify destinations and applications, but they do not guarantee reliable delivery.

</details>

---

**Q3.**
What does reliability mean in networking?

<details>
<summary><strong>A3.</strong></summary>

detecting loss, detecting missing data, confirming delivery, preserving correct order

</details>

---

**Q4.**
Why is sending data different from successfully delivering data?

<details>
<summary><strong>A4.</strong></summary>

Sending data only means the sender transmitted it. Successful delivery means the receiver actually received it.

</details>

---

**Q5.**
What should happen if data arrives out of order?

<details>
<summary><strong>A5.</strong></summary>

The receiver should reorder the data so it can be processed in the correct sequence.

</details>

---

**Q6.**
Why might a sender need confirmation from a receiver?

<details>
<summary><strong>A6.</strong></summary>

A sender needs confirmation because packets may be lost during transmission.

</details>

---

**Q7.**
How can systems successfully transfer data even when packets are lost?

<details>
<summary><strong>A7.</strong></summary>

System can successfully transfer data by detecting missing packets and retransmitting them.

</details>

---

**Q8.**
What is the relationship between IP, Port, and TCP?

<details>
<summary><strong>A8.</strong></summary>

IP identifies the destination machine. Port identifies the destination application. TCP helps ensure that data data is delivered reliably.

</details>

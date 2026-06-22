# UDP

## Why UDP Exists

TCP reliability introduces overhead.

Not every application needs perfect delivery.

UDP exists for applications that prioritize speed, simplicity, or low latency.

## TCP vs UDP

TCP:

- reliable
- ordered
- retransmits lost data
- maintains connection state

UDP:

- best-effort delivery
- no delivery guarantees
- no retransmission
- minimal overhead

## Tradeoff

TCP:

reliability over speed

UDP:

speed over reliability

## Application Examples

TCP:

- file downloads
- web browsing
- SSH
- email

UDP:

- voice calls
- video streaming
- online gaming
- DNS

## Observation Principle

Do not ask:

Which protocol is better?

Ask:

Which problem is being solved?

# QA

**Q1.**
Why does UDP exist if TCP already provides reliable communication?

<details>
<summary><strong>A1.</strong></summary>

UDP exists because not every application wants TCP's guarantees.

</details>

---

**Q2.**
What tradeoff does UDP make compared to TCP?

<details>
<summary><strong>A2.</strong></summary>

UDP priortizes speed and low overhead over reliability.

</details>

---

**Q3.**
Why might real-time applications prefer UDP?

<details>
<summary><strong>A3.</strong></summary>

Real-time applications prefer UDP because continous communication is more important than perfect delivery.

</details>

---

**Q4.**
Why are file transfers usually better suited to TCP?

<details>
<summary><strong>A4.</strong></summary>

File transfers are better suited to TCP because missing or corrupted data can make the entire file ususable.

</details>

---

**Q5.**
What does "best-effort delivery" mean?

<details>
<summary><strong>A5.</strong></summary>

Best-effort delivery means data is sent without guaranteeing successful delivery.

</details>

---

**Q6.**
Why might retransmission be undesirable in some applications?

<details>
<summary><strong>A6.</strong></summary>

Retransmission may be undesirable because waiting for missing data can introduce delays.

</details>

---

**Q7.**
How do TCP and UDP differ in their goals?

<details>
<summary><strong>A7.</strong></summary>

TCP prioritizes reliable delivery, while UDP prioritizes speed and low latency.

</details>

---

**Q8.**
What is the relationship between IP, Port, TCP, and UDP?

<details>
<summary><strong>A8.</strong></summary>

IP address = Building address

Port = Apartment number

TCP = Registered Mail with Delivery Confirmation

UDP = Regular Mail Without Confirmation

</details>

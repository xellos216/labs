# Session 02 — IP Addresses

## Metadata

```yaml
Roadmap: Networking
Phase: 01
Session: 02
Title: IP Addresses
Status:
Review:
ArchiveVersion: 2
Date:
```

## Why IP Exists

IP addresses exist because networks contain multiple destinations.

Without destination identifiers, systems would not know where data should go.

## Core Problem

Communication requires:

- a sender
- a destination
- data

IP primarily solves destination identification.

## Mental Model

Do not think:

IP = computer

Think:

IP = network destination identifier

## Addressing

Addressing becomes necessary when multiple possible destinations exist.

The more systems that exist, the more important addressing becomes.

## Loopback

127.0.0.1 is a special address used for communication with the local machine.

It allows network software to communicate without requiring an external network.

## Observation Principle

Before memorizing address formats, ask:

- Why does addressing exist?
- What problem does it solve?
- What would happen without it?

# Review Questions

### Q1. What problem do IP addresses solve?

<details>
<summary>A</summary>

IP addresses solve the problem of identifying destination on a network

</details>

---

### Q2. Why are IP addresses unnecessary when only one destination exists?

<details>
<summary>A</summary>

Computer don't need to identify where the data should go

</details>

---

### Q3. Why does a network need destination identifiers?

<details>
<summary>A</summary>

Without destination identifiers, systems would not know where data should go

</details>

---

### Q4. What problem would occur if every device used the same IP address?

<details>
<summary>A</summary>

The network could not determine which device should receive the data

</details>

---

### Q5. Why is an IP address better understood as a network destination identifier than a physical location?

<details>
<summary>A</summary>

An IP address is better understood as a network destination identifier because it tells data where it should be delivered

</details>

---

### Q6. Why might a computer have more than one IP address?

<details>
<summary>A</summary>

A device may have multiple IP addresses because it can be connected to multiple networks

</details>

---

### Q7. What is the purpose of the loopback address 127.0.0.1?

<details>
<summary>A</summary>

To allow a machine to communicate with itself through the network stack

</details>

---

### Q8. What problems could occur if two devices share the same IP address?

<details>
<summary>A</summary>

IP conflicts may occur, causing packets to be delivered incorrectly or communication to fail

</details>

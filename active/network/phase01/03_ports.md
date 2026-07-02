# Ports

## Metadata

```yaml
Roadmap: Networking
Phase: 01
Session: 03
Title: Ports
Status:
Review:
ArchiveVersion: 2
Date:
```

## Why Ports Exist

Ports exist because one machine can run multiple networked applications.

IP addresses identify machines.

Ports identify communication endpoints on those machines.

## Core Problem

IP answers:

Which machine?

Port answers:

Which application?

## Mental Model

IP = Building Address

Port = Apartment Number

## Communication

A network destination is commonly represented as:

IP:Port

Examples:

192.168.0.10:22
192.168.0.10:80
192.168.0.10:443

## Operating System Role

Applications use ports.

The operating system tracks port ownership and routes incoming data to the correct application.

## Observation Principle

Before memorizing port numbers, ask:

- Why does this port exist?
- Which application uses it?
- What problem is being solved?

# Review Questions

### Q1. What problem do ports solve?

<details>
<summary>A</summary>

Ports solve the problem of determining which application should receive incoming data.

</details>

---

### Q2. Why are IP addresses alone insufficient?

<details>
<summary>A</summary>

IP addresses alone are insufficient because a single computer can run multiple application simultaneously.

</details>

---

### Q3. Why can multiple applications share the same IP address?

<details>
<summary>A</summary>

Multiple applications can share the same IP address because ports distinguish one application from another.

</details>

---

### Q4. What does a port identify?

<details>
<summary>A</summary>

A port identifies a communication endpoint or application on a machine.

</details>

---

### Q5. Why is a port better understood as an application identifier than a protocol identifier?

<details>
<summary>A</summary>

A port is better understood as an application identifier because it determines which application should receive incoming data.

</details>

---

### Q6. Why does a browser need both an IP address and a port?

<details>
<summary>A</summary>

A browser needs both an IP address and a port to reach the correct application on the correct machine.

</details>

---

### Q7. What could happen if two applications attempt to listen on the same IP and port?

<details>
<summary>A</summary>

One of the applications would fail to bind to the port because the port is already in use.

</details>

---

### Q8. What is the relationship between IP addresses and ports?

<details>
<summary>A</summary>

An IP address identifies a machine, while a port identifies an application on that machine.

</details>

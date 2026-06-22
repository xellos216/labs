# DNS

## Why DNS Exists

Humans are good at remembering names.

Computers communicate using IP addresses.

DNS exists to translate between human-friendly names and network addresses.

## Core Problem

Humans use:

- google.com
- github.com
- wikipedia.org

Networks use:

- IP addresses

DNS bridges that gap.

## Mental Model

DNS = Phone Book

Domain Name

↓

IP Address

## Resolution

DNS resolution is the process of converting a domain name into an IP address.

Example:

google.com

↓

142.250.x.x

## DNS Server

A DNS server answers questions such as:

"What is the IP address of google.com?"

## Observation Principle

Before memorizing DNS record types, ask:

- Why does name resolution exist?
- What problem does it solve?
- What would happen without it?

# QA

**Q1.**
What problem does DNS solve?

<details>
<summary><strong>A1.</strong></summary>

DNS translates human-friendly domain names into IP addresses.

</details>

---

**Q2.**
Why do humans prefer domain names over IP addresses?

<details>
<summary><strong>A2.</strong></summary>

Humans prefer domain names because they are easier to remember than numeric IP addresses.

</details>

---

**Q3.**
What is the relationship between a domain name and an IP address?

<details>
<summary><strong>A3.</strong></summary>

A domain name is a human-friendly identifier that DNS translates into an IP address.

</details>

---

**Q4.**
Why can't computers communicate using only domain names?

<details>
<summary><strong>A4.</strong></summary>

Computers ultimately communicate using IP addresses, not domain names.

</details>

---

**Q5.**
Why might a domain name point to different IP addresses over time?

<details>
<summary><strong>A5.</strong></summary>

Because the server behind a domain can change. DNS can return different IP addresses for the same domain because of server migration, load balancing, CDN, or failure recovery.

</details>

---

**Q6.**
What role does a DNS server play?

<details>
<summary><strong>A6.</strong></summary>

A DNS server answers queries by providing the IP address associated with a domain name.

</details>

---

**Q7.**
Why is DNS often compared to a phone book?

<details>
<summary><strong>A7.</strong></summary>

DNS is compared to a phone book because it translates human-readable names into network addressess

</details>

---

**Q8.**
What is the relationship between DNS and the networking concepts learned previously?

<details>
<summary><strong>A8.</strong></summary>

DNS helps find the IP address that communication should be sent to before TCP and ports can be used.

</details>

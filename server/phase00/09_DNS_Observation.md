# Linux Server Administration
## Phase 00 — Session 09
# DNS Observation

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 09
Title: DNS Observation
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-07-02
```

---

# Objective

Understand how a virtual machine resolves human-readable domain names into IP addresses.

The goal is to distinguish:

```text
Name
```

from:

```text
Address
```

and understand the relationship between DHCP, DNS, routing, and packet transmission.

---

# Learning Summary

A packet is not delivered using a domain name such as:

```text
google.com
```

A domain name is a human-friendly identifier. Before traffic can be sent across an IP network, the domain name must be resolved into an IP address.

DNS performs this translation.

Example model:

```text
google.com
↓

DNS Query
↓

Resolved IP Address
↓

Routing
↓

Packet Transmission
```

DHCP and DNS are related but not the same.

DHCP can provide network configuration to the Guest, including:

- IP address
- subnet information
- default gateway
- DNS server address

DNS then uses the configured DNS server to translate names into IP addresses.

Important correction:

```text
google.com
≠
8.8.8.8
```

`8.8.8.8` is commonly used as a DNS server address, not necessarily the IP address of `google.com`.

The more accurate model is:

```text
google.com
↓

Ask DNS server, such as 8.8.8.8

↓

Receive actual Google server IP
```

---

# Key Concepts

- DNS
- Domain Name
- IP Address
- Name Resolution
- DNS Server
- DHCP-provided DNS
- Default Gateway
- Routing
- `/etc/resolv.conf`
- `dig`
- `nslookup`
- `systemd-resolved`

---

# Practical Observations

## Observation 1

```text
Prediction

↓

Packets need IP addresses, not domain names.

↓

Observation

↓

A command such as ping google.com must first resolve google.com into an IP address.

↓

Explanation

Routers forward packets based on IP addresses. Domain names are resolved before packet transmission.
```

---

## Observation 2

```text
Prediction

↓

DHCP can provide DNS information.

↓

Observation

↓

A newly booted VM can often use domain names immediately after receiving DHCP configuration.

↓

Explanation

DHCP may provide the DNS server address along with IP address, subnet, and default gateway information.
```

---

## Observation 3

```text
Prediction

↓

If DNS fails, IP connectivity may still work.

↓

Observation

↓

ping 8.8.8.8 may succeed while ping google.com fails.

↓

Explanation

The network route may be valid, but name resolution may be broken. Direct IP traffic can still work because it does not require DNS.
```

---

# Commands / Code

```bash
ping google.com
```

Tests both DNS resolution and network reachability.

If this fails, the problem could be DNS, routing, firewalling, or general connectivity.

---

```bash
ping 8.8.8.8
```

Tests direct IP reachability.

If this works while `ping google.com` fails, DNS is a likely problem.

---

```bash
dig google.com
```

Queries DNS records for a domain name.

Useful for observing name resolution directly.

---

```bash
nslookup google.com
```

Another tool for querying DNS resolution.

---

```bash
cat /etc/resolv.conf
```

Shows resolver configuration, often including the DNS server used by the system.

---

```bash
resolvectl status
```

Shows DNS configuration when `systemd-resolved` is in use.

---

# Connections

```text
DHCP
↓

Provides network configuration
↓

IP Address
Gateway
DNS Server
```

---

```text
DNS
↓

Name Resolution
↓

Domain Name
to
IP Address
```

---

```text
Application
↓

Domain Name

↓

DNS Query

↓

Resolved IP Address

↓

Routing

↓

Packet Transmission
```

---

# Common Misconceptions

## Incorrect

```text
Packets are sent to domain names.
```

Correct:

```text
Packets are sent to IP addresses.
Domain names must be resolved before packet transmission.
```

---

## Incorrect

```text
google.com resolves to 8.8.8.8.
```

Correct:

```text
8.8.8.8 is commonly a DNS server address.
google.com resolves to one or more Google service IP addresses, which may vary by time and location.
```

---

## Incorrect

```text
If ping google.com fails, the whole network is broken.
```

Correct:

```text
DNS may be broken while IP connectivity still works.
Testing direct IP reachability helps separate DNS problems from routing or connectivity problems.
```

---

## Incorrect

```text
DHCP and DNS do the same thing.
```

Correct:

```text
DHCP provides network configuration.
DNS resolves names into IP addresses.
```

---

# Key Takeaways

- Domain names are for humans; IP addresses are used for packet delivery.
- DNS connects names to addresses.
- DHCP can tell a VM which DNS server to use.
- DNS failure and network failure are different failure modes.
- `ping 8.8.8.8` and `ping google.com` test different parts of the system.
- `8.8.8.8` is a DNS server address, not the general IP address of `google.com`.
- Name resolution happens before routing and packet transmission.

---

# Review Questions

### Q1. Why can a packet not be delivered using only a domain name?

<details>
<summary>A</summary>

</details>

---

### Q2. What problem does DNS solve?

<details>
<summary>A</summary>

</details>

---

### Q3. What is the difference between a domain name and an IP address?

<details>
<summary>A</summary>

</details>

---

### Q4. What information can DHCP provide that helps DNS work?

<details>
<summary>A</summary>

</details>

---

### Q5. Why is it incorrect to say that `google.com` equals `8.8.8.8`?

<details>
<summary>A</summary>

</details>

---

### Q6. What does it suggest if `ping 8.8.8.8` succeeds but `ping google.com` fails?

<details>
<summary>A</summary>

</details>

---

### Q7. Complete the flow:

```text
Application
↓

Domain Name
↓

?
↓

Resolved IP Address
↓

?
↓

Packet Transmission
```

<details>
<summary>A</summary>

</details>

---

### Q8. How are DHCP and DNS related, but different?

<details>
<summary>A</summary>

</details>

---

### Q9. Why can DNS results vary depending on time, location, or network?

<details>
<summary>A</summary>

</details>

---

### Q10. How does DNS prepare the VM for later package installation, SSH workflows, and general server administration?

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 00
Session 10

Topic:
netplan Fundamentals

How Ubuntu Server stores and applies network configuration.
```

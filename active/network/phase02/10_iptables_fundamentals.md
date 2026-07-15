# Phase 02 - Session 10

## Metadata

```yaml
Roadmap: Networking
Phase: 02
Session: 10
Title: iptables Fundamentals
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-14
```

---

# Objective

Understand how Linux classifies packets into iptables chains, how ordered rules
produce a decision, and how stateful filtering permits legitimate response
traffic while rejecting unsolicited inbound traffic.

This session focused on reading the existing firewall configuration without
modifying it.

---

# Learning Summary

iptables presents packet-processing rules as tables containing chains. A packet
enters a chain according to its relationship with the local host.

```text
Packet destined for this host
        ↓
INPUT

Packet created by this host
        ↓
OUTPUT

Packet routed through this host
        ↓
FORWARD
```

Rules inside a chain are evaluated in order. Each rule contains match
conditions and a target. Match conditions may include protocol, source and
destination addresses, ports, interfaces, and connection state.

```text
Packet enters chain
        ↓
Rule 1 match?
        ├─ no  → Rule 2
        └─ yes → target
```

A terminating target such as `ACCEPT`, `DROP`, or `REJECT` ends the decision
for that chain. If no rule produces a final decision, the chain policy is used.

The observed host used the following filter policies:

```text
INPUT   DROP
FORWARD DROP
OUTPUT  ACCEPT
```

This means unsolicited inbound and forwarded traffic is denied by default,
while locally generated outbound traffic is allowed unless a rule blocks it.
The host can still use the Internet because replies to locally initiated
connections match a `RELATED,ESTABLISHED` rule before the INPUT policy is
reached.

The rules were not a small hand-written list. UFW and Tailscale had created
custom chains and connected them to the built-in chains. The output therefore
represented a packet-processing graph rather than three isolated lists.

---

# Key Concepts

- iptables
- filter table
- nat table
- built-in chain
- custom chain
- rule order
- match conditions
- target
- chain policy
- packet and byte counters
- INPUT
- OUTPUT
- FORWARD
- ACCEPT
- DROP
- REJECT
- RETURN
- connection tracking
- NEW
- ESTABLISHED
- RELATED
- stateful firewall
- MASQUERADE

---

# Practical Observations

## Observation 1 - Built-In Filter Policies

Prediction:

```text
INPUT   → DROP
OUTPUT  → ACCEPT
FORWARD → little or no use
```

Observation:

```text
Chain INPUT (policy DROP ...)
Chain FORWARD (policy DROP ...)
Chain OUTPUT (policy ACCEPT ...)
```

Explanation:

```text
INPUT
= packets whose final destination is this host
= unmatched packets are dropped

OUTPUT
= packets created by this host
= unmatched packets are accepted

FORWARD
= packets routed through this host
= unmatched packets are dropped
```

A policy is not evaluated before the rules. It is the fallback decision used
only when the packet reaches the end of the built-in chain without a terminating
match.

```text
Built-in chain
        ↓
Rules evaluated in order
        ↓
No final decision
        ↓
Policy applied
```

---

## Observation 2 - Reading the Rule Columns

The filter output used columns similar to:

```text
pkts bytes target prot opt in out source destination
```

They were interpreted as:

```text
pkts
= number of matching packets

bytes
= total size of matching packets

target
= action or custom chain entered after a match

prot
= protocol such as tcp, udp, icmp, or all

in
= incoming interface

out
= outgoing interface

source
= source address range

destination
= destination address range
```

A rule counter of `0 packets, 0 bytes` means that no observed packet has matched
that rule since its counters were initialized. It does not prove that the
service or port was never used through another rule or path.

---

## Observation 3 - A Rule Is a Set of AND Conditions

A documentation-safe version of one observed allow rule was:

```text
ACCEPT tcp -- * * 192.168.0.20 192.168.0.10 tcp dpt:2222
```

The rule means:

```text
protocol is TCP
AND source IP is 192.168.0.20
AND destination IP is 192.168.0.10
AND destination port is 2222
        ↓
ACCEPT
```

The learner initially described the rule only as allowing TCP. The corrected
model was that all listed match conditions must be true. If any condition does
not match, evaluation continues to the next rule.

---

## Observation 4 - Interface-Scoped Rules

A documentation-safe Tailscale rule was represented as:

```text
ACCEPT tcp -- tailscale0 * 0.0.0.0/0 0.0.0.0/0 tcp dpt:2222
```

Explanation:

```text
packet entered through tailscale0
AND protocol is TCP
AND destination port is 2222
AND source IPv4 address may be any address
AND destination IPv4 address may be any address
        ↓
ACCEPT
```

`0.0.0.0/0` means the complete IPv4 address space in that field. The rule does
not expose the port through every interface because `tailscale0` is still a
required match condition.

```text
Ordinary Ethernet or Wi-Fi input
→ interface condition does not match

Tailscale input
→ remaining conditions are evaluated
```

---

## Observation 5 - Rule Order Controls the Result

The session used this simplified ordered chain:

```text
1. ACCEPT all  ctstate RELATED,ESTABLISHED
2. ACCEPT tcp  source 192.168.0.20  dpt:2222
3. DROP   all
```

Predicted outcomes:

```text
Response belonging to an existing connection
→ Rule 1
→ ACCEPT

New TCP connection from 192.168.0.20 to port 2222
→ Rule 1 does not match
→ Rule 2 matches
→ ACCEPT

New TCP connection from another source to port 2222
→ Rules 1 and 2 do not match
→ Rule 3 matches
→ DROP
```

This established that iptables is an ordered decision process. A later rule
cannot override a terminating decision already made by an earlier rule.

---

## Observation 6 - Custom Chains Form a Processing Graph

The built-in INPUT chain referenced chains created by Tailscale and UFW.
Documentation-safe structure:

```text
INPUT
        ↓
ts-input
        ↓
ufw-before-logging-input
        ↓
ufw-before-input
        ↓
ufw-after-input
        ↓
ufw-after-logging-input
        ↓
ufw-reject-input
        ↓
ufw-track-input
        ↓
INPUT policy if still undecided
```

A target such as `ts-input` or `ufw-before-input` is not itself an allow or deny
decision. It transfers evaluation to a custom chain.

```text
Built-in chain
        ↓
Custom chain
        ↓
ACCEPT / DROP / REJECT
or
RETURN to caller
```

`RETURN` causes evaluation to resume in the calling chain after the rule that
entered the custom chain.

---

## Observation 7 - Stateful Reply Traffic

The observed UFW rules included a high-counter rule equivalent to:

```text
ACCEPT all -- * * 0.0.0.0/0 0.0.0.0/0 ctstate RELATED,ESTABLISHED
```

This explains why Internet access works despite an INPUT policy of DROP.

```text
Local application starts connection
        ↓
OUTPUT chain
        ↓
OUTPUT policy ACCEPT
        ↓
Remote response returns
        ↓
INPUT chain
        ↓
RELATED,ESTABLISHED rule matches
        ↓
ACCEPT
```

The INPUT policy is never reached for that accepted response.

The session used this simplified state model:

```text
NEW
= packet attempting to begin a new tracked connection

ESTABLISHED
= packet belonging to a tracked connection that has already seen traffic

RELATED
= packet or connection associated with an existing tracked connection
```

This is the basis of stateful firewall behavior: packets are judged partly by
the connection they belong to, not only by isolated header fields.

---

## Observation 8 - DROP and REJECT Differ

The learner predicted:

```text
DROP
→ sender receives no firewall response

REJECT
→ sender receives an explicit failure response
```

Explanation:

```text
DROP
        ↓
Packet silently discarded
        ↓
Sender usually waits for timeout
```

```text
REJECT
        ↓
Packet refused with an error response
        ↓
Sender can fail quickly
```

`REJECT` more clearly communicates failure. `DROP` and `REJECT` are policy
choices; one is not universally more secure than the other.

---

## Observation 9 - FORWARD Was Not Completely Unused

The initial prediction was that FORWARD would be unused. The counters showed
that forwarded packets had passed through Tailscale and UFW forwarding chains.
A documentation-safe forwarding rule was similar to:

```text
ACCEPT all -- virbr0 * 192.168.122.0/24 0.0.0.0/0
```

This connected the host's libvirt virtual network to the FORWARD path.

```text
Virtual machine
        ↓
virbr0
        ↓
Host FORWARD chain
        ↓
Other network
```

The host was not operating as a general-purpose router, but virtual networking
and Tailscale caused limited forwarding activity.

---

## Observation 10 - filter and nat Tables Solve Different Problems

The default command displayed the filter table:

```bash
sudo iptables -L -n -v
```

The NAT table was selected explicitly:

```bash
sudo iptables -t nat -L -n -v
```

The observed NAT chains were:

```text
PREROUTING
INPUT
OUTPUT
POSTROUTING
```

Their policies appeared as `ACCEPT`, but this should not be interpreted as the
same kind of firewall allow policy as the filter table. In the NAT table, the
primary question is whether an address or port translation rule applies.

The observed POSTROUTING chain referenced a Tailscale custom chain containing a
conditional MASQUERADE rule.

```text
POSTROUTING
        ↓
ts-postrouting
        ↓
MASQUERADE when a packet mark matches
```

The POSTROUTING chain had traffic counters, while the visible MASQUERADE rule
had a zero counter. This means packets passed through POSTROUTING, but none of
the counted packets matched that specific MASQUERADE condition.

---

# Commands / Code

```bash
sudo iptables -L -n -v
```

Lists the filter table chains and rules.

```text
-L
= list rules

-n
= show numeric addresses and ports instead of resolving names

-v
= verbose output, including interfaces and counters
```

---

```bash
sudo iptables -t nat -L -n -v
```

Lists chains and rules from the NAT table instead of the default filter table.

```text
-t nat
= select the nat table
```

These commands were used only for observation. No firewall rules were added,
removed, or reordered during the session.

---

# Connections

```text
Session 09 - Linux Packet Flow
        ↓
Packets move through kernel networking paths

Session 10 - iptables Fundamentals
        ↓
Rules inspect packets at INPUT, OUTPUT, and FORWARD paths

Session 11 - nftables Overview
        ↓
Modern Linux packet-filtering interface and ruleset model

Session 12 - Connection Tracking
        ↓
Deeper explanation of NEW, ESTABLISHED, RELATED, and tracked flows
```

Integrated model:

```text
Locally generated packet
        ↓
OUTPUT rules
        ↓
Routing and transmission
```

```text
Packet addressed to local host
        ↓
INPUT rules
        ↓
Local socket or application
```

```text
Packet routed through host
        ↓
FORWARD rules
        ↓
Outgoing network
```

---

# Common Misconceptions

- Incorrect: An INPUT policy of DROP immediately discards every inbound packet.
- Correct: INPUT rules are evaluated first; only unresolved packets reach the
  policy.

---

- Incorrect: A rule mentioning TCP allows all TCP traffic.
- Correct: Protocol, addresses, ports, interfaces, and state conditions are
  combined with AND semantics.

---

- Incorrect: `0.0.0.0/0` makes an interface-scoped rule accessible through all
  interfaces.
- Correct: It removes an address restriction, but the interface condition still
  applies.

---

- Incorrect: A zero counter proves that a service has never been used.
- Correct: It only proves that no counted packet matched that particular rule.

---

- Incorrect: FORWARD was unused because the host was not intentionally acting
  as a router.
- Correct: Virtual networking and Tailscale produced forwarding traffic.

---

- Incorrect: NAT-table ACCEPT and filter-table ACCEPT always mean the same
  thing.
- Correct: The tables serve different purposes; the NAT table primarily selects
  translation behavior.

---

- Incorrect: DROP is always more secure than REJECT.
- Correct: They expose different failure behavior and should be selected based
  on policy and operational needs.

---

# Key Takeaways

- INPUT handles packets destined for the host, OUTPUT handles packets created by
  the host, and FORWARD handles routed-through traffic.
- Rules are evaluated in order, and the first terminating match decides the
  packet's result.
- A built-in chain policy is the fallback after all rules fail to decide.
- Match conditions use AND semantics.
- Custom chains created by UFW and Tailscale form a packet-processing graph.
- Packet and byte counters are evidence that a rule has matched traffic.
- `RELATED,ESTABLISHED` allows replies to locally initiated connections despite
  a default-deny INPUT policy.
- DROP silently discards traffic, while REJECT reports failure.
- The filter table controls packet acceptance, while the NAT table controls
  address and port translation.
- Virtual machines and overlay networking can cause FORWARD traffic even when
  the host is not used as a conventional router.

---

# Review Questions

### Q1. Which built-in chain handles a packet whose final destination is the local host?

<details>
<summary>A</summary>

</details>

---

### Q2. What is the difference between a rule target and a built-in chain policy?

<details>
<summary>A</summary>

</details>

---

### Q3. Why does an INPUT policy of DROP not prevent ordinary web browsing?

<details>
<summary>A</summary>

</details>

---

### Q4. How should multiple match fields in one iptables rule be combined when reading the rule?

<details>
<summary>A</summary>

</details>

---

### Q5. What does `0.0.0.0/0` mean in the source field, and why can an interface condition still restrict that rule?

<details>
<summary>A</summary>

</details>

---

### Q6. What can be concluded from a rule showing `0 packets, 0 bytes`, and what cannot be concluded?

<details>
<summary>A</summary>

</details>

---

### Q7. Why can rule order change the final result for the same packet?

<details>
<summary>A</summary>

</details>

---

### Q8. What is the role of `RETURN` in a custom chain?

<details>
<summary>A</summary>

</details>

---

### Q9. Compare DROP and REJECT from the sender's perspective.

<details>
<summary>A</summary>

</details>

---

### Q10. Why did the host show FORWARD traffic even though it was not configured as a general-purpose router?

<details>
<summary>A</summary>

</details>

---

### Q11. How do the filter and NAT tables differ in purpose?

<details>
<summary>A</summary>

</details>

---

### Q12. Complete the stateful firewall flow:

```text
Local application starts connection
        ↓
?
        ↓
Remote response returns
        ↓
?
        ↓
ACCEPT before INPUT policy
```

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Next:
Phase 02
Session 11

Topic:
nftables Overview
```

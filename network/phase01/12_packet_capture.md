# Packet Capture

## Objective

By the end of this session, you should be able to explain:

- What a packet capture is
- Why packet capture exists
- Why security engineers capture packets
- How packet captures relate to sockets and connections
- What information can be observed from network traffic

## Why Packet Capture Exists

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

Socket
↓
Application ↔ Network Stack
```

Question:

```text
How do we observe what is actually happening
on the network?
```

Applications tell us:

```text
Connected

Failed

Timeout
```

But those are only symptoms.

Packet capture allows us to observe the actual traffic.

## Core Problem

Suppose:

```text
curl https://example.com
```

fails.

Question:

```text
DNS problem?

Routing problem?

TCP problem?

TLS problem?

Server problem?
```

Without observing traffic:

```text
We don't know.
```

Packet capture exists to reveal what is actually happening.

## Mental Model

Think:

```text
Packet Capture
=
Network Telescope
```

or

```text
Packet Capture
=
Traffic Camera
```

It allows us to observe communication that is normally invisible.

## Example

Suppose:

```text
Firefox
↓
google.com
```

A packet capture may reveal:

```text
DNS Query

↓

DNS Response

↓

TCP Handshake

↓

TLS Handshake

↓

Encrypted Traffic
```

Instead of guessing:

```text
Maybe DNS failed...
```

you can actually observe the traffic.

## What Can Be Observed?

Packet captures commonly reveal:

```text
Source IP

Destination IP

Source Port

Destination Port

Protocol

Packet Size

Timing
```

Sometimes:

```text
Application Data
```

can also be observed.

This depends on whether encryption is being used.

## Observation Principle

Before learning tcpdump or Wireshark filters, ask:

```text
What question am I trying to answer?
```

Examples:

```text
Did DNS succeed?

Did TCP connect?

Did the server respond?

Was traffic encrypted?
```

# QA

**Q1.**
What problem does packet capture solve?

<details>
<summary><strong>A1.</strong></summary>

What really happened in the communication</details>

**Q2.**
Why might logs be insufficient when troubleshooting networking problems?

<details>
<summary><strong>A2.</strong></summary>
Logs cannot show everything what actually happened</details>

**Q3.**
What is a packet capture?

<details>
<summary><strong>A3.</strong></summary>

Network Telescope</details>

**Q4.**
Why is packet capture often described as a network telescope?

<details>
<summary><strong>A4.</strong></summary>

They can reveal what happened below</details>

**Q5.**
What kinds of information can commonly be observed in packets?

<details>
<summary><strong>A5.</strong></summary>

IP, Port, protocol, packet size, time</details>

**Q6.**
Why might packet capture be useful during security investigations?

<details>
<summary><strong>A6.</strong></summary>

They give us the clue what happen</details>

**Q7.**
What is the relationship between packet captures and network troubleshooting?

<details>
<summary><strong>A7.</strong></summary>

Packet capture is like assistant for troubleshooting</details>

**Q8.**
How does packet capture relate to DNS, TCP, TLS, and sockets?

<details>
<summary><strong>A8.</strong></summary>

Packet capture can reveal what they do</details>

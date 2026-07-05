# Network Troubleshooting

## Metadata

```yaml
Roadmap: Networking
Phase: 01
Session: 13
Title: Network Troubleshooting
Status:
Review:
ArchiveVersion: 2
Date:
```

## Objective

By the end of this session, you should be able to explain:

- What network troubleshooting actually is
- Why troubleshooting requires a layered approach
- How to systematically isolate networking failures
- How DNS, IP, Routing, TCP, TLS, and HTTP contribute to failures
- Why guessing is inferior to observation

## Why Troubleshooting Exists

In the real world:

```text
"It doesn't work."
```

is one of the most common networking problems.

Users rarely say:

```text
DNS failed.
```

or

```text
TCP handshake failed.
```

Instead they say:

```text
The website won't load.

SSH doesn't connect.

The API is down.

The internet is broken.
```

The job of troubleshooting is to discover:

```text
What failed?

Where did it fail?

Why did it fail?
```

## Core Problem

Suppose:

```bash
curl https://example.com
```

returns:

```text
Connection failed
```

Question:

```text
What actually failed?
```

Possibilities:

```text
DNS

IP

Routing

TCP

TLS

HTTP

Server
```

The error message alone rarely tells the whole story.

## Mental Model

Think:

```text
Troubleshooting
=
Eliminating Possibilities
```

Not:

```text
Guessing
```

Instead:

```text
Observe

↓

Test

↓

Eliminate

↓

Repeat
```

## The Troubleshooting Ladder

When a network problem occurs:

```text
DNS
↓
IP
↓
Routing
↓
TCP
↓
TLS
↓
HTTP
↓
Application
```

Move step-by-step.

Do not skip layers.

## Example

Suppose:

```bash
curl https://google.com
```

fails.

Bad troubleshooting:

```text
Google is down.
```

Good troubleshooting:

```text
Can DNS resolve?

↓

Can I reach the IP?

↓

Can TCP connect?

↓

Can TLS negotiate?

↓

Does HTTP respond?
```

## Observation Principle

Ask:

```text
What evidence do I have?
```

Not:

```text
What do I think happened?
```

The network does not care about assumptions.

It only reveals evidence.

# Review Questions

### Q1. What is the goal of network troubleshooting?

<details>
<summary>A</summary>

</details>

### Q2. Why is guessing a poor troubleshooting strategy?

<details>
<summary>A</summary>

</details>

### Q3. Why should troubleshooting proceed layer by layer?

<details>
<summary>A</summary>

</details>

### Q4. What does it mean to eliminate possibilities?

<details>
<summary>A</summary>

</details>

### Q5. What kinds of failures can produce a simple "connection failed" error?

<details>
<summary>A</summary>

</details>

### Q6. Why is observation more valuable than assumptions?

<details>
<summary>A</summary>

</details>

### Q7. How does packet capture help troubleshooting?

<details>
<summary>A</summary>

</details>

### Q8. How does troubleshooting relate to DNS, IP, Routing, TCP, TLS, HTTP, and sockets?

<details>
<summary>A</summary>

</details>

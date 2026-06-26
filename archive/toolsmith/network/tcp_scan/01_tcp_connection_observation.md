# Minimal TCP Port Scanner

## Session Goal

Understand what a TCP port scanner actually observes.

Build the smallest possible scanner to observe TCP connection behavior.

## What Is A Port Scanner?

A TCP port scanner does not directly identify services.

It attempts a TCP connection and observes the result.

The scanner is asking:

```text
Can I establish a TCP connection to this host and port?
```

## Core Observation

A TCP scanner observes:

```text
TCP Connection Attempt
↓
Result
```

Possible results:

```text
Open
Closed
Timeout
```

## Mental Model

Think:

```text
Scanner
↓
TCP connect()
↓
Observe Result
```

Not:

```text
Scanner
↓
Magically Knows Service
```

The scanner only observes connection behavior.

## Open Port

A port is considered open when:

```text
TCP Handshake
=
Successful
```

The remote side accepts the connection.

Example:

```text
127.0.0.1:8000
```

If a local web server is listening:

```text
connect()
↓
Success
↓
Open
```

## Closed Port

A port is considered closed when:

```text
Target Host Reachable
+
Nothing Listening
```

Example:

```text
127.0.0.1:9999
```

Possible observation:

```text
Connection Refused
```

## Timeout

Timeout means:

```text
No Response Received
```

Possible causes:

```text
Firewall
Packet Filtering
Dropped Packets
Host Unreachable
```

A timeout does not automatically mean the port is open or closed.

## Program Design

Input:

```bash
python tcp_scan.py 127.0.0.1 22
```

Output:

```text
127.0.0.1:22 open
```

## Expected Program Flow

```text
Read Arguments
↓
Create Socket
↓
Set Timeout
↓
Attempt Connection
↓
Observe Result
↓
Print Result
↓
Close Socket
```

## First Imports

```python
import socket
import sys
```

### socket

Provides access to:

```text
TCP
UDP
Network Communication
Sockets
```

### sys

Provides access to:

```text
Command Line Arguments
Program Exit
Runtime Information
```

Example:

```python
sys.argv
```

## Observation Habit

When using a scanner, ask:

- What exactly is being observed?
- What does success actually mean?
- What does failure actually mean?
- What assumptions am I making?
- Am I observing a service or only a connection?

## Transferable Mental Model

```text
Host
+
Port
↓
TCP Connection Attempt
↓
Observation
↓
Conclusion
```

Most security tools are fundamentally:

```text
Send Something
↓
Observe Response
↓
Interpret Result
```

# QA

**Q1.**

What is the primary observation made by a TCP port scanner?

<details>
<summary><strong>A1.</strong></summary>
A TCP port scanner observes the result of a TCP connection attempt.


</details>

---

**Q2.**

What does an open port mean from a TCP perspective?

<details>
<summary><strong>A2.</strong></summary>
The remote side accepts the connection

</details>

---

**Q3.**

What is the difference between an open port and a running service?

<details>
<summary><strong>A3.</strong></summary>
Open port = TCP connection succeded
Running service = Some application is listening behind that port

</details>

---

**Q4.**

Why is a timeout different from a closed port?

<details>
<summary><strong>A4.</strong></summary>
Closed means the host responded and refused the connection.
Timeout means no response was received.


</details>

---

**Q5.**

Why should localhost be the first target when testing a scanner?

<details>
<summary><strong>A5.</strong></summary>
They suits for testing


</details>

---

**Q6.**

Complete:

```text
Host
+
Port
↓
________________
↓
Observation
```

<details>
<summary><strong>A6.</strong></summary>
TCP connection attempt

</details>

---

**Q7.**

What is the purpose of `socket.settimeout()`?

<details>
<summary><strong>A7.</strong></summary>
To prevent the scanner from waiting forever.


</details>

---

**Q8.**

What information does `sys.argv` provide?

<details>
<summary><strong>A8.</strong></summary>
It provides command-line arguments.


</details>

---

**Q9.**

Does a successful `connect()` identify whether the service is HTTP or SSH?

Why?

<details>
<summary><strong>A9.</strong></summary>
No. connect() only tells us that a TCP connection succeeded.
It does not identify the service.


</details>

---

**Q10.**

In one sentence, explain what a TCP port scanner actually does.

<details>
<summary><strong>A10.</strong></summary>
A TCP port scanner does not observe services.

</details>

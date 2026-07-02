# Multi-Port Scanner

## Session Goal

Extend the single-port scanner into a scanner that can observe multiple ports automatically.

Learn:

```text
One Observation
↓
Repeated Many Times
```

using loops.

## Previous Session

Session 01:

```text
Host
+
Port
↓
connect()
↓
Open / Closed
```

Example:

```text
127.0.0.1:4212
```

One port.

One result.

## New Goal

Instead of:

```bash
python3 tcp_scan.py 127.0.0.1 22

python3 tcp_scan.py 127.0.0.1 80

python3 tcp_scan.py 127.0.0.1 443
```

we want:

```bash
python3 tcp_scan.py 127.0.0.1
```

and automatically scan:

```text
22
80
443
8000
```

## Core Observation

The scanner is still doing exactly the same thing.

```text
connect()
↓
Observe
↓
Report
```

The only difference is:

```text
Repeated Multiple Times
```

## Mental Model

Think:

```text
Port List
↓
Loop
↓
Connect
↓
Observe
↓
Print Result
```

The scanner itself is not changing.

The repetition is changing.

## Current Problem

Right now:

```python
host = sys.argv[1]
port = int(sys.argv[2])
```

requires:

```bash
python3 tcp_scan.py 127.0.0.1 4212
```

every time.

That becomes annoying very quickly.

## First Port List

For now:

```python
ports = [22, 80, 443, 4212]
```

Hardcoded is fine.

We are learning loops.

Not user interfaces.

## New Concept: List

Example:

```python
ports = [22, 80, 443]
```

A list stores multiple values.

Think:

```text
Port Collection
```

## New Concept: Loop

Example:

```python
ports = [22, 80, 443]

for port in ports:
    print(port)
```

Output:

```text
22
80
443
```

Python takes each value from the list and places it into:

```python
port
```

one at a time.

## Observation Habit

When you see:

```python
scan(22)
scan(80)
scan(443)
scan(4212)
```

ask:

```text
Can a loop do this?
```

Usually:

```text
Yes
```

## Transferable Mental Model

Many security tools are:

```text
Target List
↓
Loop
↓
Observation
↓
Results
```

Examples:

```text
Port Scanner
Directory Enumerator
Header Collector
JWT Analyzer
Log Analyzer
```

## Design Exercise

Suppose:

```python
ports = [22, 80, 443, 4212]
```

Question:

How many times will the loop execute?

## Prediction Exercise

Suppose:

```text
22    closed
80    closed
443   closed
4212  open
```

Question:

How many successful TCP connections occur?

## Build Plan

Current scanner:

```python
host = sys.argv[1]
port = int(sys.argv[2])
```

Session 02 scanner:

```python
host = sys.argv[1]

ports = [22, 80, 443, 4212]
```

and:

```python
for port in ports:
    ...
```

will perform the scans.

Do not write the final implementation yet.

First predict what this prints:

```python
ports = [22, 80, 443, 4212]

for port in ports:
    print(port)
```

## QA

**Q1.**

What new capability does Session 02 add?

<details>
<summary><strong>A1.</strong></summary>
Scan multiple values in order


</details>

---

**Q2.**

What is a Python list?

<details>
<summary><strong>A2.</strong></summary>
a collection that stores multiple values in order


</details>

---

**Q3.**

Complete:

```text
Port List
↓
________
↓
Connect
↓
Observe
```

<details>
<summary><strong>A3.</strong></summary>
Loop

</details>

---

**Q4.**

How many times will this loop execute?

```python
ports = [22, 80, 443]

for port in ports:
    print(port)
```

<details>
<summary><strong>A4.</strong></summary>
3

</details>

---

**Q5.**

What changes between scans in a multi-port scanner?

<details>
<summary><strong>A5.</strong></summary>
port


</details>

---

**Q6.**

What stays the same between scans?

<details>
<summary><strong>A6.</strong></summary>
host, scan_port(), logic, socket/connect/close flow

</details>

---

**Q7.**

Why is a loop better than manually writing multiple scan calls?

<details>
<summary><strong>A7.</strong></summary>
It reduces duplicate code and keeps the structure consistent when adding new ports.

</details>

---

**Q8.**

In one sentence, explain how a multi-port scanner works.

<details>
<summary><strong>A8.</strong></summary>
A multi-port scanner loops over a port list and runs the same TCP connection test for each port.


</details>

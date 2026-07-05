# Phase 01 — Session 14
# Networking Concepts Inside HTB

## Metadata

```yaml
Roadmap: Networking
Phase: 01
Session: 14
Title: Networking Concepts Inside HTB
Status:
Review:
ArchiveVersion: 2
Date:
```

## Goal

Connect networking fundamentals to real HTB enumeration workflows.

By the end of this session, you should be able to view an HTB machine as:

```text
a remote system reachable through a network
```

instead of:

```text
a box to hack
```

---

# Mental Model

When you connect to HTB:

```text
Your Machine
↓
VPN
↓
HTB Network
↓
Target Machine
```

Everything learned so far still applies:

```text
DNS
IP
Routing
ARP
TCP
TLS
HTTP
```

The difference is:

```text
you are now observing
another machine
instead of your own
```

---

# HTB Is A Networking Environment

Many beginners think:

```text
HTB
=
security
```

More accurately:

```text
HTB
=
networked systems
+
security
```

Every attack begins with:

```text
communication
```

before:

```text
exploitation
```

---

# HTB Enumeration Flow

Typical workflow:

```text
Target IP
↓
Reachability
↓
Open Ports
↓
Services
↓
Applications
↓
Behavior
↓
Attack Surface
```

---

# Step 1 — Reachability

Question:

```text
Can I reach the machine?
```

Example:

```bash
ping TARGET_IP
```

Observation:

```text
reply
timeout
packet loss
TTL
```

---

# Step 2 — Open Ports

Question:

```text
What is listening?
```

Example:

```bash
nmap TARGET_IP
```

Observation:

```text
22/tcp
80/tcp
443/tcp
21/tcp
```

Remember:

```text
Open Port
≠ Vulnerability

Open Port
=
Service Exists
```

---

# Step 3 — Service Identification

Question:

```text
What service is behind the port?
```

Examples:

```bash
nc TARGET_IP 80
```

```bash
curl http://TARGET_IP
```

```bash
nmap -sV TARGET_IP
```

Observation:

```text
Apache
nginx
OpenSSH
vsftpd
```

---

# Step 4 — Protocol Thinking

Instead of:

```text
Port 80
```

think:

```text
HTTP
```

Instead of:

```text
Port 22
```

think:

```text
SSH
```

Instead of:

```text
Port 21
```

think:

```text
FTP
```

The goal is:

```text
port
→ protocol
→ behavior
```

---

# Step 5 — Application Observation

Question:

```text
What does the service actually do?
```

Examples:

```bash
curl TARGET_IP
```

```bash
curl -I TARGET_IP
```

```bash
curl -v TARGET_IP
```

Observe:

```text
headers
redirects
status codes
content
```

---

# Network Layers Inside HTB

When visiting:

```text
http://TARGET_IP
```

What happened?

```text
Routing
↓
TCP
↓
HTTP
↓
Response
```

When visiting:

```text
https://TARGET_IP
```

What happened?

```text
Routing
↓
TCP
↓
TLS
↓
HTTP
↓
Response
```

---

# Enumeration As Observation

Bad mindset:

```text
Run tool
Get answer
```

Good mindset:

```text
Observe
↓
Form hypothesis
↓
Verify
↓
Observe again
```

Example:

```text
Port 80 open
```

Question:

```text
Web server?
Proxy?
API?
Redirector?
```

Not:

```text
What exploit?
```

---

# HTB Example Reasoning

Suppose:

```text
10.129.x.x
```

Target responds.

Nmap shows:

```text
22/tcp
80/tcp
```

Reasoning:

```text
Machine reachable

↓

SSH exists

↓

HTTP exists

↓

Two observable services

↓

Investigate behavior
```

---

# Observation Exercise

Choose any active HTB machine.

Run:

```bash
ping TARGET_IP
```

Questions:

```text
1. Does it reply?

2. What TTL do you observe?

3. Is packet loss present?
```

---

Run:

```bash
nmap TARGET_IP
```

Questions:

```text
1. Which ports are open?

2. Which protocols are exposed?

3. Which service interests you most?
```

---

Run:

```bash
curl http://TARGET_IP
```

Questions:

```text
1. Does HTTP respond?

2. What status code appears?

3. What content is returned?
```

---

# Review Questions

### Q1. Why is reachability checked before scanning ports?

<details>
<summary>A</summary>

</details>

### Q2. Why is an open port not automatically a vulnerability?

<details>
<summary>A</summary>

</details>

### Q3. Why do we identify protocols before looking for weaknesses?

<details>
<summary>A</summary>

</details>

### Q4. Why is enumeration fundamentally a networking activity?

<details>
<summary>A</summary>

</details>

---

# Final Mental Model

```text
Target IP
↓
Reachability
↓
Routing
↓
TCP Connection
↓
Protocol Identification
↓
Application Observation
↓
Attack Surface Discovery
```

HTB machines are not puzzles floating in isolation.

They are networked systems.

Understanding how information reaches them is the foundation of understanding how they can be observed, administered, secured, and eventually tested.

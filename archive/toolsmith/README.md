# Security Toolsmith

> Build small security tools from scratch to understand how common security, networking, and analysis tools work internally.
>
> Philosophy:
>
> - Understanding before automation
> - Observation before exploitation
> - Build before attack
> - Small tools over black-box usage
> - Ethical and defensive learning only
> - Local labs, HTB, and explicitly permitted targets only

---

# Learning Outcome

By the end of this project, you should understand:

- TCP/IP communication
- Socket programming
- DNS resolution
- HTTP request/response flow
- Parsing structured data
- Encoding and decoding formats
- JWT structure
- Basic fingerprinting concepts
- Log analysis fundamentals
- Error handling
- CLI tool design
- How many common security tools work internally

---

# Phase 01 — Networking Observation Tools

Goal:

Understand network communication through direct socket interaction.

---

## Session 01 - Minimal TCP Port Scanner

Build:

- Single-port TCP scanner

Concepts:

- TCP
- Sockets
- connect()
- Open vs closed ports
- Timeouts

---

## Session 02 - Multi-Port Scanner

Build:

- Scan a list of ports

Concepts:

- Loops
- Reusable functions
- Result collection

---

## Session 03 - Service Guessing

Build:

- Common port identification

Concepts:

- Port conventions
- Service mapping

Example:

```text
22   -> SSH
80   -> HTTP
443  -> HTTPS
```

---

## Session 04 - Simple Banner Grabber

Build:

- Connect and read banners

Concepts:

- recv()
- Initial service responses

Observe:

```text
SSH-2.0-OpenSSH_9.7
```

---

## Session 05 - DNS Resolver

Build:

- Hostname → IP resolver

Concepts:

- DNS
- Name resolution

---

## Session 06 - Reverse DNS Lookup

Build:

- IP → hostname lookup

Concepts:

- PTR records
- Reverse mapping

---

# Phase 02 — HTTP Observation Tools

Goal:

Understand HTTP without using requests first.

---

## Session 01 - Raw HTTP Client

Build:

- Send HTTP requests using sockets

Concepts:

- HTTP protocol
- Request lines
- Headers

---

## Session 02 - HTTP Header Fetcher

Build:

- Retrieve response headers

Concepts:

- Status codes
- Response metadata

Observe:

```http
Server:
Content-Type:
Content-Length:
```

---

## Session 03 - Response Body Reader

Build:

- Retrieve page contents

Concepts:

- recv loops
- Content handling

---

## Session 04 - HTTP Fingerprint Collector

Build:

- Collect identifying information

Observe:

```text
Server
X-Powered-By
Cookies
Redirects
```

---

## Session 05 - Redirect Tracker

Build:

- Follow Location headers

Concepts:

- 301
- 302
- Redirect chains

---

## Session 06 - Response Comparison Tool

Build:

- Compare two responses

Concepts:

- Content differences
- Header differences

---

# Phase 03 — Encoding and Token Analysis

Goal:

Understand how encoded data appears in real applications.

---

## Session 01 - Base64 Inspector

Build:

- Detect and decode Base64

Concepts:

- Encoding vs encryption

---

## Session 02 - URL Encoding Analyzer

Build:

- Decode URL-encoded strings

Concepts:

```text
%20
%2F
%3A
```

---

## Session 03 - Hex Inspector

Build:

- Detect and decode hexadecimal data

Concepts:

- Binary representation

---

## Session 04 - JWT Structure Analyzer

Build:

- Parse JWT sections

Concepts:

```text
header.payload.signature
```

---

## Session 05 - JWT Pretty Printer

Build:

- Human-readable JWT output

Concepts:

- JSON parsing
- Formatting

---

## Session 06 - JWT Fingerprinting

Build:

- Detect:

```text
alg
typ
exp
iat
sub
role
```

Concepts:

- Metadata observation

---

# Phase 04 — Web Content Discovery Tools

Goal:

Understand how discovery tools work internally.

---

## Session 01 - Directory Enumerator

Build:

- Test common paths

Concepts:

- HTTP status codes

---

## Session 02 - Wordlist Reader

Build:

- Read external wordlists

Concepts:

- File handling

---

## Session 03 - Directory Brute-Forcer

Build:

- Automated path discovery

Concepts:

- Request loops

---

## Session 04 - Extension Enumerator

Build:

- Try:

```text
.php
.html
.txt
.js
```

---

## Session 05 - Response Length Analysis

Build:

- Compare page sizes

Concepts:

- False positive detection

---

## Session 06 - Simple Content Fingerprinting

Build:

- Analyze:

```text
titles
headers
keywords
```

---

# Phase 05 — Log Analysis Tools

Goal:

Understand security-relevant log observation.

---

## Session 01 - Log Reader

Build:

- Read log files

Concepts:

- File parsing

---

## Session 02 - Pattern Detector

Build:

- Search for keywords

Example:

```text
error
failed
warning
```

---

## Session 03 - IP Address Extractor

Build:

- Extract IPv4 addresses

Concepts:

- Regular expressions

---

## Session 04 - Frequency Counter

Build:

- Count repeated events

Concepts:

- Dictionaries

---

## Session 05 - Authentication Failure Detector

Build:

- Find failed login attempts

Concepts:

- Pattern matching

---

## Session 06 - Mini Log Analyzer

Build:

- Combine previous tools

Output:

```text
Top IPs
Top errors
Failed logins
```

---

# Phase 06 — Response and Payload Fingerprinting

Goal:

Learn to observe structures rather than attack them.

---

## Session 01 - Content-Type Fingerprinter

Build:

- Detect:

```text
JSON
HTML
XML
Plain text
```

---

## Session 02 - JSON Structure Analyzer

Build:

- Inspect JSON keys

Concepts:

- Recursive parsing

---

## Session 03 - Header Pattern Detector

Build:

- Identify common technologies

Observe:

```text
Apache
Nginx
Express
Flask
```

---

## Session 04 - Cookie Inspector

Build:

- Analyze cookie attributes

Observe:

```text
Secure
HttpOnly
SameSite
```

---

## Session 05 - Response Similarity Tool

Build:

- Compare multiple responses

Concepts:

- Fingerprinting

---

## Session 06 - Mini Web Recon Observer

Build:

Combines:

- Header collection
- Content type detection
- Technology hints
- Redirect analysis

---

# Phase 07 — Toolsmith Project

Goal:

Combine everything learned into a unified toolkit.

---

## Final Project

### security-toolsmith

Structure:

```text
security-toolsmith/
├── networking/
│   ├── tcp_scanner.py
│   ├── banner_grabber.py
│   └── dns_lookup.py
│
├── http/
│   ├── header_fetcher.py
│   ├── redirect_tracker.py
│   └── response_compare.py
│
├── encoding/
│   ├── base64_inspector.py
│   ├── hex_inspector.py
│   └── jwt_analyzer.py
│
├── discovery/
│   ├── dir_enum.py
│   └── content_fingerprint.py
│
├── logs/
│   ├── pattern_detector.py
│   └── log_analyzer.py
│
├── fingerprinting/
│   ├── header_fingerprint.py
│   └── response_similarity.py
│
├── examples/
├── sample_logs/
├── sample_tokens/
├── README.md
└── requirements.txt
```

---

# After Completion

Natural next projects:

1. HTTP Proxy Observer
2. Packet Capture Analysis
3. Local IDS Prototype
4. Web Application Mapper
5. Network Traffic Visualizer
6. Mini Burp-like Observer
7. Mini Wireshark-like Parser
8. Security Automation Toolkit

These projects build directly on the concepts learned in Security Toolsmith.

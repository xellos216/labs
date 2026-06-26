# Roadmap Index

> This document provides a high-level overview of every roadmap in the Labs project.
>
> It serves as the project's entry point and navigation document rather than a learning archive.

---

# Purpose

The Roadmap Index exists to:

* provide a quick overview of all learning tracks
* define the purpose of each roadmap
* show long-term progression
* avoid duplicate roadmap creation
* simplify project navigation

It should remain concise and stable.

---

# Roadmap Overview

| Location             | Roadmap                     | Primary Focus                                | Status   |
| -------------------- | --------------------------- | -------------------------------------------- | -------- |
| `unix/`              | Unix                        | CLI, text processing, observability          | Active   |
| `c/`                 | C Programming               | Memory, ELF, assembly foundations            | Active   |
| `network/`           | Networking                  | Communication, protocols, packet reasoning   | Active   |
| `server/`            | Linux Server Administration | Operations, troubleshooting, recovery        | Active   |
| `window/`            | Windows Fundamentals        | Windows architecture and enterprise systems  | Active   |
| `crypto/`            | Cryptography                | Byte reasoning and transformation analysis   | Active   |
| `payload/`           | Payload Construction        | Parser reasoning and input interpretation    | Active   |
| `archive/flask/`     | Flask                       | HTTP, web applications, security foundations | Archived |
| `archive/toolsmith/` | Security Toolsmith          | Building security-related utilities          | Archived |

Status meanings:

* **Active** — maintained as a current top-level learning track
* **Archived** — preserved for history or reference and not treated as a
  current top-level track

Other directories under `archive/` preserve earlier projects and learning
records. They are not automatically treated as current roadmaps.

---

# Suggested Learning Relationships

The roadmaps are designed to reinforce one another.

```text
Unix
        │
        ▼
C Programming
        │
        ▼
Linux Internals
        │
        ▼
Networking
        │
        ▼
Linux Server Administration
        │
        ▼
Windows Fundamentals
        │
        ▼
Flask
        │
        ▼
Security Toolsmith
        │
        ▼
Cryptography
        │
        ▼
Payload Construction
        │
        ▼
Embedded Linux & Firmware Analysis
```

This is a conceptual dependency graph rather than a strict prerequisite order.

---

# Roadmap Summaries

## Unix

Focus

* stream processing
* composable CLI workflows
* observability
* shell reasoning

Supports:

* Server Administration
* Networking
* Embedded Linux
* Toolsmith

---

## C Programming

Focus

* process memory
* ELF
* assembly
* debugging

Supports:

* Linux Internals
* Reverse Engineering
* Embedded Linux

---

## Networking

Focus

* packet flow
* Linux networking
* protocols
* packet analysis

Supports:

* Flask
* Server Administration
* HTB
* Security

---

## Linux Server Administration

Focus

* services
* authentication
* logging
* troubleshooting
* recovery

Supports:

* Infrastructure
* Security
* Production Linux

---

## Windows Fundamentals

Focus

* Windows architecture
* enterprise systems
* authentication
* Active Directory

Supports:

* Enterprise Security
* Incident Response
* Windows Internals

---

## Flask

Focus

* HTTP
* sessions
* authentication
* web application architecture

Supports:

* Web Security
* Payload Construction

---

## Security Toolsmith

Focus

* building small security utilities
* sockets
* HTTP
* parsers

Supports:

* Security Automation
* Python Engineering

---

## Cryptography

Focus

* bytes
* transformations
* XOR
* token analysis

Supports:

* Payload Construction
* Web Security

---

## Payload Construction

Focus

* parser reasoning
* trust boundaries
* input interpretation
* multi-stage execution

Supports:

* Web Security
* Secure Software Design

---

# Current Status

Each roadmap progresses independently.

Progress should always follow:

* the roadmap document
* completed archive documents

Never infer skipped phases or sessions.

Repository location is authoritative for lifecycle classification:

* top-level topic directories represent current learning areas
* `archive/` contains preserved historical material

Status does not imply completion. Determine progress from the roadmap and its
recorded phase or session documents.

---

# Future Roadmaps

Potential future additions include:

* Reverse Engineering
* Windows Internals
* Malware Analysis
* Digital Forensics
* Cloud Infrastructure
* Kubernetes
* eBPF
* Operating System Internals

These should be added only after a dedicated roadmap has been created.

---

# Maintenance Rules

When adding a new roadmap:

* update this index
* add the roadmap to Project Sources
* follow `ROADMAP_FORMAT.md`
* preserve existing roadmap names whenever practical

When archiving a roadmap:

* update its location and status in this index
* preserve its learning history
* avoid rewriting its documents solely to match current templates

This document should remain an overview, not a detailed curriculum.

---

# Project Vision

Together, these roadmaps form a connected systems curriculum.

The long-term objective is to understand complete computing systems—from source code and hardware to networking, operating systems, applications, and security—through evidence-based reasoning and practical observation.

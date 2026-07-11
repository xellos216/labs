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

# Repository Structure

Labs is organized by learning status and project function.

```text
active/
backlog/
archive/
docs/
AGENTS.md
README.md
```

## active/

`active/` contains roadmaps that are currently practiced or expanded.

Canonical active roadmap path:

```text
active/<roadmap>/README.md
```

## backlog/

`backlog/` contains planned, paused, or future roadmaps.

Backlog roadmap path:

```text
backlog/<roadmap>/README.md
```

## archive/

`archive/` contains roadmaps whose planned learning sessions are complete and whose records remain available for review and reference.

Archived roadmap path:

```text
archive/<roadmap>/README.md
```

## docs/

`docs/labs/` contains project governance, templates, source policy, and workflow rules.

The top-level `archive/` directory is a roadmap lifecycle location, not a historical restoration tree. Historical or pre-redaction material should not be reintroduced unless the user explicitly requests a dedicated restoration, migration, or private archival task.

---

# Roadmap Overview

| Location                            | Roadmap                     | Primary Focus                                 | Status  |
| ----------------------------------- | --------------------------- | --------------------------------------------- | ------- |
| `active/unix/`                      | Unix                        | CLI, text processing, observability           | Active  |
| `active/c/`                         | C Programming               | Memory, ELF, assembly foundations             | Active  |
| `active/network/`                   | Networking                  | Communication, protocols, packet reasoning    | Active  |
| `active/server/`                    | Linux Server Administration | Operations, troubleshooting, recovery         | Active  |
| `active/crypto/`                    | Cryptography                | Byte reasoning and transformation analysis    | Active  |
| `active/payload/`                   | Payload Construction        | Parser reasoning and input interpretation     | Active  |
| `backlog/flask/`                    | Flask                       | HTTP, web applications, security foundations  | Backlog |
| `backlog/toolsmith/`                | Security Toolsmith          | Building security-related utilities           | Backlog |
| `backlog/vulnerability_report_lab/` | Vulnerability Report Lab    | Vulnerability verification and report writing | Backlog |
| `backlog/devtool/`                  | DevTools                    | Browser troubleshooting and request analysis  | Backlog |
| `backlog/echotrace/`                | EchoTrace                   | Public-comment pattern analysis               | Backlog |
| `backlog/ironforge/`                | Iron Forge                  | Systems/network/home-lab planning             | Backlog |
| `backlog/LFS/`                      | Linux From Scratch          | Linux build process and system construction   | Backlog |
| `backlog/myjarvis/`                 | MyJarvis                    | Personal assistant / lab interface project    | Backlog |
| `backlog/window/`                   | Windows                     | Paused or alternate Windows roadmap material  | Backlog |
| `archive/numbersystem/`             | Number Systems              | Binary, hex, bytes, encoding foundations      | Archive |

Status meanings:

* **Active** — maintained as a current learning track under `active/`
* **Backlog** — planned, paused, or future work under `backlog/`
* **Archive** — planned learning sessions are complete; review and reference continue under `archive/`

Repository location is authoritative for lifecycle classification.

---

# Roadmap File Policy

Each roadmap owns its roadmap document inside its current lifecycle directory.

Canonical roadmap paths:

```text
active/<roadmap>/README.md
backlog/<roadmap>/README.md
archive/<roadmap>/README.md
```

Current active examples:

```text
active/unix/README.md
active/c/README.md
active/network/README.md
active/server/README.md
active/crypto/README.md
active/payload/README.md
```

Backlog roadmap path:

```text
backlog/<roadmap>/README.md
```

Examples:

```text
backlog/flask/README.md
backlog/toolsmith/README.md
backlog/devtool/README.md
backlog/window/README.md
```

Archived roadmap example:

```text
archive/numbersystem/README.md
```

Do not create duplicate canonical roadmap files in a separate central roadmap directory unless the project structure is explicitly revised.

If a roadmap file is missing, moved, or conflicts with this index, report the conflict before continuing the learning sequence.

Individual roadmap documents should normally be read from the GitHub remote or repository working tree, not treated as canonical ChatGPT Project Sources.

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
Flask / Web Foundations
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

Location:

```text
active/unix/
```

Focus:

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

Location:

```text
active/c/
```

Focus:

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

Location:

```text
active/network/
```

Focus:

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

Location:

```text
active/server/
```

Focus:

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

Location:

```text
backlog/window/
```

Focus:

* Windows architecture
* enterprise systems
* authentication
* Active Directory

Supports:

* Enterprise Security
* Incident Response
* Windows Internals

---

## Cryptography

Location:

```text
active/crypto/
```

Focus:

* bytes
* transformations
* XOR
* token analysis

Supports:

* Payload Construction
* Web Security

---

## Payload Construction

Location:

```text
active/payload/
```

Focus:

* parser reasoning
* trust boundaries
* input interpretation
* multi-stage execution

Supports:

* Web Security
* Secure Software Design

---

## Number Systems

Location:

```text
archive/numbersystem/
```

Focus:

* binary
* hexadecimal
* bytes
* encoding
* numeric representation

Supports:

* C Programming
* Cryptography
* Payload Construction
* Low-level systems reasoning

---

## Flask

Location:

```text
backlog/flask/
```

Focus:

* HTTP
* sessions
* authentication
* web application architecture

Supports:

* Web Security
* Payload Construction

---

## Security Toolsmith

Location:

```text
backlog/toolsmith/
```

Focus:

* building small security utilities
* sockets
* HTTP
* parsers

Supports:

* Security Automation
* Python Engineering

---

## Vulnerability Report Lab

Location:

```text
backlog/vulnerability_report_lab/
```

Focus:

* vulnerability verification
* reproducible PoC writing
* false-positive filtering
* impact analysis
* report writing
* safe disclosure literacy

Supports:

* Web Security
* Practical Security Research
* Embedded Linux & Firmware Analysis
* IoT Device Security

---

# Current Status

Each roadmap progresses independently.

Progress should always follow:

* the roadmap document
* completed archive documents
* committed repository state

Never infer skipped phases or sessions.

Repository location is authoritative for lifecycle classification:

* `active/` contains current learning tracks
* `backlog/` contains planned or paused tracks
* `archive/` contains tracks whose planned learning sessions are complete

Active and Backlog status do not imply completion. Archive status means the planned session sequence is complete, but review questions, factual corrections, and reference use may continue.

Determine progress from the roadmap and its recorded phase/session documents.

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
* Embedded Linux & Firmware Analysis

These should be added only after a dedicated roadmap has been created.

---

# Maintenance Rules

When adding a new active roadmap:

* add it under `active/<roadmap>/`
* create `active/<roadmap>/README.md`
* update this index
* follow the established roadmap format

When adding a backlog roadmap:

* add it under `backlog/<roadmap>/`
* create `backlog/<roadmap>/README.md`
* update this index if it is a meaningful project roadmap

When archiving a completed roadmap:

* move the roadmap directory to `archive/<roadmap>/`
* keep its roadmap and session records together
* update this index and any lifecycle-specific references
* do not treat review-only work as reactivation

When restoring historical material:

* use a dedicated branch
* verify privacy and redaction before commit
* preserve original context when possible
* avoid reintroducing pre-redaction material into the public baseline without explicit approval

This document should remain an overview, not a detailed curriculum.

---

# Project Vision

Together, these roadmaps form a connected systems curriculum.

The long-term objective is to understand complete computing systems — from source code and hardware to networking, operating systems, applications, and security — through evidence-based reasoning and practical observation.

# Project Iron Forge

## Philosophy

Project Iron Forge is a long-term systems-understanding project.

The objective is not to acquire hardware.

The objective is to understand how real systems are:

- Designed
- Built
- Connected
- Operated
- Observed
- Maintained
- Secured

The project gradually develops:

- Systems thinking
- Linux administration
- Networking understanding
- Security reasoning
- Virtualization skills
- Infrastructure design skills
- Home lab operation skills
- Game security foundations
- Future anti-cheat foundations

---

# Dependency Chain

```text
Purpose-Built Machine
        ↓
Network Appliance
        ↓
Home Lab
        ↓
Enterprise Lab
        ↓
Game Security Lab
        ↓
Research Lab
```

---

# Phase 01 — Purpose-Built Machine

## Objective

Understand how a computer is designed for a specific purpose.

The goal is not to memorize hardware models.

The goal is to understand why hardware exists and how hardware choices affect system behavior.

---

## Learning Outcomes

By the end of this phase, you should be able to answer:

- Why was this machine designed this way?
- Why does this workload need this CPU?
- Why does this workload need this amount of RAM?
- Why is this storage configuration appropriate?
- What bottlenecks exist?
- What tradeoffs were made?

---

## Session 01
Workloads Before Hardware

Topics:

- Purpose-driven design
- Workload analysis
- Systems thinking
- Hardware as a solution to workload requirements

Deliverables:

- QA.md
- notes.md

---

## Session 02
CPU Fundamentals

Topics:

- What a CPU actually does
- Instructions
- Computation
- Control flow
- Why CPUs exist

Linux Connections:

- Processes
- Scheduling

Security Connections:

- Code execution
- Trust boundaries

Deliverables:

- QA.md
- notes.md

---

## Session 03
Cores and Threads

Topics:

- Core
- Thread
- Parallelism
- Concurrency

Linux Connections:

- Scheduler

Networking Connections:

- Concurrent services

Deliverables:

- QA.md
- notes.md

---

## Session 04
CPU Selection Logic

Topics:

- Desktop CPUs
- Server CPUs
- Embedded CPUs
- Workload matching

Deliverables:

- QA.md
- notes.md

---

## Session 05
Memory Fundamentals

Topics:

- RAM
- Volatility
- Working memory
- Memory hierarchy

Linux Connections:

- Virtual memory
- Page cache

Deliverables:

- QA.md
- notes.md

---

## Session 06
Memory Capacity and Tradeoffs

Topics:

- RAM sizing
- Overcommitment
- Bottlenecks

Deliverables:

- QA.md
- notes.md

---

## Session 07
Storage Fundamentals

Topics:

- Persistence
- Files
- Block devices

Linux Connections:

- Filesystems

Deliverables:

- QA.md
- notes.md

---

## Session 08
SSD vs HDD

Topics:

- Latency
- Throughput
- IOPS

Deliverables:

- QA.md
- notes.md

---

## Session 09
NVMe vs SATA

Topics:

- Storage interfaces
- PCIe

Deliverables:

- QA.md
- notes.md

---

## Session 10
Motherboards

Topics:

- Buses
- Chipsets
- Expansion

Deliverables:

- QA.md
- notes.md

---

## Session 11
Power Supplies

Topics:

- Power delivery
- Efficiency
- Reliability

Deliverables:

- QA.md
- notes.md

---

## Session 12
Cooling and Thermals

Topics:

- Heat generation
- Thermal limits
- Throttling

Deliverables:

- QA.md
- notes.md

---

## Session 13
Hardware Bottlenecks

Topics:

- CPU bottlenecks
- RAM bottlenecks
- Storage bottlenecks

Deliverables:

- QA.md
- notes.md

---

## Session 14
Machine Design Exercise

Topics:

- Gaming PC
- NAS
- Router
- Virtualization Host

Deliverables:

- machine_design.md

---

# Phase 02 — Network Appliance

## Objective

Understand how packets move between systems.

Build networking understanding from first principles.

---

## Learning Outcomes

By the end of this phase, you should be able to answer:

- How does a packet move?
- What is a router?
- What is a firewall?
- What is NAT?
- What is DNS?
- What is DHCP?

---

## Session 01
Networks as Information Movement

## Session 02
Packets

## Session 03
MAC Addresses

## Session 04
IP Addresses

## Session 05
Subnetting Fundamentals

## Session 06
Switches

## Session 07
Routers

## Session 08
Routing Tables

## Session 09
NAT

## Session 10
DHCP

## Session 11
DNS

## Session 12
Firewalls

## Session 13
Network Segmentation

## Session 14
VLAN Fundamentals

## Session 15
Consumer Router Analysis

## Session 16
OPNsense Architecture

## Session 17
pfSense Architecture

## Session 18
Network Design Exercise

Deliverables:

- QA.md
- notes.md
- network_design.md

---

# Phase 03 — Home Lab

## Objective

Understand virtualization and infrastructure consolidation.

---

## Learning Outcomes

By the end of this phase, you should be able to answer:

- What is a hypervisor?
- What is virtualization?
- Why use virtual machines?
- How do multiple systems share one machine?

---

## Session 01
Physical vs Virtual Machines

## Session 02
Hypervisors

## Session 03
Type 1 vs Type 2 Hypervisors

## Session 04
QEMU

## Session 05
KVM

## Session 06
Virtual Hardware

## Session 07
Virtual Networking

## Session 08
Storage Allocation

## Session 09
Snapshots

## Session 10
Backups

## Session 11
Containers

## Session 12
Namespaces

## Session 13
cgroups

## Session 14
Proxmox Architecture

## Session 15
Resource Planning

## Session 16
Home Lab Design Exercise

Deliverables:

- QA.md
- notes.md
- homelab_design.md

---

# Phase 04 — Enterprise Lab

## Objective

Understand how organizations manage users and systems.

---

## Learning Outcomes

By the end of this phase, you should be able to answer:

- How do companies authenticate users?
- What is Active Directory?
- Why is centralized management important?

---

## Session 01
Enterprise Infrastructure Overview

## Session 02
Identity

## Session 03
Authentication

## Session 04
Authorization

## Session 05
Windows Server Fundamentals

## Session 06
Active Directory

## Session 07
Domain Controllers

## Session 08
DNS in Enterprise Environments

## Session 09
DHCP in Enterprise Environments

## Session 10
Kerberos Fundamentals

## Session 11
LDAP Concepts

## Session 12
Group Policy

## Session 13
File Servers

## Session 14
User Lifecycle Management

## Session 15
Enterprise Lab Design Exercise

Deliverables:

- QA.md
- notes.md
- enterprise_lab.md

---

# Phase 05 — Game Security Lab

## Objective

Apply systems, networking, and security knowledge to multiplayer games.

---

## Learning Outcomes

By the end of this phase, you should be able to answer:

- Why is cheating possible?
- What should the server trust?
- What should the client trust?
- How do anti-cheat systems think?

---

## Session 01
Game Systems Overview

## Session 02
Client-Server Architecture

## Session 03
Authority Models

## Session 04
Trust Boundaries

## Session 05
State Synchronization

## Session 06
Latency

## Session 07
Prediction

## Session 08
Packet Flow

## Session 09
Logging

## Session 10
Telemetry

## Session 11
Detection Concepts

## Session 12
Server-Side Validation

## Session 13
Behavioral Analysis

## Session 14
Anti-Cheat Design Principles

## Session 15
Game Security Lab Design Exercise

Deliverables:

- QA.md
- notes.md
- game_security_lab.md

---

# Phase 06 — Research Lab

## Objective

Build a reusable systems and security research environment.

---

## Learning Outcomes

By the end of this phase, you should be able to answer:

- How do operators observe systems?
- How do researchers organize experiments?
- How do monitoring systems work?

---

## Session 01
Observability

## Session 02
Metrics

## Session 03
Logs

## Session 04
Tracing Concepts

## Session 05
System Monitoring

## Session 06
Network Monitoring

## Session 07
Automation Fundamentals

## Session 08
Experiment Management

## Session 09
Research Documentation

## Session 10
Security Tooling

## Session 11
Lab Safety

## Session 12
Personal Knowledge Systems

## Session 13
Long-Term Infrastructure Maintenance

## Session 14
Research Environment Design Exercise

Deliverables:

- QA.md
- notes.md
- research_lab.md

---

# Final Outcome

Project Iron Forge ultimately produces a practitioner capable of reasoning about:

- Linux systems
- Networking
- Infrastructure
- Virtualization
- Enterprise environments
- Security fundamentals
- Multiplayer system design
- Game security concepts
- Anti-cheat foundations

from first principles rather than tool memorization.

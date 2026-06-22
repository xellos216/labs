# Linux Server Administration Daily Sessions

Practical Linux server administration training focused on systems understanding, observability, operational security, troubleshooting, recovery, and real-world maintenance.

Environment:

* Host OS: Arch Linux
* Shell: zsh
* Terminal: tmux
* Editor: neovim
* Workflow: CLI-first

---

# Lab Environment Policy

All administration exercises should be performed inside a dedicated virtual machine whenever practical.

## Host System

Primary workstation:

* Arch Linux
* Personal daily-driver environment

Used for:

* note taking
* documentation
* SSH access
* administration tooling
* learning materials

The host system should not be modified unnecessarily during exercises.

## Primary Lab Environment

Recommended lab server:

* Ubuntu Server LTS

Purpose:

* isolated experimentation
* failure recovery practice
* service administration
* security testing
* troubleshooting drills

---

# Learning Objectives

Students should be able to:

* create and manage users
* understand authentication systems
* manage services
* analyze logs
* troubleshoot failures
* understand networking
* apply security controls
* recover broken systems

without risking the host system.

---

# Failure-Driven Learning

Failures are expected.

Students are encouraged to:

* break configurations
* misconfigure services
* break networking
* create authentication failures
* recover systems

Administration skill develops through:

```text
observe
→ predict
→ modify
→ break
→ investigate
→ recover
```

---

# Observability First

Every exercise should answer:

```text
What changed inside the system?
```

before:

```text
What command did I run?
```

Preferred observations:

* process state changes
* service state changes
* log entries
* authentication events
* network behavior
* ownership changes
* permission changes

---

# Learning Method

Every session follows:

```text
Prediction
→ Execute
→ Observe
→ Explain
```

Practical exercises follow:

```text
Observe
→ Modify
→ Verify
→ Break
→ Recover
```

---

# Philosophy

Linux administration is not a collection of commands.

Core principles:

```text
Observe
→ Understand
→ Predict
→ Modify
→ Verify
```

Priorities:

* understanding before memorization
* observation before modification
* system reasoning before automation
* practical experimentation
* mental model formation

---

# Goal

Develop the ability to:

* administer Linux servers confidently
* understand system behavior
* troubleshoot failures methodically
* reason about security controls
* recover services
* think like a Linux administrator

---

# Phase 00 — Virtualization & Lab Foundation

Goal:

Build and understand a complete Linux administration lab.

Sessions:

01. Linux Virtualization Overview
02. Installing the Lab Environment
03. QEMU and KVM Relationship
04. libvirt Architecture
05. Creating the First Ubuntu Server VM
06. VM Hardware Observation
07. Virtual Network Fundamentals
08. DHCP Observation
09. DNS Observation
10. netplan Fundamentals
11. systemd-networkd Observation
12. SSH Administration Workflow
13. Snapshots & Recovery
14. Failure Laboratory
15. Build Everything From Scratch

---

# Phase 01 — Users, Identity & Access

01. Users, Groups, and Identity
02. /etc/passwd Observation
03. /etc/shadow Overview
04. Group Membership
05. Ownership and Access
06. Permission Reasoning
07. umask Behavior
08. Special Permissions
09. setuid and setgid
10. Sticky Bit
11. User Lifecycle Management
12. Account Locking
13. Privilege Boundaries
14. Identity Mental Model

---

# Phase 02 — Authentication & Privilege Escalation Controls

01. Authentication Mental Model
02. PAM Fundamentals
03. Observing PAM Configuration
04. Login Flow Analysis
05. sudo Fundamentals
06. sudoers Reasoning
07. Privilege Delegation
08. Environment Handling
09. Authentication Failures
10. Password Policies
11. Account Restrictions
12. Multi-User Administration
13. Operational Security Considerations
14. Authentication System Walkthrough

---

# Phase 03 — Processes & Services

01. Processes Revisited
02. Process Trees
03. Service Concepts
04. Introduction to systemd
05. systemctl Observation
06. Unit Files
07. Service Dependencies
08. Service Startup Flow
09. Signals and Service Control
10. Failed Services
11. Service Recovery
12. Boot Targets
13. System Boot Sequence
14. Service Mental Model

---

# Phase 04 — Logging & Observability

01. Why Logging Exists
02. System Logs Overview
03. journalctl Fundamentals
04. Boot Log Analysis
05. Service Log Analysis
06. Filtering Journal Data
07. rsyslog Architecture
08. Log Routing
09. Authentication Logs
10. Failure Investigation
11. Log Rotation
12. Building Timelines
13. Incident Observation Workflow
14. Observability Mental Model

---

# Phase 05 — Package & Software Management

01. Software on Linux
02. Package Databases
03. Package Manager Fundamentals
04. Dependency Reasoning
05. Package Verification
06. Repository Trust
07. Configuration Files
08. Safe Upgrades
09. Rollback Concepts
10. Service Impact Analysis
11. Security Updates
12. Maintenance Windows
13. Operational Change Management
14. Package Management Mental Model

---

# Phase 06 — Remote Administration & SSH

01. Remote Administration Concepts
02. SSH Architecture
03. sshd Observation
04. Authentication Methods
05. Public Key Authentication
06. Authorized Keys
07. SSH Configuration
08. Connection Troubleshooting
09. SSH Logging
10. Hardening SSH
11. Remote Service Management
12. Secure Administrative Workflows
13. SSH Failure Recovery
14. Remote Administration Mental Model

---

# Phase 07 — Firewalling & Network Access Control

01. Service Exposure
02. Firewall Mental Models
03. iptables Fundamentals
04. Chains and Rules
05. Packet Traversal
06. Stateful Filtering
07. nftables Overview
08. Observing Active Rules
09. Allow vs Deny Strategies
10. Host Hardening
11. Network Segmentation Concepts
12. Firewall Troubleshooting
13. Real Administration Scenarios
14. Network Access Control Mental Model

---

# Phase 08 — Auditing & Security Monitoring

01. Auditing Fundamentals
02. auditd Overview
03. Audit Events
04. Watching Files
05. Watching Processes
06. Privilege Escalation Observation
07. Authentication Auditing
08. File Integrity Concepts
09. Security Event Investigation
10. Timeline Reconstruction
11. Indicators of Misuse
12. Operational Monitoring
13. Security Observation Workflow
14. Audit Mental Model

---

# Phase 09 — Linux Hardening

01. Attack Surface Review
02. Principle of Least Privilege
03. Service Reduction
04. User Hardening
05. Authentication Hardening
06. SSH Hardening
07. fail2ban Fundamentals
08. SSH Brute Force Defense
09. Filesystem Hardening
10. Network Hardening
11. Logging Hardening
12. Auditing Hardening
13. Hardening Validation
14. Defense-in-Depth Mental Model

---

# Phase 10 — Monitoring, Troubleshooting & Recovery

01. Troubleshooting Frameworks
02. What Changed?
03. Resource Exhaustion
04. CPU Investigation
05. Memory Investigation
06. Disk Investigation
07. Network Investigation
08. Service Outages
09. Dependency Failures
10. Boot Failures
11. Authentication Failures
12. Backup Concepts
13. Restore Testing
14. Configuration Recovery

---

# Phase 11 — Real Server Operations Lab

01. Server Health Assessment
02. New User Onboarding
03. Service Deployment
04. Service Failure Investigation
05. Suspicious Login Investigation
06. SSH Lockout Recovery
07. Firewall Misconfiguration Recovery
08. Disk Space Emergency
09. Runaway Process Investigation
10. Log-Based Incident Analysis
11. System Hardening Review
12. Patch Management Workflow
13. Full Operational Walkthrough
14. Capstone Administration Scenario

---

# Final Outcome

By completing this roadmap, students should be able to:

* Explain how Linux systems authenticate users
* Manage identities and permissions safely
* Understand service lifecycle and systemd
* Investigate failures through logs
* Administer systems remotely with SSH
* Reason about firewall behavior
* Audit security-relevant activity
* Harden Linux systems methodically
* Troubleshoot production-like issues
* Recover systems confidently
* Build durable mental models of Linux operations

Linux administration should stop feeling like a collection of commands and become a coherent model of how systems are operated, observed, secured, maintained, and recovered.

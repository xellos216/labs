# Linux Server Administration Daily Sessions

## Objective

Practical Linux server administration training focused on systems understanding, observability, operational security, troubleshooting, recovery, and real-world maintenance.

Build the ability to operate, observe, secure and recover Linux servers without
treating administration as a collection of commands.

---

# Lab Environment Policy

All administration exercises should be performed inside a dedicated virtual machine whenever practical.

## Host System

Primary workstation:

- Arch Linux
- Personal daily-driver environment

Used for:

- note taking
- documentation
- SSH access
- administration tooling
- learning materials

Primary workflow:

- zsh
- tmux
- neovim
- CLI-first tooling

The host system should not be modified unnecessarily during exercises.

## Primary Lab Environment

Recommended lab server:

- Ubuntu Server LTS

Purpose:

- isolated experimentation
- failure recovery practice
- service administration
- security testing
- troubleshooting drills

---

# Global Outcomes

Students should be able to:

- create and manage users
- understand authentication systems
- manage services
- analyze logs
- troubleshoot failures
- understand networking
- apply security controls
- recover broken systems

without risking the host system.

---

# Failure-Driven Learning

Failures are expected.

Students are encouraged to:

- break configurations
- misconfigure services
- break networking
- create authentication failures
- recover systems

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

- process state changes
- service state changes
- log entries
- authentication events
- network behavior
- ownership changes
- permission changes

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

- understanding before memorization
- observation before modification
- system reasoning before automation
- practical experimentation
- mental model formation

---

# Goal

Develop the ability to:

- administer Linux servers confidently
- understand system behavior
- troubleshoot failures methodically
- reason about security controls
- recover services
- think like a Linux administrator

---

# Typical Phase Structure

Each phase preserves its existing 14-session or 15-session scope.

```text
System Concept
      │
      ▼
Direct Observation
      │
      ▼
Controlled Modification
      │
      ▼
Failure Investigation
      │
      ▼
Recovery and Mental Model
```

The roadmap defines the intended curriculum. Existing phase records document
learning history and are not used to silently rename or replace roadmap
sessions.

---

# Phase 00 — Virtualization & Lab Foundation

## Goal

Build and understand a complete Linux administration lab.

---

## Outcomes

After completing this phase, you should be able to:

- explain the relationship between QEMU, KVM and libvirt
- create and inspect an Ubuntu Server virtual machine
- explain basic virtual networking, DHCP and DNS behavior
- administer the VM through SSH
- use snapshots to support controlled failure and recovery

---

## Typical Tools

- QEMU
- KVM
- libvirt
- virsh
- virt-manager
- SSH
- netplan

---

## Example Labs

- build an Ubuntu Server VM from scratch
- observe virtual hardware and network configuration
- trace DHCP and DNS behavior inside the lab
- configure remote administration over SSH
- break and recover the VM with snapshots

---

### Session 01

Linux Virtualization Overview

---

### Session 02

Installing the Lab Environment

---

### Session 03

QEMU and KVM Relationship

---

### Session 04

libvirt Architecture

---

### Session 05

Creating the First Ubuntu Server VM

---

### Session 06

VM Hardware Observation

---

### Session 07

Virtual Network Fundamentals

---

### Session 08

DHCP Observation

---

### Session 09

DNS Observation

---

### Session 10

netplan Fundamentals

---

### Session 11

systemd-networkd Observation

---

### Session 12

SSH Administration Workflow

---

### Session 13

Snapshots & Recovery

---

### Session 14

Failure Laboratory

---

### Session 15

Build Everything From Scratch

---

# Phase 01 — Users, Identity & Access

## Goal

Understand how Linux represents identity and enforces local access boundaries.

---

## Outcomes

After completing this phase, you should be able to:

- explain users, groups, ownership and identity records
- inspect `/etc/passwd` and `/etc/shadow`
- reason about permissions, umask and special permission bits
- manage the user account lifecycle
- explain privilege boundaries between accounts

---

## Typical Tools

- id
- getent
- useradd
- usermod
- passwd
- chmod
- chown

---

## Example Labs

- create users and groups with distinct access requirements
- predict and verify permissions produced by umask
- observe setuid, setgid and sticky-bit behavior
- lock and restore a local account
- investigate an ownership-related access failure

---

### Session 01

Users, Groups, and Identity

---

### Session 02

/etc/passwd Observation

---

### Session 03

/etc/shadow Overview

---

### Session 04

Group Membership

---

### Session 05

Ownership and Access

---

### Session 06

Permission Reasoning

---

### Session 07

umask Behavior

---

### Session 08

Special Permissions

---

### Session 09

setuid and setgid

---

### Session 10

Sticky Bit

---

### Session 11

User Lifecycle Management

---

### Session 12

Account Locking

---

### Session 13

Privilege Boundaries

---

### Session 14

Identity Mental Model

---

# Phase 02 — Authentication & Privilege Escalation Controls

## Goal

Understand Linux authentication and controlled privilege delegation.

---

## Outcomes

After completing this phase, you should be able to:

- explain the role of PAM in authentication flows
- inspect login and authentication configuration
- reason about sudo policy and privilege delegation
- diagnose authentication failures
- apply account restrictions and password policies

---

## Typical Tools

- PAM configuration
- sudo
- visudo
- passwd
- chage
- authentication logs

---

## Example Labs

- trace a local login through PAM
- create and validate a limited sudo policy
- compare preserved and reset environment variables
- reproduce an authentication failure
- document a complete authentication walkthrough

---

### Session 01

Authentication Mental Model

---

### Session 02

PAM Fundamentals

---

### Session 03

Observing PAM Configuration

---

### Session 04

Login Flow Analysis

---

### Session 05

sudo Fundamentals

---

### Session 06

sudoers Reasoning

---

### Session 07

Privilege Delegation

---

### Session 08

Environment Handling

---

### Session 09

Authentication Failures

---

### Session 10

Password Policies

---

### Session 11

Account Restrictions

---

### Session 12

Multi-User Administration

---

### Session 13

Operational Security Considerations

---

### Session 14

Authentication System Walkthrough

---

# Phase 03 — Processes & Services

## Goal

Understand how Linux runs processes and manages long-lived services.

---

## Outcomes

After completing this phase, you should be able to:

- inspect process trees and runtime state
- explain systemd units, dependencies and startup flow
- control services and interpret failed states
- connect signals to service lifecycle behavior
- recover a failed service methodically

---

## Typical Tools

- ps
- pstree
- systemctl
- systemd-analyze
- kill
- journalctl

---

## Example Labs

- trace a service from unit file to running process
- inspect unit dependencies
- introduce and diagnose a service failure
- observe signal-driven service control
- reconstruct the system boot and service startup sequence

---

### Session 01

Processes Revisited

---

### Session 02

Process Trees

---

### Session 03

Service Concepts

---

### Session 04

Introduction to systemd

---

### Session 05

systemctl Observation

---

### Session 06

Unit Files

---

### Session 07

Service Dependencies

---

### Session 08

Service Startup Flow

---

### Session 09

Signals and Service Control

---

### Session 10

Failed Services

---

### Session 11

Service Recovery

---

### Session 12

Boot Targets

---

### Session 13

System Boot Sequence

---

### Session 14

Service Mental Model

---

# Phase 04 — Logging & Observability

## Goal

Use system logs to explain behavior, investigate failures and reconstruct events.

---

## Outcomes

After completing this phase, you should be able to:

- explain the roles of journald and rsyslog
- filter boot, service and authentication logs
- trace log routing and rotation
- build timelines from system events
- perform a log-driven failure investigation

---

## Typical Tools

- journalctl
- systemctl
- rsyslog
- logger
- logrotate

---

## Example Labs

- compare logs across multiple boots
- isolate messages from one failed service
- trace a message through log routing
- inspect authentication events
- build an incident timeline from journal data

---

### Session 01

Why Logging Exists

---

### Session 02

System Logs Overview

---

### Session 03

journalctl Fundamentals

---

### Session 04

Boot Log Analysis

---

### Session 05

Service Log Analysis

---

### Session 06

Filtering Journal Data

---

### Session 07

rsyslog Architecture

---

### Session 08

Log Routing

---

### Session 09

Authentication Logs

---

### Session 10

Failure Investigation

---

### Session 11

Log Rotation

---

### Session 12

Building Timelines

---

### Session 13

Incident Observation Workflow

---

### Session 14

Observability Mental Model

---

# Phase 05 — Package & Software Management

## Goal

Manage software changes while preserving system integrity and service availability.

---

## Outcomes

After completing this phase, you should be able to:

- explain package databases, dependencies and repositories
- verify package provenance and repository trust
- plan safe upgrades and security updates
- evaluate configuration and service impact
- document rollback and operational change procedures

---

## Typical Tools

- apt
- apt-cache
- dpkg
- systemctl
- package verification tools

---

## Example Labs

- inspect package metadata and dependencies
- verify repository configuration
- plan and apply a controlled package upgrade
- identify configuration-file changes
- assess service impact and rollback options

---

### Session 01

Software on Linux

---

### Session 02

Package Databases

---

### Session 03

Package Manager Fundamentals

---

### Session 04

Dependency Reasoning

---

### Session 05

Package Verification

---

### Session 06

Repository Trust

---

### Session 07

Configuration Files

---

### Session 08

Safe Upgrades

---

### Session 09

Rollback Concepts

---

### Session 10

Service Impact Analysis

---

### Session 11

Security Updates

---

### Session 12

Maintenance Windows

---

### Session 13

Operational Change Management

---

### Session 14

Package Management Mental Model

---

# Phase 06 — Remote Administration & SSH

## Goal

Administer Linux servers remotely through observable and secure SSH workflows.

---

## Outcomes

After completing this phase, you should be able to:

- explain SSH client and server architecture
- configure password and public-key authentication
- inspect SSH configuration and logs
- troubleshoot failed connections
- harden and recover remote administrative access

---

## Typical Tools

- ssh
- sshd
- ssh-keygen
- ssh-copy-id
- journalctl
- ss

---

## Example Labs

- configure public-key authentication
- trace an SSH connection through server logs
- diagnose a rejected connection
- apply and verify SSH hardening settings
- recover from an SSH configuration failure

---

### Session 01

Remote Administration Concepts

---

### Session 02

SSH Architecture

---

### Session 03

sshd Observation

---

### Session 04

Authentication Methods

---

### Session 05

Public Key Authentication

---

### Session 06

Authorized Keys

---

### Session 07

SSH Configuration

---

### Session 08

Connection Troubleshooting

---

### Session 09

SSH Logging

---

### Session 10

Hardening SSH

---

### Session 11

Remote Service Management

---

### Session 12

Secure Administrative Workflows

---

### Session 13

SSH Failure Recovery

---

### Session 14

Remote Administration Mental Model

---

# Phase 07 — Firewalling & Network Access Control

## Goal

Understand and control how network traffic reaches services on a Linux host.

---

## Outcomes

After completing this phase, you should be able to:

- map listening services to network exposure
- explain chains, rules and packet traversal
- reason about stateful filtering
- inspect active iptables and nftables rules
- diagnose and recover from firewall misconfiguration

---

## Typical Tools

- ss
- ip
- iptables
- nft
- conntrack
- tcpdump

---

## Example Labs

- map listening sockets to firewall policy
- trace a packet through filtering decisions
- compare stateless and stateful rules
- implement a minimal allow policy
- reproduce and recover from blocked administrative access

---

### Session 01

Service Exposure

---

### Session 02

Firewall Mental Models

---

### Session 03

iptables Fundamentals

---

### Session 04

Chains and Rules

---

### Session 05

Packet Traversal

---

### Session 06

Stateful Filtering

---

### Session 07

nftables Overview

---

### Session 08

Observing Active Rules

---

### Session 09

Allow vs Deny Strategies

---

### Session 10

Host Hardening

---

### Session 11

Network Segmentation Concepts

---

### Session 12

Firewall Troubleshooting

---

### Session 13

Real Administration Scenarios

---

### Session 14

Network Access Control Mental Model

---

# Phase 08 — Auditing & Security Monitoring

## Goal

Observe and investigate security-relevant activity on a Linux server.

---

## Outcomes

After completing this phase, you should be able to:

- explain the purpose and structure of Linux auditing
- watch files, processes and privilege-related activity
- inspect authentication and audit events
- reconstruct security timelines
- distinguish routine operations from indicators of misuse

---

## Typical Tools

- auditd
- auditctl
- ausearch
- aureport
- journalctl

---

## Example Labs

- create and verify a file watch
- observe privilege-related events
- correlate authentication and audit records
- investigate a simulated security event
- build a concise security timeline

---

### Session 01

Auditing Fundamentals

---

### Session 02

auditd Overview

---

### Session 03

Audit Events

---

### Session 04

Watching Files

---

### Session 05

Watching Processes

---

### Session 06

Privilege Escalation Observation

---

### Session 07

Authentication Auditing

---

### Session 08

File Integrity Concepts

---

### Session 09

Security Event Investigation

---

### Session 10

Timeline Reconstruction

---

### Session 11

Indicators of Misuse

---

### Session 12

Operational Monitoring

---

### Session 13

Security Observation Workflow

---

### Session 14

Audit Mental Model

---

# Phase 09 — Linux Hardening

## Goal

Reduce Linux server risk through layered, verifiable security controls.

---

## Outcomes

After completing this phase, you should be able to:

- assess and reduce server attack surface
- apply least privilege to users and services
- harden authentication, SSH, filesystems and networking
- strengthen logging and auditing
- validate controls as a defense-in-depth system

---

## Typical Tools

- systemctl
- ss
- sshd configuration
- fail2ban
- nftables or iptables
- auditd

---

## Example Labs

- inventory and reduce exposed services
- apply user and SSH hardening controls
- configure and observe fail2ban behavior
- review filesystem and network protections
- perform a post-hardening validation

---

### Session 01

Attack Surface Review

---

### Session 02

Principle of Least Privilege

---

### Session 03

Service Reduction

---

### Session 04

User Hardening

---

### Session 05

Authentication Hardening

---

### Session 06

SSH Hardening

---

### Session 07

fail2ban Fundamentals

---

### Session 08

SSH Brute Force Defense

---

### Session 09

Filesystem Hardening

---

### Session 10

Network Hardening

---

### Session 11

Logging Hardening

---

### Session 12

Auditing Hardening

---

### Session 13

Hardening Validation

---

### Session 14

Defense-in-Depth Mental Model

---

# Phase 10 — Monitoring, Troubleshooting & Recovery

## Goal

Diagnose production-like failures and restore service through evidence-driven workflows.

---

## Outcomes

After completing this phase, you should be able to:

- apply a repeatable troubleshooting framework
- investigate CPU, memory, disk and network exhaustion
- diagnose service, dependency, boot and authentication failures
- explain backup and restore requirements
- recover configurations and verify restored behavior

---

## Typical Tools

- ps
- top
- free
- df
- du
- ss
- journalctl
- systemctl

---

## Example Labs

- identify a CPU or memory bottleneck
- investigate disk-space exhaustion
- trace a service dependency failure
- diagnose a boot or authentication problem
- test restoration of data and configuration

---

### Session 01

Troubleshooting Frameworks

---

### Session 02

What Changed?

---

### Session 03

Resource Exhaustion

---

### Session 04

CPU Investigation

---

### Session 05

Memory Investigation

---

### Session 06

Disk Investigation

---

### Session 07

Network Investigation

---

### Session 08

Service Outages

---

### Session 09

Dependency Failures

---

### Session 10

Boot Failures

---

### Session 11

Authentication Failures

---

### Session 12

Backup Concepts

---

### Session 13

Restore Testing

---

### Session 14

Configuration Recovery

---

# Phase 11 — Real Server Operations Lab

## Goal

Integrate administration, observability, security and recovery skills in realistic operations.

---

## Outcomes

After completing this phase, you should be able to:

- assess the health and exposure of an unfamiliar server
- perform routine identity, service and patch operations
- investigate suspicious authentication and log activity
- recover from SSH, firewall, disk and process failures
- complete and explain an end-to-end administration scenario

---

## Typical Tools

- systemctl
- journalctl
- SSH
- user and permission tools
- firewall tools
- process and storage inspection tools

---

## Example Labs

- onboard a user and deploy a service
- investigate a suspicious login
- recover from SSH and firewall lockout
- resolve a disk-space emergency or runaway process
- perform a full operational capstone walkthrough

---

### Session 01

Server Health Assessment

---

### Session 02

New User Onboarding

---

### Session 03

Service Deployment

---

### Session 04

Service Failure Investigation

---

### Session 05

Suspicious Login Investigation

---

### Session 06

SSH Lockout Recovery

---

### Session 07

Firewall Misconfiguration Recovery

---

### Session 08

Disk Space Emergency

---

### Session 09

Runaway Process Investigation

---

### Session 10

Log-Based Incident Analysis

---

### Session 11

System Hardening Review

---

### Session 12

Patch Management Workflow

---

### Session 13

Full Operational Walkthrough

---

### Session 14

Capstone Administration Scenario

---

# Final Outcome

By completing this roadmap, students should be able to:

- explain how Linux systems authenticate users
- manage identities and permissions safely
- understand service lifecycle and systemd
- investigate failures through logs
- administer systems remotely with SSH
- reason about firewall behavior
- audit security-relevant activity
- harden Linux systems methodically
- troubleshoot production-like issues
- recover systems confidently
- build durable mental models of Linux operations

Linux administration should stop feeling like a collection of commands and become a coherent model of how systems are operated, observed, secured, maintained, and recovered.

---

# Core Mental Model

```text
Identity and Authentication
           │
           ▼
Processes and Services
           │
           ▼
Logs and Observability
           │
           ▼
Networking and Remote Access
           │
           ▼
Security Controls and Monitoring
           │
           ▼
Troubleshooting and Recovery
```

Administration is the controlled process of observing system state, making a
change, verifying its effect and recovering when assumptions fail.

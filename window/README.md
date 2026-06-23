# Windows Fundamentals for Security & Systems Understanding

## Objective

Build a strong mental model of how Windows systems work from the perspective of:

- Information Security
- System Administration Awareness
- Incident Response
- Enterprise Infrastructure
- Active Directory Environments
- Future Windows Security Learning

This roadmap is not designed to create a Windows administrator.

The goal is to understand how Windows systems operate, how enterprises use them, and how attackers and defenders interact with them.

---

# Philosophy

Windows should not be approached as:

- a collection of GUI menus
- certification trivia
- version-specific features
- memorization exercises

Instead, Windows should be studied as:

```text
Hardware
→ Kernel
→ Services
→ Users
→ Authentication
→ Networking
→ Enterprise Infrastructure
```

Core principles:

- understanding before memorization
- observation before modification
- systems thinking
- security awareness
- enterprise context
- transferable mental models

---

# Learning Method

## Concept Sessions (30%)

Purpose:

Build mental models.

Focus:

- architecture
- design decisions
- Linux comparisons
- security implications

Questions:

```text
Why does this component exist?

What problem does it solve?

How does Linux solve the same problem?

Where does it appear in real enterprises?
```

---

## Task Sessions (70%)

Purpose:

Observe Windows directly.

Focus:

- built-in tools
- system investigation
- process observation
- event analysis
- service inspection

Workflow:

```text
Predict
→ Observe
→ Explain
→ Verify
```

---

# Recommended Lab Environment

Primary workstation:

- Arch Linux

Recommended Windows lab:

- Windows 11
- Windows Server Evaluation Edition (later phases)
- Virtual Machine (QEMU/KVM preferred)

Why:

- safe experimentation
- snapshot recovery
- enterprise simulation
- Active Directory labs

---

# Phase 01 — Windows Foundations

## Purpose

Build a high-level mental model of Windows as an operating system.

Many Linux users understand commands before understanding Windows architecture.

This phase reverses that.

---

## Core Concepts

- What Windows actually is
- User Mode vs Kernel Mode
- Windows architecture overview
- Windows boot process
- Windows editions
- GUI vs underlying system
- Registry introduction
- Windows management philosophy

---

## Skills Gained

- Explain major Windows components
- Navigate Windows confidently
- Understand where system settings live
- Compare Windows architecture to Linux

---

## Typical Tools

- Settings
- Control Panel
- Task Manager
- System Information
- msinfo32

---

## Example Labs

- Explore Task Manager
- Identify hardware information
- Observe startup applications
- Compare Windows boot flow to Linux boot flow

---

# Phase 02 — Filesystem & NTFS

## Purpose

Understand how Windows stores data and enforces filesystem security.

NTFS is one of the most important foundations for security and administration.

---

## Core Concepts

- Drives and volumes
- NTFS architecture
- Files and directories
- Alternate Data Streams
- Metadata
- Recycle Bin
- Junctions and symbolic links
- Windows path conventions

---

## Skills Gained

- Navigate Windows storage
- Understand NTFS permissions
- Interpret filesystem behavior
- Recognize security-relevant filesystem features

---

## Typical Tools

- File Explorer
- diskmgmt.msc
- fsutil
- PowerShell

---

## Example Labs

- Create directories and files
- Inspect NTFS permissions
- Create symbolic links
- Explore Alternate Data Streams

---

# Phase 03 — Users, Groups & Permissions

## Purpose

Understand identity and authorization in Windows.

This phase forms the foundation for Active Directory.

---

## Core Concepts

- Local users
- Local groups
- Security Identifiers (SIDs)
- Access Tokens
- Permissions
- Access Control Lists (ACLs)
- Privileges vs permissions

---

## Skills Gained

- Understand Windows authorization
- Inspect identities
- Reason about access decisions
- Compare Linux permissions with ACLs

---

## Typical Tools

- lusrmgr.msc
- Computer Management
- whoami
- PowerShell

---

## Example Labs

- Create local users
- Create groups
- Inspect group membership
- Examine access tokens
- Compare ACL behavior

---

# Phase 04 — Processes & Services

## Purpose

Understand how Windows executes software and background functionality.

Most enterprise security monitoring revolves around processes and services.

---

## Core Concepts

- Processes
- Threads
- Parent-child relationships
- Services
- Service Control Manager (SCM)
- Startup mechanisms
- Scheduled Tasks

---

## Skills Gained

- Inspect running software
- Understand service architecture
- Trace execution flow
- Identify persistence locations

---

## Typical Tools

- Task Manager
- Resource Monitor
- services.msc
- tasklist
- PowerShell

---

## Example Labs

- Enumerate running processes
- Inspect services
- Observe startup behavior
- Compare system services with Linux daemons

---

# Phase 05 — Event Logs & Observability

## Purpose

Understand how Windows records system activity.

Event Logs are the foundation of enterprise monitoring and incident response.

---

## Core Concepts

- Windows Event Log architecture
- Log channels
- Event IDs
- Audit events
- Security logs
- Operational logs

---

## Skills Gained

- Investigate system activity
- Read security events
- Build timelines
- Understand enterprise monitoring

---

## Typical Tools

- Event Viewer
- PowerShell
- wevtutil

---

## Example Labs

- Review login events
- Review service start events
- Review application crashes
- Build a simple activity timeline

---

# Phase 06 — PowerShell Fundamentals

## Purpose

Learn the primary automation and administration language used in modern Windows environments.

---

## Core Concepts

- Objects vs text
- Cmdlets
- Pipelines
- Variables
- Filtering
- Querying system information

---

## Skills Gained

- Navigate PowerShell
- Query Windows internals
- Automate investigations
- Understand common security tooling

---

## Typical Tools

- PowerShell
- Windows Terminal

---

## Example Labs

- Enumerate processes
- Enumerate services
- Enumerate users
- Export system information

---

# Phase 07 — Networking on Windows

## Purpose

Understand how Windows participates in networks.

Focus on observation rather than protocol theory.

---

## Core Concepts

- Network interfaces
- DNS
- Routing
- Windows Firewall
- TCP/IP implementation
- Network profiles

---

## Skills Gained

- Troubleshoot Windows networking
- Inspect network configuration
- Understand host-level networking

---

## Typical Tools

- ipconfig
- netstat
- PowerShell
- Windows Defender Firewall

---

## Example Labs

- Inspect routing tables
- Observe DNS resolution
- Compare Windows networking tools with Linux equivalents

---

# Phase 08 — SMB & File Sharing

## Purpose

Understand the protocol most commonly encountered in enterprise Windows environments.

---

## Core Concepts

- SMB
- Shares
- Administrative shares
- Network drives
- Authentication and authorization

---

## Skills Gained

- Access shared resources
- Troubleshoot SMB access
- Understand common attack surfaces

---

## Typical Tools

- File Explorer
- net use
- PowerShell

---

## Example Labs

- Create SMB shares
- Connect to remote shares
- Observe permissions
- Inspect share configurations

---

# Phase 09 — Windows Authentication

## Purpose

Understand how Windows verifies identity.

This phase prepares for Active Directory and Kerberos.

---

## Core Concepts

- Authentication vs authorization
- Credentials
- NTLM
- Local authentication
- Domain authentication
- Access tokens

---

## Skills Gained

- Explain authentication flow
- Identify authentication mechanisms
- Understand enterprise login behavior

---

## Typical Tools

- whoami
- runas
- Event Viewer

---

## Example Labs

- Observe login events
- Compare local vs domain authentication
- Inspect security tokens

---

# Phase 10 — Active Directory Fundamentals

## Purpose

Understand the most important identity system in enterprise Windows environments.

---

## Core Concepts

- Domains
- Domain Controllers
- Organizational Units
- Users
- Groups
- Group Policy
- LDAP

---

## Skills Gained

- Explain AD architecture
- Understand enterprise identity management
- Navigate AD terminology confidently

---

## Typical Tools

- Active Directory Users and Computers
- Group Policy Management
- PowerShell

---

## Example Labs

- Build a simple AD lab
- Create users and groups
- Explore Group Policy

---

# Phase 11 — Kerberos Fundamentals

## Purpose

Understand the authentication protocol that powers modern Active Directory environments.

---

## Core Concepts

- Kerberos
- Tickets
- TGT
- Service Tickets
- KDC
- Single Sign-On

---

## Skills Gained

- Explain Kerberos workflows
- Understand ticket-based authentication
- Recognize common security implications

---

## Typical Tools

- klist
- Event Viewer
- PowerShell

---

## Example Labs

- Inspect Kerberos tickets
- Trace authentication events
- Compare Kerberos to NTLM

---

# Phase 12 — Windows Security Fundamentals

## Purpose

Understand how Windows protects itself and how defenders observe systems.

---

## Core Concepts

- Windows Defender
- UAC
- Credential protection
- Attack surface
- Security boundaries
- Hardening concepts

---

## Skills Gained

- Understand native Windows security controls
- Evaluate host security posture
- Interpret defensive mechanisms

---

## Typical Tools

- Windows Security
- Defender
- Event Viewer
- PowerShell

---

## Example Labs

- Observe Defender activity
- Review security events
- Explore UAC behavior

---

# Phase 13 — Enterprise Environment Concepts

## Purpose

Understand how Windows exists inside larger organizations.

---

## Core Concepts

- Enterprise architecture
- Workstations
- Servers
- Domain Controllers
- Centralized management
- Patch management
- Monitoring systems

---

## Skills Gained

- Understand enterprise workflows
- Understand administrative boundaries
- Interpret enterprise terminology

---

## Typical Tools

- Active Directory
- Group Policy
- Management Consoles

---

## Example Labs

- Map a sample enterprise
- Trace administrative responsibilities
- Analyze enterprise authentication paths

---

# Phase 14 — Introductory Incident Response

## Purpose

Learn how investigators examine Windows systems after suspicious activity.

---

## Core Concepts

- Evidence sources
- Event logs
- Process history
- User activity
- Timeline reconstruction

---

## Skills Gained

- Perform basic investigations
- Collect observations
- Build activity timelines

---

## Typical Tools

- Event Viewer
- PowerShell
- Task Manager

---

## Example Labs

- Investigate failed logins
- Investigate service changes
- Build a host timeline

---

# Phase 15 — Foundations for Future Windows Security Learning

## Purpose

Connect Windows fundamentals to future security disciplines.

---

## Core Concepts

- Security monitoring
- Threat detection
- AD attack paths
- Endpoint security
- Privilege escalation concepts
- Defensive architecture

---

## Skills Gained

- Read Windows security material comfortably
- Approach AD security training confidently
- Transition into advanced topics

---

## Typical Tools

- PowerShell
- Event Viewer
- Sysinternals Suite
- Windows Security Tools

---

## Example Labs

- Investigate suspicious processes
- Trace authentication activity
- Map an AD environment
- Analyze endpoint telemetry

---

# Final Outcome

Upon completing this roadmap, you should be able to:

- Explain how Windows systems are structured
- Navigate Windows confidently despite primarily using Linux
- Understand NTFS, permissions, and identities
- Inspect processes, services, and logs
- Use PowerShell for investigation and administration
- Understand SMB and enterprise file sharing
- Explain Windows authentication mechanisms
- Understand Active Directory architecture
- Explain Kerberos authentication flows
- Understand enterprise security concepts
- Perform basic Windows incident-response activities
- Begin Windows security learning without knowledge gaps

Windows should stop feeling like a collection of GUI tools and become a coherent system of:

```text
Identity
→ Authentication
→ Authorization
→ Services
→ Observability
→ Enterprise Infrastructure
→ Security
```

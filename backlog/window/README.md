# Windows Fundamentals for Security & Systems Understanding

## Objective

Build a strong mental model of how Windows systems work from the perspective of:

- Information Security
- System Administration Awareness
- Incident Response
- Enterprise Infrastructure
- Active Directory
- Future Windows Security Learning

This roadmap is **not** intended to make you a Windows administrator.

Instead, its purpose is to understand how Windows systems are designed, how they operate, and how they are used in modern enterprise environments.

---

# Philosophy

Windows should not be studied as:

- a collection of GUI menus
- certification trivia
- version-specific features
- commands to memorize

Instead, study Windows as a complete operating system.

```text
Hardware
        │
        ▼
NT Kernel
        │
        ▼
Processes
Services
Filesystem
Networking
Authentication
        │
        ▼
Enterprise Infrastructure
```

Core principles:

- understanding before memorization
- observation before modification
- systems thinking
- security-oriented learning
- enterprise awareness
- transferable mental models

---

# Learning Method

This roadmap follows a hybrid structure.

## Concept Sessions (≈30%)

Purpose:

Build accurate mental models.

Topics include:

- architecture
- why components exist
- problems they solve
- Linux comparisons
- enterprise context

---

## Observation Sessions (≈40%)

Purpose:

Observe Windows directly.

Focus on:

- inspecting
- comparing
- identifying
- tracing
- explaining

using built-in Windows tools.

---

## Hands-on Sessions (≈30%)

Purpose:

Apply concepts through practical investigation.

Typical workflow:

```text
Predict

↓

Observe

↓

Modify

↓

Verify

↓

Explain
```

---

# Lab Environment

Host System

- Arch Linux

Windows Lab

- Windows 11 VM
- Windows Server Evaluation VM (later phases)
- QEMU/KVM recommended

The VM exists for:

- safe experimentation
- snapshots
- Active Directory labs
- incident response exercises

---

# Typical Phase Structure

Every phase follows a consistent pattern.

```text
Session 01–02
Concept

↓

Session 03–04
Observation

↓

Session 05–08
Hands-on Investigation

↓

Session 09–11
Applied Observation

↓

Session 12
Mini Review Lab
```

This allows learning to continue easily across different chat sessions.

---

# Phase 01 — Windows Foundations

## Goal

Understand Windows as an operating system rather than a graphical interface.

Build the mental model that will support every later topic.

---

## Outcomes

After completing this phase, you should be able to:

- explain what Windows actually is
- distinguish GUI from the operating system
- explain User Mode vs Kernel Mode
- identify major Windows components
- understand the Windows boot sequence
- navigate basic Windows administration tools

---

## Typical Tools

- Task Manager
- Resource Monitor
- System Information
- msinfo32
- winver
- Settings
- Control Panel

---

## Example Labs

- Observe running processes
- Observe services
- Compare Task Manager to Linux tools
- Observe startup programs
- Inspect system information

---

### Session 01

What Is Windows?

---

### Session 02

User Mode vs Kernel Mode

---

### Session 03

Observing Windows with Task Manager

---

### Session 04

Processes vs Applications

---

### Session 05

Major Windows Components

- Explorer
- Services
- Registry
- Win32
- Drivers

---

### Session 06

Observing Windows Services

---

### Session 07

System Information

- msinfo32
- winver
- systeminfo

---

### Session 08

Resource Monitor

CPU

Memory

Disk

Network

---

### Session 09

Windows Boot Process Overview

---

### Session 10

Observing Startup Programs

---

### Session 11

Mini Investigation

"What is currently running on my Windows system?"

---

### Session 12

Phase Review Lab

---

# Phase 02 — Filesystem & NTFS

## Goal

Understand how Windows stores data and enforces filesystem security.

---

## Outcomes

After completing this phase, you should be able to:

- navigate Windows storage
- understand NTFS
- explain metadata
- understand Alternate Data Streams
- understand Windows path conventions
- compare NTFS with ext4

---

## Typical Tools

- File Explorer
- Disk Management
- fsutil
- PowerShell

---

## Example Labs

- Create NTFS directories
- Inspect permissions
- Create symbolic links
- Observe Alternate Data Streams
- Compare Windows and Linux paths

---

### Session 01

Windows Drives, Volumes and Paths

---

### Session 02

NTFS Overview

---

### Session 03

Observing the Windows Filesystem

---

### Session 04

Windows Special Directories

- System32
- Program Files
- Users
- ProgramData

---

### Session 05

NTFS Metadata

---

### Session 06

Alternate Data Streams

---

### Session 07

Symbolic Links and Junctions

---

### Session 08

Windows Path Resolution

---

### Session 09

Disk Management Observation

---

### Session 10

Filesystem Investigation

---

### Session 11

Mini Investigation

Tracing a File Through Windows

---

### Session 12

Phase Review Lab

---

# Phase 03 — Users, Groups & Permissions

## Goal

Understand identity, authorization and permission management in Windows.

This phase builds the foundation for Active Directory.

---

## Outcomes

After completing this phase, you should be able to:

- explain users and groups
- understand SIDs
- explain Access Tokens
- understand ACLs
- compare Windows authorization with Linux permissions

---

## Typical Tools

- Computer Management
- lusrmgr.msc
- whoami
- PowerShell

---

## Example Labs

- Create local users
- Create groups
- Inspect ACLs
- Compare permissions
- Observe access tokens

---

### Session 01

Windows Users and Groups

---

### Session 02

Security Identifiers (SID)

---

### Session 03

Observing Local Users

---

### Session 04

Observing Group Membership

---

### Session 05

Windows Permissions

---

### Session 06

ACL Fundamentals

---

### Session 07

Access Tokens

---

### Session 08

Privileges vs Permissions

---

### Session 09

Comparing Linux and Windows Authorization

---

### Session 10

Permission Investigation

---

### Session 11

Mini Investigation

"Why can this user access this file?"

---

### Session 12

Phase Review Lab

---

# Phase 04 — Processes & Services

## Goal

Understand how Windows executes programs and manages background services.

This phase connects directly to system administration, incident response, malware analysis, and endpoint security.

---

## Outcomes

After completing this phase, you should be able to:

- explain Windows processes and threads
- distinguish applications from processes
- understand Windows Services
- explain the Service Control Manager (SCM)
- inspect process trees
- identify common persistence mechanisms

---

## Typical Tools

- Task Manager
- Resource Monitor
- services.msc
- tasklist
- taskkill
- sc
- PowerShell

---

## Example Labs

- Observe running processes
- Observe parent-child relationships
- Start and stop services
- Inspect service startup types
- Compare Windows Services with Linux systemd services

---

### Session 01

Processes vs Threads

---

### Session 02

Windows Services & Service Control Manager (SCM)

---

### Session 03

Observing Running Processes

---

### Session 04

Observing Process Trees

---

### Session 05

Inspecting Windows Services

---

### Session 06

Starting, Stopping and Restarting Services

---

### Session 07

Service Startup Types

- Automatic
- Manual
- Disabled

---

### Session 08

Scheduled Tasks as Persistence

---

### Session 09

Comparing systemd and Windows Services

---

### Session 10

Process Investigation

---

### Session 11

Mini Investigation

"What started this process?"

---

### Session 12

Phase Review Lab

---

# Phase 05 — Event Logs & Observability

## Goal

Understand how Windows records system activity and how defenders investigate it.

This phase forms the foundation for enterprise monitoring and incident response.

---

## Outcomes

After completing this phase, you should be able to:

- explain Windows Event Logs
- understand Event IDs
- inspect authentication events
- inspect service events
- build simple activity timelines

---

## Typical Tools

- Event Viewer
- wevtutil
- PowerShell

---

## Example Labs

- Observe logon events
- Observe service events
- Observe application crashes
- Filter Event Logs
- Build an investigation timeline

---

### Session 01

Why Windows Event Logs Exist

---

### Session 02

Windows Event Log Architecture

---

### Session 03

Exploring Event Viewer

---

### Session 04

Windows Log Categories

- Application
- Security
- System
- Setup

---

### Session 05

Authentication Events

---

### Session 06

Service Events

---

### Session 07

Application Events

---

### Session 08

Filtering Event Logs

---

### Session 09

Building Timelines

---

### Session 10

Simple Incident Investigation

---

### Session 11

Mini Investigation

"What happened on this computer?"

---

### Session 12

Phase Review Lab

---

# Phase 06 — PowerShell Fundamentals

## Goal

Learn PowerShell as the standard Windows automation and administration interface.

Focus on understanding objects rather than memorizing commands.

---

## Outcomes

After completing this phase, you should be able to:

- understand object-based pipelines
- navigate PowerShell
- query Windows components
- automate system observation
- compare PowerShell with Bash

---

## Typical Tools

- PowerShell
- Windows Terminal

---

## Example Labs

- List processes
- List services
- List users
- Query event logs
- Export system information

---

### Session 01

Why PowerShell Exists

---

### Session 02

Objects vs Text

---

### Session 03

Exploring the PowerShell Console

---

### Session 04

Finding Commands

- Get-Command
- Get-Help

---

### Session 05

Object Pipelines

---

### Session 06

Working with Processes

---

### Session 07

Working with Services

---

### Session 08

Working with Files

---

### Session 09

Working with Event Logs

---

### Session 10

Building Small Investigation Commands

---

### Session 11

Mini Investigation

"Collect basic system information with PowerShell"

---

### Session 12

Phase Review Lab

---

# Phase 07 — Networking on Windows

## Goal

Understand how Windows participates in modern networks from the operating system perspective.

This phase focuses on host networking rather than networking protocols themselves.

---

## Outcomes

After completing this phase, you should be able to:

- inspect Windows network configuration
- understand Windows network interfaces
- inspect routing information
- understand Windows Firewall
- troubleshoot common connectivity issues
- compare Windows networking with Linux networking

---

## Typical Tools

- ipconfig
- ping
- tracert
- netstat
- arp
- route
- PowerShell
- Windows Defender Firewall

---

## Example Labs

- Observe network interfaces
- Inspect routing tables
- Observe ARP cache
- Compare ipconfig with ip addr
- Observe listening ports

---

### Session 01

Windows Networking Overview

---

### Session 02

Network Interfaces

---

### Session 03

Observing Network Configuration

(ipconfig)

---

### Session 04

Routing Tables

(route print)

---

### Session 05

ARP Cache Observation

---

### Session 06

DNS Resolution

---

### Session 07

Listening Ports and Connections

(netstat)

---

### Session 08

Windows Defender Firewall

---

### Session 09

Comparing Linux and Windows Networking

---

### Session 10

Network Troubleshooting

---

### Session 11

Mini Investigation

"Why can't this computer reach the network?"

---

### Session 12

Phase Review Lab

---

# Phase 08 — SMB & File Sharing

## Goal

Understand the protocol that powers most enterprise Windows file sharing.

Learn both the administration perspective and the security perspective.

---

## Outcomes

After completing this phase, you should be able to:

- explain SMB
- create Windows shares
- distinguish share permissions from NTFS permissions
- understand administrative shares
- troubleshoot common sharing problems

---

## Typical Tools

- File Explorer
- Computer Management
- net share
- net use
- PowerShell

---

## Example Labs

- Create SMB shares
- Connect to remote shares
- Compare share permissions
- Observe hidden administrative shares

---

### Session 01

What is SMB?

---

### Session 02

Shares vs NTFS Permissions

---

### Session 03

Observing Existing Shares

---

### Session 04

Creating Shared Folders

---

### Session 05

Mapping Network Drives

---

### Session 06

Administrative Shares

- C$
- ADMIN$
- IPC$

---

### Session 07

SMB Authentication Flow

---

### Session 08

Troubleshooting File Sharing

---

### Session 09

Comparing Samba and Windows SMB

---

### Session 10

Share Permission Investigation

---

### Session 11

Mini Investigation

"Why can one user access the share while another cannot?"

---

### Session 12

Phase Review Lab

---

# Phase 09 — Windows Authentication

## Goal

Understand how Windows verifies identity before introducing Active Directory.

This phase builds the conceptual foundation for Kerberos and enterprise authentication.

---

## Outcomes

After completing this phase, you should be able to:

- distinguish authentication from authorization
- explain local authentication
- explain domain authentication
- understand access tokens
- understand NTLM at a conceptual level

---

## Typical Tools

- whoami
- runas
- Event Viewer
- PowerShell

---

## Example Labs

- Observe logon events
- Compare local and domain users
- Inspect access tokens
- Observe authentication failures

---

### Session 01

Authentication vs Authorization

---

### Session 02

Windows Credentials

---

### Session 03

Observing Local Logon

---

### Session 04

Access Tokens

---

### Session 05

NTLM Fundamentals

---

### Session 06

Domain Logon Overview

---

### Session 07

runas and Alternate Credentials

---

### Session 08

Authentication Events

---

### Session 09

Authentication Troubleshooting

---

### Session 10

Following a Windows Logon

---

### Session 11

Mini Investigation

"How did this user successfully log in?"

---

### Session 12

Phase Review Lab

---

# Phase 10 — Active Directory Fundamentals

## Goal

Understand Active Directory as the identity and management system used in enterprise Windows environments.

This phase focuses on architecture and mental models rather than administration.

---

## Outcomes

After completing this phase, you should be able to:

- explain what Active Directory is
- understand Domains and Domain Controllers
- understand Organizational Units (OUs)
- explain Group Policy at a high level
- understand why enterprises centralize identity

---

## Typical Tools

- Active Directory Users and Computers (ADUC)
- Group Policy Management
- Active Directory Administrative Center
- PowerShell

---

## Example Labs

- Build a small Active Directory lab
- Create users and groups
- Join a client to a domain
- Explore Organizational Units
- Observe Group Policy application

---

### Session 01

Why Active Directory Exists

---

### Session 02

Domains and Domain Controllers

---

### Session 03

Observing an Active Directory Environment

---

### Session 04

Users, Groups and Organizational Units

---

### Session 05

Joining a Computer to a Domain

---

### Session 06

Group Policy Fundamentals

---

### Session 07

Domain Administration Overview

---

### Session 08

LDAP Fundamentals

---

### Session 09

Comparing Local Authentication and Domain Authentication

---

### Session 10

Tracing an Active Directory Login

---

### Session 11

Mini Investigation

"Where does this user account actually exist?"

---

### Session 12

Phase Review Lab

---

# Phase 11 — Kerberos Fundamentals

## Goal

Understand the authentication protocol that powers modern Active Directory environments.

This phase emphasizes the authentication workflow instead of protocol implementation details.

---

## Outcomes

After completing this phase, you should be able to:

- explain why Kerberos exists
- understand tickets
- explain TGT and Service Tickets
- understand the role of the KDC
- compare Kerberos and NTLM

---

## Typical Tools

- klist
- Event Viewer
- PowerShell

---

## Example Labs

- Inspect Kerberos tickets
- Observe ticket renewal
- Compare Kerberos and NTLM authentication
- Trace a domain login

---

### Session 01

Why Kerberos Exists

---

### Session 02

Kerberos Architecture

---

### Session 03

Observing Kerberos Tickets

---

### Session 04

Ticket Granting Ticket (TGT)

---

### Session 05

Service Tickets

---

### Session 06

Key Distribution Center (KDC)

---

### Session 07

Single Sign-On

---

### Session 08

Comparing NTLM and Kerberos

---

### Session 09

Kerberos Authentication Timeline

---

### Session 10

Authentication Investigation

---

### Session 11

Mini Investigation

"How did this user access a network resource without entering another password?"

---

### Session 12

Phase Review Lab

---

# Phase 12 — Windows Security Fundamentals

## Goal

Understand the built-in security architecture of Windows before studying offensive or defensive techniques.

Focus on security boundaries and defensive components.

---

## Outcomes

After completing this phase, you should be able to:

- explain User Account Control (UAC)
- understand Windows Defender
- understand Windows security boundaries
- recognize common protection mechanisms
- understand host hardening concepts

---

## Typical Tools

- Windows Security
- Windows Defender
- Local Security Policy
- Event Viewer
- PowerShell

---

## Example Labs

- Observe Windows Defender
- Observe UAC prompts
- Inspect Windows Security settings
- Review security-related Event Logs
- Compare Windows protections with Linux equivalents

---

### Session 01

Windows Security Architecture Overview

---

### Session 02

Security Boundaries

---

### Session 03

User Account Control (UAC)

---

### Session 04

Windows Defender

---

### Session 05

Windows Firewall Revisited

---

### Session 06

Credential Protection Concepts

---

### Session 07

Least Privilege on Windows

---

### Session 08

Security Configuration Observation

---

### Session 09

Host Hardening Concepts

---

### Session 10

Security Event Investigation

---

### Session 11

Mini Investigation

"How is this Windows system protecting itself?"

---

### Session 12

Phase Review Lab

---

# Phase 13 — Enterprise Environment Concepts

## Goal

Understand how Windows systems operate inside real enterprise environments.

This phase connects Windows fundamentals to organizational infrastructure and day-to-day IT operations.

---

## Outcomes

After completing this phase, you should be able to:

- explain a typical enterprise Windows environment
- understand centralized management
- understand endpoint management
- understand software deployment concepts
- understand enterprise terminology

---

## Typical Tools

- Active Directory
- Group Policy
- Microsoft Management Console (MMC)
- Windows Admin Center
- PowerShell

---

## Example Labs

- Map a small enterprise network
- Trace a Group Policy update
- Observe domain-managed settings
- Compare standalone PCs with domain-joined PCs
- Explore centralized administration

---

### Session 01

What Is an Enterprise Environment?

---

### Session 02

Typical Enterprise Architecture

---

### Session 03

Servers vs Workstations

---

### Session 04

Centralized Management

---

### Session 05

Group Policy in Practice

---

### Session 06

Software Deployment Concepts

---

### Session 07

Patch Management Concepts

---

### Session 08

Enterprise Monitoring Overview

---

### Session 09

Endpoint Management Concepts

---

### Session 10

Enterprise Workflow Observation

---

### Session 11

Mini Investigation

"How would an administrator manage hundreds of Windows computers?"

---

### Session 12

Phase Review Lab

---

# Phase 14 — Introductory Incident Response

## Goal

Learn how defenders investigate Windows systems after suspicious activity.

The focus is observation, evidence collection and reasoning—not malware removal.

---

## Outcomes

After completing this phase, you should be able to:

- identify useful evidence sources
- inspect Windows Event Logs
- investigate suspicious processes
- reconstruct simple timelines
- perform basic host investigations

---

## Typical Tools

- Event Viewer
- Task Manager
- Resource Monitor
- PowerShell
- Windows Security

---

## Example Labs

- Investigate failed logons
- Investigate service modifications
- Trace application crashes
- Build a simple activity timeline
- Identify suspicious startup entries

---

### Session 01

What Is Incident Response?

---

### Session 02

Windows Evidence Sources

---

### Session 03

Observing Running Processes

---

### Session 04

Investigating Logon Activity

---

### Session 05

Investigating Services

---

### Session 06

Investigating Startup Programs

---

### Session 07

Timeline Reconstruction

---

### Session 08

Basic Host Triage

---

### Session 09

Simple Investigation Workflow

---

### Session 10

Case Study

Suspicious User Activity

---

### Session 11

Mini Investigation

"What happened on this Windows machine?"

---

### Session 12

Phase Review Lab

---

# Phase 15 — Foundations for Future Windows Security Learning

## Goal

Connect everything learned into a coherent security-focused mental model.

Prepare for Windows Internals, Active Directory Security, Malware Analysis, Digital Forensics, Reverse Engineering and Enterprise Security.

---

## Outcomes

After completing this phase, you should be able to:

- understand how Windows components interact
- navigate Windows confidently
- investigate systems methodically
- understand enterprise authentication
- begin advanced Windows security topics without major knowledge gaps

---

## Typical Tools

- PowerShell
- Event Viewer
- Windows Security
- Sysinternals Suite
- Windows Terminal

---

## Example Labs

- Investigate suspicious processes
- Trace authentication activity
- Inspect services and startup entries
- Analyze a complete Windows host
- Perform an end-to-end system walkthrough

---

### Session 01

Connecting the Windows Architecture

---

### Session 02

Observability Review

---

### Session 03

Authentication Review

---

### Session 04

Filesystem Review

---

### Session 05

Networking Review

---

### Session 06

Enterprise Review

---

### Session 07

Security Review

---

### Session 08

Complete Windows Investigation Workflow

---

### Session 09

Capstone Lab

Investigating an Unknown Windows System

---

### Session 10

Preparing for Windows Internals

---

### Session 11

Preparing for Active Directory Security

---

### Session 12

Final Capstone Review

---

# Final Outcome

Upon completing this roadmap, you should be able to:

- Explain how Windows systems are architected.
- Understand the relationship between User Mode and Kernel Mode.
- Navigate Windows confidently despite primarily using Linux.
- Understand NTFS, permissions, identities and access control.
- Inspect processes, services and system activity.
- Use PowerShell as an investigation and administration tool.
- Troubleshoot Windows networking.
- Understand SMB and enterprise file sharing.
- Explain Windows authentication, NTLM and Kerberos.
- Understand Active Directory architecture and enterprise identity management.
- Interpret Windows Event Logs and perform basic host investigations.
- Understand the role of Windows Defender, UAC and native security controls.
- Reason about enterprise Windows environments.
- Build timelines from observable system activity.
- Transition smoothly into advanced topics such as:
  - Windows Internals
  - Active Directory Security
  - Incident Response
  - Malware Analysis
  - Digital Forensics
  - Endpoint Detection & Response (EDR)
  - Reverse Engineering

---

# Core Mental Model

Windows should no longer appear as a collection of GUI applications.

Instead, it should become a coherent operating system built around:

```text
Hardware
        │
        ▼
NT Kernel
        │
        ▼
Processes
Services
Filesystem
Networking
Authentication
Observability
        │
        ▼
Enterprise Infrastructure
        │
        ▼
Security
```

The objective is not to memorize Windows.

The objective is to understand **why Windows behaves the way it does**, so that administration, troubleshooting and security analysis become natural extensions of systems thinking.

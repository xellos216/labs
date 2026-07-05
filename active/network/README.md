# Networking Roadmap

## Objective

Build a coherent mental model of how systems communicate, how data moves
through networks and how network behavior can be observed and explained.

This roadmap connects networking to:

- Linux
- web systems
- troubleshooting
- packet analysis
- security
- controlled lab environments

---

# Philosophy

Networking is not a collection of protocols to memorize.

Networking is the study of how systems move information, coordinate actions, and solve communication problems.

The objective is to understand:

- Why protocols exist
- What problems they solve
- How data moves through systems
- How networking connects to Linux
- How networking connects to web systems
- How networking connects to security
- How networking connects to offensive security

Core principles:

- understanding before memorization
- observation before exploitation
- systems thinking
- transferable skills over shortcuts
- mastery-oriented learning

---

# Learning Method

The roadmap progresses from concepts to direct observation and then to
integrated investigation.

## Concept Sessions

Explain why protocols and network components exist, what problems they solve
and how they interact.

## Observation Sessions

Inspect interfaces, routes, sockets, packets and application traffic using
Linux and packet-analysis tools.

## Hands-on Sessions

Apply the mental model through local experiments, troubleshooting exercises
and ethically scoped lab environments.

Typical workflow:

```text
Predict

↓

Observe

↓

Trace

↓

Explain
```

---

# Lab Environment

Host system:

- Arch Linux

Primary workflow:

- zsh
- tmux
- neovim
- CLI-first tooling

Preferred lab boundaries:

- local services
- network namespaces
- virtual machines
- packet captures generated in controlled environments
- authorized training platforms

---

# Typical Phase Structure

Every phase retains its existing 14-session scope.

```text
Protocol or System Concept
          │
          ▼
Linux or Packet Observation
          │
          ▼
Applied Investigation
          │
          ▼
Integrated Mental Model
```

---

# Phase 01 — Foundations

## Goal

Build a mental model of networking as a system for moving information.

---

## Outcomes

- understand what a network actually is
- understand why IP exists
- understand why ports exist
- understand why TCP and UDP exist
- understand how Linux participates in networking
- build a foundation for later security learning

---

## Typical Tools

- ip
- ss
- ping
- traceroute
- dig
- curl
- tcpdump

---

## Example Labs

- inspect local addresses, routes and sockets
- compare TCP and UDP behavior
- observe a TCP three-way handshake
- trace DNS resolution and HTTP requests
- capture and explain a simple network exchange

---

### Session 01

What is a Network?

---

### Session 02

IP Addresses

---

### Session 03

Ports

---

### Session 04

TCP

---

### Session 05

UDP

---

### Session 06

TCP Three-Way Handshake

---

### Session 07

DNS

---

### Session 08

Routing

---

### Session 09

HTTP

---

### Session 10

TLS

---

### Session 11

Sockets

---

### Session 12

Packet Capture

---

### Session 13

Network Troubleshooting

---

### Session 14

Networking Concepts Inside HTB

---

# Phase 02 — Linux Networking

## Goal

Understand how Linux implements networking.

---

## Outcomes

- understand network interfaces
- understand Linux packet flow
- understand routing tables
- understand NAT
- understand Linux firewall concepts
- observe networking from the operating system perspective

---

## Typical Tools

- ip
- ss
- arping
- sysctl
- iptables
- nft
- conntrack
- network namespaces

---

## Example Labs

- inspect interfaces and the loopback device
- observe ARP and neighbor-table changes
- trace a routing decision
- build an isolated namespace network
- inspect firewall and connection-tracking state

---

### Session 01

Network Interfaces

---

### Session 02

Loopback Interface

---

### Session 03

ARP

---

### Session 04

Neighbor Tables

---

### Session 05

Routing Tables

---

### Session 06

Default Gateway

---

### Session 07

DHCP

---

### Session 08

NAT

---

### Session 09

Linux Packet Flow

---

### Session 10

iptables Fundamentals

---

### Session 11

nftables Overview

---

### Session 12

Connection Tracking

---

### Session 13

Network Namespaces

---

### Session 14

Observing Linux Networking Internals

---

# Phase 03 — Packet Thinking

## Goal

Learn to think in packets instead of applications.

---

## Outcomes

- understand packet structure
- interpret packet captures
- understand protocol behavior through observation
- improve troubleshooting and enumeration skills

---

## Typical Tools

- Wireshark
- tshark
- tcpdump
- ping
- traceroute
- dig
- curl

---

## Example Labs

- annotate an Ethernet frame and IP packet
- compare TCP and UDP packet structures
- follow an ARP or ICMP exchange
- reconstruct DNS and HTTP conversations
- explain a packet capture as a sequence of events

---

### Session 01

What Is a Packet?

---

### Session 02

Ethernet Frames

---

### Session 03

MAC Addresses

---

### Session 04

ARP Traffic

---

### Session 05

ICMP

---

### Session 06

Traceroute Mechanics

---

### Session 07

TCP Packet Anatomy

---

### Session 08

UDP Packet Anatomy

---

### Session 09

DNS Packets

---

### Session 10

HTTP Packets

---

### Session 11

TLS Packets

---

### Session 12

Wireshark Workflow

---

### Session 13

tcpdump Workflow

---

### Session 14

Packet Storytelling

---

# Phase 04 — Web Networking

## Goal

Understand web applications as networking systems.

---

## Outcomes

- understand browser-to-server communication
- understand HTTP deeply
- understand sessions and authentication
- understand how web applications use networking

---

## Typical Tools

- browser developer tools
- curl
- HTTP proxy
- tcpdump
- Wireshark
- openssl

---

## Example Labs

- trace a browser request lifecycle
- inspect HTTP requests and responses
- compare cookies, sessions and JWT transport
- observe proxy and reverse-proxy behavior
- map the network components of a real web application

---

### Session 01

Browser Request Lifecycle

---

### Session 02

HTTP Request Structure

---

### Session 03

HTTP Response Structure

---

### Session 04

Cookies

---

### Session 05

Sessions

---

### Session 06

JWT

---

### Session 07

Caching

---

### Session 08

Proxies

---

### Session 09

Reverse Proxies

---

### Session 10

Load Balancers

---

### Session 11

CDN Fundamentals

---

### Session 12

WebSocket

---

### Session 13

API Networking

---

### Session 14

Observing Real Web Applications

---

# Phase 05 — Security Networking

## Goal

Understand security from a networking perspective.

---

## Outcomes

- understand attack surfaces
- understand enumeration theory
- understand network visibility
- understand common security controls

---

## Typical Tools

- nmap
- dig
- curl
- nc
- tcpdump
- Wireshark
- firewall and IDS observation tools

---

## Example Labs

- map the exposed services of an authorized target
- compare scan results with packet captures
- inspect DNS and web enumeration traffic
- analyze suspicious network behavior
- compare segmentation, firewall and IDS visibility

---

### Session 01

Attack Surface

---

### Session 02

Port Scanning Theory

---

### Session 03

Nmap Internals

---

### Session 04

Service Enumeration

---

### Session 05

Banner Grabbing

---

### Session 06

DNS Enumeration

---

### Session 07

Web Enumeration

---

### Session 08

Packet Inspection

---

### Session 09

Traffic Analysis

---

### Session 10

Man-in-the-Middle Concepts

---

### Session 11

Network Segmentation

---

### Session 12

Firewalls

---

### Session 13

IDS and IPS

---

### Session 14

Network Security Mental Models

---

# Phase 06 — HTB Networking Lab

## Goal

Apply networking concepts in real environments.

---

## Outcomes

- understand HTB networking environments
- improve observation skills
- build strong enumeration habits
- connect theory to practice

---

## Typical Tools

- VPN client
- ip
- ping
- traceroute
- nmap
- curl
- tcpdump

---

## Example Labs

- verify VPN routing and target reachability
- separate host, port and service discovery
- identify protocols from observable behavior
- document an enumeration workflow
- analyze failure and pivoting concepts in an authorized lab

---

### Session 01

HTB Network Architecture

---

### Session 02

VPN Concepts

---

### Session 03

Target Reachability

---

### Session 04

Host Discovery

---

### Session 05

Port Discovery

---

### Session 06

Service Discovery

---

### Session 07

Web Discovery

---

### Session 08

Protocol Identification

---

### Session 09

Traffic Observation

---

### Session 10

Enumeration Workflow

---

### Session 11

Building Observation Notes

---

### Session 12

Failure Analysis

---

### Session 13

Network-Based Pivot Thinking

---

### Session 14

HTB Machine Walkthrough Analysis

---

# Phase 07 — Advanced Networking

## Goal

Understand modern networking systems and architectures.

---

## Outcomes

- understand large-scale networks
- understand cloud networking
- understand container networking
- understand modern infrastructure design

---

## Typical Tools

- ip
- bridge
- network namespaces
- WireGuard
- container networking tools
- routing and cloud architecture diagrams

---

## Example Labs

- calculate and verify subnet and CIDR boundaries
- inspect VLAN and routing concepts in an isolated lab
- observe container network interfaces and bridges
- trace traffic through a VPN
- compare cloud, service-mesh and zero-trust architectures

---

### Session 01

VLAN

---

### Session 02

Subnetting

---

### Session 03

CIDR

---

### Session 04

BGP Overview

---

### Session 05

VPN Technologies

---

### Session 06

WireGuard

---

### Session 07

IPv6

---

### Session 08

Containers and Networking

---

### Session 09

Docker Networking

---

### Session 10

Kubernetes Networking

---

### Session 11

Cloud Networking

---

### Session 12

Service Mesh Concepts

---

### Session 13

Zero Trust Networking

---

### Session 14

Modern Internet Architecture

---

# Final Outcome

By completing this roadmap, you should be able to:

- explain how data moves across systems
- understand why networking protocols exist
- troubleshoot Linux networking issues
- analyze network traffic with confidence
- understand how web systems use networking
- understand how security depends on networking
- perform higher-quality HTB enumeration
- develop strong troubleshooting ability
- build a unified mental model connecting Linux, networking, web systems and security

Networking will no longer appear as isolated technologies.

Instead, it will become a coherent system for understanding how computers communicate.

---

# Core Mental Model

```text
Application Data
       │
       ▼
Sockets and Transport
       │
       ▼
IP Addressing and Routing
       │
       ▼
Links, Interfaces and Packets
       │
       ▼
Local and Remote Systems
       │
       ▼
Observable Network Behavior
```

Networking becomes understandable when each layer can be connected to the
packets, operating-system state and application behavior it produces.

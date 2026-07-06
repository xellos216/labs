# Phase 02 - Session 08

## Metadata

```yaml
Roadmap: Networking
Phase: 02
Session: 08
Title: NAT
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-07-07
```

---

# Objective

Understand what NAT does, why private IP addresses can communicate with the
Internet, and how a NAT device maps internal traffic to externally visible
address and port pairs.

---

# Learning Summary

NAT is primarily an address and port translation mechanism. It allows hosts on
an internal network to communicate with external networks by translating
private internal address and port pairs into externally visible address and
port pairs.

The core model is:

```text
Internal IP:Port
        ↔
External IP:Port
```

External servers do not directly see the private internal address. They see the
translated public address and port. When a response returns, the NAT device
uses its translation table to decide which internal IP and port should receive
the packet.

This session also separated NAT from ARP and neighbor tables. NAT decides which
internal IP and port a returning packet belongs to. ARP or the neighbor table
is used later when the router must deliver the packet on the local link.

A practical observation showed two different paths on the same host:

- a wired path where the local IPv4 address matched the externally visible
  address, so NAT was not visible at the host edge
- a Wi-Fi path where the local address was private but the externally visible
  address was public, showing NAT behavior

---

# Key Concepts

- NAT
- Source NAT
- Port Address Translation
- Private IP address
- Public IP address
- NAT table
- Internal IP and port
- External IP and port
- Translation port
- Return traffic
- Firewall distinction
- ARP / Neighbor Table distinction

---

# Practical Observations

## Observation 1 - Private Addresses Are Not Directly Seen Externally

Prediction:

```text
An external server cannot directly reply to an internal private IP address.
```

Explanation:

Private addresses such as `192.168.0.10` are used inside local networks. They
are not the address normally seen by an external Internet server.

For NAT-based outbound traffic, the external server sees a translated public
address and port.

```text
Internal host
192.168.0.10:53000
        ↓
NAT router
198.51.100.25:40001
        ↓
External server
```

The server replies to the translated public endpoint, not directly to the
private address.

---

## Observation 2 - NAT Remembers Address and Port Mappings

Prediction:

```text
The NAT device must remember more than the internal MAC address.
```

Explanation:

The important NAT state is the mapping between internal and external address
and port pairs.

```text
NAT table

198.51.100.25:40001  ↔  192.168.0.10:53000
```

When the response returns to `198.51.100.25:40001`, the NAT device looks up the
translation table and forwards the packet back to `192.168.0.10:53000`.

MAC resolution happens later, when the NAT router sends the packet on the local
link.

```text
NAT table
        ↓
Internal IP:Port selected
        ↓
Neighbor Table / ARP
        ↓
Internal MAC resolved
        ↓
Local frame transmitted
```

---

## Observation 3 - Wired Path Without Visible NAT

Prediction:

```text
If the local interface has a public IPv4 address, the external address may
match the local interface address.
```

Observation:

```text
Local wired interface address:
203.0.113.10/24

External address observed by a public IP-check service:
203.0.113.10
```

Explanation:

The local wired interface and the external observer saw the same IPv4 address.
This indicates that, on that path, the host was not behind an immediately
visible private-to-public NAT boundary.

The useful distinction is:

```text
Public-address path:
Host public IP
        ↓
Internet
        ↓
External server sees the same public IP
```

---

## Observation 4 - Wi-Fi Path With NAT

Prediction:

```text
If the Wi-Fi interface uses a private address, an external IP-check service
should see a different public address.
```

Observation:

```text
Local Wi-Fi interface address:
192.168.0.10/24

External address observed when forcing the Wi-Fi interface:
198.51.100.25
```

Explanation:

The local Wi-Fi address was private, while the external service saw a public
address. This is evidence that traffic on the Wi-Fi path passed through NAT.

```text
Wi-Fi host
192.168.0.10:<local-port>
        ↓
NAT router
198.51.100.25:<translated-port>
        ↓
Internet
        ↓
External server
```

The external server does not know the internal private address. It replies to
the public address and translated port.

---

## Observation 5 - Multiple Internal Hosts Can Share One Public IP

Prediction:

```text
Two internal hosts can use the same internal source port if the NAT device
uses different external translated ports.
```

Explanation:

```text
Laptop:
192.168.0.10:53000  ↔  198.51.100.25:40001

Phone:
192.168.0.11:53000  ↔  198.51.100.25:40002
```

The internal source ports are the same, but the internal IP addresses differ.
The NAT device can also assign different external translated ports, so the
returning traffic can be mapped to the correct internal host.

External server view:

```text
198.51.100.25:40001
198.51.100.25:40002
```

The server does not need to know which internal device made each connection.
It only replies to the externally visible address and port.

---

## Observation 6 - NAT and Security

Prediction:

```text
NAT hides internal addresses, but its primary role may not be security policy.
```

Explanation:

NAT has security side effects because internal private addresses are not
directly exposed and unsolicited inbound connections usually have no existing
translation mapping.

However, NAT is primarily address and port translation. Firewalling is the
policy mechanism that explicitly permits or denies packets.

```text
NAT
= address and port translation

Firewall
= allow / deny policy
```

NAT can reduce direct exposure, but it should not be treated as a replacement
for a firewall.

---

# Commands / Code

```bash
ip -4 addr
```

Shows the local IPv4 addresses assigned to the host's interfaces.

---

```bash
curl -4 ifconfig.me
```

Shows the IPv4 address observed by an external service for the default route.

---

```bash
curl -4 https://icanhazip.com
```

Alternative external IPv4 check.

---

```bash
curl -4 --interface wlan0 https://icanhazip.com
```

Forces the request through a specific interface when supported by the system
and route configuration. This can reveal whether that interface path appears
externally as a different public IP.

---

```bash
ip route get 8.8.8.8 from 192.168.0.10
```

Asks the kernel how it would route traffic with a specific source address.
This does not necessarily force a specific outgoing interface. The selected
interface still depends on routing policy.

---

# Connections

```text
Session 05 - Routing Tables
        ↓
Kernel decides the outgoing path

Session 06 - Default Gateway
        ↓
Off-LAN traffic goes to the first router

Session 07 - DHCP
        ↓
Hosts receive IP, gateway, DNS, and lease configuration

Session 08 - NAT
        ↓
The gateway or router may translate internal IP:Port to external IP:Port
```

Combined model:

```text
Application
        ↓
Socket with local port
        ↓
Routing decision
        ↓
Default gateway / NAT router
        ↓
Source IP:Port translation
        ↓
Internet
        ↓
External server replies to translated endpoint
        ↓
NAT table maps response back to internal IP:Port
        ↓
Local delivery through neighbor resolution
```

---

# Common Misconceptions

- Incorrect: NAT mainly remembers the internal MAC address.
- Correct: NAT primarily remembers address and port mappings. MAC resolution is
  a separate local-link delivery step.

---

- Incorrect: External servers see the private IP address of the internal host.
- Correct: External servers normally see the translated public IP and port.

---

- Incorrect: Internal source ports must be different for NAT to distinguish
  hosts.
- Correct: Internal IP addresses can differ, and the NAT device can assign
  different external translated ports.

---

- Incorrect: NAT and firewall are the same thing.
- Correct: NAT translates addresses and ports. A firewall enforces allow or
  deny policy.

---

- Incorrect: NAT is always visible on every network path.
- Correct: One interface may have a public address directly, while another
  interface may be behind NAT.

---

# Key Takeaways

- NAT maps internal IP:Port pairs to external IP:Port pairs.
- External servers reply to the translated public endpoint, not the internal
  private address.
- NAT state is usually tracked by protocol, internal address and port, external
  translated address and port, and timeout or connection state.
- ARP and neighbor tables are separate from NAT; they handle local-link MAC
  resolution.
- Multiple internal hosts can share one public IP through different translated
  ports.
- NAT can have security side effects, but it is not the same as a firewall.
- Network paths can differ: one interface can expose a public IP directly while
  another uses private addressing behind NAT.

---

# Review Questions

### Q1. What problem does NAT solve for private internal networks?

<details>
<summary>A</summary>

</details>

---

### Q2. Why can't an external server normally reply directly to `192.168.0.10`?

<details>
<summary>A</summary>

</details>

---

### Q3. What information does a NAT table need to remember for returning traffic?

<details>
<summary>A</summary>

</details>

---

### Q4. Why is the internal MAC address not the main NAT mapping key?

<details>
<summary>A</summary>

</details>

---

### Q5. If two internal devices use the same source port, how can NAT still distinguish them externally?

<details>
<summary>A</summary>

</details>

---

### Q6. What observation showed that the wired path did not have visible private-to-public NAT at the host edge?

<details>
<summary>A</summary>

</details>

---

### Q7. What observation showed that the Wi-Fi path was using NAT?

<details>
<summary>A</summary>

</details>

---

### Q8. Why is NAT not the same as a firewall?

<details>
<summary>A</summary>

</details>

---

### Q9. Complete the return path:

```text
External server
        ↓
Public IP:translated port
        ↓
?
        ↓
Internal IP:original port
        ↓
?
        ↓
Internal host MAC
```

<details>
<summary>A</summary>

</details>

---

### Q10. How does NAT connect to routing, default gateways, and neighbor tables?

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Next:
Phase 02
Session 09

Topic:
Linux Packet Flow
```

# Linux Server Administration
## Phase 00 — Session 10
# netplan Fundamentals

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 10
Title: netplan Fundamentals
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-07-03
```

---

# Objective

Understand how Ubuntu Server stores and applies network configuration through netplan.

The goal is to distinguish:

```text
network configuration file
```

from:

```text
actual runtime network state
```

and understand how netplan connects DHCP, interfaces, systemd-networkd, and the Linux kernel network stack.

---

# Learning Summary

Ubuntu Server commonly uses netplan to declare network configuration.

A netplan file describes the desired network state. It does not directly represent the live network state by itself.

Example:

```yaml
network:
  version: 2
  ethernets:
    ens3:
      dhcp4: true
```

The important line is:

```yaml
dhcp4: true
```

This means that the interface should use DHCP to receive IPv4 configuration.

The interface name is also important.

```yaml
ens3:
  dhcp4: true
```

This tells Ubuntu which network interface should receive this configuration.

A key correction from the session:

```text
Host configures ens3
```

is not the accurate model.

The more accurate model is:

```text
Guest Ubuntu configures its own ens3 interface through netplan.
```

From the Host perspective, the same virtual NIC may appear as a Host-side interface such as:

```text
vnet0
```

From the Guest perspective, it may appear as:

```text
ens3
```

So the same virtual network path can be viewed differently depending on where it is observed.

---

# Key Concepts

- netplan
- YAML network configuration
- desired state
- runtime state
- network interface name
- `ens3`
- `dhcp4: true`
- `netplan apply`
- systemd-networkd
- Linux kernel network stack
- Host-side `vnet`
- Guest-side virtual NIC

---

# Practical Observations

## Observation 1

```text
Prediction

↓

dhcp4: true means DHCP is enabled.

↓

Observation

↓

The configuration declares that the interface should receive IPv4 configuration through DHCP.

↓

Explanation

netplan uses dhcp4: true to tell the backend network manager to request IPv4 configuration dynamically.
```

---

## Observation 2

```text
Prediction

↓

The interface name tells the Host which target to configure.

↓

Correction

↓

The interface name tells the Guest Ubuntu network configuration system which Guest-side interface to configure.

↓

Explanation

netplan runs inside the Guest. It applies configuration to interfaces visible inside the Guest, such as ens3. The Host may see the corresponding connection as vnet0 or another vnet interface.
```

---

## Observation 3

```text
Prediction

↓

Changing the configuration file does not automatically change the live network state.

↓

Observation

↓

A separate apply step is needed.

↓

Explanation

The configuration file records desired state. The actual runtime state changes when netplan applies the configuration through its backend, such as systemd-networkd.
```

---

## Observation 4

```text
Prediction

↓

systemd-networkd and the kernel network stack are closer to the real runtime network state than the YAML file.

↓

Observation

↓

The YAML file describes intended configuration, while the backend and kernel reflect active interface state.

↓

Explanation

The file is configuration data. The backend and kernel are responsible for applying and maintaining the actual network state.
```

---

## Observation 5

```text
Prediction

↓

If the wrong interface name is used, DHCP configuration will not be applied to the real NIC.

↓

Observation

↓

The real interface may not receive IP, gateway, DNS, or subnet configuration.

↓

Explanation

DHCP is not failing because the server refuses to respond. The Guest is failing to request DHCP configuration on the correct interface.
```

---

# Commands / Code

```bash
ls /etc/netplan/
```

Lists netplan configuration files.

---

```bash
cat /etc/netplan/*.yaml
```

Displays the current netplan configuration.

---

```bash
sudo netplan apply
```

Applies the declared netplan configuration to the running system.

---

```bash
ip addr
```

Shows the current runtime IP address state of network interfaces.

---

```bash
ip route
```

Shows the current runtime routing table, including the default gateway.

---

```bash
resolvectl status
```

Shows DNS resolver configuration when systemd-resolved is used.

---

```bash
networkctl status
```

Shows systemd-networkd-managed interface state.

---

# Connections

```text
DHCP
↓

Provides IP / Gateway / DNS
↓

netplan declares DHCP use
↓

systemd-networkd requests configuration
↓

kernel applies interface state
```

---

```text
Guest Ubuntu
↓

ens3

↓

Host virtual networking

↓

vnet0

↓

libvirt virtual network

↓

Physical network or NAT
```

---

```text
/etc/netplan/*.yaml
↓

desired network configuration

↓

sudo netplan apply

↓

systemd-networkd

↓

Linux kernel network stack

↓

actual interface state
```

---

# Common Misconceptions

## Incorrect

```text
The Host configures the Guest interface ens3 directly.
```

Correct:

```text
netplan runs inside the Guest Ubuntu system and configures the Guest-side interface ens3.
The Host sees the corresponding virtual network connection as a vnet interface.
```

---

## Incorrect

```text
Editing the netplan file immediately changes the active network state.
```

Correct:

```text
The file records desired state.
The active system changes after the configuration is applied.
```

---

## Incorrect

```text
The netplan YAML file is the live network state.
```

Correct:

```text
The YAML file is configuration.
The live state is visible through tools such as ip addr, ip route, networkctl, and resolvectl.
```

---

## Incorrect

```text
If the interface name is wrong, DHCP itself is broken.
```

Correct:

```text
The DHCP configuration is being applied to the wrong target or to no real target.
The correct interface may never send the expected DHCP request.
```

---

# Key Takeaways

- netplan is Ubuntu Server's network configuration declaration layer.
- `dhcp4: true` means the interface should use DHCP for IPv4 configuration.
- Interface names matter because settings must be applied to a specific network interface.
- The Guest-side interface name and Host-side interface name are different perspectives of the virtual network path.
- Editing a configuration file and changing runtime network state are separate steps.
- `netplan apply` connects the desired configuration to the running system.
- systemd-networkd and the kernel network stack are closer to the live network state than the YAML file.
- Wrong interface names can prevent IP, gateway, DNS, and subnet configuration from being applied.

---

# Review Questions

### Q1. What problem does netplan solve on Ubuntu Server?

<details>
<summary>A</summary>

</details>

---

### Q2. What does `dhcp4: true` mean in a netplan configuration?

<details>
<summary>A</summary>

</details>

---

### Q3. Why must a netplan file specify an interface name such as `ens3`?

<details>
<summary>A</summary>

</details>

---

### Q4. Why is it inaccurate to say that the Host configures the Guest interface `ens3` directly?

<details>
<summary>A</summary>

</details>

---

### Q5. What is the difference between a netplan configuration file and the live network state?

<details>
<summary>A</summary>

</details>

---

### Q6. What role does `sudo netplan apply` play?

<details>
<summary>A</summary>

</details>

---

### Q7. Complete the flow:

```text
/etc/netplan/*.yaml
↓

?
↓

systemd-networkd
↓

?
↓

actual interface state
```

<details>
<summary>A</summary>

</details>

---

### Q8. What can happen if the netplan file references the wrong interface name?

<details>
<summary>A</summary>

</details>

---

### Q9. How are `ens3` and `vnet0` related in a virtualized network environment?

<details>
<summary>A</summary>

</details>

---

### Q10. Why is it useful for a server administrator to distinguish desired configuration from runtime state?

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 00
Session 11

Topic:
systemd-networkd Observation

How Ubuntu's network backend applies and exposes runtime interface state.
```

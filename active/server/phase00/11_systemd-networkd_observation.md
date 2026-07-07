# Linux Server Administration
## Phase 00 — Session 11
# systemd-networkd Observation

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 11
Title: systemd-networkd Observation
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-07
```

---

# Objective

Understand the difference between a network configuration file and the runtime service that applies and maintains network interface state.

The goal is to distinguish:

```text
/etc/netplan/*.yaml
```

from:

```text
systemd-networkd
```

and understand why correct configuration still requires a working runtime network manager.

---

# Learning Summary

Netplan stores the desired network configuration, but it does not directly maintain the live network state.

A typical Ubuntu Server network path is:

```text
/etc/netplan/*.yaml
↓

netplan apply
↓

systemd-networkd
↓

Linux kernel network stack
↓

actual interface state
```

`systemd-networkd` is closer to the runtime side of the system. It reads generated network configuration, manages interfaces, requests DHCP configuration, and helps produce the active state visible through commands such as `networkctl`, `ip addr`, and `ip route`.

A key distinction from the session:

```text
cat /etc/netplan/*.yaml
```

shows the intended configuration.

```text
networkctl status
```

shows the currently managed network state.

A correct YAML file alone does not guarantee working networking. If `systemd-networkd` is stopped, broken, or not applying the configuration, DHCP requests may not be made and the VM may fail to receive IP, gateway, or DNS configuration.

---

# Key Concepts

- systemd-networkd
- runtime network manager
- netplan backend
- desired configuration
- runtime state
- `networkctl status`
- DHCP request execution
- kernel network stack
- service state
- interface state

---

# Practical Observations

## Observation 1

```text
Prediction

↓

systemd-networkd is closer to a runtime network service than a configuration document.

↓

Observation

↓

The netplan YAML file stores configuration, while systemd-networkd manages interface state.

↓

Explanation

A file records desired state. A runtime service applies and maintains that state in the running system.
```

---

## Observation 2

```text
Prediction

↓

networkctl status shows the current runtime network state.

↓

Observation

↓

The command can show interface state, address, gateway, and DNS information.

↓

Explanation

networkctl observes state managed by systemd-networkd. It is not simply printing the original netplan YAML file.
```

---

## Observation 3

```text
Prediction

↓

cat /etc/netplan/*.yaml and networkctl status observe different layers.

↓

Observation

↓

The first command shows declared configuration. The second command shows applied runtime status.

↓

Explanation

Troubleshooting requires checking both what the system is supposed to do and what it is actually doing.
```

---

## Observation 4

```text
Prediction

↓

The YAML file does not directly perform DHCP.

↓

Observation

↓

A runtime network manager such as systemd-networkd performs the DHCP request.

↓

Explanation

The file can declare dhcp4: true, but a running service must translate that declaration into network behavior.
```

---

## Observation 5

```text
Prediction

↓

A valid netplan file can still fail to produce network connectivity if systemd-networkd fails.

↓

Observation

↓

The intended configuration may not be reflected in the live interface state.

↓

Explanation

The configuration layer and runtime layer are separate. Failure in the runtime manager can prevent DHCP, address assignment, route configuration, and DNS setup.
```

---

# Commands / Code

```bash
cat /etc/netplan/*.yaml
```

Displays the declared netplan configuration.

---

```bash
sudo netplan apply
```

Applies the declared netplan configuration through the configured backend.

---

```bash
networkctl status
```

Shows systemd-networkd-managed runtime network state.

---

```bash
systemctl status systemd-networkd
```

Checks whether the systemd-networkd service is running.

---

```bash
journalctl -u systemd-networkd
```

Shows logs from the runtime network manager.

---

```bash
ip addr
```

Shows addresses currently assigned to interfaces.

---

```bash
ip route
```

Shows the runtime routing table.

---

```bash
resolvectl status
```

Shows DNS resolver state and configured DNS servers when systemd-resolved is in use.

---

# Connections

```text
netplan YAML
↓

desired network configuration
↓

netplan apply
↓

systemd-networkd
↓

DHCP request / address setup / route setup
↓

Linux kernel network stack
↓

actual network state
```

---

```text
Configuration file
↓

Runtime service
↓

Kernel state
↓

Network behavior
```

---

# Common Misconceptions

## Incorrect

```text
systemd-networkd is just another configuration file.
```

Correct:

```text
systemd-networkd is a runtime service that manages network interface state.
```

---

## Incorrect

```text
networkctl status shows the netplan YAML file.
```

Correct:

```text
networkctl status shows runtime network state managed by systemd-networkd.
```

---

## Incorrect

```text
If the netplan file is correct, networking must work.
```

Correct:

```text
A correct configuration still needs a working runtime manager and kernel state.
```

---

## Incorrect

```text
The YAML file directly sends DHCP requests.
```

Correct:

```text
The YAML file declares DHCP use. A runtime network service performs the DHCP behavior.
```

---

# Key Takeaways

- Netplan records desired network configuration.
- systemd-networkd manages runtime interface state.
- `cat /etc/netplan/*.yaml` and `networkctl status` observe different layers.
- DHCP behavior is performed by a runtime network manager, not by the YAML file itself.
- A correct configuration file can still fail if the runtime service is stopped or broken.
- Effective troubleshooting compares declared configuration with actual runtime state.

---

# Review Questions

### Q1. What role does systemd-networkd play in Ubuntu Server networking?

<details>
<summary>A</summary>

</details>

---

### Q2. What is the difference between `/etc/netplan/*.yaml` and `networkctl status`?

<details>
<summary>A</summary>

</details>

---

### Q3. Why is a correct netplan file not always enough to produce working networking?

<details>
<summary>A</summary>

</details>

---

### Q4. Which component is closer to the live network state: the YAML file or systemd-networkd?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does the YAML file not directly perform DHCP requests?

<details>
<summary>A</summary>

</details>

---

### Q6. What can happen if systemd-networkd fails while the netplan file is correct?

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

actual network state
```

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 00
Session 12

Topic:
SSH Administration Workflow

How SSH connects client, network, port, service, authentication, and shell into one remote administration workflow.
```

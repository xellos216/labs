# Linux Server Administration
## Phase 00 — Session 12
# SSH Administration Workflow

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 12
Title: SSH Administration Workflow
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-07
```

---

# Objective

Understand SSH as a remote administration workflow that depends on multiple layers working together.

The goal is to avoid treating SSH failure as a single problem and instead separate:

```text
client
network
port
service
authentication
shell
```

into distinct troubleshooting layers.

---

# Learning Summary

SSH stands for:

```text
Secure Shell
```

Its primary role in server administration is to connect to a remote machine's shell through an encrypted network connection.

A basic SSH connection can be modeled as:

```text
Host terminal
↓

ssh client
↓

TCP/IP network
↓

VM port 22
↓

sshd
↓

authentication
↓

remote shell
```

An IP address alone does not guarantee that SSH will work. The VM may be reachable at the IP layer while TCP port 22 is closed, `sshd` is stopped, a firewall blocks the connection, or authentication fails.

A key troubleshooting principle from the session:

```text
ssh does not work
```

should be refined into:

```text
Which layer failed first?
```

This same diagnostic approach applies beyond SSH to HTTP, databases, and other network services.

---

# Key Concepts

- SSH
- Secure Shell
- SSH client
- SSH server
- `sshd`
- TCP port 22
- listen socket
- authentication
- remote shell
- service manager
- socket state
- layered troubleshooting

---

# Practical Observations

## Observation 1

```text
Prediction

↓

SSH is a remote shell administration tool.

↓

Observation

↓

The Host runs an SSH client, and the VM must run an SSH server.

↓

Explanation

SSH connects a local terminal to a remote shell through an encrypted client-server workflow.
```

---

## Observation 2

```text
Prediction

↓

SSH failure can have many causes.

↓

Observation

↓

Possible causes include client issues, IP or route problems, port 22 problems, sshd failure, firewall rules, and authentication failure.

↓

Explanation

A failed SSH command is the visible result of a multi-layer workflow. The investigation should isolate the failed layer.
```

---

## Observation 3

```text
Prediction

↓

Having an IP address is not enough for SSH.

↓

Observation

↓

SSH also requires a listening TCP service on the target port.

↓

Explanation

IP reachability only means the host can potentially be reached. SSH requires TCP port 22 and sshd to be available.
```

---

## Observation 4

```text
Prediction

↓

systemctl and ss observe different parts of the SSH system.

↓

Observation

↓

systemctl shows service-manager state. ss shows kernel socket and port state.

↓

Explanation

Both perspectives are useful. A service may appear active, but checking the listening socket provides evidence that the expected port is actually open.
```

---

## Observation 5

```text
Prediction

↓

Good troubleshooting separates IP reachability, route, port, service, and authentication.

↓

Observation

↓

Each layer can fail independently.

↓

Explanation

Layered troubleshooting avoids assuming that SSH itself is the only possible failure source.
```

---

# Commands / Code

```bash
ssh user@VM_IP
```

Starts an SSH client connection to the VM.

---

```bash
ping VM_IP
```

Tests basic IP reachability.

---

```bash
systemctl status ssh
```

Checks the SSH service state on Ubuntu systems where the service is named `ssh`.

---

```bash
ss -tulpen | grep ':22'
```

Checks whether a process is listening on TCP port 22.

---

```bash
journalctl -u ssh
```

Shows SSH service logs on systems where the service unit is named `ssh`.

---

```bash
ip addr
```

Shows the VM's current IP address state.

---

```bash
ip route
```

Shows the route state used to reach other systems.

---

# Connections

```text
DHCP
↓

VM receives IP
↓

Host reaches VM IP
↓

TCP connects to port 22
↓

sshd accepts connection
↓

authentication succeeds
↓

remote shell opens
```

---

```text
systemctl status ssh
↓

service manager perspective
```

```text
ss -tulpen
↓

kernel socket perspective
```

---

# Common Misconceptions

## Incorrect

```text
SSH means Secure Shell Host.
```

Correct:

```text
SSH means Secure Shell.
```

---

## Incorrect

```text
If the VM has an IP address, SSH must work.
```

Correct:

```text
An IP address only supports reachability. SSH also needs route, TCP, port, service, firewall, and authentication to work.
```

---

## Incorrect

```text
If ssh fails, reinstall sshd first.
```

Correct:

```text
First identify the failed layer: reachability, route, port, service, firewall, or authentication.
```

---

## Incorrect

```text
systemctl status ssh and ss -tulpen show the same thing.
```

Correct:

```text
systemctl shows service state. ss shows socket and port state. They are complementary observations.
```

---

# Key Takeaways

- SSH is Secure Shell.
- SSH is a remote administration workflow, not just a single command.
- An SSH connection depends on client, network, TCP, port, service, authentication, and shell layers.
- IP reachability does not guarantee SSH availability.
- `systemctl` and `ss` observe different system layers.
- Troubleshooting should ask which layer failed first.

---

# Review Questions

### Q1. What does SSH stand for, and what problem does it solve?

<details>
<summary>A</summary>

</details>

---

### Q2. Why is SSH better understood as a workflow than as a single command?

<details>
<summary>A</summary>

</details>

---

### Q3. Why is an IP address alone insufficient to guarantee SSH access?

<details>
<summary>A</summary>

</details>

---

### Q4. What is the role of TCP port 22 in the SSH workflow?

<details>
<summary>A</summary>

</details>

---

### Q5. Compare `systemctl status ssh` and `ss -tulpen` as troubleshooting observations.

<details>
<summary>A</summary>

</details>

---

### Q6. What are several possible causes of `ssh user@VM_IP` failing?

<details>
<summary>A</summary>

</details>

---

### Q7. Complete the flow:

```text
Host terminal
↓

ssh client
↓

?
↓

VM port 22
↓

?
↓

authentication
↓

remote shell
```

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 00
Session 13

Topic:
Snapshots & Recovery

How snapshots provide a safe recovery point before risky server administration changes.
```

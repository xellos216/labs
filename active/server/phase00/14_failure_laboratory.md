# Linux Server Administration
## Phase 00 — Session 14
# Failure Laboratory

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 14
Title: Failure Laboratory
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-07
```

---

# Objective

Practice diagnosing server failures by separating the system into layers and identifying the first broken layer.

The goal is to turn:

```text
It does not work.
```

into:

```text
Which layer failed first?
```

---

# Learning Summary

Failure Laboratory connects the earlier Phase 00 topics into one troubleshooting model.

The relevant stack is:

```text
VM power state
↓

network configuration
↓

systemd-networkd
↓

DHCP / DNS / route
↓

TCP port 22
↓

sshd
↓

authentication
↓

shell
```

A failure at the top-level command, such as `ssh user@VM_IP`, does not prove that SSH itself is the root cause. SSH access depends on reachability, route, port state, service state, firewall behavior, and authentication.

A key correction from the session:

```text
ping success
≠
TCP / sshd / authentication success
```

`ping VM_IP` can show that IP reachability is working, but it does not prove that TCP port 22 is open or that `sshd` is accepting logins.

Another important distinction:

```text
ping 8.8.8.8 succeeds
ping google.com fails
```

suggests DNS failure rather than total network failure. SSH by direct IP can often work without DNS because no domain name needs to be resolved.

The general troubleshooting workflow is:

```text
Failure
↓

Separate layers
↓

Find last working layer
↓

Find first broken layer
↓

Recover
↓

Verify
```

---

# Key Concepts

- failure isolation
- last working layer
- first broken layer
- IP reachability
- TCP reachability
- port listening
- service state
- firewall blocking
- authentication failure
- DNS failure
- snapshot rollback
- verification

---

# Practical Observations

## Observation 1

```text
Prediction

↓

SSH failure should be diagnosed layer by layer.

↓

Observation

↓

SSH depends on network, TCP, service, firewall, authentication, and shell layers.

↓

Explanation

A single failed SSH command can be caused by many components. Reinstallation or random changes should not be the first response.
```

---

## Observation 2

```text
Prediction

↓

If ping succeeds but SSH fails, basic IP reachability works but higher layers remain suspicious.

↓

Observation

↓

TCP port 22, sshd, firewall rules, and authentication can still fail.

↓

Explanation

ICMP reachability is not the same as TCP service availability.
```

---

## Observation 3

```text
Prediction

↓

If ping and SSH both fail, investigate lower layers before SSH itself.

↓

Observation

↓

Possible causes include VM power state, wrong IP, missing DHCP lease, broken route, wrong virtual network, or firewall blocking ICMP.

↓

Explanation

If IP reachability is not confirmed, troubleshooting TCP 22 or authentication is premature.
```

---

## Observation 4

```text
Prediction

↓

systemctl status ssh running does not guarantee end-to-end SSH success.

↓

Observation

↓

The service can be running while the port, firewall, network path, or authentication still fails.

↓

Explanation

Service state is one layer of evidence, not proof that the whole workflow is healthy.
```

---

## Observation 5

```text
Prediction

↓

DNS failure does not always prevent SSH by direct IP.

↓

Observation

↓

Using ssh user@VM_IP avoids domain-name resolution.

↓

Explanation

DNS maps names to addresses. If the address is already known, SSH can often proceed without DNS.
```

---

## Observation 6

```text
Prediction

↓

Snapshots change recovery cost after deliberate failure.

↓

Observation

↓

Without a snapshot, recovery requires manual repair through console access and configuration rollback. With a snapshot, the VM can return to a known good state quickly.

↓

Explanation

Recovery design is part of failure-driven learning. The goal is not to avoid all failures, but to make them reversible and observable.
```

---

# Commands / Code

```bash
ping VM_IP
```

Tests basic IP reachability to the VM.

---

```bash
ssh user@VM_IP
```

Attempts SSH access by direct IP address.

---

```bash
systemctl status ssh
```

Checks SSH service state on Ubuntu systems where the service is named `ssh`.

---

```bash
ss -tulpen | grep ':22'
```

Checks whether the VM is listening on TCP port 22.

---

```bash
ip addr
```

Checks whether the VM has an IP address.

---

```bash
ip route
```

Checks route state and default gateway configuration.

---

```bash
resolvectl status
```

Checks DNS resolver configuration.

---

```bash
journalctl -u ssh
```

Checks SSH service logs.

---

# Connections

```text
DHCP
↓

IP address
↓

route
↓

TCP connection
↓

port 22
↓

sshd
↓

authentication
↓

shell
```

---

```text
ping succeeds
↓

IP reachability likely works
↓

TCP / SSH / authentication still need verification
```

---

```text
ping IP succeeds
ping name fails
↓

DNS is suspicious
```

---

```text
failure
↓

snapshot rollback or manual repair
↓

verification
```

---

# Common Misconceptions

## Incorrect

```text
If SSH fails, SSH itself must be broken.
```

Correct:

```text
SSH failure can result from network, route, port, firewall, service, or authentication problems.
```

---

## Incorrect

```text
If ping works, SSH must work.
```

Correct:

```text
Ping only supports a conclusion about basic IP reachability. SSH needs higher layers to work too.
```

---

## Incorrect

```text
If systemctl status ssh is running, SSH access is guaranteed.
```

Correct:

```text
The service may be running while port, firewall, route, or authentication still fails.
```

---

## Incorrect

```text
DNS failure always breaks SSH.
```

Correct:

```text
SSH by direct IP can often work without DNS because no name resolution is required.
```

---

## Incorrect

```text
Recovery means manually undoing every change.
```

Correct:

```text
Manual repair is one option. Snapshot rollback can restore a known good state faster when a snapshot exists.
```

---

# Key Takeaways

- Failure should be separated into layers before applying fixes.
- `ping` success is evidence for IP reachability, not full SSH health.
- SSH success depends on route, TCP, port listen state, sshd, firewall, authentication, and shell availability.
- Service state and socket state are different observations.
- DNS failure and IP connectivity failure are different failure modes.
- Snapshots reduce recovery cost during deliberate failure experiments.
- A reliable administrator finds the first broken layer and verifies recovery.

---

# Review Questions

### Q1. Why is it dangerous to treat `ssh failed` as a single-cause problem?

<details>
<summary>A</summary>

</details>

---

### Q2. What does `ping VM_IP` success prove, and what does it not prove?

<details>
<summary>A</summary>

</details>

---

### Q3. If both `ping VM_IP` and `ssh user@VM_IP` fail, which lower layers should be checked first?

<details>
<summary>A</summary>

</details>

---

### Q4. Why does `systemctl status ssh` showing `running` not guarantee SSH access?

<details>
<summary>A</summary>

</details>

---

### Q5. Why can SSH by direct IP often work even when DNS is broken?

<details>
<summary>A</summary>

</details>

---

### Q6. How does a snapshot change the recovery path after a deliberate network failure?

<details>
<summary>A</summary>

</details>

---

### Q7. Complete the failure investigation model:

```text
Failure
↓

?
↓

Find last working layer
↓

?
↓

Recover
↓

?
```

<details>
<summary>A</summary>

</details>

---

### Q8. Apply the model: `ping VM_IP` succeeds, but `ssh user@VM_IP` fails. Which layers remain suspicious?

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 00
Session 15

Topic:
Build Everything From Scratch

Rebuild the Phase 00 lab workflow from VM creation to networking, SSH access, snapshot safety, and failure recovery.
```

# Linux Server Administration
## Phase 00 — Session 13
# Snapshots & Recovery

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 00
Session: 13
Title: Snapshots & Recovery
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-07
```

---

# Objective

Understand how snapshots support safe experimentation and recovery in a Linux server administration lab.

The goal is to distinguish:

```text
quick rollback point
```

from:

```text
long-term backup
```

and understand why recoverability is part of system administration.

---

# Learning Summary

A snapshot is a saved recovery point that allows a VM to return to a known earlier state after a risky change.

This matters because server administration often involves changes that can break access or system behavior.

Examples include:

- network configuration changes
- SSH configuration changes
- firewall rule changes
- boot configuration changes
- package upgrades
- service configuration changes

A key model from the session:

```text
Known Good State
↓

Snapshot
↓

Risky Change
↓

Failure or Success
↓

Rollback if needed
↓

Repeat safely
```

Snapshots make failure cheaper. They allow controlled experiments where a learner can intentionally change configuration, observe failure, roll back, and try a different approach.

A snapshot is not the same as a backup.

```text
Snapshot
=
fast rollback to a recorded state
```

```text
Backup
=
separate recovery copy for loss, deletion, disk failure, or long-term preservation
```

The key difference is independence. A snapshot is often tied to the VM disk chain or the same storage system, while a backup can be stored separately and survive more severe failure modes.

---

# Key Concepts

- snapshot
- rollback
- known good state
- recovery point
- risky change
- controlled failure
- backup
- independent recovery copy
- VM state
- recovery cost

---

# Practical Observations

## Observation 1

```text
Prediction

↓

A broken netplan configuration does not mean the VM is permanently broken.

↓

Observation

↓

The access path can be broken while the VM still exists and can be repaired or rolled back.

↓

Explanation

A network configuration mistake can remove IP configuration or SSH access without destroying the whole VM.
```

---

## Observation 2

```text
Prediction

↓

A snapshot is a recovery point.

↓

Observation

↓

After a failed change, returning to the snapshot restores the earlier known state.

↓

Explanation

The snapshot records a state that can be restored instead of manually undoing every change.
```

---

## Observation 3

```text
Prediction

↓

Snapshots are useful before risky changes.

↓

Observation

↓

The same starting point can be used for multiple different experiments.

↓

Explanation

Snapshots support branching experiments: change, observe, rollback, and retry from the same known baseline.
```

---

## Observation 4

```text
Prediction

↓

Snapshots make experimentation safer.

↓

Observation

↓

Failure becomes reversible and easier to study.

↓

Explanation

The learner can intentionally create failures without turning every mistake into a long manual repair task.
```

---

## Observation 5

```text
Prediction

↓

Snapshots and backups are not identical.

↓

Observation

↓

Snapshots are fast rollback tools, while backups are independent recovery copies.

↓

Explanation

A snapshot may not protect against storage loss, deletion of the VM, or long-term disaster recovery needs. A backup is designed for broader recovery scenarios.
```

---

# Commands / Code

```bash
virsh snapshot-list VM_NAME
```

Lists snapshots for a libvirt-managed VM.

---

```bash
virsh snapshot-create-as VM_NAME snapshot-name
```

Creates a named snapshot for a VM when the VM and storage configuration support it.

---

```bash
virsh snapshot-revert VM_NAME snapshot-name
```

Reverts a VM to a previous snapshot.

---

```bash
virsh snapshot-delete VM_NAME snapshot-name
```

Deletes a VM snapshot when it is no longer needed.

---

# Connections

```text
netplan change
↓

IP lost
↓

SSH access lost
↓

snapshot rollback
↓

known good network state restored
```

---

```text
Failure-driven learning
↓

controlled breakage
↓

recovery point
↓

repeatable experiment
```

---

```text
Snapshot
↓

fast rollback
```

```text
Backup
↓

separate recovery copy
```

---

# Common Misconceptions

## Incorrect

```text
A network configuration failure means the VM is permanently broken.
```

Correct:

```text
The VM may still be recoverable through console access, manual repair, or snapshot rollback.
```

---

## Incorrect

```text
A snapshot records only text configuration files.
```

Correct:

```text
A VM snapshot may include disk state, VM configuration, memory state, or device state depending on the snapshot method.
```

---

## Incorrect

```text
Snapshots are only useful when avoiding failure.
```

Correct:

```text
Snapshots make it safer to create, observe, and recover from failure.
```

---

## Incorrect

```text
A snapshot is the same as a backup.
```

Correct:

```text
A snapshot is usually a fast rollback point. A backup is an independent recovery copy for broader failure scenarios.
```

---

# Key Takeaways

- A snapshot is a recovery point for returning to a known state.
- Snapshots reduce the cost of failed experiments.
- Risky administration changes should be preceded by a recovery plan.
- Snapshot-based labs allow controlled failure and repeated experiments.
- Snapshots and backups solve related but different recovery problems.
- A good administrator builds recoverability before making risky changes.

---

# Review Questions

### Q1. What problem does a VM snapshot solve during server administration practice?

<details>
<summary>A</summary>

</details>

---

### Q2. Why does a bad netplan change not necessarily mean the VM is permanently broken?

<details>
<summary>A</summary>

</details>

---

### Q3. Why is it useful to create a snapshot before changing networking, SSH, firewall, or boot settings?

<details>
<summary>A</summary>

</details>

---

### Q4. How does a snapshot change the learning value of failure?

<details>
<summary>A</summary>

</details>

---

### Q5. Compare snapshot rollback with manually undoing every configuration change.

<details>
<summary>A</summary>

</details>

---

### Q6. What is the difference between a snapshot and a backup?

<details>
<summary>A</summary>

</details>

---

### Q7. Complete the flow:

```text
Known Good State
↓

?
↓

Risky Change
↓

Failure
↓

?
↓

Known Good State restored
```

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 00
Session 14

Topic:
Failure Laboratory

How to intentionally reason through failures by separating layers, finding the first broken layer, recovering, and verifying the result.
```

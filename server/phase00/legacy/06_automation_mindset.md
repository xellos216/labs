# Linux Server Administration
## Phase 00 — Session 06
# Automation Mindset

## Objective

Understand:

- what automation actually means
- when automation is appropriate
- why automation reduces operational risk
- why documentation comes before automation
- how automation captures operational knowledge

---

## Common Misconception

Many beginners think:

```text
Automation
=
Avoiding manual work
```

In reality:

```text
Automation
=
Executing a verified procedure
consistently
```

Convenience is only one benefit.

Consistency is often the more important one.

---

# When Should Something Be Automated?

Good candidates usually have three characteristics:

```text
Repeatable
```

```text
Predictable
```

```text
Low decision-making
```

Example:

```bash
virsh start ubuntu-web
```

If this task is performed repeatedly with the same steps, it is a strong automation candidate.

---

# Repetition Creates Value

Suppose there are twenty virtual machines.

Manual approach:

```bash
virsh start vm1
virsh start vm2
virsh start vm3
...
```

Automation:

```bash
for vm in vm{1..20}
do
    virsh start "$vm"
done
```

As repetition increases, automation becomes more valuable.

---

# Consistency

Humans may accidentally:

- skip a step
- change the order
- mistype a command
- forget verification

A verified script performs the same procedure every time.

Mental model:

```text
Consistency
>
Speed
```

for many administrative tasks.

---

# Automation Reduces Human Error

Example procedure:

```text
1. Check service
2. Restart service
3. Verify status
4. Review logs
```

A human under pressure may perform:

```text
Restart
↓

Verify

↓

Forget logs
```

A script always follows the intended sequence.

Automation protects the procedure, not just the typing.

---

# Documentation Comes First

Suppose a service fails.

Good workflow:

```text
Investigate
↓

Understand
↓

Write recovery procedure
↓

Repeat successfully
↓

Automate
```

Poor workflow:

```text
Problem
↓

Immediately automate
```

Without understanding the process, automation can simply reproduce mistakes.

---

# Documentation vs Automation

Documentation explains:

```text
What should happen
```

Automation performs:

```text
What has already been verified
```

They complement each other.

Documentation captures knowledge.

Automation executes knowledge.

---

# Not Everything Should Be Automated

Example:

```text
Disk Full
```

Possible causes:

- log growth
- backup failure
- user data
- application bug
- malicious activity

The recovery steps may differ.

Investigation comes before automation.

Automation should only be applied to stable and repeatable procedures.

---

# Linux Administration Philosophy

A useful progression:

```text
Understand
```

↓

```text
Document
```

↓

```text
Verify
```

↓

```text
Automate
```

Automation is the final step, not the first.

---

# Core Mental Models

### Automation

```text
Verified procedure
expressed as code
```

---

### Documentation

```text
Knowledge
```

---

### Script

```text
Repeatable execution
```

---

### Good Automation

```text
Understand
↓

Document
↓

Verify
↓

Automate
```

---

### Poor Automation

```text
Do not understand
↓

Write script anyway
```

This often produces unreliable automation.

---

# Example Evolution

Single command:

```bash
virsh start ubuntu-web
```

↓

Small script:

```bash
virsh start ubuntu-web
sleep 5
virsh domstate ubuntu-web
```

↓

Operational workflow:

```text
Start VM
↓

Verify status

↓

Check network

↓

Prepare access
```

The automation now represents operational knowledge.

---

# Session Summary

```text
Automation is not primarily about convenience.
```

```text
Automation is verified operational knowledge expressed as code.
```

```text
Repeatable and predictable tasks are good automation candidates.
```

```text
Automation reduces human error through consistency.
```

```text
Documentation should come before automation.
```

```text
Not every problem should be automated.
```

```text
Understand
↓

Document
↓

Verify
↓

Automate
```

---

# QA

<details>
<summary>Q1. What characteristics make a task a good automation candidate?</summary>

A:

</details>

<details>
<summary>Q2. Why does the value of automation increase as repetition increases?</summary>

A:

</details>

<details>
<summary>Q3. Why does automation reduce operational mistakes?</summary>

A:

</details>

<details>
<summary>Q4. Why is consistency often more important than speed in system administration?</summary>

A:

</details>

<details>
<summary>Q5. Why should documentation come before automation?</summary>

A:

</details>

<details>
<summary>Q6. What is the relationship between documentation and automation?</summary>

A:

</details>

<details>
<summary>Q7. Why should not every administrative task be automated?</summary>

A:

</details>

<details>
<summary>Q8. Complete the recommended workflow:</summary>

```text
Understand
↓

?
↓

Verify
↓

Automate
```

A:

</details>

<details>
<summary>Q9. What is the difference between a script and documentation?</summary>

A:

</details>

<details>
<summary>Q10. What is the most important mindset from this session?</summary>

A:

</details>

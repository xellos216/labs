# QA Template Specification

> This document defines the standard format for review questions generated throughout the Labs project.
>
> The purpose of QA sections is to strengthen long-term retention and systems reasoning through active recall.

---

# Purpose

Review questions should help the learner:

- recall key concepts
- explain mechanisms
- connect related systems
- identify misconceptions
- verify understanding

QA sections are intended for self-review after learning, not during the primary learning session.

---

# Question Count

The number of questions should adapt to the scope of the session.

Recommended guideline:

| Session Size | Questions |
| --- | ---: |
| Small | 3–4 |
| Medium | 5–7 |
| Large | 8–10 |

Quality is preferred over quantity.

---

# QA Format

Questions should remain visible.

Only answers should use GitHub-compatible collapsible sections.

Use this format:

````markdown
### Q1. Question text

<details>
<summary>A</summary>

</details>
````

Do not wrap the question itself inside `<details>`.

Answers should remain blank unless explicitly requested otherwise.

---

# Difficulty Progression

Questions should gradually increase in difficulty.

Recommended progression:

```text
Recall

↓

Understanding

↓

Reasoning

↓

Application
```

---

# Question Categories

A balanced QA section should include several of the following categories.

## Recall

Tests memory of key concepts.

Example:

> What is ARP?

## Understanding

Tests conceptual understanding.

Example:

> Why does ARP exist?

## Comparison

Tests the ability to distinguish related concepts.

Example:

> Compare TCP and UDP.

## Observation

Relates to experiments performed during the session.

Example:

> What evidence showed that the packet reached the default gateway?

## Systems Thinking

Requires connecting multiple components.

Example:

> How does ARP support Ethernet communication?

## Application

Applies the concept to a new situation.

Example:

> What would happen if the ARP cache contained an incorrect MAC address?

---

# Question Writing Guidelines

Questions should:

- be technically precise
- have a clear objective
- focus on reasoning
- avoid ambiguity

Prefer:

> Why does the operating system perform this step?

over:

> What command did you type?

---

# Avoid

Avoid questions that test only memorization.

Poor examples:

- Which option was used?
- What was the third command?
- What filename was used?

Prefer questions about behavior and reasoning.

---

# Systems-Oriented Questions

Whenever practical, include at least one question that connects the current topic to the larger system.

Example:

```text
HTTP

↓

TCP

↓

IP

↓

Ethernet
```

Example question:

> Why must the operating system resolve a MAC address before transmitting an HTTP request?

---

# Observation-Based Questions

If the session included practical work, include questions based on observed evidence.

Example:

> Which observation confirmed that the process was running in user space?

Observation-based questions reinforce experimentation rather than memorization.

---

# Common Misconception Questions

When appropriate, include one question addressing a misconception corrected during the session.

Example:

> Why is an IP address alone insufficient to transmit an Ethernet frame?

These questions help prevent recurring misunderstandings.

---

# Example QA Section

### Q1. What problem does ARP solve?

<details>
<summary>A</summary>

</details>

---

### Q2. Why can't an Ethernet frame be sent using only an IP address?

<details>
<summary>A</summary>

</details>

---

### Q3. How does the ARP cache improve network performance?

<details>
<summary>A</summary>

</details>

---

### Q4. What observation showed that the destination MAC address had already been learned?

<details>
<summary>A</summary>

</details>

---

# Core Principle

A good QA section should measure understanding, not memory.

The learner should finish the review able to explain:

- why something exists
- how it works
- how it connects to other systems
- what evidence supports that understanding

---

# Answer Policy

For normal session archives, answers should remain blank unless explicitly
requested.

Answers may be included in:

* final review documents
* answer keys
* documents explicitly requested as self-contained study material

Existing documents are historical learning records and should not be
rewritten solely to remove answers.

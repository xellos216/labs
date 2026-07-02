# Phase 02 - Session 02
# Allow Lists and Deny Lists

## Metadata

```yaml
Roadmap: Payload Construction & Parser Reasoning
Phase: 02
Session: 02
Title: Allow Lists and Deny Lists
Status:
Review:
ArchiveVersion: 2
Date:
```

## Objective

Understand the differences between **Allow Lists** and **Deny Lists**, when each approach is appropriate, and why input validation depends on the nature of the expected input rather than a universal rule.

---

# Core Concepts

## What Is an Allow List?

An Allow List accepts **only explicitly permitted input**.

Everything else is rejected.

Example:

Allowed characters:

```text
a-z
0-9
_
```

Any character outside this set is rejected.

The philosophy is:

> "Accept only what is expected."

---

## What Is a Deny List?

A Deny List rejects **known unwanted input**.

Everything not listed is accepted.

Example:

Blocked characters:

```text
;
|
&
$
<
>
```

The philosophy is:

> "Block what is known to be dangerous."

---

# Comparing the Two Approaches

| Allow List | Deny List |
|------------|-----------|
| Defines what is allowed | Defines what is forbidden |
| Rejects everything else | Accepts everything else |
| Works well when valid input is predictable | Works when dangerous patterns are well understood |
| Easier to reason about for structured input | Risk of missing unknown or overlooked cases |

---

# Why Allow Lists Are Often Preferred

A Deny List depends on knowing every dangerous input.

If one dangerous character or pattern is forgotten, the validation may become incomplete.

An Allow List has a different mindset.

Instead of asking:

> "What should I block?"

it asks:

> "What should I allow?"

This usually produces a smaller and more predictable set of accepted inputs.

---

# Choosing the Right Strategy

The important question is **not**:

> "Which approach is always better?"

The correct question is:

> "What kind of input am I validating?"

---

## Good Candidates for Allow Lists

Examples:

- Username
- Student ID
- Postal code
- Phone number
- Product ID

These inputs have a clearly defined format.

Example:

```text
Username
↓

3–20 characters

↓

Lowercase letters
Numbers
Underscore
```

The expected input is narrow and predictable.

---

## Poor Candidates for Strict Allow Lists

Examples:

- Forum posts
- Blog comments
- Emails
- Chat messages

Users may legitimately enter:

- Multiple languages
- Punctuation
- Emojis
- Line breaks
- Symbols

Restricting these to a small character set would make normal use impossible.

---

# Mental Model

Instead of thinking:

```text
Allow List > Deny List
```

Think:

```text
Input Type
        │
        ▼
Choose Appropriate Validation Strategy
```

Input characteristics determine the validation approach.

---

# Session Summary

- Allow Lists explicitly define valid input.
- Deny Lists explicitly define invalid input.
- Allow Lists work best when acceptable input is predictable.
- Free-form text often requires broader acceptance with additional context-aware handling later.
- Input validation should be selected according to the characteristics of the data, not by following a universal rule.

---

# Key Takeaways

```text
Structured Input
        │
        ▼
Allow List

Free-form Input
        │
        ▼
Broader Validation
+
Appropriate Safe Processing
```

Always begin by asking:

> "What should valid input look like?"

---

# Review Questions

### Q1. What is the main difference between an Allow List and a Deny List?

<details>
<summary>A</summary>

</details>

---

### Q2. Why can a Deny List become incomplete over time?

<details>
<summary>A</summary>

</details>

---

### Q3. Give three examples of inputs that are good candidates for an Allow List.

<details>
<summary>A</summary>

</details>

---

### Q4. Why is a forum post or blog comment usually not a good candidate for a strict Allow List?

<details>
<summary>A</summary>

</details>

---

### Q5. Complete the sentence:

> The correct validation strategy should be chosen based on _____________________.

<details>
<summary>A</summary>

</details>

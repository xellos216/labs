# Phase 02 - Session 03
# Normalization Before Validation

## Metadata

```yaml
Roadmap: Payload Construction & Parser Reasoning
Phase: 02
Session: 03
Title: Normalization Before Validation
Status:
Review:
ArchiveVersion: 2
Date:
```

## Objective

Understand why input should be **normalized before validation**, and how processing order affects application behavior.

The key mental model is that validation should operate on the **canonical form** of the input rather than one of its many possible representations.

---

# Core Concepts

## What Is Normalization?

Normalization is the process of converting different representations of the same data into a single, consistent form.

Example:

```text
/
%2F
%2f
```

After URL decoding:

```text
/
/
/
```

Although the inputs look different, they now share the same canonical representation.

---

## Why Validation Depends on Normalization

Validation is only reliable if it examines the same representation that later components will interpret.

If validation occurs before normalization, different representations of the same input may receive different validation results.

---

# Comparing Processing Orders

## Validation Before Normalization

```text
Input
   │
   ▼
Validation
   │
   ▼
Normalization
   │
   ▼
Parser
```

Example:

```text
Input:
/      → Rejected

Input:
%2F    → Accepted

↓

URL Decode

↓

/
```

The validator and parser observe different data.

---

## Normalization Before Validation

```text
Input
   │
   ▼
Normalization
   │
   ▼
Validation
   │
   ▼
Parser
```

Example:

```text
/
%2F
%2f

↓

Normalize

↓

/
/
/

↓

Validate
```

All equivalent representations are evaluated consistently.

---

# Canonical Form

A canonical form is the normalized representation that the system ultimately interprets.

Validation should be performed against this form rather than against arbitrary user-supplied representations.

Mental model:

```text
User Input
        │
        ▼
Normalization
        │
        ▼
Canonical Form
        │
        ▼
Validation
        │
        ▼
Parser
```

---

# Why Processing Order Matters

Changing the order of processing changes what each component sees.

Example:

```text
Filter sees:

%2F

Parser sees:

/
```

The disagreement occurs because the filter examined the encoded representation while the parser examined the decoded representation.

---

# Session Summary

- Normalization converts multiple representations into one canonical form.
- Validation should occur after normalization.
- Equivalent inputs should receive equivalent validation results.
- Processing order directly affects application behavior.
- Validation should inspect the same representation that downstream components interpret.

---

# Key Takeaways

```text
Multiple Representations
        │
        ▼
Normalization
        │
        ▼
Canonical Form
        │
        ▼
Validation
        │
        ▼
Parser
```

Always ask:

> "Am I validating the original representation, or the representation the system will actually use?"

---

# Review Questions

### Q1. What is the purpose of normalization?

<details>
<summary>A</summary>

</details>

---

### Q2. Why can validation before normalization produce inconsistent results?

<details>
<summary>A</summary>

</details>

---

### Q3. What is meant by the term "canonical form"?

<details>
<summary>A</summary>

</details>

---

### Q4. Why should validation operate on the canonical form instead of the original user input?

<details>
<summary>A</summary>

</details>

---

### Q5. In the processing flow below, which component should generally come first, and why?

```text
Input
   │
   ▼
Normalization
   │
   ▼
Validation
   │
   ▼
Parser
```

<details>
<summary>A</summary>

</details>

이 문서는 **Payload Construction Roadmap**의 **Phase 02 - Session 03 (Normalization Before Validation)** 아카이브 및 복습용 문서이다.

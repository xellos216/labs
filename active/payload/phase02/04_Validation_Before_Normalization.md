---
Roadmap: Payload Construction
Phase: Phase 02 - Filter Evasion & Payload Mutation
Session: Session 04
Title: Validation Before Normalization
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-07-03
---

# Phase 02 - Session 04
# Validation Before Normalization

## Objective

Understand why validating input before normalization can produce unsafe or incorrect behavior.

This session focused on the risk that an input may appear acceptable during validation, but later change meaning during normalization before it reaches the parser.

---

## Learning Summary

Validation and normalization are separate processing stages.

If validation happens before normalization, the validator may inspect one representation while the parser receives another representation.

This creates a mismatch:

```text
Validated Form
      ≠
Interpreted Form
```

The core issue is not a specific payload string. The issue is that the input's meaning can change after validation has already approved it.

---

## Key Concepts

- Validation
- Normalization
- Canonical form
- Parser interpretation
- Processing order
- Representation mismatch
- Meaning change after validation

---

## Processing Flow

Unsafe order:

```text
Input
  ↓
Validate
  ↓
Normalize
  ↓
Parser
```

Safer order:

```text
Input
  ↓
Normalize
  ↓
Validate
  ↓
Parser
```

The safer order validates the form that the system will actually interpret.

---

## Practical Observation

### Prediction

If validation checks the original input before normalization, an input may pass validation even though normalization later transforms it into a forbidden or dangerous form.

### Example Model

Assume the application wants to block parent-directory traversal.

Validation checks for a forbidden form before normalization.

```text
Input
  ↓
Check forbidden pattern
  ↓
Pass
  ↓
Normalize
  ↓
Open File
```

A simplified example:

```text
Validation sees:
...

Normalization produces:
..

Parser sees:
..
```

### Observation

The important mismatch is:

```text
Validation Time:
Input appears acceptable

Interpretation Time:
Input has changed meaning
```

### Explanation

Validation before normalization is risky because the input can be approved in one representation, then transformed into another representation that has a different meaning.

The validator and parser are no longer reasoning about the same data.

---

## Mental Model

```text
Bad Model:

Input
  ↓
Validate one representation
  ↓
Normalize into another representation
  ↓
Parser interprets changed meaning
```

```text
Better Model:

Input
  ↓
Normalize to canonical form
  ↓
Validate canonical form
  ↓
Parser interprets validated form
```

The key requirement is:

```text
Validated meaning
=
Interpreted meaning
```

---

## Common Misconception

### Misconception

If the input passes validation, it must be safe for later processing.

### Correction

Passing validation only means the input satisfied the validator at that stage.

If another processing step later changes the input, the parser may receive a different form from the one that was validated.

---

## Connection to Session 03

Session 03 showed why normalization should happen before validation.

Example:

```text
%2F
  ↓
URL Decode
  ↓
/
```

Session 04 showed the opposite failure mode:

```text
Validate
  ↓
Normalize
  ↓
Meaning changes after validation
```

Both sessions lead to the same principle:

```text
Validate the final interpreted form, not an earlier representation.
```

---

## Key Takeaways

- Validation before normalization can produce inconsistent or unsafe results.
- The validator and parser must operate on the same representation.
- Normalization can change the meaning of input.
- Validation should generally happen after converting input into canonical form.
- The important question is not "Was this input checked?" but "Was the final interpreted form checked?"

---

## Review Questions

### Q1. What is validation?

<details>
<summary>A</summary>

</details>

---

### Q2. What is normalization?

<details>
<summary>A</summary>

</details>

---

### Q3. Why can validation before normalization be unsafe?

<details>
<summary>A</summary>

</details>

---

### Q4. What does this mismatch mean?

```text
Validated Form
≠
Interpreted Form
```

<details>
<summary>A</summary>

</details>

---

### Q5. Which processing order is generally safer, and why?

```text
A. Input → Validate → Normalize → Parser

B. Input → Normalize → Validate → Parser
```

<details>
<summary>A</summary>

</details>

---

### Q6. Complete the sentence:

Validation Before Normalization is risky because validation may finish before the input's __________________ changes.

<details>
<summary>A</summary>

</details>

---

## Next Session

```text
Next:
Phase 02
Session 05

Topic:
Separator Constraints
```

# Phase 02 - Session 01
# Filters and Parsers Are Different Systems

## Objective

Understand that an **input filter** and a **parser** are different components with different responsibilities.

The key mental model is that a filter decides **whether an input is allowed**, while a parser decides **what that input actually means**.

---

# Core Concepts

## A Filter Does Not Execute Input

A filter only evaluates an incoming string according to predefined rules.

Typical examples:

- Block specific characters
- Block specific words
- Allow only certain patterns
- Reject overly long input

The filter never determines the final meaning of the input.

---

## A Parser Interprets Input

After the filter allows an input to pass, the parser analyzes it according to the language or grammar it understands.

Examples:

- Shell parser
- SQL parser
- HTML parser
- JSON parser
- URL parser

The parser is responsible for transforming characters into meaningful structures.

---

## They Solve Different Problems

```text
Filter
↓

"Should this input be accepted?"

Parser
↓

"What does this input mean?"
```

These are separate questions handled by separate systems.

---

# Processing Flow

A simplified data flow:

```text
User Input
      │
      ▼
Filter
      │
      ▼
Parser
      │
      ▼
Execution / Data Access
      │
      ▼
Observable Result
```

Understanding where a behavior changes requires identifying **which stage** caused the change.

---

# Why This Matters

A filter may consider two inputs different because their characters differ.

A parser may consider those same inputs equivalent because they produce the same parsed structure.

Likewise:

- A filter may reject an input that the parser could have handled safely.
- A filter may accept an input whose meaning is different from what the filter designer expected.

The important lesson is **not** that filters are inherently bad, but that filters and parsers operate using different models.

---

# Mental Model

Think of the filter as a security guard checking what is written on a package.

Think of the parser as the worker who opens the package and determines what is actually inside.

Both inspect the same object, but they answer different questions.

---

# Session Summary

- Filters and parsers are independent components.
- Filters decide whether an input is accepted.
- Parsers determine the meaning of accepted input.
- Security reasoning begins by identifying each processing stage instead of treating the application as a single black box.
- Always model the complete path from input to interpretation.

---

# Key Takeaways

```text
Input
   │
   ▼
Filter
(accept / reject)
   │
   ▼
Parser
(assign meaning)
   │
   ▼
Behavior
```

Never confuse:

- **Filtering** with **Parsing**
- **Characters** with **Meaning**
- **Acceptance** with **Interpretation**

---

# QA

## Q1. What is the primary responsibility of a filter?

<details>
<summary>Answer</summary>

</details>

---

## Q2. What is the primary responsibility of a parser?

<details>
<summary>Answer</summary>

</details>

---

## Q3. Why can a filter and a parser disagree about the same input?

<details>
<summary>Answer</summary>

</details>

---

## Q4. Complete the processing pipeline:

`Input → ______ → ______ → Behavior`

<details>
<summary>Answer</summary>

</details>

---

## Q5. Why is it important to distinguish "acceptance" from "interpretation" when analyzing application behavior?

<details>
<summary>Answer</summary>

</details>

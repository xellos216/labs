# Filter Model Fundamentals

## Goal

Understand why filters fail.

The target is not bypass strings.

The target is reasoning about:

```text
filter
↓
normalization
↓
parser
↓
execution
```

---

# Core Model

Whenever input is processed, ask:

```text
What does the filter see?

What does the parser see?

What actually executes?
```

These three views are often different.

---

# Filter vs Parser

A filter examines text.

A parser interprets text.

Example:

```text
Input:
cat /etc/passwd
```

Filter view:

```text
"cat /etc/passwd"
```

Parser view:

```text
command: cat
argument: /etc/passwd
```

Execution view:

```text
cat reads the file
```

Important:

```text
filter
≠
parser
```

A filter may block text that looks dangerous.

A parser only cares about what the syntax means.

---

# Blacklist Thinking

Many filters use:

```text
if "cat" exists
→ block
```

This is a blacklist.

The filter assumes:

```text
text
=
behavior
```

But parsers do not work that way.

A parser only sees the final interpreted form.

---

# Normalization

Systems often transform data before parsing.

Examples:

```text
URL decoding
character conversion
case conversion
whitespace normalization
```

Example:

```text
Input:
%20
```

After normalization:

```text
(space)
```

Question:

```text
What does the filter inspect?

Before normalization?

Or after normalization?
```

This question becomes critical in payload reasoning.

---

# Multiple Interpretations

A single input may have multiple meanings.

Example:

```text
user input
↓
web server
↓
application
↓
shell
```

Each layer may interpret data differently.

Example:

```text
%20
```

Web layer:

```text
space
```

Shell layer:

```text
argument separator
```

Same bytes.

Different interpretations.

---

# Parser Mismatch

Parser mismatch occurs when:

```text
filter understanding
≠
parser understanding
```

Example model:

```text
Filter:
"Looks safe."

Parser:
"Looks executable."
```

This difference creates opportunities for payload mutation.

---

# Observation Exercise

Consider:

```text
Filter blocks:
cat
```

Input:

```text
cat file.txt
```

Question:

```text
What does the filter see?

What does the parser see?

What executes?
```

---

Consider:

```text
Input
↓
normalization
↓
filter
↓
parser
```

Question:

```text
How might this behave differently from:

Input
↓
filter
↓
normalization
↓
parser
```

Do not think about bypasses.

Think about processing order.

---

# Mental Checklist

Whenever you encounter a filter:

```text
1. What text is inspected?

2. Does normalization happen?

3. Which parser executes later?

4. Do filter and parser agree?

5. What finally executes?
```

---

# Review

Core ideas:

```text
filter
≠
parser
```

```text
text
≠
behavior
```

```text
normalization changes meaning
```

```text
multiple layers may interpret differently
```

```text
filter/parser mismatch
creates mutation opportunities
```

---

# QA

**Q1.**

What is the difference between a filter and a parser?

<details>
<summary><strong>A1.</strong></summary>
A filter examines text

A parser interprets the text and assigns meaning to it</details>

---

**Q2.**

Why is the assumption below often incorrect?

```text
text
=
behavior
```

<details>
<summary><strong>A2.</strong></summary>
The same text can be interpreted differently after normalization and parsing.

Therefore text itself does not directly determine behavior.</details>

---

**Q3.**

What is normalization?

Give two examples.

<details>
<summary><strong>A3.</strong></summary>
Normalization is the process of transforming input into a standard form before parsing.

- URL decoding
- case conversion
- whitespace normalization</details>

---

**Q4.**

Why can the same input have different meanings across processing layers?

<details>
<summary><strong>A4.</strong></summary>

Because each processing layer may apply different interpretation rules to the same input.</details>

---

**Q5.**

What is parser mismatch?

<details>
<summary><strong>A5.</strong></summary>

filter understanding != parser understanding</details>

---

**Q6.**

Why is processing order important?

Consider:

```text
Input
↓
filter
↓
normalization
↓
parser
```

vs

```text
Input
↓
normalization
↓
filter
↓
parser
```

<details>
<summary><strong>A6.</strong></summary>

The filter may inspect different data depending on the processing order.</details>

---

**Q7.**

When analyzing a filter, what are the five questions from the Mental Checklist?

<details>
<summary><strong>A7.</strong></summary>
1. What text is inspected?
2. Does normalization happen?
3. Which parser executes later?
4. Do filter and parser agree?
5. What finally executes?</details>

---

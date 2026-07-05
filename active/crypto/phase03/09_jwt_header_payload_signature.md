# Session 09 — JWT Header, Payload and Signature

## Metadata

```yaml
Roadmap: Cryptography
Phase: 03
Session: 09
Title: JWT Header, Payload and Signature
Status:
Review:
ArchiveVersion: 2
Date:
```

## Core Concept

Real-world tokens often contain:

- nested wrappers
- structured segments
- semantic boundaries
- layered metadata

Important skill:

```text
distinguish structure layers from wrapper layers
```

---

# Structure Layer vs Wrapper Layer

Example:

```text
header.payload.signature
```

This is a:

```text
structure layer
```

Example:

```python
base64.b64encode(
    b'header.payload.signature'
)
```

This creates:

```text
wrapper layer
```

---

# Important Observation

Important distinction:

```text
delimiter visible
!=
outermost layer
```

Sometimes:

- delimiters are directly visible
- sometimes wrappers hide them

---

# Controlled Recursive Peeling

Bad workflow:

```text
decode until it crashes
```

Good workflow:

```text
observe
→ fingerprint
→ peel ONE layer
→ re-classify semantic state
→ continue carefully
```

---

# Segment Semantics

Example:

```text
header.payload.signature
```

Segments may represent:

- metadata
- payload
- integrity/authentication data

Important idea:

```text
different segments
can have different semantic roles
```

---

# Fingerprinting

Important clues:

## Structure clues

```text
.
:
{
}
```

---

## Wrapper clues

```text
hex alphabet
base64 alphabet
printable-safe encoding
```

---

# Semantic State Tracking

Always ask:

```text
What semantic layer am I observing?
```

Possible states:

- raw bytes
- JSON bytes
- structured token
- base64 wrapper
- hex wrapper
- nested wrapper

---

# Real-world Relevance

Real systems often use:

- JWT-like structures
- API tokens
- metadata segments
- transport wrappers
- nested printable layers

Many practical problems become:

```text
structure + semantic layer tracing
```

# Review Questions

## Step 1 — Segment Meaning Observation

Inspect the following tokens.

```python
A = b'header.payload.signature'
B = b'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZ3Vlc3QifQ.sig'
C = b'ZXlKaGJHY2lPaUpJVXpJMU5pU2o5LmV5SjFjMlZ5SWpvaVoyVmxjM1FpZlEuc2ln'
```

### Q1. What does each value look like?

- plaintext structure
- JWT-like structure
- base64 wrapper
- nested wrapper

<details>
<summary>A</summary>

A = JWT-like structure

B = JWT-like structure

C = base64 wrapper

</details>

---

### Q2. Which values directly expose semantic segment boundaries?

<details>
<summary>A</summary>

A, B

</details>

---

### Q3. Which value appears to wrap a JWT-like structure?

<details>
<summary>A</summary>

B = structure visible

C = wrapper around structure

</details>

## Step 2 — Segment Semantics

Analyze the following structure.

```text
header.payload.signature
```

### Q4. Why can each segment have a different semantic meaning?

<details>
<summary>A</summary>

header = metadata

payload = actual data

signature = integrity / authentication

</details>

---

### Q5. Why is the `.` delimiter an important fingerprint?

<details>
<summary>A</summary>

semantic boundary clue

</details>

---

### Q6. Why can separate wrappers be applied to individual segments?

<details>
<summary>A</summary>

Because each segment may have an independent semantic role.

</details>

## Step 3 — Controlled Recursive Peeling

Inspect the following token.

```python
token = b'ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKemRXSWlPaUpoWkcxcGJpSjkuYzJsbg=='
```

### Q7. What does the current outermost layer look like?

<details>
<summary>A</summary>

base64 wrapper

</details>

---

### Q8. What should be inspected after the first peel?

<details>
<summary>A</summary>

JSON-like, JWT-like, fingerfrint, hex-str-like, ...

</details>

---

### Q9. Why should fingerprinting be repeated immediately after peeling?

<details>
<summary>A</summary>

Because the result may contain additional layers.

</details>

---

### Q10. Why should recursive decoding not be repeated blindly?

<details>
<summary>A</summary>

Because the current transformation must be identified before choosing the
matching reversal operation.

</details>

## Step 4 — Semantic State Tracking

Infer the semantic state of each value.

```python
import base64

x = b'{"role":"guest"}'

a = base64.b64encode(x)
b = b'header.' + a + b'.signature'
c = base64.b64encode(b)
```

### Q11. What is the semantic state of `a`?

<details>
<summary>A</summary>

base64 wrapper

</details>

---

### Q12. What is the semantic state of `b`?

<details>
<summary>A</summary>

JWT-like-structure token

</details>

---

### Q13. What is the semantic state of `c`?

<details>
<summary>A</summary>

JWT-structure in base64 wrpper

</details>

---

### Q14. At which layer is the delimiter directly visible?

<details>
<summary>A</summary>

b

</details>

## Step 5 — Structure Versus Wrapper

Identify the values with structural fingerprints.

```python
A = b'header.payload.signature'
B = b'ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKemRXSWlPaUpvYjIxbkluMC5zaWc='
D = b'91af23de'
```

### Q15. Which value directly exposes a JWT-like structure?

<details>
<summary>A</summary>

A

</details>

---

### Q16. Which value likely wraps a JWT-like structure?

<details>
<summary>A</summary>

Most likely `B`.

</details>

---

### Q17. Why must wrapper and structure layers be analyzed separately?

<details>
<summary>A</summary>

Wrappers provide transport-safe representation, while structures organize
semantic content.

</details>

## Mini Task

Write an analyzer with the following features.

For the input token:

- print the original value and type
- detect printable, hex-like, and Base64-like forms
- detect delimiters and print the segment count
- peel one layer
- inspect delimiters and segments again
- reclassify the semantic state

Important:

Goal:

```text
controlled recursive peeling
```

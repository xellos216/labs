# Session 10 — Token Roles and Claims

## Metadata

```yaml
Roadmap: Cryptography
Phase: 03
Session: 10
Title: Token Roles and Claims
Status:
Review:
ArchiveVersion: 2
Date:
```

## Core Concept

Real-world tokens are not just wrappers.

Different segments often have:

- different semantic roles
- different meanings
- different security purposes

Important skill:

```text
reason about semantic purpose
not only encoding layer
```

---

# Structure vs Semantic Role

Example:

```text
header.payload.signature
```

Structure layer:

- delimiter-separated segments

Semantic roles:

- header → metadata/configuration
- payload → actual data
- signature → integrity/authentication

Important distinction:

```text
structure
!=
semantic purpose
```

---

# Metadata Fingerprinting

Metadata often contains:

- algorithm info
- timestamps
- configuration
- token type
- expiration info

Examples:

```json
{"alg":"HS256"}
{"exp":1730000000}
{"iat":1720000000}
```

---

# Payload Fingerprinting

Payload often contains:

- user info
- permissions
- role
- session data

Examples:

```json
{"user":"guest"}
{"role":"admin"}
```

---

# Integrity / Authentication Segments

Signature-like segments often:

- look noisy
- may not be JSON
- may not be human-readable
- exist for integrity/authentication

Important:

```text
not every segment
is semantic payload
```

---

# Controlled Recursive Analysis

Good workflow:

```text
observe
→ identify wrapper layer
→ peel one layer
→ identify structure
→ identify semantic roles
→ continue carefully
```

Bad workflow:

```text
blind decode recursion
```

---

# Important Mental Model

Always ask:

```text
What is the purpose
of this segment?
```

Possible answers:

- metadata
- payload
- integrity
- transport wrapper
- nested structure

---

# Real-world Relevance

Real systems often contain:

- auth metadata
- expiration timestamps
- role information
- integrity signatures
- transport-safe wrappers

Many practical problems become:

```text
semantic role tracing
+
layer tracing
```

# Review Questions

## Step 1 — Segment Role Observation

Inspect the following tokens.

```python
A = b'header.payload.signature'
B = b'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.sig'
C = b'eyJ0eXAiOiJKV1QifQ.eyJyb2xlIjoiZ3Vlc3QifQ.signature'
```

### Q1. Which semantic role is each segment likely to have?

<details>
<summary>A</summary>

header -> metadata/configuration

payload -> actual data

signature -> integrity/authentication

</details>

---

### Q2. Which segments look like metadata?

<details>
<summary>A</summary>

eyJhbGciOiJIUzI1NiJ9

eyJ0eXAiOiJKV1QifQ

</details>

---

### Q3. Which segments look like application payloads?

<details>
<summary>A</summary>

eyJ1c2VyIjoiYWRtaW4ifQ

eyJyb2xlIjoiZ3Vlc3QifQ

</details>

---

### Q4. Why does the signature segment differ from the semantic payload?

<details>
<summary>A</summary>

It likely contains integrity or authentication data rather than application
data.

</details>

## Step 2 — Metadata Fingerprinting

Inspect the following values.

```python
A = b'{"alg":"HS256"}'
B = b'{"role":"admin"}'
C = b'{"exp":1730000000}'
D = b'{"iat":1720000000}'
```

### Q5. Which values look like configuration or metadata?

<details>
<summary>A</summary>

A, C, D

</details>

---

### Q6. Which value looks like a user payload?

<details>
<summary>A</summary>

B

</details>

---

### Q7. Why are timestamp-like fields likely to serve a metadata role?

<details>
<summary>A</summary>

Because timestamps commonly control token state, issuance, or expiration.

</details>

## Step 3 — Wrapper Versus Semantic Role

Analyze the following structure.

```text
base64(header).base64(payload).signature
```

### Q8. Why can the header and payload be analyzed separately?

<details>
<summary>A</summary>

Because they have different semantic roles.

</details>

---

### Q9. Why might the payload change while the header remains unchanged?

<details>
<summary>A</summary>

Because configuration metadata may remain stable while application data
changes.

</details>

---

### Q10. Why must structure and semantic role be distinguished?

<details>
<summary>A</summary>

Because a value's shape and its actual purpose are separate properties.

</details>

## Step 4 — Controlled Analysis

Inspect the following token.

```python
token = b'ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKeWIyeGxJam9pWjNWbGMzUWlmUS5zaWduYXR1cmU='
```

### Q11. What does the outermost layer look like?

<details>
<summary>A</summary>

base64 wrapper

</details>

---

### Q12. What should be inspected first after peeling one layer?

<details>
<summary>A</summary>

delimiter, segment count, JWT-like structure, segment semantic role

</details>

---

### Q13. Why is payload fingerprinting important?

<details>
<summary>A</summary>

Because the payload usually contains the application data.

</details>

---

### Q14. Why is structure recognition alone insufficient?

<details>
<summary>A</summary>

Recognizing structure does not establish semantic meaning.

</details>

## Step 5 — Semantic State Classification

Classify the following values by semantic role.

```python
A = b'{"alg":"HS256"}'
B = b'{"user":"guest"}'
C = b'signature'
D = b'eyJ1c2VyIjoiZ3Vlc3QifQ=='
E = b'header.payload.signature'
```

Possible classifications:

- metadata
- payload
- integrity/authentication
- wrapper
- structure layer

### Q15. Semantic role of `A`:

<details>
<summary>A</summary>

metadata

</details>

---

### Q16. Semantic role of `B`:

<details>
<summary>A</summary>

payload

</details>

---

### Q17. Semantic role of `C`:

<details>
<summary>A</summary>

Integrity / authentication

</details>

---

### Q18. Semantic role of `D`:

<details>
<summary>A</summary>

wrapper

</details>

---

### Q19. Semantic role of `E`:

<details>
<summary>A</summary>

structure layer

</details>

## Mini Task

Write an analyzer with the following features.

For the input token:

- detect printable, hexadecimal, and Base64-like forms
- analyze delimiters and count segments
- peel ONE layer
- infer each segment's semantic role:
  - metadata?
  - payload?
  - signature?
  - wrapper?
- detect JSON-like content and timestamp-like fields

Important:

Goal:

```text
semantic role reasoning
```

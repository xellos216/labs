# Session 14 — Tampering and Verification State

## Metadata

```yaml
Roadmap: Cryptography
Phase: 03
Session: 14
Title: Tampering and Verification State
Status:
Review:
ArchiveVersion: 2
Date:
```

## Core Concept

Real-world token analysis is not only about:

- decoding
- wrappers
- structures
- semantic roles

Important skill:

```text
reason about security boundaries
```

---

# Readable vs Valid

Important distinctions:

```text
readable
!=
trusted

modifiable
!=
valid after modification
```

Readable:

- content observable

Valid:

- integrity verification passed
- accepted by verifier/server

---

# Tampering & Verification

Example:

```text
payload modified
↓
signature unchanged
↓
verification failure
↓
token rejected
```

Important idea:

```text
modification capability
does not imply
verification capability
```

---

# Integrity Verification

Integrity mechanisms often use:

- HMAC
- signatures
- MAC/authentication fields

Purpose:

```text
detect unauthorized modification
```

---

# Authentication Connection

Sometimes:

```text
valid signature
→ proof of authorized generation
```

Meaning:

- integrity
- authenticity
- trust

can become connected concepts.

---

# Semantic Role vs Security Role

Example:

```text
header.payload.signature
```

Possible reasoning:

- header → metadata/security configuration
- payload → application data
- signature → integrity/authentication

---

# Controlled Recursive Analysis

Good workflow:

```text
observe
→ fingerprint
→ peel carefully
→ identify semantic roles
→ identify trust boundaries
→ reason about verification
```

Bad workflow:

```text
decode only
```

---

# Important Mental Model

Always separate:

```text
representation
structure
semantic role
trust property
verification state
security boundary
```

These are different reasoning layers.

---

# Real-world Relevance

Real systems often separate:

- readable payload
- metadata
- integrity verification
- authentication logic
- transport wrappers

Many practical problems become:

```text
semantic reasoning
+
verification reasoning
+
security boundary analysis
```

# Review Questions

## Step 1 — Modification Versus Verification

Analyze the following situation.

```text
original payload:
{"role":"user"}

modified payload:
{"role":"admin"}

signature:
unchanged
```

### Q1. Why is the payload still readable?

<details>
<summary>A</summary>

Because modification does not prevent the JSON or text from being parsed and
observed.

</details>

---

### Q2. Why does modification not immediately imply privilege escalation?

<details>
<summary>A</summary>

Modification does not imply validity after modification.

</details>

---

### Q3. Why is a signature mismatch likely?

<details>
<summary>A</summary>

The payload changed while the signature did not, so the signature no longer
matches the signed content.

</details>

---

### Q4. Why does integrity verification act as a security boundary?

<details>
<summary>A</summary>

Because it separates data that satisfies authenticity and integrity checks
from data that does not.

</details>

## Step 2 — Verification Failure Reasoning

Analyze the following flow.

```text
payload modified
→ signature verification
→ failed
→ token rejected
```

### Q5. Why can the server reject the token?

<details>
<summary>A</summary>

signature verification failure

</details>

---

### Q6. Why does successful JSON parsing not imply successful authentication?

<details>
<summary>A</summary>

An invalid signature provides no proof of integrity or authorized issuance.

</details>

---

### Q7. Why must the semantic payload and integrity segment be analyzed separately?

<details>
<summary>A</summary>

Because they perform different roles.

</details>

---

### Q8. Why is trust reasoning higher-level than decoding?

<details>
<summary>A</summary>

Decoding makes data readable; trust reasoning determines whether it should be
accepted.

</details>

## Step 3 — Semantic Role Versus Security Role

Inspect the following values.

```python
A = b'{"alg":"HS256"}'
B = b'{"user":"guest"}'
C = b'{"exp":1730000000}'
D = b'signature'
```

### Q9. Which values look like metadata or security configuration?

<details>
<summary>A</summary>

A, C

</details>

---

### Q10. Which value looks like application payload?

<details>
<summary>A</summary>

B

</details>

---

### Q11. Which value looks related to integrity or authentication?

<details>
<summary>A</summary>

D

</details>

---

### Q12. Why can the `exp` field affect security or trust decisions?

<details>
<summary>A</summary>

Because it defines the token's validity period.

</details>

## Step 4 — Controlled Recursive Analysis

Inspect the following token.

```python
token = b'ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKeWIyeGxJam9pWjNWbGMzUWlmUS5jMmxuYm1GMGRYSmw='
```

### Q13. What does the outermost layer look like?

<details>
<summary>A</summary>

base64 wrapper

</details>

---

### Q14. What should be inspected first after peeling one layer?

<details>
<summary>A</summary>

Delimiters, JSON-like content, JWT-like structure, and segment boundaries.

</details>

---

### Q15. Why is semantic-role inference needed for each segment?

<details>
<summary>A</summary>

Because different segments serve different purposes.

</details>

---

### Q16. Why does structure recognition not complete security reasoning?

<details>
<summary>A</summary>

Because recognizing a token's shape does not establish how it is verified or
trusted.

</details>

## Step 5 — Security Boundary Reasoning

Consider the following situation.

```text
An attacker modified the payload but does not know the secret key.
```

### Q17. Why is payload modification alone insufficient to create a valid token?

<details>
<summary>A</summary>

Because the attacker cannot generate a matching valid signature without the
required secret.

</details>

---

### Q18. Why is signature-generation capability important?

<details>
<summary>A</summary>

Because a modified payload must be paired with a valid signature.

Without the secret key, an attacker may edit the payload, but cannot generate a signature that matches the modified content.

</details>

---

### Q19. Why can integrity verification be connected to authentication?

<details>
<summary>A</summary>

Because valid authentication data can prove generation by a party possessing
the required secret or private key.

</details>

---

### Q20. Why must visibility, modification, and verification capability be distinguished?

<details>
<summary>A</summary>

Because each capability has different security implications.

</details>

## Mini Task

Write an analyzer with the following features.

For the input token:

- detect printable, hexadecimal, and Base64-like forms
- analyze delimiters and count segments
- peel ONE layer
- detect JSON-like content and timestamp-like fields
- infer metadata, payload, and signature roles
- distinguish readable, modifiable, trusted, and verifiable states
- explain integrity and authentication reasoning

Important:

Goal:

```text
security boundary reasoning
```

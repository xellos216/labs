# Session 16 — Phase Review Lab — Reconstructing a Web Token Flow

## Metadata

```yaml
Roadmap: Cryptography
Phase: 03
Session: 16
Title: Phase Review Lab — Reconstructing a Web Token Flow
Status:
Review:
ArchiveVersion: 2
Date:
```

## Goal

The goal was not merely to learn decoding functions. It was to distinguish:

```text
what is known
what is inferred
what remains unknown
```

Use this analysis pipeline:

```text
representation
-> structure
-> semantic role
-> capability
-> verification state
```

## Core Distinctions

```text
representation != semantic role
semantic role != capability
capability != verification state

readable != trusted
modifiable != valid after modification
signature present != verification passed
```

# Review Questions

## Step 1 — Complete Pipeline

### Q1. What does each analysis layer describe?

<details>
<summary>A</summary>

Representation describes the visible form; structure describes organization;
semantic role describes purpose; capability describes possible actions; and
verification state describes the result of security checks.

</details>

---

### Q2. Why are representation and semantic role different?

<details>
<summary>A</summary>

Representation describes appearance, while semantic role describes purpose.

</details>

---

### Q3. Why are semantic role and capability different?

<details>
<summary>A</summary>

A role belongs to data; a capability belongs to an actor or process.

</details>

---

### Q4. Why are capability and verification state different?

<details>
<summary>A</summary>

The ability to attempt an action does not establish its result.

</details>

---

## Step 2 — Classification Drill

### Q5. Which items are representations?

<details>
<summary>A</summary>

Base64 wrapper and hexadecimal wrapper.

</details>

---

### Q6. Which items describe structure?

<details>
<summary>A</summary>

JWT-like organization, segment count, and delimiters.

</details>

---

### Q7. Which items are semantic roles?

<details>
<summary>A</summary>

Metadata, payload, and signature.

</details>

---

### Q8. Which items are capabilities?

<details>
<summary>A</summary>

Observation, modification, and verification.

</details>

---

### Q9. Which items are verification states?

<details>
<summary>A</summary>

Trusted, untrusted, unknown, failed, and passed.

</details>

---

## Step 3 — Integrated Token Analysis

```python
token = (
    b"eyJhbGciOiJIUzI1NiJ9."
    b"eyJ1c2VyIjoiZ3Vlc3QiLCJyb2xlIjoicmVhZGVyIn0."
    b"c2lnbmF0dXJl"
)
```

### Q10. What is the representation?

<details>
<summary>A</summary>

Printable Base64-like segments.

</details>

---

### Q11. What is the structure?

<details>
<summary>A</summary>

A three-segment, dot-delimited JWT-like structure.

</details>

---

### Q12. What are the likely semantic roles?

<details>
<summary>A</summary>

Segment 0 is header-like metadata, segment 1 is claims-like payload, and
segment 2 is signature-like integrity data.

</details>

---

### Q13. Is the verification state known?

<details>
<summary>A</summary>

No. It remains unknown until verification is performed.

</details>

---

## Step 4 — Common Mistakes

### Q14. Why is `readable = trusted` wrong?

<details>
<summary>A</summary>

Readable content may be forged or modified.

</details>

---

### Q15. Why is `payload = capability` wrong?

<details>
<summary>A</summary>

Payload is a semantic role; capability describes what an actor can do.

</details>

---

### Q16. Why is `signature exists = verification passed` wrong?

<details>
<summary>A</summary>

The signature may be invalid and has not necessarily been checked.

</details>

---

### Q17. Why is `modifiable = valid after modification` wrong?

<details>
<summary>A</summary>

Modification can invalidate authentication data.

</details>

---

## Step 5 — Final Mental Model

### Q18. What should happen first when a new token is observed?

<details>
<summary>A</summary>

Fingerprint its representation and visible structure.

</details>

---

### Q19. Why peel only one layer before inspecting again?

<details>
<summary>A</summary>

Each peel can reveal a new semantic state requiring a different next step.

</details>

---

### Q20. Why does verification state come last?

<details>
<summary>A</summary>

The relevant representation, structure, roles, algorithm, and key context
must be known before a trust decision can be made.

</details>

---

### Q21. Summarize Phase 01 in one sentence.

<details>
<summary>A</summary>

Track each layer, separate purpose from capability, and never infer trust
without verification.

</details>

## Final Mini Task

Analyze one token and report:

```text
representation:
structure:
semantic roles:
capabilities:
verification state:
security reasoning:
```

The objective is accurate classification of each observation, not merely
producing decoded output.

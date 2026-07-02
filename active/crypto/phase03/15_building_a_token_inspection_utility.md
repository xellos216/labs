# Session 15 — Building a Token Inspection Utility

## Metadata

```yaml
Roadmap: Cryptography
Phase: 03
Session: 15
Title: Building a Token Inspection Utility
Status:
Review:
ArchiveVersion: 2
Date:
```

## Core Concept

Phase 01 is about separating what is observed, inferred, and still unknown.

```text
representation
-> structure
-> semantic role
-> capability
-> verification state
```

| Layer | Main question | Examples |
|---|---|---|
| Representation | How is it currently represented? | Base64, hex, bytes |
| Structure | How is it organized? | delimiters, segments, JSON |
| Semantic role | What does each part mean? | metadata, payload, signature |
| Capability | What can an actor do? | observe, modify, verify |
| Verification state | What is the check result? | passed, failed, unknown |

```text
readable != modifiable != verifiable != trusted
```

# Review Questions

## Step 1 — Analysis Layers

### Q1. Which layer is observed first?

<details>
<summary>A</summary>

Representation.

</details>

---

### Q2. Where do delimiters and segment counts belong?

<details>
<summary>A</summary>

Structure.

</details>

---

### Q3. Where do metadata, payload, and signature belong?

<details>
<summary>A</summary>

Semantic role.

</details>

---

### Q4. Where do trusted and untrusted belong?

<details>
<summary>A</summary>

Verification state.

</details>

---

## Step 2 — Integrated Reasoning

```python
token = (
    b"eyJhbGciOiJIUzI1NiJ9."
    b"eyJ1c2VyIjoiZ3Vlc3QiLCJyb2xlIjoicmVhZGVyIn0."
    b"c2lnbmF0dXJl"
)
```

### Q5. What is inspected from the representation perspective?

<details>
<summary>A</summary>

Whether each visible value is raw data or an encoding wrapper.

</details>

---

### Q6. What is inspected from the structure perspective?

<details>
<summary>A</summary>

The delimiters, three segments, and JWT-like organization.

</details>

---

### Q7. What is inspected from the semantic-role perspective?

<details>
<summary>A</summary>

Which segment is metadata, payload, or integrity data.

</details>

---

### Q8. Can the verification state be known from appearance alone?

<details>
<summary>A</summary>

No. It remains unknown until verification is performed.

</details>

---

## Step 3 — Observation Limits

```text
can: read payload, decode payload, inspect metadata
cannot: verify signature, access secret key
```

### Q9. What observation capability exists?

<details>
<summary>A</summary>

Reading claims and inspecting metadata.

</details>

---

### Q10. What verification capability exists?

<details>
<summary>A</summary>

None in the stated situation.

</details>

---

### Q11. Why can trusted status not be determined?

<details>
<summary>A</summary>

The signature has not been verified.

</details>

---

### Q12. What is the current verification state?

<details>
<summary>A</summary>

Unknown.

</details>

---

## Step 4 — Security Reasoning

```text
payload: {"role":"admin"}
signature: present
verification: not performed
```

### Q13. Is the payload readable?

<details>
<summary>A</summary>

Yes.

</details>

---

### Q14. Is the payload trusted?

<details>
<summary>A</summary>

No; trust is not established.

</details>

---

### Q15. Why is signature presence insufficient?

<details>
<summary>A</summary>

A present signature may be invalid or unrelated to the content.

</details>

---

### Q16. What additional operation is required?

<details>
<summary>A</summary>

Signature verification under the expected algorithm and key.

</details>

---

## Step 5 — Final Classification

```text
1. Base64 wrapper
2. JWT-like structure
3. payload
4. observation capability
5. verification failed
6. metadata
7. trusted
8. modification capability
9. signature
10. verification capability
```

### Q17. Which item is representation?

<details>
<summary>A</summary>

1.

</details>

---

### Q18. Which item is structure?

<details>
<summary>A</summary>

2.

</details>

---

### Q19. Which items are semantic roles?

<details>
<summary>A</summary>

3, 6, and 9.

</details>

---

### Q20. Which items are capabilities?

<details>
<summary>A</summary>

4, 8, and 10.

</details>

---

### Q21. Which items are verification states?

<details>
<summary>A</summary>

5 and 7.

</details>

## Mini Task

Refactor the analyzer to print:

```text
=== ANALYSIS REPORT ===
representation:
structure:
semantic roles:
capabilities:
verification state:
security reasoning:
```

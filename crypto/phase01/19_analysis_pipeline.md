# Analysis Pipeline

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

# QA

## Step 1 — Analysis Layers

**Q1.** Which layer is observed first?

<details><summary><strong>A1.</strong></summary>

Representation.

</details>

---

**Q2.** Where do delimiters and segment counts belong?

<details><summary><strong>A2.</strong></summary>

Structure.

</details>

---

**Q3.** Where do metadata, payload, and signature belong?

<details><summary><strong>A3.</strong></summary>

Semantic role.

</details>

---

**Q4.** Where do trusted and untrusted belong?

<details><summary><strong>A4.</strong></summary>

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

**Q1.** What is inspected from the representation perspective?

<details><summary><strong>A1.</strong></summary>

Whether each visible value is raw data or an encoding wrapper.

</details>

---

**Q2.** What is inspected from the structure perspective?

<details><summary><strong>A2.</strong></summary>

The delimiters, three segments, and JWT-like organization.

</details>

---

**Q3.** What is inspected from the semantic-role perspective?

<details><summary><strong>A3.</strong></summary>

Which segment is metadata, payload, or integrity data.

</details>

---

**Q4.** Can the verification state be known from appearance alone?

<details><summary><strong>A4.</strong></summary>

No. It remains unknown until verification is performed.

</details>

---

## Step 3 — Observation Limits

```text
can: read payload, decode payload, inspect metadata
cannot: verify signature, access secret key
```

**Q1.** What observation capability exists?

<details><summary><strong>A1.</strong></summary>

Reading claims and inspecting metadata.

</details>

---

**Q2.** What verification capability exists?

<details><summary><strong>A2.</strong></summary>

None in the stated situation.

</details>

---

**Q3.** Why can trusted status not be determined?

<details><summary><strong>A3.</strong></summary>

The signature has not been verified.

</details>

---

**Q4.** What is the current verification state?

<details><summary><strong>A4.</strong></summary>

Unknown.

</details>

---

## Step 4 — Security Reasoning

```text
payload: {"role":"admin"}
signature: present
verification: not performed
```

**Q1.** Is the payload readable?

<details><summary><strong>A1.</strong></summary>

Yes.

</details>

---

**Q2.** Is the payload trusted?

<details><summary><strong>A2.</strong></summary>

No; trust is not established.

</details>

---

**Q3.** Why is signature presence insufficient?

<details><summary><strong>A3.</strong></summary>

A present signature may be invalid or unrelated to the content.

</details>

---

**Q4.** What additional operation is required?

<details><summary><strong>A4.</strong></summary>

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

**Q1.** Which item is representation?

<details><summary><strong>A1.</strong></summary>

1.

</details>

---

**Q2.** Which item is structure?

<details><summary><strong>A2.</strong></summary>

2.

</details>

---

**Q3.** Which items are semantic roles?

<details><summary><strong>A3.</strong></summary>

3, 6, and 9.

</details>

---

**Q4.** Which items are capabilities?

<details><summary><strong>A4.</strong></summary>

4, 8, and 10.

</details>

---

**Q5.** Which items are verification states?

<details><summary><strong>A5.</strong></summary>

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

# Security Capabilities

## Core Concept

Reading data, changing data, and producing data that passes verification are
three different capabilities.

```text
observation != modification != verification
```

- Observation: read, decode, inspect, and classify.
- Modification: alter content or construct a new value.
- Verification: satisfy integrity checks or generate valid authentication
  data.

A readable and editable payload may still be rejected when its signature is
invalid.

## Analysis Flow

```text
observe
-> fingerprint
-> peel
-> identify structure and roles
-> identify capabilities
-> reason about the security boundary
```

# QA

## Step 1 — Observation Versus Verification

```text
payload: {"role":"admin"}

attacker can:
- read and decode the payload

attacker cannot:
- generate a valid signature
```

**Q1.** What can the attacker observe?

<details><summary><strong>A1.</strong></summary>

The payload and its fields.

</details>

---

**Q2.** Which verification capability is missing?

<details><summary><strong>A2.</strong></summary>

Generating authentication data that passes verification.

</details>

---

**Q3.** Why must observation and verification be distinguished?

<details><summary><strong>A3.</strong></summary>

Reading data does not grant the ability to produce valid trusted data.

</details>

---

**Q4.** Why is a readable payload not automatically trusted?

<details><summary><strong>A4.</strong></summary>

Trust depends on integrity and authenticity checks, not readability.

</details>

---

## Step 2 — Capability Reasoning

```text
known: token, payload, metadata
unknown: secret key
```

**Q1.** What can the attacker understand?

<details><summary><strong>A1.</strong></summary>

The visible metadata, payload structure, and readable claims.

</details>

---

**Q2.** What is difficult to generate?

<details><summary><strong>A2.</strong></summary>

A valid signature for modified content.

</details>

---

**Q3.** Why does the secret key create a verification boundary?

<details><summary><strong>A3.</strong></summary>

Only a party with the required key can normally generate matching
authentication data.

</details>

---

**Q4.** Why are knowledge and valid generation different?

<details><summary><strong>A4.</strong></summary>

Knowing a payload does not reveal the secret required to authenticate it.

</details>

---

## Step 3 — Capability Classification

Classify these actions:

```text
A. read payload
B. modify payload
C. generate signature
D. pass signature verification
E. inspect metadata
```

**Q1.** What is `A`?

<details><summary><strong>A1.</strong></summary>

Observation capability.

</details>

---

**Q2.** What is `B`?

<details><summary><strong>A2.</strong></summary>

Modification capability.

</details>

---

**Q3.** What is `C`?

<details><summary><strong>A3.</strong></summary>

Verification-related generation capability.

</details>

---

**Q4.** What is `D`?

<details><summary><strong>A4.</strong></summary>

Verification capability.

</details>

---

**Q5.** What is `E`?

<details><summary><strong>A5.</strong></summary>

Observation capability.

</details>

---

## Step 4 — Controlled Analysis

**Q1.** What does a Base64-looking outer value indicate?

<details><summary><strong>A1.</strong></summary>

A likely representation wrapper that can be peeled.

</details>

---

**Q2.** What should be inspected after peeling?

<details><summary><strong>A2.</strong></summary>

Structure, semantic roles, available capabilities, and security boundaries.

</details>

---

**Q3.** Why infer semantic roles?

<details><summary><strong>A3.</strong></summary>

Different segments can represent metadata, payload, or authentication data.

</details>

---

**Q4.** Why can fingerprinting not prove verification capability?

<details><summary><strong>A4.</strong></summary>

It can identify a signature-like field but cannot prove that the signature is
valid.

</details>

---

## Step 5 — Security Boundary

```text
payload: {"role":"admin"}
signature: unknown
secret key: unknown
```

**Q1.** Why can the token not yet be trusted?

<details><summary><strong>A1.</strong></summary>

Its authentication data has not been verified.

</details>

---

**Q2.** Why is signature presence insufficient?

<details><summary><strong>A2.</strong></summary>

Presence does not imply successful verification.

</details>

---

**Q3.** Why is verification state a separate reasoning layer?

<details><summary><strong>A3.</strong></summary>

Structure can be observed without performing cryptographic verification.

</details>

---

**Q4.** Why separate observation, modification, and verification?

<details><summary><strong>A4.</strong></summary>

Each grants a different ability and crosses a different security boundary.

</details>

## Mini Task

Build an analyzer that reports representation, structure, semantic roles,
observation capability, modification capability, verification capability,
and the resulting security-boundary reasoning.

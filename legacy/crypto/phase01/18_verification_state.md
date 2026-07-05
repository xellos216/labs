# Verification State

## Three Separate Concepts

```text
semantic role:      What is this segment?
capability:         What can an actor do?
verification state: What was the verification result?
```

Examples:

| Category | Examples |
|---|---|
| Semantic role | metadata, payload, signature |
| Capability | observe, modify, verify |
| Verification state | trusted, untrusted, unknown, passed, failed |

Do not confuse a signature, which is a semantic role, with verification
failure, which is a state.

## Security Reasoning Stack

```text
representation
-> structure
-> semantic role
-> capability
-> verification state
```

# QA

## Step 1 — Three Concepts

```text
A. metadata  B. payload  C. signature
D. observation  E. modification  F. verification
G. trusted  H. untrusted  I. verification failed
```

**Q1.** What category contains `A`, `B`, and `C`?

<details><summary><strong>A1.</strong></summary>

Semantic role.

</details>

---

**Q2.** What category contains `D`, `E`, and `F`?

<details><summary><strong>A2.</strong></summary>

Capability.

</details>

---

**Q3.** What category contains `G`, `H`, and `I`?

<details><summary><strong>A3.</strong></summary>

Verification state.

</details>

---

**Q4.** Why must the categories remain separate?

<details><summary><strong>A4.</strong></summary>

They describe purpose, ability, and result respectively.

</details>

---

## Step 2 — Semantic Roles

**Q1.** What is the header's likely role?

<details><summary><strong>A1.</strong></summary>

Metadata or security configuration.

</details>

---

**Q2.** What is the payload's likely role?

<details><summary><strong>A2.</strong></summary>

Application data or claims.

</details>

---

**Q3.** What is the signature's likely role?

<details><summary><strong>A3.</strong></summary>

Integrity and authentication data.

</details>

---

**Q4.** Why is payload not a capability?

<details><summary><strong>A4.</strong></summary>

Payload describes a segment's purpose, not an actor's ability.

</details>

---

## Step 3 — Capabilities

```text
attacker can read and inspect
attacker cannot generate a valid signature
```

**Q1.** Which observation capabilities exist?

<details><summary><strong>A1.</strong></summary>

Reading the payload and inspecting metadata.

</details>

---

**Q2.** Which modification capability may exist?

<details><summary><strong>A2.</strong></summary>

Editing payload fields or constructing altered content.

</details>

---

**Q3.** Which verification capability is missing?

<details><summary><strong>A3.</strong></summary>

Generating a valid signature and passing verification after modification.

</details>

---

**Q4.** Why is capability different from semantic role?

<details><summary><strong>A4.</strong></summary>

Capability describes an action; semantic role describes purpose.

</details>

---

## Step 4 — Verification Result

```text
payload modified
signature unchanged
verification failed
```

**Q1.** What is the verification state?

<details><summary><strong>A1.</strong></summary>

Failed.

</details>

---

**Q2.** Why is failure not a semantic role?

<details><summary><strong>A2.</strong></summary>

It is the result of a check, not the purpose of a segment.

</details>

---

**Q3.** Why is failure not a capability?

<details><summary><strong>A3.</strong></summary>

It describes an outcome rather than an available action.

</details>

---

**Q4.** What does verification state describe?

<details><summary><strong>A4.</strong></summary>

Whether verification passed, failed, or remains unknown.

</details>

---

## Step 5 — Final Classification

**Q1.** List the semantic roles.

<details><summary><strong>A1.</strong></summary>

Metadata, payload, and signature.

</details>

---

**Q2.** List the capabilities.

<details><summary><strong>A2.</strong></summary>

Observation, modification, and verification.

</details>

---

**Q3.** List the verification states.

<details><summary><strong>A3.</strong></summary>

Trusted, untrusted, unknown, passed, and failed.

</details>

---

**Q4.** Why is this separation necessary?

<details><summary><strong>A4.</strong></summary>

Security conclusions become invalid when purpose, ability, and result are
treated as interchangeable.

</details>

## Mini Task

Produce an analyzer report with separate sections for semantic roles,
capabilities, and verification state. Report the state as `unknown` when no
actual verification was performed.

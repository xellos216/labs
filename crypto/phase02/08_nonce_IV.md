# Session 08 — Why Nonces and IVs Exist

## Objective

Understand why stream ciphers require a unique Nonce or IV for each encryption, and how keystream reuse leads to practical attacks.

---

## Core Concept

A stream cipher encrypts data by XORing the plaintext with a generated keystream.

```text
Plaintext
    XOR
Keystream
    ↓
Ciphertext
```

Encryption and decryption are reversible because XOR is its own inverse.

```text
P XOR K = C
C XOR K = P
```

---

## The Danger of Keystream Reuse

Suppose two different messages are encrypted using the **same keystream**.

```text
C₁ = P₁ XOR K
C₂ = P₂ XOR K
```

An attacker can compute:

```text
C₁ XOR C₂
```

Expanding the equation:

```text
(P₁ XOR K) XOR (P₂ XOR K)

= P₁ XOR P₂ XOR K XOR K

= P₁ XOR P₂
```

Because:

```text
K XOR K = 0
```

the keystream disappears completely.

The attacker now obtains:

```text
P₁ XOR P₂
```

Although neither plaintext is immediately revealed, this relationship is often enough to recover information when portions of one plaintext are known or predictable.

---

## Known Plaintext Risk

If an attacker knows or correctly guesses part of one plaintext, the corresponding portion of the keystream can be recovered.

That recovered keystream can then be used to decrypt other ciphertexts produced with the same keystream.

This is why **keystream reuse must never occur**.

---

## Why Nonces and IVs Exist

Using only the secret key would always generate the same keystream.

```text
Secret Key
    ↓
Always the same Keystream
```

Instead, stream ciphers use an additional input.

```text
Secret Key
      +
Nonce (or IV)
      ↓
Keystream Generator
      ↓
Unique Keystream
```

Example:

```text
Secret Key = SECRET123

Nonce = 1
↓
Keystream A

Nonce = 2
↓
Keystream B

Nonce = 3
↓
Keystream C
```

The secret key remains unchanged, but each different Nonce produces a different keystream.

---

## Mental Model

```text
Secret Key
      +
Nonce (IV)
      ↓
Generate Keystream
      ↓
Plaintext XOR Keystream
      ↓
Ciphertext
```

The purpose of a Nonce or IV is **not to store the keystream**, but to ensure that a fresh keystream is generated for every encryption.

---

# QA

### Q1

Why is reusing the same keystream dangerous in a stream cipher?

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

### Q2

Simplify the following expression:

```text
(P₁ XOR K) XOR (P₂ XOR K)
```

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

### Q3

Why doesn't an attacker immediately recover both plaintexts after obtaining `P₁ XOR P₂`?

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

### Q4

What additional information often allows an attacker to recover plaintext after keystream reuse?

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

### Q5

Why are Nonces or IVs used together with a secret key?

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

### Q6

Complete the following pipeline.

```text
Secret Key
      +
?
      ↓
Generate Keystream
      ↓
Plaintext XOR Keystream
      ↓
Ciphertext
```

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

## Key Takeaways

- Stream ciphers encrypt by XORing plaintext with a keystream.
- Reusing a keystream allows it to cancel out during XOR operations.
- `C₁ XOR C₂ = P₁ XOR P₂` when the same keystream is reused.
- Known or predictable plaintext can reveal the reused keystream.
- Nonces and IVs exist to produce a unique keystream for each encryption while keeping the secret key unchanged.

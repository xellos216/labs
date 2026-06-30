# Session 09 — Plaintext, Keystream and Ciphertext

## Objective

Understand the relationship between plaintext, keystream, and ciphertext in a stream cipher, and explain why the same XOR operation performs both encryption and decryption.

---

## Core Concept

A stream cipher encrypts data by XORing the plaintext with a keystream.

```text
Plaintext
    XOR
Keystream
    ↓
Ciphertext
```

Encryption is expressed as:

```text
P XOR K = C
```

where:

- `P` = Plaintext
- `K` = Keystream
- `C` = Ciphertext

---

## Why Decryption Uses the Same XOR Operation

Starting from:

```text
C = P XOR K
```

Decrypting simply means XORing the ciphertext with the same keystream.

```text
C XOR K

= (P XOR K) XOR K

= P XOR (K XOR K)

= P XOR 0

= P
```

Therefore:

```text
C XOR K = P
```

No separate decryption algorithm is required.

---

## XOR Properties That Make This Possible

Three XOR properties make stream cipher decryption possible.

### 1. Self-Canceling

```text
A XOR A = 0
```

Applying the same value twice removes it.

---

### 2. Identity Element

```text
A XOR 0 = A
```

XORing with zero leaves the value unchanged.

---

### 3. Associative Property

```text
(A XOR B) XOR C

=

A XOR (B XOR C)
```

This allows the two identical keystream values to be grouped together first.

---

## Encryption and Decryption

```text
Encryption

Plaintext
    XOR
Keystream
    ↓
Ciphertext
```

```text
Decryption

Ciphertext
    XOR
Keystream
    ↓
Plaintext
```

Both operations use the identical XOR operation.

Only the input data changes.

---

## Relationship Between Two Ciphertexts

If the same keystream is reused:

```text
C₁ = P₁ XOR K

C₂ = P₂ XOR K
```

Then:

```text
C₁ XOR C₂

= (P₁ XOR K) XOR (P₂ XOR K)

= (P₁ XOR P₂) XOR (K XOR K)

= P₁ XOR P₂
```

The keystream disappears because:

```text
K XOR K = 0
```

---

## Why This Is Dangerous

Reusing a keystream exposes the relationship between plaintexts.

The attacker obtains:

```text
P₁ XOR P₂
```

This does **not** immediately reveal either plaintext.

However, if part of one plaintext is known or predictable (Known Plaintext), the attacker can recover portions of the keystream and eventually decrypt other ciphertext encrypted with the same keystream.

---

## Mental Model

```text
Plaintext
      │
      ▼
XOR with Keystream
      │
      ▼
Ciphertext
      │
      ▼
XOR with the Same Keystream
      │
      ▼
Plaintext
```

The same XOR operation performs both encryption and decryption because the keystream cancels itself.

---

# QA

### Q1

Why can a stream cipher use the same XOR operation for both encryption and decryption?

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

### Q2

Which XOR properties make `C XOR K = P` possible?

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

### Q3

Derive the following equation.

```text
C XOR K = P
```

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

### Q4

Simplify the following expression.

```text
(P₁ XOR K) XOR (P₂ XOR K)
```

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

### Q5

Why does `C₁ XOR C₂` remove the keystream when the same keystream is reused?

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

### Q6

Why doesn't obtaining `P₁ XOR P₂` immediately reveal both plaintexts, and what additional information can allow recovery?

<details>
<summary><strong>A</strong></summary>

&nbsp;

</details>

---

## Key Takeaways

- Stream ciphers encrypt by XORing plaintext with a keystream.
- Decryption is performed by XORing the ciphertext with the same keystream.
- XOR's self-canceling, identity, and associative properties make this possible.
- Reusing a keystream removes the keystream from `C₁ XOR C₂`, exposing `P₁ XOR P₂`.
- Known plaintext or predictable data can be used to recover reused keystreams and decrypt related ciphertexts.

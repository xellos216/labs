# Session 01 — What XOR Actually Does

## Objective

Understand XOR as a reversible byte transformation and distinguish it from representation changes such as Base64.

---

## Mental Model

XOR is a reversible byte transformation.

It is not:

- encoding
- compression
- hashing

It transforms bytes using another byte sequence.

---

## XOR Rules

0 XOR 0 = 0

0 XOR 1 = 1

1 XOR 0 = 1

1 XOR 1 = 0

Same -> 0

Different -> 1

---

## Toggle Intuition

Key bit = 0

- keep original bit

Key bit = 1

- flip original bit

Therefore XOR behaves like a controlled bit-flipper.

---

## Reversibility

P XOR K = C

C XOR K = P

Applying the same key twice restores the original value.

(P XOR K) XOR K = P

---

## Important Observation

XOR changes values.

Base64 changes representation.

Example:

base64:
bytes -> text representation

XOR:
bytes -> different bytes

---

## Crypto Mindset

When observing unknown data:

- representation?
- transformation?
- XOR?
- key present?
- reversible?

Always separate:

representation

from

transformation

---

## Transferable Pattern

Input Bytes
→ XOR
→ Output Bytes

The structure may stay identical.

The values change.

Focus on:

byte relationships

not visual appearance.

---

# QA

### Q1

What does XOR return when both input bits are the same?

<details>
<summary><strong>A</strong></summary>

Result is 0

</details>

---

### Q2

What does XOR return when the two input bits are different?

<details>
<summary><strong>A</strong></summary>

Result is 1

</details>

---

### Q3

Why can XOR be understood as a toggle operation?

<details>
<summary><strong>A</strong></summary>

Because a key bit of 1 flips a bit and a key bit of 0 keeps it unchanged.

</details>

---

### Q4

Calculate the following expression.

0101 XOR 0011

<details>
<summary><strong>A</strong></summary>

= 0110

</details>

---

### Q5

Why does the following identity hold?

(P XOR K) XOR K = P

<details>
<summary><strong>A</strong></summary>

Applying the same key twice restores the original value.

</details>

---

### Q6

What is the most important difference between Base64 and XOR?

<details>
<summary><strong>A</strong></summary>

Base64 changes representation, while XOR changes values.

</details>

---

### Q7

What XOR-related question should you ask when examining ciphertext?

<details>
<summary><strong>A</strong></summary>

Could this data be XOR-transformed?

</details>

---

## Key Takeaways

- XOR returns `0` for equal bits and `1` for different bits.
- A key bit of `0` preserves a bit, while a key bit of `1` flips it.
- Applying the same XOR key twice restores the original value.
- XOR transforms byte values; it does not merely change their representation.
- Analyze XOR in terms of byte relationships rather than visual appearance.

# XOR Operation

What XOR Actually Does

## Mental Model

XOR is a reversible byte transformation.

It is not:

- encoding
- compression
- hashing

It transforms bytes using another byte sequence.

## XOR Rules

0 XOR 0 = 0

0 XOR 1 = 1

1 XOR 0 = 1

1 XOR 1 = 0

Same -> 0

Different -> 1

## Toggle Intuition

Key bit = 0

- keep original bit

Key bit = 1

- flip original bit

Therefore XOR behaves like a controlled bit-flipper.

## Reversibility

P XOR K = C

C XOR K = P

Applying the same key twice restores the original value.

(P XOR K) XOR K = P

## Important Observation

XOR changes values.

Base64 changes representation.

Example:

base64:
bytes -> text representation

XOR:
bytes -> different bytes

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

## Transferable Pattern

Input Bytes
→ XOR
→ Output Bytes

The structure may stay identical.

The values change.

Focus on:

byte relationships

not visual appearance.

# QA

**Q1.**

What does XOR return when both input bits are the same?

<details>
<summary><strong>A1.</strong></summary>

Result is 0

</details>

---

**Q2.**

What does XOR return when the two input bits are different?

<details>
<summary><strong>A2.</strong></summary>

Result is 1

</details>

---

**Q3.**

Why can XOR be understood as a toggle operation?

<details>
<summary><strong>A3.</strong></summary>

Because a key bit of 1 flips a bit and a key bit of 0 keeps it unchanged.

</details>

---

**Q4.**

Calculate the following expression.

1 XOR 0

<details>
<summary><strong>A4.</strong></summary>

= 1

</details>

---

**Q5.**

Calculate the following expression.

1 XOR 1

<details>
<summary><strong>A5.</strong></summary>

= 0

</details>

---

**Q6.**

Calculate the following expression.

0101 XOR 0011

<details>
<summary><strong>A6.</strong></summary>

= 0110

</details>

---

**Q7.**

Why is XOR frequently used in cryptography?

<details>
<summary><strong>A7.</strong></summary>

Because applying the same key again restores the original data.

</details>

---

**Q8.**

Find `C` in the following expression.

P = 0101

K = 0011

C = P XOR K

<details>
<summary><strong>A8.</strong></summary>

= 0110

</details>

---

**Q9.**

Find `P` in the following expression.

C = 0110

K = 0011

P = C XOR K

<details>
<summary><strong>A9.</strong></summary>

= 0101

</details>

---

**Q10.**

Why does the following identity hold?

(P XOR K) XOR K = P

<details>
<summary><strong>A10.</strong></summary>

Applying the same key twice restores the original value.

</details>

---

**Q11.**

Why is XOR called a transformation rather than a change of representation?

<details>
<summary><strong>A11.</strong></summary>

XOR changes byte values, not their representation.

</details>

---

**Q12.**

What is the most important difference between Base64 and XOR?

<details>
<summary><strong>A12.</strong></summary>

Base64 changes representation, while XOR changes values.

</details>

---

**Q13.**

Which statement best describes the relationship between XOR input and output?

A. The input length changes.

B. The input byte values are transformed.

C. Only the structure changes.

D. The input is converted to ASCII.

<details>
<summary><strong>A13.</strong></summary>

B

</details>

---

**Q14.**

What XOR-related question should you ask when examining ciphertext?

<details>
<summary><strong>A14.</strong></summary>

Could this data be XOR-transformed?

</details>

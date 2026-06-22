# XOR Viewpoints

Keep vs Flip Mental Model

## Session Goal

Separate two XOR viewpoints.

Do not mix them.

## Viewpoint 1

XOR Truth Rule

Same -> 0

Different -> 1

Examples:

0 XOR 0 = 0

1 XOR 1 = 0

0 XOR 1 = 1

1 XOR 0 = 1

This viewpoint explains:

"How XOR produces a result."

## Viewpoint 2

Key Interpretation

Key = 0

- keep bit

Key = 1

- flip bit

Examples:

1010 XOR 0000

= 1010

1010 XOR 1111

= 0101

This viewpoint explains:

"What the key does."

## Important Distinction

These are not competing explanations.

They describe XOR from different angles.

Truth Rule

→ explains result generation

Key Interpretation

→ explains transformation behavior

## Reversibility

P XOR K = C

C XOR K = P

The same key performs:

encrypt

and

decrypt

## Observation Habit

When analyzing XOR:

1. What is the key?

2. Which bits are flipped?

3. Which bits remain unchanged?

4. Can the same key restore the original data?

## Transferable Mental Model

Plaintext Bits

→ XOR Key

→ Some bits stay

→ Some bits flip

→ Ciphertext Bits

Think in bit relationships.

Not in characters.

# QA

**Q1.**

Calculate the following XOR result.

1010 XOR 0000

<details>
<summary><strong>A1.</strong></summary>

= 1010

</details>

---

**Q2.**

Calculate the following XOR result.

1010 XOR 1111

<details>
<summary><strong>A2.</strong></summary>

= 0101

</details>

---

**Q3.**

Why does a key bit of 0 preserve the original bit in XOR?

<details>
<summary><strong>A3.</strong></summary>

XOR with 0 leaves the original bit unchanged.

</details>

---

**Q4.**

Why does a key bit of 1 flip the original bit in XOR?

<details>
<summary><strong>A4.</strong></summary>

XOR with 1 changes 0 to 1 and 1 to 0.

</details>

---

**Q5.**

Calculate the following expression.

1100 XOR 0101

<details>
<summary><strong>A5.</strong></summary>

1001

</details>

---

**Q6.**

Calculate the following expression.

1001 XOR 1001

<details>
<summary><strong>A6.</strong></summary>

= 0000

</details>

---

**Q7.**

Calculate the following expression.

1111 XOR 0011

<details>
<summary><strong>A7.</strong></summary>

= 1100

</details>

---

**Q8.**

Find `C` in the following expression.

P = 1100

K = 0101

C = P XOR K

<details>
<summary><strong>A8.</strong></summary>

= 1001

</details>

---

**Q9.**

Find `P` in the following expression.

C = 1001

K = 0101

P = C XOR K

<details>
<summary><strong>A9.</strong></summary>

= 1100

</details>

---

**Q10.**

Which is the most important property of XOR?

A. It compresses data.

B. It is irreversible.

C. The same key can restore the original value.

D. It reduces the data length.

<details>
<summary><strong>A10.</strong></summary>

C

</details>

---

**Q11.**

Distinguish between the following two concepts.

1. Same → 0 / Different → 1

2. Key=0 → Keep / Key=1 → Flip

<details>
<summary><strong>A11.</strong></summary>

The first explains how XOR calculates its result. The second explains how
the key affects the original bit.

</details>

---

**Q12.**

Why are "Same -> 0 / Different -> 1" and "Keep / Flip" different viewpoints?

<details>
<summary><strong>A12.</strong></summary>

Same/Different is the XOR calculation rule. Keep/Flip interprets XOR from
the key's point of view.

</details>

---

**Q13.**

Explain why the following identity holds.

(P XOR K) XOR K = P

<details>
<summary><strong>A13.</strong></summary>

XORing the same value twice restores the original value.

</details>

---

**Q14.**

Why might XOR be considered when examining ciphertext?

<details>
<summary><strong>A14.</strong></summary>

Because XOR is a common reversible transformation.

If data looks transformed but can potentially be restored with a key, XOR is one possibility to investigate.

</details>

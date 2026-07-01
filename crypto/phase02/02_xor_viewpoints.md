# Session 02 — XOR Truth Tables and Bitwise Reasoning

## Metadata

```yaml
Roadmap: Cryptography
Phase: 02
Session: 02
Title: XOR Truth Tables and Bitwise Reasoning
Status:
Review:
ArchiveVersion: 2
Date:
```

## Objective

Separate two XOR viewpoints.

Do not mix them.

---

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

---

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

---

## Important Distinction

These are not competing explanations.

They describe XOR from different angles.

Truth Rule

→ explains result generation

Key Interpretation

→ explains transformation behavior

---

## Reversibility

P XOR K = C

C XOR K = P

The same key performs:

encrypt

and

decrypt

---

## Observation Habit

When analyzing XOR:

1. What is the key?

2. Which bits are flipped?

3. Which bits remain unchanged?

4. Can the same key restore the original data?

---

## Transferable Mental Model

Plaintext Bits

→ XOR Key

→ Some bits stay

→ Some bits flip

→ Ciphertext Bits

Think in bit relationships.

Not in characters.

---

# Review Questions

### Q1. Calculate the following XOR result.

1010 XOR 0000

<details>
<summary>A</summary>

= 1010

</details>

---

### Q2. Calculate the following XOR result.

1010 XOR 1111

<details>
<summary>A</summary>

= 0101

</details>

---

### Q3. Calculate the following expression.

1100 XOR 0101

<details>
<summary>A</summary>

1001

</details>

---

### Q4. Distinguish between the following two concepts.

1. Same → 0 / Different → 1

2. Key=0 → Keep / Key=1 → Flip

<details>
<summary>A</summary>

The first explains how XOR calculates its result. The second explains how
the key affects the original bit.

</details>

---

### Q5. Explain why the following identity holds.

(P XOR K) XOR K = P

<details>
<summary>A</summary>

XORing the same value twice restores the original value.

</details>

---

### Q6. Why might XOR be considered when examining ciphertext?

<details>
<summary>A</summary>

Because XOR is a common reversible transformation.

If data looks transformed but can potentially be restored with a key, XOR is one possibility to investigate.

</details>

---

## Key Takeaways

- The same/different rule explains how XOR calculates its result.
- The keep/flip model explains what each key bit does to the input.
- These viewpoints describe the same operation from different perspectives.
- XOR is reversible because applying the same key twice cancels its effect.
- Bit relationships are more useful than character appearance when analyzing XOR.

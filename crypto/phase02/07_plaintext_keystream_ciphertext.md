# Session 07 — Plaintext, Keystream, and Ciphertext Relationships

## Objective

Understand how plaintext, keystream, and ciphertext are mathematically related.

---

## Core Relationship

```text
Plaintext
XOR
Keystream
=
Ciphertext
```

This can be rewritten as:

```text
P XOR K = C
```

---

## Reversibility

Because XOR is reversible:

```text
C XOR K = P
```

And:

```text
P XOR C = K
```

Knowing any two values allows you to recover the third.

---

## Three-Way Relationship

```text
P XOR K = C

C XOR K = P

P XOR C = K
```

All three equations describe the same relationship.

---

## Important Observation

You do not always need the original key.

Sometimes:

```text
Ciphertext
+
Known Plaintext
```

can reveal:

```text
Keystream
```

---

## Example

Given:

```text
P = 41

K = 01
```

Then:

```text
C = 40
```

Verification:

```text
40 XOR 01 = 41

41 XOR 40 = 01
```

---

## Analyst Mindset

Ask:

```text
What do I already know?
```

Possible situations:

```text
Know P and K
→ recover C

Know C and K
→ recover P

Know P and C
→ recover K
```

---

## Why This Matters

Many crypto challenges are not about:

```text
finding the key
```

They are about:

```text
finding any missing piece
```

of the relationship.

---

## Observation Habit

When looking at encrypted data:

Ask:

- Do I know plaintext?
- Do I know ciphertext?
- Do I know keystream?
- Can I recover the missing value?

---

## Transferable Mental Model

```text
Plaintext
↔
Keystream
↔
Ciphertext
```

Knowing any two pieces reveals the third.

---

# QA

### Q1

What does the phrase

```text
Knowing any two reveals the third
```

mean?

<details>
<summary><strong>A</strong></summary>

Know P and K
→ recover C

Know C and K
→ recover P

Know P and C
→ recover K

</details>

---

### Q2

Given:

```text
P = 0x42
K = 0x02
```

Recover C.

<details>
<summary><strong>A</strong></summary>

0x40

</details>

---

### Q3

Given:

```text
C = 0x40
K = 0x02
```

Recover P.

<details>
<summary><strong>A</strong></summary>

0x42

</details>

---

### Q4

Given:

```text
P = 0x42
C = 0x40
```

Recover K.

<details>
<summary><strong>A</strong></summary>

0x02

</details>

---

### Q5

Why are the following equations equivalent?

```text
P XOR K = C

C XOR K = P

P XOR C = K
```

<details>
<summary><strong>A</strong></summary>

Applying XOR with the same value restores the original value.

</details>

---

### Q6

When analyzing ciphertext, why might known plaintext be valuable?

<details>
<summary><strong>A</strong></summary>

Known plaintext may reveal missing values in the XOR relationship.


</details>

---

### Q7

In one sentence, explain the relationship between plaintext, keystream, and ciphertext.

<details>
<summary><strong>A</strong></summary>

Knowing any two of plaintext, keystream, and ciphertext allows recovery of the third.

</details>

---

## Key Takeaways

- Stream-style encryption follows the relationship `P XOR K = C`.
- XOR reversibility also gives `C XOR K = P` and `P XOR C = K`.
- Knowing any two of plaintext, keystream, and ciphertext reveals the third.
- Known plaintext can expose the corresponding part of a keystream.
- Analysis should begin by identifying which values are already known.

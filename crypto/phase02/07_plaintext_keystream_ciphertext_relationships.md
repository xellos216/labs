# Plaintext, Keystream, Ciphertext Relationships

## Session Goal

Understand how plaintext, keystream, and ciphertext are mathematically related.

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

## Three-Way Relationship

```text
P XOR K = C

C XOR K = P

P XOR C = K
```

All three equations describe the same relationship.

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

## Observation Habit

When looking at encrypted data:

Ask:

- Do I know plaintext?
- Do I know ciphertext?
- Do I know keystream?
- Can I recover the missing value?

## Transferable Mental Model

```text
Plaintext
↔
Keystream
↔
Ciphertext
```

Knowing any two pieces reveals the third.

# QA

**Q1.**

Complete:

```text
P XOR K = __
```

<details>
<summary><strong>A1.</strong></summary>


</details>

---

**Q2.**

Complete:

```text
C XOR K = __
```

<details>
<summary><strong>A2.</strong></summary>


</details>

---

**Q3.**

Complete:

```text
P XOR C = __
```

<details>
<summary><strong>A3.</strong></summary>


</details>

---

**Q4.**

Calculate:

```text
0x41 XOR 0x01
```

<details>
<summary><strong>A4.</strong></summary>


</details>

---

**Q5.**

Given:

```text
C = 0x40
K = 0x01
```

Recover P.

<details>
<summary><strong>A5.</strong></summary>


</details>

---

**Q6.**

Given:

```text
P = 0x41
C = 0x40
```

Recover K.

<details>
<summary><strong>A6.</strong></summary>


</details>

---

**Q7.**

Why does knowing plaintext sometimes help recover a keystream?

<details>
<summary><strong>A7.</strong></summary>


</details>

---

**Q8.**

What does the phrase

```text
Knowing any two reveals the third
```

mean?

<details>
<summary><strong>A8.</strong></summary>


</details>

---

**Q9.**

Given:

```text
P = 0x42
K = 0x02
```

Recover C.

<details>
<summary><strong>A9.</strong></summary>


</details>

---

**Q10.**

Given:

```text
C = 0x40
K = 0x02
```

Recover P.

<details>
<summary><strong>A10.</strong></summary>


</details>

---

**Q11.**

Given:

```text
P = 0x42
C = 0x40
```

Recover K.

<details>
<summary><strong>A11.</strong></summary>


</details>

---

**Q12.**

Why are the following equations equivalent?

```text
P XOR K = C

C XOR K = P

P XOR C = K
```

<details>
<summary><strong>A12.</strong></summary>


</details>

---

**Q13.**

When analyzing ciphertext, why might known plaintext be valuable?

<details>
<summary><strong>A13.</strong></summary>


</details>

---

**Q14.**

In one sentence, explain the relationship between plaintext, keystream, and ciphertext.

<details>
<summary><strong>A14.</strong></summary>


</details>

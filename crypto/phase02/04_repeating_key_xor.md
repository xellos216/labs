# Repeating-Key XOR

Repeating-Key XOR Introduction

## Session Goal

Understand how a key can be reused across many bytes.

## Single-Byte XOR

Example:

```text
Plaintext

41 42 43 44

Key

01
```

Applied:

```text
41 XOR 01
42 XOR 01
43 XOR 01
44 XOR 01
```

Same key every time.

## Repeating-Key XOR

Example:

```text
Plaintext

41 42 43 44 45 46

Key

01 02
```

Applied:

```text
41 XOR 01
42 XOR 02
43 XOR 01
44 XOR 02
45 XOR 01
46 XOR 02
```

The key repeats.

## Important Observation

The key is usually shorter than the data.

Therefore:

```text
key
→ repeat
→ repeat
→ repeat
```

until all plaintext bytes are processed.

## Mental Model

Think of the key as a stencil.

```text
01 02
01 02
01 02
01 02
...
```

The pattern is reused.

## Reversibility

Nothing changes about XOR.

```text
P XOR K = C

C XOR K = P
```

The only difference:

```text
K1 K2 K1 K2 K1 K2 ...
```

instead of

```text
K1 K1 K1 K1 ...
```

## Observation Habit

When analyzing ciphertext:

Ask:

- Is there a repeating pattern?
- Could a short key be reused?
- Does the data look transformed by repeating bytes?

## Transferable Mental Model

Plaintext Bytes

→ Repeating Key

→ XOR

→ Ciphertext Bytes

A stream cipher is often conceptually similar:

```text
plaintext
XOR
keystream
=
ciphertext
```

The keystream is just much larger and usually generated dynamically.

# QA

**Q1.**

What is repeating-key XOR?

<details>
<summary><strong>A1.</strong></summary>
A short key is reused repeatedly across the plaintext.

</details>

---

**Q2.**

Which key byte is applied to each position in the following plaintext?

```text
Plaintext:
A B C D E F

Key:
X Y
```

Write the key sequence aligned with every plaintext position.

<details>
<summary><strong>A2.</strong></summary>
A B C D E F
X Y X Y X Y

</details>

---

**Q3.**

Why is it called repeating-key XOR?

<details>
<summary><strong>A3.</strong></summary>
Because the key is reused in a repeating pattern.

</details>

---

**Q4.**

Calculate the following expression.

```text
0x41 XOR 0x01
```

<details>
<summary><strong>A4.</strong></summary>
= `0100 0000` = `0x40`
</details>

---

**Q5.**

Calculate the following expression.

```text
0x42 XOR 0x02
```

<details>
<summary><strong>A5.</strong></summary>
= `0100 0000` = `0x40`
</details>

---

**Q6.**

XOR the following plaintext and key.

```text
Plaintext:

0x41 0x42 0x43 0x44

Key:

0x01 0x02
```

Write the result after repeating the key.

<details>
<summary><strong>A6.</strong></summary>
= 0x40 0x40 0x42 0x46

</details>

---

**Q7.**

Which sequence correctly represents repeating-key XOR?

A.

```text
P1 XOR K1
P2 XOR K2
P3 XOR K3
...
```

B.

```text
P1 XOR K1
P2 XOR K2
P3 XOR K1
P4 XOR K2
...
```

<details>
<summary><strong>A7.</strong></summary>
B
</details>

---

**Q8.**

Why does repeating-key XOR appear more complex than single-byte XOR?

<details>
<summary><strong>A8.</strong></summary>
Because different key bytes are used at different positions.


</details>

---

**Q9.**

Explain the following statement.

```text
The key becomes a repeating pattern.
```

<details>
<summary><strong>A9.</strong></summary>
The same key pattern is reused again and again.

</details>

---

**Q10.**

Calculate the following results.

```text
0x41 XOR 0x01 = ?
0x42 XOR 0x02 = ?
0x43 XOR 0x01 = ?
0x44 XOR 0x02 = ?
```

<details>
<summary><strong>A10.</strong></summary>
0x40

0x40

0x42

0x46

</details>

---

**Q11.**

Why is repeating-key XOR reversible?

<details>
<summary><strong>A11.</strong></summary>
Because XOR is reversible and the same repeating key can be applied again.



</details>

---

**Q12.**

Explain why the following identity holds.

```text
(P XOR K) XOR K = P
```

<details>
<summary><strong>A12.</strong></summary>
P XOR K = C

C XOR K = P


</details>

---

**Q13.**

Why can a repeated ciphertext pattern suggest repeating-key XOR?

<details>
<summary><strong>A13.</strong></summary>
Because reuse of a short key may leave periodic relationships in the
ciphertext.



</details>

---

**Q14.**

Describe repeating-key XOR in one sentence.

<details>
<summary><strong>A14.</strong></summary>
Repeating-key XOR applies a short key repeatedly across the plaintext bytes.


</details>

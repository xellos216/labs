# Keystream Mental Model

## Session Goal

Understand the concept of a keystream.

## From Repeating Key to Keystream

Repeating-Key XOR:

```text
Plaintext

41 42 43 44 45 46

Key

01 02
```

Applied:

```text
01 02 01 02 01 02
```

The repeated key becomes a stream of key bytes.

This stream is called a:

```text
keystream
```

## Important Observation

The plaintext does not interact with the original key directly.

It interacts with:

```text
keystream
```

Example:

```text
Plaintext

41 42 43 44

Keystream

01 02 01 02
```

Applied:

```text
41 XOR 01
42 XOR 02
43 XOR 01
44 XOR 02
```

## Mental Model

Think:

```text
Plaintext
XOR
Keystream
=
Ciphertext
```

Not:

```text
Plaintext
XOR
Key
=
Ciphertext
```

The key often generates the keystream.

## Repeating-Key XOR

Example:

```text
Key

01 02
```

Generated keystream:

```text
01 02 01 02 01 02 01 02 ...
```

## Stream Cipher Intuition

A stream cipher works similarly:

```text
Key
↓
Generate Keystream
↓
XOR
↓
Ciphertext
```

The difference is:

```text
Repeating-Key XOR
```

uses a predictable keystream.

While:

```text
Stream Cipher
```

tries to generate a much less predictable keystream.

## Observation Habit

When analyzing XOR-based data, ask:

- What is the keystream?
- How is it generated?
- Does it repeat?
- Is it predictable?

## Transferable Mental Model

```text
Key
→ Keystream
→ XOR
→ Ciphertext
```

Understanding the keystream is often more important than understanding the key itself.

# QA

**Q1.**

What is a keystream?

<details>
<summary><strong>A1.</strong></summary>
A keystream is the sequence of key bytes used directly in XOR operations.

</details>

---

**Q2.**

In Repeating-Key XOR, what generates the keystream?

<details>
<summary><strong>A2.</strong></summary>
The repeating key generates the keystream.

</details>

---

**Q3.**

Given:

```text
Key

01 02
```

Write the first eight bytes of the generated keystream.

<details>
<summary><strong>A3.</strong></summary>
01 02 01 02 01 02 01 02


</details>

---

**Q4.**

Calculate:

```text
0x41 XOR 0x01
```

<details>
<summary><strong>A4.</strong></summary>
0x40

</details>

---

**Q5.**

Calculate:

```text
0x42 XOR 0x02
```

<details>
<summary><strong>A5.</strong></summary>
0x40

</details>

---

**Q6.**

Calculate:

```text
0x43 XOR 0x01
```

<details>
<summary><strong>A6.</strong></summary>
0x42

</details>

---

**Q7.**

Calculate:

```text
0x44 XOR 0x02
```

<details>
<summary><strong>A7.</strong></summary>
0x46

</details>

---

**Q8.**

Complete:

```text
Plaintext
XOR
________
=
Ciphertext
```

<details>
<summary><strong>A8.</strong></summary>
Key-stream

</details>

---

**Q9.**

Why is a keystream more important than the original key during XOR operations?

<details>
<summary><strong>A9.</strong></summary>
Because XOR is performed with the keystream, not directly with the original key.


</details>

---

**Q10.**

What keystream is produced by:

```text
Key

AA BB
```

for six output bytes?

<details>
<summary><strong>A10.</strong></summary>
AA BB AA BB AA BB

</details>

---

**Q11.**

What is the main difference between:

```text
Repeating-Key XOR
```

and

```text
Stream Cipher
```

from a keystream perspective?

<details>
<summary><strong>A11.</strong></summary>
Repeating-Key XOR uses a predictable key-stream.

Stream Cipher tries to generate a much less predictable key-stream.

</details>

---

**Q12.**

Why can a predictable keystream become a weakness?

<details>
<summary><strong>A12.</strong></summary>
If the keystream is predictable, an analyst recover plaintext or infer future transformatios.


</details>

---

**Q13.**

When observing ciphertext, why might an analyst try to infer the keystream?

<details>
<summary><strong>A13.</strong></summary>
Because knowing or guessing the keystream helps recover plaintext from ciphertext.


</details>

---

**Q14.**

In one sentence, explain the relationship between:

```text
Key
Keystream
Ciphertext
```

<details>
<summary><strong>A14.</strong></summary>
The key generates the keystream, and the keystream is XORed with plaintext to produce ciphertext.


</details>

# Known Plaintext Intuition

## Session Goal

Understand why knowing even a small piece of plaintext can be useful.

## Core Idea

Previously:

```text
P XOR K = C
```

We learned:

```text
P XOR C = K
```

This means:

```text
Known Plaintext
+
Ciphertext
=
Keystream
```

## Why This Matters

Imagine:

```text
Plaintext

41

Ciphertext

40
```

Then:

```text
41 XOR 40
=
01
```

The keystream is recovered.

## Important Observation

An attacker does not always need:

```text
the entire plaintext
```

Sometimes:

```text
a few known bytes
```

are enough.

Example:

```text
Known Plaintext

41 42

Ciphertext

40 40
```

Recovery:

```text
41 XOR 40 = 01

42 XOR 40 = 02
```

Recovered:

```text
01 02
```

## Mental Model

Think:

```text
Known Plaintext
↓
Recover Keystream
↓
Recover More Plaintext
```

## Analyst Mindset

Do not ask:

```text
Can I recover everything?
```

Ask:

```text
Do I know any plaintext?
```

Even a small known fragment can be useful.

## Observation Habit

Look for:

- file headers
- common words
- protocol markers
- predictable structures
- repeated fields

Known plaintext often appears naturally.

## Example

PNG files start with:

```text
89 50 4E 47
```

If ciphertext is known:

```text
Ciphertext
XOR
Known PNG Header
=
Keystream
```

## Transferable Mental Model

```text
Known Plaintext
+
Ciphertext
=
Keystream

Keystream
+
Ciphertext
=
Plaintext
```

Small knowledge can reveal larger structures.

# QA

**Q1.**

Complete:

```text
P XOR C = __
```

<details>
<summary><strong>A1.</strong></summary>


</details>

**Q2.**

Why can known plaintext be valuable during analysis?

<details>
<summary><strong>A2.</strong></summary>


</details>

**Q3.**

Given:

```text
P = 0x41
C = 0x40
```

Recover K.

<details>
<summary><strong>A3.</strong></summary>


</details>

**Q4.**

Given:

```text
P = 0x42
C = 0x40
```

Recover K.

<details>
<summary><strong>A4.</strong></summary>


</details>

**Q5.**

Given:

```text
K = 0x01
C = 0x40
```

Recover P.

<details>
<summary><strong>A5.</strong></summary>


</details>

**Q6.**

Given:

```text
K = 0x02
C = 0x40
```

Recover P.

<details>
<summary><strong>A6.</strong></summary>


</details>

**Q7.**

What is the first question an analyst should ask when seeing ciphertext?

<details>
<summary><strong>A7.</strong></summary>


</details>

**Q8.**

Why is recovering a keystream useful?

<details>
<summary><strong>A8.</strong></summary>


</details>

**Q9.**

Given:

```text
Known Plaintext

41 42

Ciphertext

40 40
```

Recover the keystream.

<details>
<summary><strong>A9.</strong></summary>


</details>

**Q10.**

Complete:

```text
Known Plaintext
+
Ciphertext
=
________
```

<details>
<summary><strong>A10.</strong></summary>


</details>

**Q11.**

Why are file headers useful in crypto analysis?

<details>
<summary><strong>A11.</strong></summary>


</details>

**Q12.**

What does a PNG header example demonstrate?

<details>
<summary><strong>A12.</strong></summary>


</details>

**Q13.**

Explain:

```text
Known Plaintext
→ Recover Keystream
→ Recover More Plaintext
```

<details>
<summary><strong>A13.</strong></summary>


</details>

**Q14.**

In one sentence, explain the idea of a known plaintext attack.

<details>
<summary><strong>A14.</strong></summary>


</details>

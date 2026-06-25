# Session 03 — Single-Byte XOR by Hand

## Objective

Move from bits to bytes.

Observe XOR on actual byte values.

---

## Important Observation

Computers do not XOR characters.

Computers XOR bytes.

Example:

```text
"A"
↓
ASCII
↓
0x41
↓
XOR
↓
0x40
```

The operation happens on bytes.

---

## Character vs Byte

Character:

```text
A
```

Representation:

```text
0x41
```

Transformation:

```text
0x41 XOR 0x01
```

Result:

```text
0x40
```

Always separate:

character

from

byte value

---

## Reversibility

```text
P XOR K = C

C XOR K = P
```

Example:

```text
0x41 XOR 0x01 = 0x40

0x40 XOR 0x01 = 0x41
```

---

## Crypto Mindset

Do not think:

```text
"A" became "@"
```

Think:

```text
0x41 became 0x40
```

Characters are only human-friendly views.

Bytes are the real data.

---

## Observation Habit

When seeing data:

```text
41 42 43 44
```

```
Ask:
- bytes?
- hex?
- ASCII?
- transformed?
- XOR?
```

---

## Transferable Mental Model

```text
Character
→ Byte
→ Transformation
→ Byte
→ Character
```

Crypto operations happen in the byte layer.

---

# QA

### Q1

What is the hexadecimal value of the ASCII character `A`?

<details>
<summary><strong>A</strong></summary>

0x41

</details>

---

### Q2

Calculate the following expression.

0x41 XOR 0x03

<details>
<summary><strong>A</strong></summary>

= 0x43

</details>

---

### Q3

Find `C` in the following expression.

P = 0x41

K = 0x01

C = P XOR K

<details>
<summary><strong>A</strong></summary>

C = 0x40

</details>

---

### Q4

Find `P` in the following expression.

C = 0x40

K = 0x01

P = C XOR K

<details>
<summary><strong>A</strong></summary>

P = 0x41

</details>

---

### Q5

Why do we say XOR transforms bytes rather than characters?

<details>
<summary><strong>A</strong></summary>

Computers do not XOR characters. They XOR byte values.

</details>

---

### Q6

Calculate the following expression.

(0x41 XOR 0x03) XOR 0x03

<details>
<summary><strong>A</strong></summary>

= 0x41

</details>

---

### Q7

Why is it important to examine bytes before characters in XOR analysis?

<details>
<summary><strong>A</strong></summary>

Characters are only a human-friendly view; the actual calculation operates
on bytes.

</details>

---

## Key Takeaways

- XOR operates on byte values rather than characters.
- Characters, hexadecimal values, and ASCII are representations of underlying bytes.
- Single-byte XOR applies one byte-sized key value to the data.
- Applying the same key again restores the original byte.
- Inspect the byte representation before interpreting transformed data as text.

# Single-Byte XOR

Single-Byte XOR by Hand

## Session Goal

Move from bits to bytes.

Observe XOR on actual byte values.

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

## Transferable Mental Model

```text
Character
→ Byte
→ Transformation
→ Byte
→ Character
```

Crypto operations happen in the byte layer.

# QA

**Q1.**

What is the hexadecimal value of the ASCII character `A`?

<details>
<summary><strong>A1.</strong></summary>

0x41

</details>

---

**Q2.**

What is the hexadecimal value of the ASCII character `B`?

<details>
<summary><strong>A2.</strong></summary>

0x42

</details>

---

**Q3.**

Calculate the following expression.

0x41 XOR 0x00

<details>
<summary><strong>A3.</strong></summary>

= 0x41

</details>

---

**Q4.**

Calculate the following expression.

0x41 XOR 0x01

<details>
<summary><strong>A4.</strong></summary>

= 0x40

</details>

---

**Q5.**

Calculate the following expression.

0x41 XOR 0x03

<details>
<summary><strong>A5.</strong></summary>

= 0x43

</details>

---

**Q6.**

Find `C` in the following expression.

P = 0x41

K = 0x01

C = P XOR K

<details>
<summary><strong>A6.</strong></summary>

C = 0x40

</details>

---

**Q7.**

Find `P` in the following expression.

C = 0x40

K = 0x01

P = C XOR K

<details>
<summary><strong>A7.</strong></summary>

P = 0x41

</details>

---

**Q8.**

Why do we say XOR transforms bytes rather than characters?

<details>
<summary><strong>A8.</strong></summary>

Computers do not XOR characters. They XOR byte values.

</details>

---

**Q9.**

Explain the following statement.

`"A" XOR 0x01`

is actually:

`0x41 XOR 0x01`

<details>
<summary><strong>A9.</strong></summary>

The hexadecimal ASCII value of `A` is `0x41`.

</details>

---

**Q10.**

Which statement is the most accurate?

A. XOR transforms strings.

B. XOR transforms bytes.

C. XOR transforms ASCII.

D. XOR transforms character meaning.

<details>
<summary><strong>A10.</strong></summary>

B

</details>

---

**Q11.**

Calculate the following expression.

0x42 XOR 0x03

<details>
<summary><strong>A11.</strong></summary>

= 0x41

</details>

---

**Q12.**

Calculate the following expression.

(0x41 XOR 0x03) XOR 0x03

<details>
<summary><strong>A12.</strong></summary>

= 0x41

</details>

---

**Q13.**

Why is it important to examine bytes before characters in XOR analysis?

<details>
<summary><strong>A13.</strong></summary>

Characters are only a human-friendly view; the actual calculation operates
on bytes.

</details>

---

**Q14.**

What question should you ask first when seeing the following data?

```text
41 42 43 44
```

<details>
<summary><strong>A14.</strong></summary>

ASCII-like?

</details>

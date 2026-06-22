# Detecting Repeating Patterns

## Session Goal

Learn to observe signs of key reuse.

## Key Observation

A short key must repeat.

Example:

```text
Key

01 02 03

Applied

01 02 03
01 02 03
01 02 03
...
```

The longer the plaintext becomes,

the more often the key repeats.

## Why This Matters

Repeated key usage can create:

- repeated relationships
- repeated transformations
- observable structure

These clues may help an analyst infer:

- key length
- key reuse
- transformation behavior

## Important Distinction

A repeated pattern does not prove XOR.

However:

```text
repeated pattern
→ possible key reuse
→ possible Repeating-Key XOR
```

is a reasonable hypothesis.

## Analyst Mindset

Do not immediately ask:

```text
What is the key?
```

First ask:

```text
Do I see repetition?
```

Then ask:

```text
Could a short key be reused?
```

## Observation Habit

Look for:

- repeating blocks
- repeating relationships
- periodic structure
- recurring transformations

## Transferable Mental Model

Ciphertext

→ Observe

→ Find repetition

→ Hypothesize key reuse

→ Test hypothesis

Observation comes before recovery.

# QA

**Q1.** What is a repeating pattern in the context of Repeating-Key XOR?

<details>
<summary><strong>A1.</strong></summary>
A pattern that appears again and again because a short key is reused.</details>


---

**Q2.**

Given the following key:

```text
01 02 03
```

Write the key bytes that would be applied to:

```text
P1 P2 P3 P4 P5 P6 P7
```

<details>
<summary><strong>A2.</strong></summary>
P1 P2 P3 P4 P5 P6 P7
01 02 03 01 02 03 01</details>

---

**Q3.** Why is key length important when analyzing Repeating-Key XOR?

<details>
<summary><strong>A3.</strong></summary>
Because the key length determines how often the pattern repeats./details>


---

**Q4.**

Calculate:

```text
0x41 XOR 0x01
```

<details>
<summary><strong>A4.</strong></summary>
0x40</details>

---

**Q5.**

Calculate:

```text
0x42 XOR 0x02
```

<details>
<summary><strong>A5.</strong></summary>
0x40</details>

---

**Q6.**

Calculate:

```text
0x43 XOR 0x03
```

<details>
<summary><strong>A6.</strong></summary>
0x40</details>


---

**Q7.**

Calculate:

```text
0x44 XOR 0x01
```

<details>
<summary><strong>A7.</strong></summary>
0x45</details>


---

**Q8.** What observation might suggest that a short key is being reused?

<details>
<summary><strong>A8.</strong></summary>
repeated structures, repeated relationships, periodic patterns</details>


---

**Q9.** Why does a repeating key sometimes leave detectable patterns?

<details>
<summary><strong>A9.</strong></summary>
Because the same key bytes are reused again and again</details>


---

**Q10.**

Complete the sequence:

```text
Key:

01 02 03

Applied:

01 02 03 __ __ __ __
```

<details>
<summary><strong>A10.</strong></summary>
01 02 03 01 02 03 01</details>


---

**Q11.** Why is Repeating-Key XOR generally weaker than using a completely unique key for every byte?

<details>
<summary><strong>A11.</strong></summary>
Repeated key usage can create:

repeated relationships

repeated transformations

observable structure </details>

---

**Q12.**

Explain the difference between:

```text
Single-Byte XOR
```

and

```text
Repeating-Key XOR
```

<details>
<summary><strong>A12.</strong></summary>
Single-Bytes XOR uses one key byte.
Repeating-key XOR uses multiple key bytes that repeat.</details>

---

**Q13.** When analyzing ciphertext, why should repeated structures attract attention?

<details>
<summary><strong>A13.</strong></summary>
Because repeated structures may indicate key reuse</details>


---

**Q14.** In one sentence, explain why pattern detection is useful in crypto analysis.

<details>
<summary><strong>A14.</strong></summary>
Patterns may reveal key reuse and transformation behavior</details>


# Session 06 — Repeating-Key XOR

## Metadata

```yaml
Roadmap: Cryptography
Phase: 02
Session: 06
Title: Repeating-Key XOR
Status:
Review:
ArchiveVersion: 2
Date:
```

## Objective

Understand how a key can be reused across many bytes.

---

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

---

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

---

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

---

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

---

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

---

## Observation Habit

When analyzing ciphertext:

Ask:

- Is there a repeating pattern?
- Could a short key be reused?
- Does the data look transformed by repeating bytes?

---

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

---

# Review Questions

### Q1. What is repeating-key XOR?

<details>
<summary>A</summary>

A short key is reused repeatedly across the plaintext.

</details>

---

### Q2. Which key byte is applied to each position in the following plaintext?

```text
Plaintext:
A B C D E F

Key:
X Y
```

Write the key sequence aligned with every plaintext position.

<details>
<summary>A</summary>

A B C D E F
X Y X Y X Y

</details>

---

### Q3. XOR the following plaintext and key.

```text
Plaintext:

0x41 0x42 0x43 0x44

Key:

0x01 0x02
```

Write the result after repeating the key.

<details>
<summary>A</summary>

= 0x40 0x40 0x42 0x46

</details>

---

### Q4. Which sequence correctly represents repeating-key XOR?

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
<summary>A</summary>

B
</details>

---

### Q5. Why does repeating-key XOR appear more complex than single-byte XOR?

<details>
<summary>A</summary>

Because different key bytes are used at different positions.


</details>

---

### Q6. How is repeating-key XOR conceptually related to a stream cipher?

<details>
<summary>A</summary>

Both XOR plaintext with a keystream. Repeating-key XOR creates that
keystream by repeating a short key, while a stream cipher usually generates
it dynamically.

</details>

---

### Q7. Why is repeating-key XOR reversible?

<details>
<summary>A</summary>

Because XOR is reversible and the same repeating key can be applied again.



</details>

---

### Q8. Why can a repeated ciphertext pattern suggest repeating-key XOR?

<details>
<summary>A</summary>

Because reuse of a short key may leave periodic relationships in the
ciphertext.



</details>

---

## Key Takeaways

- Repeating-key XOR cycles a short key across a longer plaintext.
- Each plaintext byte is XORed with the key byte aligned to its position.
- The repeated key forms a predictable keystream.
- XOR remains reversible when the same repeated key sequence is applied again.
- Periodic ciphertext relationships can suggest reuse of a short key.

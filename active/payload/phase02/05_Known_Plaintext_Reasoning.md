# Session 10 — Known Plaintext Reasoning

```yaml
Roadmap: Cryptography
Phase: Phase 02 — XOR & Stream Cipher Intuition
Session: Session 10
Title: Known Plaintext Reasoning
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-07-03
```

---

## Objective

Understand how knowing part of a plaintext and its matching ciphertext allows partial keystream recovery in XOR-based stream encryption.

This session connects the basic XOR relationship:

```text
P XOR K = C
```

to the practical attack idea:

```text
Known Plaintext + Matching Ciphertext
        ↓
Partial Keystream Recovery
        ↓
Partial Decryption of Other Ciphertexts
```

---

## Learning Summary

In a stream cipher, plaintext is encrypted by XORing it with a keystream.

```text
Plaintext XOR Keystream = Ciphertext
```

Because XOR is reversible, any two known values in the relationship can recover the third.

If the attacker knows both:

```text
Plaintext byte
Ciphertext byte
```

then the attacker can recover the corresponding keystream byte.

```text
Plaintext XOR Ciphertext = Keystream
```

This is the basis of known plaintext reasoning.

The recovered keystream is only useful for the same byte positions. If the attacker recovers `K[0..4]`, that keystream segment can decrypt another ciphertext only at positions `0..4`, assuming the same keystream was reused.

---

## Key Concepts

- Known plaintext
- Matching ciphertext
- Partial keystream recovery
- Byte position alignment
- Keystream reuse
- XOR reversibility

---

## Core Relationship

Starting from encryption:

```text
P XOR K = C
```

To recover the keystream, XOR both sides with `P`.

```text
P XOR C
= P XOR (P XOR K)
= (P XOR P) XOR K
= 0 XOR K
= K
```

Therefore:

```text
P XOR C = K
```

This means:

```text
Known Plaintext Byte XOR Matching Ciphertext Byte = Keystream Byte
```

---

## Position Matters

Keystream recovery is position-specific.

```text
P[0] XOR C[0] = K[0]
P[1] XOR C[1] = K[1]
P[2] XOR C[2] = K[2]
```

If `"HELLO"` is known to be the first five plaintext bytes, then the attacker can recover only the first five keystream bytes.

```text
P[0..4] XOR C[0..4] = K[0..4]
```

That recovered keystream segment can decrypt another ciphertext only at the same positions.

```text
C2[0..4] XOR K[0..4] = P2[0..4]
```

It cannot directly decrypt `C2[10..14]`, because that would require `K[10..14]`.

---

## Practical Python Pattern

If the known plaintext is a Python string:

```python
plain = "HELLO"
cipher = bytes.fromhex("c0 c1 c2 c3 c4")

keystream = []

for p, c in zip(plain, cipher):
    k = ord(p) ^ c
    keystream.append(k)

print(keystream)
print(bytes(keystream).hex())
```

Here, `ord(p)` converts each character into its integer byte value.

Example:

```text
'H' -> ord('H') -> 0x48
```

---

## Byte-Oriented Python Pattern

For crypto work, using `bytes` directly is usually cleaner.

```python
plain = b"HELLO"
cipher = bytes.fromhex("c0 c1 c2 c3 c4")

keystream = bytes(p ^ c for p, c in zip(plain, cipher))

print(keystream.hex())
```

When `plain` is already a `bytes` object, each `p` is already an integer byte value, so `ord()` is unnecessary.

---

## Using Recovered Keystream on Another Ciphertext

If the same keystream was reused, the recovered keystream can decrypt the matching positions of another ciphertext.

```python
recovered_keystream = bytes.fromhex("88 99 aa bb cc")
other_ciphertext = bytes.fromhex("c0 d1 e2 f3 04")

other_plaintext = bytes(
    k ^ c for k, c in zip(recovered_keystream, other_ciphertext)
)

print(other_plaintext.hex())
print(other_plaintext.decode(errors="replace"))
```

The relationship is:

```text
Other Ciphertext XOR Recovered Keystream = Other Plaintext
```

Position-by-position:

```text
C2[0] XOR K[0] = P2[0]
C2[1] XOR K[1] = P2[1]
C2[2] XOR K[2] = P2[2]
```

---

## Attack Flow

```text
1. The attacker knows part of a plaintext and its matching ciphertext.

2. The attacker computes:

   Plaintext XOR Ciphertext = Keystream

3. The attacker recovers part of the keystream.

4. If another ciphertext used the same keystream at the same positions,

5. The attacker computes:

   Other Ciphertext XOR Recovered Keystream = Other Plaintext
```

---

## Practical Observations

### Observation 1

```text
Prediction:
If plaintext and matching ciphertext are known, the keystream can be recovered.

Observation:
Plaintext XOR Ciphertext produces the corresponding keystream bytes.

Explanation:
Because P XOR K = C, rearranging with XOR gives P XOR C = K.
```

---

### Observation 2

```text
Prediction:
Recovered keystream can decrypt another ciphertext encrypted with the same keystream.

Observation:
Other Ciphertext XOR Recovered Keystream produces other plaintext bytes.

Explanation:
Stream cipher decryption uses C XOR K = P.
```

---

### Observation 3

```text
Prediction:
Recovered keystream is only useful for the same byte positions.

Observation:
K[0..4] decrypts C2[0..4], but not C2[10..14].

Explanation:
Stream ciphers apply keystream byte-by-byte. Each plaintext byte depends on the keystream byte at the same position.
```

---

## Common Misconceptions

### Misconception 1

Known plaintext immediately reveals the full secret key.

Correct understanding:

Known plaintext reveals only the corresponding keystream bytes, not necessarily the original secret key.

---

### Misconception 2

Recovered keystream bytes can decrypt any part of another ciphertext.

Correct understanding:

Recovered keystream bytes are position-specific. `K[0..4]` can decrypt only positions `0..4`.

---

### Misconception 3

The other plaintext or ciphertext must be the same.

Correct understanding:

The plaintexts and ciphertexts do not need to be the same. The required condition is reuse of the same keystream at the same positions.

---

## Connections

```text
XOR Reversibility
        ↓
Plaintext / Keystream / Ciphertext Relationship
        ↓
Known Plaintext Reasoning
        ↓
Partial Keystream Recovery
        ↓
Stream Reuse Risk
```

This session connects directly to stream cipher misuse. If a keystream is reused, a small amount of known plaintext can expose part of the keystream, which can then expose corresponding positions in other ciphertexts.

---

## Key Takeaways

- In XOR-based stream encryption, any two of `P`, `K`, and `C` can recover the third.
- Known plaintext plus matching ciphertext reveals the corresponding keystream bytes.
- The core recovery formula is `P XOR C = K`.
- Recovered keystream is position-specific.
- Another ciphertext can be partially decrypted only if it reused the same keystream at the same positions.
- Known plaintext reasoning is a practical bridge from XOR theory to stream cipher attack intuition.

---

# Review Questions

### Q1. What does “known plaintext” mean in this session?

<details>
<summary>A</summary>

&nbsp;

</details>

---

### Q2. Starting from `P XOR K = C`, derive the formula for recovering `K`.

<details>
<summary>A</summary>

&nbsp;

</details>

---

### Q3. Why must the known plaintext byte and ciphertext byte be from the same position?

<details>
<summary>A</summary>

&nbsp;

</details>

---

### Q4. In Python, why is `ord(p)` needed when `plain = "HELLO"` but not when `plain = b"HELLO"`?

<details>
<summary>A</summary>

&nbsp;

</details>

---

### Q5. If an attacker recovers `K[0..4]`, which part of another ciphertext can be decrypted with it?

<details>
<summary>A</summary>

&nbsp;

</details>

---

### Q6. What condition must be true before recovered keystream bytes can decrypt another ciphertext?

<details>
<summary>A</summary>

&nbsp;

</details>

---

### Q7. Why does known plaintext usually recover only part of a keystream rather than the entire secret key?

<details>
<summary>A</summary>

&nbsp;

</details>

---

## Next Session

```text
Next:
Phase 02
Session 11

Topic:
Recovering Partial Keystreams
```

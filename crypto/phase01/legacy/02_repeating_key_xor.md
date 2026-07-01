# Repeating-Key XOR

## Core Concept

Repeating-key XOR uses:

```text
a short key
reused across the whole plaintext
```

So the real object being applied is not just the key itself,
but:

```text
the expanded keystream
```

---

# Key Repetition

Example:

```python
text = b"HELLO"
key = b"KEY"
```

The key flow becomes:

```text
K E Y K E
```

Typical implementation:

```python
key[i % len(key)]
```

Important idea:

```text
the short key is repeated to match the plaintext length
```

---

# Encryption Flow

Example:

```python
cipher = bytes([
    text[i] ^ key[i % len(key)]
    for i in range(len(text))
])
```

Important properties:

* XOR does not change length
* the result may be non-printable
* `cipher.hex()` is often added only for readability

So:

```text
repeating-key XOR is a real transformation
hex is only a representation layer
```

---

# Decryption Flow

XOR is self-inverse.

That means:

```text
plaintext ^ key -> cipher
cipher ^ key    -> plaintext
```

If the ciphertext is written as hex first,
the reverse order is:

```text
hex string
→ fromhex()
→ cipher bytes
→ XOR again
→ plaintext bytes
```

---

# Keystream Thinking

In practice, it is useful to think in terms of:

```text
plaintext
↔ keystream
↔ cipher
```

not just:

```text
plaintext
↔ key
```

Why:

```text
the keystream is the actual byte sequence used at each position
```

This becomes especially important when analyzing leakage.

---

# Known Plaintext and Recovery

If:

```text
cipher = plaintext ^ keystream
```

then:

```text
cipher ^ plaintext = keystream
```

This means known plaintext reveals the keystream segment used at that location.

Important consequence:

* longer known plaintext reveals a longer segment
* repeated key patterns become visible
* reuse creates analysis opportunities

---

# Representation vs Real Recovery

When you see:

```python
cipher_hex = "030015070a"
```

remember:

* this is not the actual ciphertext state
* it is a printable wrapper around ciphertext bytes
* `fromhex()` restores the real bytes
* XOR is still the real reversal step

---

# Why This Session Matters

This session introduces the idea that crypto analysis often becomes:

```text
index-by-index byte flow tracking
```

It also sets up later topics:

* known-plaintext attacks
* keystream reuse
* nonce and IV importance

# QA

## Step 1 — Key Flow Recognition

Infer the key flow for the following values.

```python
text = b"HELLO"
key = b"KEY"
```

**Q1.**
Why is it called repeating-key XOR?

<details>
<summary><strong>A1.</strong></summary>

Because a short key is repeated to match the plaintext length.

</details>

---

**Q2.**
What key sequence aligns with `HELLO`?

<details>
<summary><strong>A2.</strong></summary>

KEYKE

</details>

---

**Q3.**
How is repetition implemented?

<details>
<summary><strong>A3.</strong></summary>

`i % len(key)` cycles through the key indexes.

</details>

## Step 2 — Pair Observation

Determine whether XOR has occurred in the following code.

```python
for i in range(len(text)):
    p = text[i]
    k = key[i % len(key)]
```

**Q1.**
Has encryption occurred at this point?

<details>
<summary><strong>A1.</strong></summary>

No. This step only observes how plaintext bytes align with key bytes.

</details>

---

**Q2.**
Why is the `%` operator required?

<details>
<summary><strong>A2.</strong></summary>

Because the index must return to the beginning after reaching the end of the
key.

</details>

---

**Q3.**
What is the main relationship to observe?

<details>
<summary><strong>A3.</strong></summary>

Which key byte is paired with each plaintext byte.

</details>

## Step 3 — Cipher State Recognition

Classify the result of the following code.

```python
cipher = bytes([
    text[i] ^ key[i % len(key)]
    for i in range(len(text))
])
```

**Q1.**
Is `cipher` plaintext or transformed bytes?

<details>
<summary><strong>A1.</strong></summary>

transformed bytes

</details>

---

**Q2.**
Why might it be difficult to read directly?

<details>
<summary><strong>A2.</strong></summary>

Because it may contain raw byte values outside the printable ASCII range.

</details>

---

**Q3.**
Why is `cipher.hex()` useful?

<details>
<summary><strong>A3.</strong></summary>

It displays raw bytes through a human-readable hexadecimal representation.

</details>

## Step 4 — Reverse Logic

Explain the recovery logic in the following code.

```python
plain = bytes([
    cipher[i] ^ key[i % len(key)]
    for i in range(len(cipher))
])
```

**Q1.**
Why does XORing with the same key recover the plaintext?

<details>
<summary><strong>A1.</strong></summary>

Because XOR is self-inverse: `A ^ B ^ B = A`.

</details>

---

**Q2.**
If the value is a hex string, what must happen before decryption?

<details>
<summary><strong>A2.</strong></summary>

Use `bytes.fromhex()` to restore the raw ciphertext bytes.

</details>

---

**Q3.**
Does `decode()` perform the actual decryption?

<details>
<summary><strong>A3.</strong></summary>

No. It converts bytes into a string interpretation.

</details>

## Step 5 — Keystream Thinking

Determine what the following code recovers.

```python
keystream = bytes([
    cipher[i] ^ plaintext[i]
    for i in range(len(cipher))
])
```

**Q1.**
What does `keystream` represent?

<details>
<summary><strong>A1.</strong></summary>

It is the sequence of key bytes actually used at each XOR position.

</details>

---

**Q2.**
Why might a repeating pattern appear?

<details>
<summary><strong>A2.</strong></summary>

Because a short key is reused.

</details>

---

**Q3.**
Why is known plaintext a useful attack clue?

<details>
<summary><strong>A3.</strong></summary>

Because it directly reveals the keystream covering the known plaintext
range.

</details>

## Mini Task

Explain the following flow step by step.

```python
text = b"HELLO"
key = b"KEY"
cipher = bytes([text[i] ^ key[i % len(key)] for i in range(len(text))])
```

Answer format:

```text
text:
type:
meaning:

key:
type:
meaning:

cipher:
type:
meaning:
```

# Keystream Reuse

## Core Concept

The dangerous part of repeating-key XOR is not only that a key exists,
but that:

```text
the effective keystream is reused
```

Once that happens, relationships start to leak.

---

# Keystream vs Key

A short key becomes an expanded keystream when applied to plaintext.

Example:

```text
key      = KEY
plaintext length = 5
keystream = KEYKE
```

What matters in analysis is often:

```text
which keystream byte touched which plaintext byte
```

---

# Known Plaintext Recovery

If:

```text
cipher = plaintext ^ keystream
```

then:

```text
cipher ^ plaintext = keystream
```

This means that known plaintext directly reveals the keystream segment used for that range.

Important consequence:

* short known plaintext reveals a short segment
* longer known plaintext reveals more
* repeated structure makes patterns easier to spot

---

# Partial Recovery Still Matters

Even if the full key is not recovered,
partial keystream recovery is still useful.

Why:

* other ciphertexts may reuse the same positions
* forgery attempts may become easier
* structural guesses become more realistic

So:

```text
partial leakage is still meaningful leakage
```

---

# Two Ciphertexts with the Same Keystream

If two ciphertexts reuse the same keystream:

```text
c1 = p1 ^ k
c2 = p2 ^ k
```

then:

```text
c1 ^ c2 = p1 ^ p2
```

The keystream cancels out.

This is dangerous because the relation between plaintexts becomes visible even when neither plaintext is fully known.

---

# Why Reuse Is the Real Problem

The issue is not simply:

```text
"XOR is weak"
```

The issue is:

```text
reusing the same keystream creates reusable structure for the attacker
```

This is the same reason one-time pads must never reuse key material.

---

# Link to Stream Ciphers

This session is conceptually important because many stream-cipher safety rules are really about:

```text
preventing keystream reuse
```

That is why nonce and IV design matter later.

They are not decoration.

They exist to stop the same effective stream from appearing again.

---

# Why This Session Matters

This session shifts the mental model from:

```text
I have ciphertext
```

to:

```text
I have byte relationships caused by keystream reuse
```

That shift is essential for understanding both attacks and safe design.

# QA

## Step 1 — Keystream Observation

Identify the main object to observe in the following structure.

```python
plaintext = b"HELLO"
key = b"KEY"
cipher = bytes([
    plaintext[i] ^ key[i % len(key)]
    for i in range(len(plaintext))
])
```

**Q1.**
Why is the length preserved?

<details>
<summary><strong>A1.</strong></summary>

Because XOR transforms one byte at each position without changing the number
of bytes.

</details>

---

**Q2.**
What does the effective key sequence look like?

<details>
<summary><strong>A2.</strong></summary>

A repeated keystream such as `KEYKE`.

</details>

---

**Q3.**
Is the primary focus of this session the ciphertext or the keystream?

<details>
<summary><strong>A3.</strong></summary>

keystream

</details>

## Step 2 — Recovering the Keystream

Explain why the following code recovers the keystream.

```python
recovered = bytes([
    plaintext[i] ^ cipher[i]
    for i in range(len(cipher))
])
```

**Q1.**
Why does `plaintext ^ cipher` recover the keystream?

<details>
<summary><strong>A1.</strong></summary>

Because `cipher = plaintext ^ keystream`; XORing with the plaintext again
cancels the plaintext and leaves the keystream.

</details>

---

**Q2.**
Why might the result contain a repeating pattern?

<details>
<summary><strong>A2.</strong></summary>

Because a short key is repeated to form the keystream.

</details>

---

**Q3.**
Why is known plaintext important?

<details>
<summary><strong>A3.</strong></summary>

Because it directly recovers the keystream segment used over the known
plaintext range.

</details>

## Step 3 — Partial Knowledge

Determine what increases in the following code as `known` grows.

```python
partial = bytes([cipher[i] ^ known[i] for i in range(len(known))])
```

**Q1.**
What increases as `known` becomes longer?

<details>
<summary><strong>A1.</strong></summary>

The recoverable keystream segment.

</details>

---

**Q2.**
Why is the complete key not always recovered immediately?

<details>
<summary><strong>A2.</strong></summary>

Because only the keystream positions covered by known plaintext are exposed.

</details>

---

**Q3.**
Why is partial information still dangerous?

<details>
<summary><strong>A3.</strong></summary>

Because it may help analyze or forge data at matching positions in other
ciphertexts.

</details>

## Step 4 — Two-Ciphertext Problem

Determine what remains after the following operation.

```python
x = bytes([c1[i] ^ c2[i] for i in range(len(c1))])
```

**Q1.**
Is `x` the key or another relationship?

<details>
<summary><strong>A1.</strong></summary>

It is `p1 ^ p2`, which remains after the shared keystream cancels.

</details>

---

**Q2.**
Why is this value useful for analysis?

<details>
<summary><strong>A2.</strong></summary>

Because it can reveal differences and structural relationships between the
two plaintexts.

</details>

---

**Q3.**
Why is this called a reuse problem?

<details>
<summary><strong>A3.</strong></summary>

Because the same keystream is used for multiple messages.

</details>

## Step 5 — State Classification

Classify the following values by state.

```python
A = plaintext
B = cipher
C = recovered
D = bytes([c1[i] ^ c2[i] for i in range(len(c1))])
```

Possible states:

* plaintext bytes
* cipher bytes
* recovered keystream
* plaintext relation

**Q1.**
State of `A`:

<details>
<summary><strong>A1.</strong></summary>

plaintext bytes

</details>

---

**Q2.**
State of `B`:

<details>
<summary><strong>A2.</strong></summary>

cipher bytes

</details>

---

**Q3.**
State of `C`:

<details>
<summary><strong>A3.</strong></summary>

recovered keystream

</details>

---

**Q4.**
State of `D`:

<details>
<summary><strong>A4.</strong></summary>

plaintext relation

</details>

## Mini Task

Briefly explain the following sequence.

```text
known plaintext
↓
recover keystream segment
↓
analyze another ciphertext
```

Answer format:

```text
step1:
step2:
step3:
```

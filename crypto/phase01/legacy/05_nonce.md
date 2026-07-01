# Nonce

## Core Concept

A nonce is important not because it must be secret,
but because it helps ensure:

```text
the keystream is different each time
```

The real safety target is:

```text
keystream uniqueness
```

---

# Why Nonce Exists

If the same key always produced the same effective stream,
then identical reuse problems would appear again.

So the nonce acts as an additional input to keystream generation.

Mental model:

```text
key + nonce
→ keystream
→ XOR with plaintext
→ ciphertext
```

---

# Same Key, Different Nonce

The key point is:

```text
same key
different nonce
different keystream
```

If the keystream changes,
even the same plaintext can produce a different ciphertext.

That is exactly the desired outcome.

---

# Nonce Does Not Need Secrecy

The nonce does not usually need to be hidden.

What matters is not:

```text
can the attacker see the nonce?
```

but:

```text
is the nonce reused under the same key?
```

Visibility is usually acceptable.

Reuse is the real danger.

---

# Reuse Brings Back the Old Problem

If the same key and same nonce are reused,
the same effective keystream can reappear.

Then the Session04 problem returns:

```text
c1 ^ c2 = p1 ^ p2
```

So nonce misuse is often just another path back to keystream reuse.

---

# Wrapper vs Real Security

A token may later be wrapped in base64,
but base64 does not solve the reuse problem.

Important distinction:

* XOR with reused keystream creates leakage
* base64 only makes the bytes printable

These are completely different concerns.

---

# Practical Mental Model

When thinking about nonce design, ask:

```text
Will this input prevent the same effective keystream from appearing again?
```

That question is more useful than asking whether the nonce is “mysterious” or “hidden.”

---

# Why This Session Matters

This session reframes nonce as a structural safety tool.

The point is not decoration, metadata, or secrecy.

The point is:

```text
do not let the same byte stream come back
```

# QA

## Step 1 — Toy Nonce Mixing

Infer the role of the nonce in the following example.

```python
plaintext = b"HELLO"
key = 0x23
nonce = 0x10
keystream = bytes([key ^ nonce for _ in plaintext])
```

**Q1.**
Why does this example compute `key ^ nonce`?

<details>
<summary><strong>A1.</strong></summary>

This toy example illustrates that both the key and nonce influence the
keystream.

</details>

---

**Q2.**
Why is the same value repeated?

<details>
<summary><strong>A2.</strong></summary>

Because this code repeats the single byte `key ^ nonce` to match the
plaintext length.

</details>

---

**Q3.**
Do real stream ciphers always work this way?

<details>
<summary><strong>A3.</strong></summary>

No. This is only a simplified example of the nonce's role.

</details>

## Step 2 — Effect of Changing the Nonce

Explain what the following change affects.

```python
nonce2 = 0x20
keystream2 = bytes([key ^ nonce2 for _ in plaintext])
```

**Q1.**
Why does the keystream change?

<details>
<summary><strong>A1.</strong></summary>

Because the nonce input used for keystream generation changed.

</details>

---

**Q2.**
Why does the result change even though the key is the same?

<details>
<summary><strong>A2.</strong></summary>

Because a different nonce changes the input combination used to generate the
keystream.

</details>

---

**Q3.**
What is the key lesson of this step?

<details>
<summary><strong>A3.</strong></summary>

The nonce, not only the key, affects the generated keystream.

</details>

## Step 3 — Same Plaintext, Different Ciphertext

Explain why the following results differ.

```python
cipher = bytes([plaintext[i] ^ keystream[i] for i in range(len(plaintext))])
cipher2 = bytes([plaintext[i] ^ keystream2[i] for i in range(len(plaintext))])
```

**Q1.**
Why do the ciphertexts differ when the plaintext is identical?

<details>
<summary><strong>A1.</strong></summary>

Because different keystreams were used for XOR.

</details>

---

**Q2.**
Why is this important?

<details>
<summary><strong>A2.</strong></summary>

It helps prevent identical messages from producing repeated ciphertext.

</details>

---

**Q3.**
Does changing the nonce automatically solve every security problem?

<details>
<summary><strong>A3.</strong></summary>

No. Nonces must still be managed so they are not reused under the same key.

</details>

## Step 4 — Danger of Nonce Reuse

Determine what the following code reveals.

```python
same_keystream = bytes([key ^ nonce for _ in range(len(p1))])
c1 = bytes([p1[i] ^ same_keystream[i] for i in range(len(p1))])
c2 = bytes([p2[i] ^ same_keystream[i] for i in range(len(p2))])
x = bytes([c1[i] ^ c2[i] for i in range(len(c1))])
```

**Q1.**
Why does nonce reuse recreate the keystream-reuse problem?

<details>
<summary><strong>A1.</strong></summary>

Because using the same key and nonce generates the same keystream again.

</details>

---

**Q2.**
Why does `c1 ^ c2 = p1 ^ p2` hold?

<details>
<summary><strong>A2.</strong></summary>

Because the shared keystream is XORed twice and cancels out.

</details>

---

**Q3.**
Why is this relationship dangerous?

<details>
<summary><strong>A3.</strong></summary>

Because comparing ciphertexts can reveal relationships between the two
plaintexts.

</details>

## Step 5 — Wrapper Awareness

Distinguish what changes and what remains unchanged.

```python
token = base64.b64encode(cipher)
```

**Q1.**
Does adding Base64 improve the cryptographic security?

<details>
<summary><strong>A1.</strong></summary>

No. It only adds a textual representation layer.

</details>

---

**Q2.**
Why is Base64 still used frequently?

<details>
<summary><strong>A2.</strong></summary>

It makes raw bytes easier to handle in text-based systems.

</details>

---

**Q3.**
What is a common analysis mistake?

<details>
<summary><strong>A3.</strong></summary>

Assuming that analysis is complete after Base64 decoding.

</details>

## Mini Task

Explain the following flow.

```text
same key + same nonce
↓
same keystream
↓
reuse problem
```

Answer format:

```text
cause:
effect:
risk:
```

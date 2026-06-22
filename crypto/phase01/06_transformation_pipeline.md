# Transformation Pipeline

## Core Concept

A token may contain several layers at once.

Example pattern:

```text
plaintext
→ XOR
→ cipher bytes
→ hex
→ base64
→ token
```

The main skill is:

```text
separating real transformation from outer representation layers
```

---

# Real Transformation vs Wrapper

In this pipeline:

* XOR changes the actual byte values
* hex makes bytes printable in one way
* base64 wraps that printable content again

So not every visible step has the same meaning.

Important distinction:

```text
hex and base64 are wrappers
XOR is the real transformation
```

---

# Why Length Changes

Layered tokens often get longer because wrappers expand the visible form.

Typical pattern:

* raw bytes may be compact
* hex turns one byte into two visible characters
* base64 changes the size again for transport-safe representation

So longer token length often suggests:

```text
stacked wrapper layers
```

---

# Reverse Order Matters

Reverse analysis must follow the opposite order of construction.

For the pipeline above:

```text
token
→ base64 decode
→ bytes containing hex text
→ decode bytes→str
→ fromhex()
→ cipher bytes
→ XOR again
→ plaintext
```

If the order is wrong,
the data state will not line up with the next operation.

---

# Representation Recovery vs Real Recovery

Some steps only recover a representation:

* `base64.b64decode()`
* `.decode()`
* `bytes.fromhex()`

Those steps are necessary,
but they do not automatically mean the plaintext is back.

The real semantic recovery happens when the actual transformation is reversed.

In this session, that is:

```text
XOR
```

---

# Fingerprinting Intermediate States

After removing one layer,
do not assume you are done.

Ask:

```text
What state am I looking at now?
```

Common intermediate states:

* raw bytes
* bytes containing hex text
* printable base64-looking bytes
* actual cipher bytes
* plaintext bytes

---

# Why This Session Matters

This session teaches a general reverse-analysis habit:

```text
1. identify the outermost wrapper
2. peel one layer
3. re-classify the new state
4. continue until the real transformation is reached
```

That habit is more important than memorizing one specific token example.

# QA

## Step 1 — Pipeline Recognition

Distinguish the real transformation from the wrappers.

```python
plaintext = b"admin=true"
key = 0x23
cipher = bytes([x ^ key for x in plaintext])
hx = cipher.hex()
token = base64.b64encode(hx.encode())
```

**Q1.**
Why is `hx.encode()` required?

<details>
<summary><strong>A1.</strong></summary>

Because `hx` is a hexadecimal string and must be converted to bytes before
being passed to Base64.

</details>

---

**Q2.**
What content is Base64-encoded in `token`?

<details>
<summary><strong>A2.</strong></summary>

It is the Base64 representation of the byte-encoded result of
`cipher.hex()`.

</details>

---

**Q3.**
Where does the actual data transformation occur?

<details>
<summary><strong>A3.</strong></summary>

At the XOR step.

</details>

## Step 2 — Length and Wrapper Observation

Use the following output to identify where length changes occur.

```python
print("plaintext    :", plaintext)
print("cipher       :", cipher)
print("cipher hex   :", hx)
print("token        :", token)
```

**Q1.**
Why does the token become longer?

<details>
<summary><strong>A1.</strong></summary>

Hex represents each byte with two characters, and Base64 adds another
representation layer.

</details>

---

**Q2.**
At which stages does the length change?

<details>
<summary><strong>A2.</strong></summary>

At the hexadecimal and Base64 stages.

</details>

---

**Q3.**
What do hexadecimal and Base64 both represent in this pipeline?

<details>
<summary><strong>A3.</strong></summary>

Outer representation layers.

</details>

## Step 3 — First Reverse Step

Explain what remains after the following operation.

```python
raw = base64.b64decode(token)
```

**Q1.**
Why is the result bytes?

<details>
<summary><strong>A1.</strong></summary>

Because Base64 decoding restores the inner bytes.

</details>

---

**Q2.**
Why is the result not yet plaintext?

<details>
<summary><strong>A2.</strong></summary>

Because the hexadecimal wrapper remains and XOR has not been reversed.

</details>

---

**Q3.**
Is `raw` plaintext, ciphertext, or hexadecimal string content?

<details>
<summary><strong>A3.</strong></summary>

Bytes containing the hexadecimal representation of the ciphertext.

</details>

## Step 4 — Hex Reconstruction

Explain why the following order is necessary.

```python
cipher2 = bytes.fromhex(raw.decode())
```

**Q1.**
Why is `decode()` called before `fromhex()`?

<details>
<summary><strong>A1.</strong></summary>

Because `fromhex()` expects a hexadecimal string, so the bytes must first be
converted to `str`.

</details>

---

**Q2.**
What state exists after this step?

<details>
<summary><strong>A2.</strong></summary>

raw cipher bytes

</details>

---

**Q3.**
Is this actual decryption or representation recovery?

<details>
<summary><strong>A3.</strong></summary>

Representation recovery.

</details>

## Step 5 — Final Recovery Classification

Classify the following reverse flow.

```text
token
↓ base64 decode
↓ decode()
↓ fromhex()
↓ XOR
```

**Q1.**
Which step performs actual plaintext recovery?

<details>
<summary><strong>A1.</strong></summary>

XOR

</details>

---

**Q2.**
At which step do raw ciphertext bytes appear?

<details>
<summary><strong>A2.</strong></summary>

At the `fromhex()` step.

</details>

---

**Q3.**
How should the remaining steps be classified?

<details>
<summary><strong>A3.</strong></summary>

representation-layer recovery

</details>

## Mini Task

Write the reverse sequence for the following token.

```python
token = base64.b64encode(b"424e4e")
```

Answer format:

```text
1.
2.
3.
4.
```

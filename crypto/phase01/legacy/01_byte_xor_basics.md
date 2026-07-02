# Byte XOR Basics

## Core Idea

Crypto problems are usually closer to:

```text
byte manipulation
```

than to ordinary string processing.

What matters first is:

```text
understanding what state the data is in
```

before trying to transform it.

---

# bytes vs string

Important distinction:

## `str`

Human-readable text.

Example:

```python
"ABC"
```

---

## `bytes`

Actual byte values used by low-level operations.

Example:

```python
b"ABC"
```

Why this matters:

```text
XOR and most crypto-style transformations operate on bytes, not on visual characters
```

---

# Byte Observation

Example:

```python
raw = b"ABC"
list(raw)
```

Result:

```text
[65, 66, 67]
```

This shows:

* bytes are numeric values
* characters are only one way to display them
* the same byte can be viewed in decimal, hex, or binary

---

# Hex Representation

Hex is not encryption.

It is:

```text
a representation layer
```

Example:

```python
raw = b"ABC"
hx = raw.hex()
```

Now:

```python
hx == "414243"
```

Reverse:

```python
bytes.fromhex("414243")
```

Important distinction:

* `.hex()` changes bytes into a hex string
* `fromhex()` restores the original bytes
* no secret key is involved

---

# XOR as Real Transformation

XOR is different from hex.

Hex changes representation.

XOR changes the actual byte values.

Example:

```python
p = ord("A")
k = 0x20
c = p ^ k
r = c ^ k
```

Important property:

```text
A ^ B ^ B = A
```

This is why the same key can both apply and reverse XOR.

---

# Representation vs Transformation

Consider:

```python
raw = b"ABC"
key = 0x20
cipher = bytes([x ^ key for x in raw])
hx = cipher.hex()
```

Meaning:

* `raw` is original bytes
* `cipher` is transformed bytes
* `hx` is only a printable representation of `cipher`

Reverse order:

```text
hex string
→ fromhex()
→ cipher bytes
→ XOR again
→ original bytes
```

---

# Bit-level Intuition

XOR is a bit operation.

Rule:

```text
same bit   -> 0
different  -> 1
```

This matters because later topics such as:

* repeating-key XOR
* token recovery
* known-plaintext analysis

all depend on this same byte and bit model.

---

# Why This Session Matters

This session establishes the basic mental model:

```text
1. identify the current data type
2. separate representation from real transformation
3. track bytes before tracking higher-level meaning
```

Without this distinction, later crypto notes become confusing very quickly.

# QA

## Step 1 — Type Recognition

Classify the type and meaning of each value.

```python
A = "ABC"
B = b"ABC"
C = "414243"
D = b"414243"
```

**Q1.**
Which values have the `bytes` type?

<details>
<summary><strong>A1.</strong></summary>

B, D

</details>

---

**Q2.**
Which value is a human-readable hexadecimal wrapper?

<details>
<summary><strong>A2.</strong></summary>

C

</details>

---

**Q3.**
Which value is printable wrapper data stored as bytes?

<details>
<summary><strong>A3.</strong></summary>

D

</details>

## Step 2 — Hex Representation

Interpret the following code.

```python
raw = b"ABC"
hx = raw.hex()
```

**Q1.**
What is the type of `hx`?

<details>
<summary><strong>A1.</strong></summary>

str

</details>

---

**Q2.**
Is `hx` ciphertext or a representation layer?

<details>
<summary><strong>A2.</strong></summary>

A representation layer.

</details>

---

**Q3.**
Why is the result of `.hex()` easy for humans to read?

<details>
<summary><strong>A3.</strong></summary>

Because it represents bytes with printable hexadecimal characters.

</details>

## Step 3 — Reverse Flow Prediction

Restore the following value.

```python
x = "414243"
```

**Q1.**
What should you do first?

<details>
<summary><strong>A1.</strong></summary>

bytes.fromhex()

</details>

---

**Q2.**
What state does that produce?

<details>
<summary><strong>A2.</strong></summary>

raw bytes

</details>

---

**Q3.**
What should you do next to view it as human-readable text?

<details>
<summary><strong>A3.</strong></summary>

decode()

</details>

## Step 4 — XOR Property

Use the following code to explain an XOR property.

```python
p = ord("A")
k = 0x20
c = p ^ k
r = c ^ k
```

**Q1.**
Why does `r` contain the original value?

<details>
<summary><strong>A1.</strong></summary>

Because XORing with the same key twice restores the original value.

</details>

---

**Q2.**
Which operation performs the actual transformation?

<details>
<summary><strong>A2.</strong></summary>

XOR

</details>

---

**Q3.**
How do hexadecimal conversion and decoding differ from XOR?

<details>
<summary><strong>A3.</strong></summary>

XOR changes the data values. Hex conversion and decoding change how data is
represented or interpreted.

</details>

## Step 5 — State Classification

Classify the following values by state.

```python
A = b"HELLO"
B = "48454c4c4f"
C = b"48454c4c4f"
D = bytes.fromhex("48454c4c4f")
```

Possible states:

* raw bytes
* hex wrapper
* printable wrapper bytes
* restored raw bytes

**Q1.**
State of `A`:

<details>
<summary><strong>A1.</strong></summary>

raw bytes

</details>

---

**Q2.**
State of `B`:

<details>
<summary><strong>A2.</strong></summary>

hex wrapper

</details>

---

**Q3.**
State of `C`:

<details>
<summary><strong>A3.</strong></summary>

printable wrapper bytes

</details>

---

**Q4.**
State of `D`:

<details>
<summary><strong>A4.</strong></summary>

restored raw bytes

</details>

## Mini Task

Explain the following flow.

```python
x = b"HELLO"
y = x.hex()
z = bytes.fromhex(y)
```

Answer format:

```text
x:
type:
meaning:

y:
type:
meaning:

z:
type:
meaning:
```

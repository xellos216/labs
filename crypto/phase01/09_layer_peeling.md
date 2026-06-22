# Layer Peeling

## Core Concept

Reverse analysis is usually not:

```text
decode everything immediately
````

Instead:

```text
observe
→ classify
→ peel ONE layer
→ observe again
```

This is incremental reverse analysis.

---

# Important Skill

The important skill is:

```text id="h2l5kc"
recognizing which layer you are currently observing
```

Example:

```python
b"614756736247383d"
```

This is:

* bytes type
* printable
* hex-looking

Meaning:

```text id="m5w8pw"
likely a wrapper around another wrapper
```

---

# Layer Peeling

Example:

```text id="h5r84r"
plaintext
→ base64
→ hex
→ token
```

Reverse:

```text id="98fhmj"
token
→ decode bytes→str representation
→ fromhex()
→ printable base64 bytes
→ base64 decode
→ raw bytes
```

---

# Important Distinction

## Representation Conversion

```python
token.decode()
```

Only changes:

```text id="g9h6r2"
bytes ↔ str representation
```

NOT the semantic layer.

---

## Semantic Reversal

```python
bytes.fromhex(...)
base64.b64decode(...)
```

Actually peels transformation layers.

---

# Layer Boundary

Example:

```text id="s1gl4o"
plaintext
→ XOR
→ raw cipher bytes
→ hex
→ base64
→ token
```

Important boundaries:

## Raw binary-like state

```text id="t6hf9d"
raw cipher bytes
```

Often:

* non-printable
* visually noisy

---

## Printable wrapper state

```text id="hf2k1j"
hex
base64
```

Human-safe transport layers.

---

# Fingerprinting

Visual observation matters.

## Hex-like clues

```text id="sw61lj"
0-9
a-f
even length
```

---

## Base64-like clues

```text id="yd9xhm"
A-Z
a-z
0-9
=
+ /
```

---

# Important Reverse Principle

Bad workflow:

```text id="m9j5rn"
blind recursive decoding
```

Good workflow:

```text id="k8v6r5"
1. observe
2. hypothesize
3. peel one layer
4. re-observe
5. continue
```

---

# Real-world Relevance

Practical targets:

* cookies
* JWT-like structures
* API tokens
* serialized blobs
* layered encodings

Often become:

```text id="e7p6h9"
layer tracing problems
```

# QA

## Step 1 — Observe Before Decoding

Inspect the following values before decoding them.

```python
A = b"4d5467794d7a5131"
B = b"614756736247383d"
C = b"65794a68624763694f694a49557a49314e694a39"
````

**Q1.**
What does each value look like?

* raw bytes
* hex wrapper
* base64 wrapper
* layered printable encoding

<details>
<summary><strong>A1.</strong></summary>

A: layered printable encoding

B: layered printable encoding

C: layered printable encoding

</details>

---

**Q2.**
Why do these values not look like raw ciphertext bytes?

<details>
<summary><strong>A2.</strong></summary>

Because they consist only of printable hexadecimal characters.

</details>

---

**Q3.**
Which transformation should be attempted first?

<details>
<summary><strong>A3.</strong></summary>

bytes.fromhex()

</details>

## Step 2 — One Layer at a Time

Analyze the following pipeline.

```text id="w2jlqb"
plaintext
→ base64
→ hex
→ token
```

Given this token:

```python
token = b"614756736247383d"
```


**Q1.**
What is the current token state?

<details>
<summary><strong>A1.</strong></summary>

hex str wrapper

</details>

---

**Q2.**
What is the first reversal step?

<details>
<summary><strong>A2.</strong></summary>

bytes.fromhex()

</details>

---

**Q3.**
What form of data is likely to appear afterward?

<details>
<summary><strong>A3.</strong></summary>

base64 wrapper

</details>

---

**Q4.**
Which reversal should follow?

<details>
<summary><strong>A4.</strong></summary>

base64.b64decode()

</details>

## Step 3 — Layer Boundary Recognition

Identify the wrapper boundary in the following flow.

```text
plaintext
→ XOR
→ raw cipher bytes
→ hex
→ base64
→ token
```

**Q1.**
Where is the raw binary-like state?

<details>
<summary><strong>A1.</strong></summary>

raw cipher bytes

</details>

---

**Q2.**
Where does the human-readable state begin?

<details>
<summary><strong>A2.</strong></summary>

hex

</details>

---

**Q3.**
Which layer serves as the printable transport representation?

<details>
<summary><strong>A3.</strong></summary>

base64

</details>

## Step 4 — Predict Intermediate States

Predict the intermediate states without executing the code.

```python
import base64

x = b"hello"

a = base64.b64encode(x)
b = a.hex()
c = b.encode()
```


**Q1.**
What is the semantic meaning of `a`?

<details>
<summary><strong>A1.</strong></summary>

base64 wrapper

</details>

---

**Q2.**
What is the semantic meaning of `b`?

<details>
<summary><strong>A2.</strong></summary>

hex wrapper

</details>

---

**Q3.**
Is `c` a raw payload or a wrapper representation?

<details>
<summary><strong>A3.</strong></summary>

wrapper representation

</details>

---

**Q4.**
What is the current outermost layer?

<details>
<summary><strong>A4.</strong></summary>

hex wrapper bytes (b'hexstr')

</details>

## Step 5 — Reverse Workflow Design

Consider the following situation.

```text id="e8zq3f"
You observed this web token:
ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKemRXSWlPaUpoWkcxcGJpSjku
```


**Q1.**
What does this value look like visually?

<details>
<summary><strong>A1.</strong></summary>

base64-like printable wrapper

</details>

---

**Q2.**
What should be attempted first?

<details>
<summary><strong>A2.</strong></summary>

base64.b64decode()

</details>

---

**Q3.**
Which features should be inspected after decoding?

<details>
<summary><strong>A3.</strong></summary>

printable, structured, JSON-like, hex-like, another base64, compressed

</details>

---

**Q4.**
Why should you avoid decoding every layer at once?

<details>
<summary><strong>A4.</strong></summary>

Because the semantic state of the decoded result is not yet known.

</details>

## Mini Task

Write an analyzer with the following features.

For the input token:

* print the original value
* print its type
* test whether it is printable
* test whether it is hex-like
* attempt Base64 decoding
* fingerprint the result again

Important:

Automatic full decryption is not the objective.

Goal:

```text id="o4m8k8"
observe
→ classify
→ peel one layer
→ observe again
```


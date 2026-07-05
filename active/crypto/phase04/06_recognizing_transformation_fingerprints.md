# Session 06 — Recognizing Transformation Fingerprints

## Metadata

```yaml
Roadmap: Cryptography
Phase: 04
Session: 06
Title: Recognizing Transformation Fingerprints
Status:
Review:
ArchiveVersion: 2
Date:
```

## Core Idea

Many crypto/web tokens are not “encrypted blobs.”

Often they are:

```text
data
→ transformation
→ printable wrapper
→ another wrapper
→ token
````

The important skill:

```text
recognize transformation layers visually
```

---

# Common Visual Patterns

## Hex-like

Usually:

* only:

  * 0-9
  * a-f
* even length often appears
* highly printable

Example:

```text
68656c6c6f
```

Possible meaning:

```text
hex representation of bytes
```

---

## Base64-like

Often contains:

```text
A-Z
a-z
0-9
+ /
=
```

Examples:

```text
aGVsbG8=
SGVsbG8gd29ybGQ=
```

Possible meaning:

```text
printable transport wrapper
```

---

# Important Mental Model

Never ask only:

```text
"What is this string?"
```

Instead ask:

```text
"What transformation pipeline produced this?"
```

---

# Common Layered Structure

Example:

```text
plaintext
→ hex
→ base64
→ token
```

Reverse:

```text
token
→ base64 decode
→ hex-looking printable bytes
→ fromhex()
→ raw bytes
```

---

# State Recognition

Important distinction:

## Raw bytes

```python
b"hello"
```

Actual byte values.

---

## Printable wrapper

```python
b"68656c6c6f"
```

Still bytes type,
but semantically a wrapper representation.

---

## Human-readable wrapper

```python
"68656c6c6f"
```

A string representation of bytes.

---

# Reverse Analysis Flow

Typical workflow:

```text
1. Observe visually
2. Predict likely encoding
3. Decode ONE layer
4. Observe again
5. Repeat
```

NOT:

```text
blindly decode everything
```

---

# Important Observation Skill

After decoding:

always ask:

```text
Did I get:
- raw bytes?
- printable bytes?
- another wrapper?
- structured text?
- compressed data?
```

---

# Real-world Importance

Cookies/tokens/API values often use:

* base64
* hex
* JSON
* compression
* XOR/simple transforms
* layered wrapping

Most analysis problems become:

```text
layer tracing problems
```

# Review Questions

## Step 1 — Visual Fingerprinting

Inspect the following values visually before executing anything.

```python
A = "68656c6c6f"
B = "aGVsbG8="
C = "4f2a1b9c"
D = "U0dWc2JHOD0="
E = "7b2261646d696e223a747275657d"
````

### Q1. Which values look hexadecimal?

<details>
<summary>A</summary>

A, C

</details>

---

### Q2. Which values look like Base64?

<details>
<summary>A</summary>

B, D

</details>

---

### Q3. Which value may decode into JSON?

<details>
<summary>A</summary>

E, JSON fingerprint sign

</details>

---

### Q4. Which value appears to contain another printable layer inside Base64?

<details>
<summary>A</summary>

D

</details>

## Step 2 — Reverse Pipeline Thinking

Analyze the following token flow.

```text
token
↓
aGVsbG8=
```

### Q5. Which transformation most likely produced this token?

<details>
<summary>A</summary>

base64

</details>

---

### Q6. What should be attempted first during analysis?

<details>
<summary>A</summary>

base64.b64decode()

</details>

---

### Q7. What data state is likely after Base64 decoding?

<details>
<summary>A</summary>

printable raw bytes, printable-like bytes

</details>

## Step 3 — Multi-Layer Recognition

Analyze the following pipeline.

```text
plaintext
→ hex
→ base64
→ token
```

### Q8. Why might hexadecimal conversion appear before Base64?

<details>
<summary>A</summary>

Because `.hex()` returns a string, which can be encoded to bytes and then
wrapped in Base64 for transport.

</details>

---

### Q9. What feature is likely to appear after Base64 decoding?

<details>
<summary>A</summary>

printable, human-readable patterns

</details>

---

### Q10. How can a "hex inside Base64" structure be recognized?

<details>
<summary>A</summary>

The decoded text contains only hexadecimal characters and has a plausible
even length.

</details>

## Step 4 — State Classification

Classify the following values by state.

```python
A = b"hello"
B = "68656c6c6f"
C = b"68656c6c6f"
D = b"aGVsbG8="
E = base64.b64decode(b"aGVsbG8=")
```

Possible states:

* plaintext str
* raw bytes
* hex wrapper
* base64 wrapper
* printable wrapper bytes

### Q11. State of `A`:

<details>
<summary>A</summary>

raw bytes

</details>

---

### Q12. State of `B`:

<details>
<summary>A</summary>

human-readable hex wrapper

</details>

---

### Q13. State of `C`:

<details>
<summary>A</summary>

hex wrapper

</details>

---

### Q14. State of `D`:

<details>
<summary>A</summary>

printable wrapper bytes

</details>

---

### Q15. State of `E`:

<details>
<summary>A</summary>

raw bytes

</details>

## Step 5 — Reverse Observation

Make a prediction before fully decoding the value.

```python
token = b"4d5467794d7a5131"
```

### Q16. What does this value look like?

* raw cipher bytes
* hex
* base64
* layered printable encoding

<details>
<summary>A</summary>

layered printable encoding

</details>

---

### Q17. What should be attempted first?

<details>
<summary>A</summary>

bytes.fromhex()

</details>

---

### Q18. What kind of data may appear next?

<details>
<summary>A</summary>

A printable string that may itself be Base64-like.

</details>

## Mini Task

Write a small analyzer.

Goals:

For the input token:

* print the original value
* print its type
* test:

  * base64 decode
  * hex detection
  * printable detection

Important:

Do not try to automate every interpretation.

Focus on:

* observation
* intermediate states
* readable debugging output

all(chr(x) in "0123456789abcdef" for x in token.lower())

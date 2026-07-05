# Session 07 — Nested Encoding Layers

## Metadata

```yaml
Roadmap: Cryptography
Phase: 03
Session: 07
Title: Nested Encoding Layers
Status:
Review:
ArchiveVersion: 2
Date:
```

## Core Concept

Many real-world tokens eventually contain:

- JSON
- serialized objects
- structured text
- metadata

The important skill:

```text id="k4t9w1"
recognize structured payloads hidden inside wrappers
````

---

# Common Nested Structure

Example:

```text id="m7r1k5"
JSON
→ base64
→ hex
→ base64
→ token
```

Reverse:

```text id="x8d2f7"
token
→ base64 decode
→ hex-looking bytes
→ fromhex()
→ base64-looking bytes
→ base64 decode
→ JSON bytes
```

---

# Structured Data Fingerprinting

## JSON-like clues

Often contains:

```text id="q1p8y6"
{
}
:
"
,
```

Hex fingerprints:

```text id="j5f2d8"
7b = {
7d = }
22 = "
3a = :
```

---

# Nested Wrapper Recognition

Important observation:

```text id="h3v7m2"
printable does not mean plaintext
```

Example:

```python id="r9k4t1"
b'65794a685a4731706269493664484a315a58303d'
```

This is:

* printable
* hex-looking
* likely wrapping another printable layer

---

# Semantic State Tracking

Always ask:

```text id="d2x8m4"
What semantic layer am I currently observing?
```

Possible states:

* raw bytes
* plaintext bytes
* JSON bytes
* base64 wrapper
* hex wrapper
* layered wrapper

---

# Important Reverse Workflow

Good workflow:

```text id="w6j2n8"
1. observe
2. fingerprint
3. peel ONE layer
4. re-classify semantic state
5. continue
```

Bad workflow:

```text id="f1q9z5"
recursive blind decoding
```

---

# Important Distinction

## Representation Conversion

```python id="a7m3v2"
.decode()
.encode()
```

Only changes representation.

---

## Semantic Reversal

```python id="z4k1d6"
bytes.fromhex()
base64.b64decode()
```

Actually changes semantic layer state.

---

# Real-world Relevance

Real tokens often contain:

* session metadata
* JWT-like payloads
* serialized JSON
* layered transport wrappers

Many practical problems become:

```text id="u9c5r1"
nested layer tracing problems
```

# Review Questions

## Step 1 — Observe Structure

Classify what each value looks like.

```python
A = b'{"admin":true}'
B = b'eyJhZG1pbiI6dHJ1ZX0='
C = b'65794a685a4731706269493664484a315a58303d'
D = b'WlhsS2FHRkhNbkJpU1Raa1NrcDFaM2s9'
````

### Q1. What does each value look like?

* raw bytes
* JSON-like
* base64 wrapper
* hex wrapper
* layered printable encoding

<details>
<summary>A</summary>

A = JSON-like

B = layered printable encoding

C = hex wrapper

D = base64 wrapper

</details>

---

### Q2. Which value most directly resembles structured data?

<details>
<summary>A</summary>

A

</details>

---

### Q3. Which values resemble nested wrappers?

<details>
<summary>A</summary>

C, D

</details>

## Step 2 — Wrapper Depth Prediction

Analyze the following pipeline.

```text id="n8w1x3"
JSON
→ base64
→ hex
→ base64
→ token
```

### Q4. What is the outermost layer?

<details>
<summary>A</summary>

outermost layer = base64

</details>

---

### Q5. Which state is likely after the first reversal?

<details>
<summary>A</summary>

hex wrapper

</details>

---

### Q6. Why can printable wrappers be nested multiple times?

<details>
<summary>A</summary>

Because wrappers change representation rather than the underlying semantic
content. They provide printable, transport-safe forms.

</details>

## Step 3 — Structured Data Recognition

Identify the values with JSON-related fingerprints.

```python
A = b'{"id":1}'
B = b'7b226964223a317d'
C = b'eyJpZCI6MX0='
D = b'91af23d1'
```

### Q7. Which value contains actual JSON bytes?

<details>
<summary>A</summary>

A

</details>

---

### Q8. Which value is JSON wrapped in hexadecimal?

<details>
<summary>A</summary>

B

</details>

---

### Q9. Which value is JSON wrapped in Base64?

<details>
<summary>A</summary>

C

</details>

## Step 4 — Intermediate Semantic State

Infer the semantic state without executing the code.

```python
import base64

x = b'{"user":"guest"}'

a = base64.b64encode(x)
b = a.hex()
c = base64.b64encode(b.encode())
```

### Q10. What is the semantic meaning of `a`?

<details>
<summary>A</summary>

base64 wrapper

</details>

---

### Q11. What is the semantic meaning of `b`?

<details>
<summary>A</summary>

hex wrapper str

</details>

---

### Q12. What is the semantic meaning of `c`?

<details>
<summary>A</summary>

base64 wrapper around hex-wrapper-bytes

</details>

---

### Q13. Where does the actual payload currently exist?

<details>
<summary>A</summary>

x

</details>

## Step 5 — Reverse Workflow Design

Inspect the following token.

```python
token = b'5a586c4b61474648626d4a7053545a6b536b70315a336b39'
```

### Q14. What does this value look like?

<details>
<summary>A</summary>

hexstr-like-wrapper

</details>

---

### Q15. What is the first reversal?

<details>
<summary>A</summary>

bytes.fromhex()

</details>

---

### Q16. Which fingerprints should be inspected next?

<details>
<summary>A</summary>

base64-like, JSON-like, ...

</details>

---

### Q17. Why is semantic state tracking important?

<details>
<summary>A</summary>

Because representations can be nested repeatedly, and values with the same
`bytes` type may have completely different semantic states.

</details>

## Mini Task

Write an analyzer with the following features.

For the input token:

* print the original value
* print its type
* detect printable, hex-like, Base64-like, and JSON-like forms
* peel one layer
* fingerprint the result again

Important:

The objective is not automatic decryption but:

```text id="n2x5k9"
state tracking
```

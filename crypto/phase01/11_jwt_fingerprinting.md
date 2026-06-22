# JWT Fingerprinting

## Core Concept

Many real-world tokens are not just encoded blobs.

They often contain:

- structure
- delimiters
- metadata boundaries
- nested payloads

Important skill:

```text id="m9v2r7"
recognize structure hidden inside wrappers
````

---

# JWT-like Structures

Common structure:

```text id="n5x8k1"
header.payload.signature
```

Usually:

* multiple segments
* delimiter-separated
* printable wrappers

---

# Important Observation

Example:

```python id="x2r7v4"
b'eyJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6dHJ1ZX0.sig'
```

This visually suggests:

* structured token
* delimiter-based boundaries
* likely wrapper layers

---

# Nested Wrappers

Example:

```python id="q4k1n8"
b'65794a68624763694f694a49557a49314e694a392e...'
```

This may be:

```text id="h8m5r2"
hex wrapper
around
JWT-like printable structure
```

---

# Delimiter Fingerprinting

Important clue:

```text id="w7n2k4"
.
```

Delimiters can reveal:

* segment boundaries
* metadata separation
* semantic structure

---

# Reverse Workflow

Good workflow:

```text id="z2m8x1"
1. observe wrappers
2. observe delimiters
3. peel one layer
4. re-observe structure
5. continue
```

---

# Important Distinction

## Representation Conversion

```python id="j4m9k6"
.decode()
.encode()
```

Representation only.

---

## Semantic Reversal

```python id="u5x2r7"
bytes.fromhex()
base64.b64decode()
```

Actually changes semantic state.

---

# Semantic State Tracking

Possible states:

* plaintext bytes
* JSON bytes
* structured token
* hex wrapper
* base64 wrapper
* nested wrapper

Important question:

```text id="r8k1m4"
What semantic layer am I currently observing?
```

---

# Real-world Relevance

Real systems often use:

* JWT-like structures
* session tokens
* metadata segments
* nested wrappers
* transport-safe encodings

Many problems become:

```text id="k1x9m5"
structure + layer tracing problems
```


# QA

## Step 1 — Visual Structure Observation

Inspect the following tokens.

```python
A = b'eyJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6dHJ1ZX0.signature'
B = b'ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKemRXSWlPaUpoWkcxcGJpSmtmUS5zaWc='
C = b'65794a68624763694f694a49557a49314e694a392e65794a7a645749694f694a685a47317062694a6b66512e736967'
````


**Q1.**
What does each value look like?

* structured token
* base64 wrapper
* hex wrapper
* layered wrapper

<details>
<summary><strong>A1.</strong></summary>

A = structure token / JWT-like structure

B  = base64 wrapper

C = hex wrapper

</details>

---

**Q2.**
Which value directly exposes a delimiter-based structure?

<details>
<summary><strong>A2.</strong></summary>

A

</details>

---

**Q3.**
Which values appear to wrap another structured token?

<details>
<summary><strong>A3.</strong></summary>

B may contain a structured token inside a Base64 wrapper.

C may contain a structured token inside a hexadecimal wrapper.

</details>

## Step 2 — Delimiter Recognition

Analyze the following structure.

```text id="m4x7r2"
header.payload.signature
```


**Q1.**
Why can the `.` delimiter be important?

<details>
<summary><strong>A1.</strong></summary>

It exposes segment boundaries typical of a JWT-like structure.

</details>

---

**Q2.**
What can happen to the delimiter when a wrapper is added?

<details>
<summary><strong>A2.</strong></summary>

The wrapper can hide the delimiter, so peel the current layer and inspect the
result again.

</details>

---

**Q3.**
Why is it important to inspect delimiters again after decoding?

<details>
<summary><strong>A3.</strong></summary>

Because a wrapper may conceal a multi-segment structure.

</details>

## Step 3 — JWT-Like Fingerprinting

Identify the values with JWT-related fingerprints.

```python id="h8v2q5"
A = b'eyJ1c2VyIjoiZ3Vlc3QifQ=='
B = b'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZ3Vlc3QifQ.sig'
C = b'7b2275736572223a226775657374227d'
D = b'91af23de'
```


**Q1.**
Which value is a JWT-like structured token?

<details>
<summary><strong>A1.</strong></summary>

B

</details>

---

**Q2.**
Which value is a hexadecimal wrapper around JSON?

<details>
<summary><strong>A2.</strong></summary>

C

</details>

---

**Q3.**
Which value contains only a Base64-wrapped payload?

<details>
<summary><strong>A3.</strong></summary>

A

</details>

## Step 4 — Semantic Layer Tracking

Infer the semantic state of each value.

```python id="f2k7w1"
import base64

x = b'{"role":"guest"}'

a = base64.b64encode(x)
b = b'header.' + a + b'.sig'
c = b.hex()
```


**Q1.**
What is the semantic state of `a`?

<details>
<summary><strong>A1.</strong></summary>

base64 wrapper

</details>

---

**Q2.**
What is the semantic state of `b`?

<details>
<summary><strong>A2.</strong></summary>

JWT-like-structure

</details>

---

**Q3.**
What is the semantic state of `c`?

<details>
<summary><strong>A3.</strong></summary>

JWT-like-structure hex wrapper

</details>

---

**Q4.**
At which layer does the delimiter exist?

<details>
<summary><strong>A4.</strong></summary>

The delimiter exists in the structured-token layer represented by `b`.

</details>

## Step 5 — Reverse Workflow Design

Inspect the following token.

```python id="z8m1r3"
token = b'65794a68624763694f694a49557a49314e694a392e65794a3163325679496a6f695a33566c6333516966512e63326c6e'
```


**Q1.**
What does the current outermost layer look like?

<details>
<summary><strong>A1.</strong></summary>

hex-str-like-wrapper

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
What should be inspected after reversal?

<details>
<summary><strong>A3.</strong></summary>

JWT-like (delimiter)

</details>

---

**Q4.**
Why is delimiter fingerprinting important?

<details>
<summary><strong>A4.</strong></summary>

A delimiter reveals structural segment boundaries. A wrapper may hide it, so
inspect delimiters again after peeling the wrapper.

</details>

## Mini Task

Write an analyzer with the following features.

For the input token:

* print the original value and type
* detect printable, hex-like, Base64-like, and JSON-like forms
* detect the `.` delimiter
* peel one layer
* inspect delimiters again

Goal:

```text id="a6k4v2"
semantic layer tracking
+
structure recognition
```

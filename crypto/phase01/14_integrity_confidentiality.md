# Integrity and Confidentiality

## Core Concept

Real-world tokens often contain:

- readable payloads
- metadata
- integrity/authentication segments
- transport wrappers

Important distinction:

```text
readable
!=
trusted
```

---

# Integrity vs Confidentiality

## Confidentiality

Goal:

```text
hide the content
```

Usually:
- encryption
- secrecy
- unreadable without key

---

## Integrity

Goal:

```text
detect modification
```

Usually:
- signatures
- HMAC
- authentication data

Important:

```text
integrity
!=
confidentiality
```

---

# JWT-like Reasoning

Example:

```text
header.payload.signature
```

Possible semantic roles:

- header → metadata/configuration
- payload → actual application data
- signature → integrity/authentication

---

# Important Observation

Payload may be:

- readable
- printable
- base64 decodable

BUT:

```text
readable
!=
modifiable
```

because integrity checks may exist.

---

# Trust Reasoning

Important question:

```text
Can I trust this data?
```

Different from:

```text
Can I read this data?
```

---

# Metadata Fingerprinting

Metadata-like clues:

- alg
- exp
- iat
- typ

Payload-like clues:

- user
- role
- session
- permissions

---

# Controlled Recursive Analysis

Good workflow:

```text
observe
→ identify wrapper
→ peel carefully
→ identify structure
→ identify semantic role
→ reason about trust/integrity
```

Bad workflow:

```text
blind decoding only
```

---

# Important Mental Model

Always distinguish:

```text
representation
structure
semantic role
trust property
```

These are different layers of reasoning.

---

# Real-world Relevance

Real systems often separate:

- readable payload
- integrity verification
- metadata
- transport wrapper

Many practical problems become:

```text
semantic role tracing
+
trust reasoning
```

# QA

## Step 1 — Semantic Purpose Observation

Inspect the following structure.

```text
header.payload.signature
```


**Q1.**
Which segment most likely contains application data?

<details>
<summary><strong>A1.</strong></summary>

payload

</details>

---

**Q2.**
Which segment most likely serves integrity or authentication?

<details>
<summary><strong>A2.</strong></summary>

signature

</details>

---

**Q3.**
Why does the signature have a different purpose from the payload?

<details>
<summary><strong>A3.</strong></summary>

The payload carries application data, while the signature helps verify
integrity and authenticity.

</details>

---

**Q4.**
Why can a token remain security-relevant even when its payload is readable?

<details>
<summary><strong>A4.</strong></summary>

Readable does not mean trusted or freely modifiable. A signature can detect
changes to a readable payload.

</details>

## Step 2 — Integrity Versus Confidentiality

Analyze the following situation.

```text
payload:
{"role":"admin"}

signature:
HMAC(...)
```


**Q1.**
What does payload readability imply?

<details>
<summary><strong>A1.</strong></summary>

The payload is not confidential.

</details>

---

**Q2.**
What is the purpose of the signature?

<details>
<summary><strong>A2.</strong></summary>

To determine whether the payload passes integrity and authenticity checks.

</details>

---

**Q3.**
Why does readable not mean safely modifiable?

<details>
<summary><strong>A3.</strong></summary>

Because modifying readable data can cause signature verification to fail.

</details>

---

**Q4.**
Why must integrity and confidentiality be distinguished?

<details>
<summary><strong>A4.</strong></summary>

Integrity detects unauthorized changes. Confidentiality hides content.

</details>

## Step 3 — Metadata Reasoning

Inspect the following values.

```python
A = b'{"alg":"HS256"}'
B = b'{"exp":1730000000}'
C = b'{"role":"guest"}'
D = b'signature'
```


**Q1.**
Which values look like metadata or configuration?

<details>
<summary><strong>A1.</strong></summary>

A, B

</details>

---

**Q2.**
Which value looks like the application payload?

<details>
<summary><strong>A2.</strong></summary>

C

</details>

---

**Q3.**
Which value looks related to integrity or authentication?

<details>
<summary><strong>A3.</strong></summary>

D

</details>

---

**Q4.**
Why is a field such as `exp` closer to metadata?

<details>
<summary><strong>A4.</strong></summary>

Because it describes token validity, such as expiration, rather than primary
application data.

</details>

## Step 4 — Controlled Token Analysis

Inspect the following token.

```python
token = b'ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKeWIyeGxJam9pWVdSdGFXNGlmUS5jMmxuYm1GMGRYSmw='
```


**Q1.**
What does the outermost layer look like?

<details>
<summary><strong>A1.</strong></summary>

base64 wrapper

</details>

---

**Q2.**
What should be inspected first after peeling one layer?

<details>
<summary><strong>A2.</strong></summary>

delimiter, JSON-like, hex-str-like, JWT-structure, ...

</details>

---

**Q3.**
How can each segment's semantic role be inferred?

<details>
<summary><strong>A3.</strong></summary>

By inspecting its decoded structure, field names, and content.

</details>

---

**Q4.**
Why is wrapper fingerprinting alone insufficient?

<details>
<summary><strong>A4.</strong></summary>

It identifies only the outer representation; meaningful data appears after
the layer is peeled.

</details>

## Step 5 — Trust Reasoning

Consider the following situation.

```text
payload:
{"role":"admin"}

The payload becomes readable after Base64 decoding.
```


**Q1.**
Why does readability not establish trust?

<details>
<summary><strong>A1.</strong></summary>

Because signature or integrity verification is needed to determine whether
the server issued the value and whether it was modified.

</details>

---

**Q2.**
Why is integrity verification required?

<details>
<summary><strong>A2.</strong></summary>

To detect whether the data has been modified.

</details>

---

**Q3.**
Why are "visible" and "verified" different concepts?

<details>
<summary><strong>A3.</strong></summary>

Visibility concerns decoding and representation. Verification concerns
integrity and trust. Readable data is not trusted before verification.

</details>

---

**Q4.**
Why is semantic-purpose reasoning important in token analysis?

<details>
<summary><strong>A4.</strong></summary>

Because metadata, payload, and signature segments have different purposes and
different effects on readability, trust, and tamper detection.

</details>

## Mini Task

Write an analyzer with the following features.

For the input token:

- detect printable, hexadecimal, and Base64-like forms
- analyze delimiters and count segments
- peel ONE layer
- infer semantic roles:
  - metadata?
  - payload?
  - integrity/authentication?
  - wrapper?
- detect JSON-like content and timestamp-like fields
- distinguish readable from trusted

Important:

Goal:

```text
semantic trust reasoning
```

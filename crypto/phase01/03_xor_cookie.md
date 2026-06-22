# XOR Cookie

## Core Concept

Many web tokens look mysterious only because they are:

```text
raw bytes
wrapped in a printable transport layer
```

In this session, the important distinction is:

```text
XOR is the real transformation
base64 is the outer wrapper
```

---

# Why Base64 Appears

Base64 is used because web systems prefer:

* printable ASCII
* transport-safe values
* text-friendly storage

Example:

```python
text = "admin=true"
raw = text.encode()
token = base64.b64encode(raw)
```

Important point:

```text
base64 output often looks like text,
but it is still bytes in Python
```

---

# Base64 Is Not Encryption

Base64 does not hide meaning with a secret.

It only converts data into a printable alphabet.

That means:

```text
base64 decode restores bytes without any key
```

So when you see a token-like string,
one of the first questions should be:

```text
is there an outer base64 wrapper?
```

---

# XOR Inside the Token

Example:

```python
plaintext = b"admin=true"
key = 0x23
cipher = bytes([x ^ key for x in plaintext])
token = base64.b64encode(cipher)
```

Meaning:

* `cipher` is the real transformed state
* `token` is only the printable wrapper around that state

This is a common pattern:

```text
plaintext
→ transformation
→ printable wrapper
→ token
```

---

# Reverse Flow

Reverse order:

```text
token
→ base64 decode
→ cipher bytes
→ XOR again
→ plaintext bytes
```

Important distinction:

* `base64.b64decode()` removes a wrapper
* XOR reverses the actual transformation
* `.decode()` only changes bytes into a string view

---

# Forging Perspective

If the key and transformation pipeline are known,
the same pipeline can be applied to another plaintext.

Example idea:

```text
target plaintext
→ XOR with same key
→ base64
→ forged token
```

This shows why:

```text
knowing the real transformation matters much more than recognizing the wrapper
```

---

# Representation vs Security

When analyzing a token, do not confuse:

* printable appearance
* transport format
* actual security layer

Base64 helps with transport.

XOR changes the underlying bytes.

Those are not the same kind of operation.

---

# Why This Session Matters

This session establishes a very common web-crypto pattern:

```text
token-looking value
!=
encrypted blob by default
```

Often the correct workflow is:

```text
1. test for base64
2. restore inner bytes
3. ask what real transformation remains
```

# QA

## Step 1 — Wrapper Recognition

Identify the role of each operation in the following flow.

```python
text = "admin=true"
raw = text.encode()
token = base64.b64encode(raw)
```

**Q1.**
Why is `encode()` called before `b64encode()`?

<details>
<summary><strong>A1.</strong></summary>

Because `base64.b64encode()` expects a bytes-like input.

</details>

---

**Q2.**
What is the actual type of `token`, even if it looks textual?

<details>
<summary><strong>A2.</strong></summary>

bytes

</details>

---

**Q3.**
Why does Base64 output look printable?

<details>
<summary><strong>A3.</strong></summary>

Because the Base64 alphabet consists of printable ASCII characters.

</details>

## Step 2 — Reverse Layer Thinking

Determine which layers are removed by the following code.

```python
raw = base64.b64decode(token)
plain = raw.decode()
```

**Q1.**
Why does `b64decode()` not return a `str` directly?

<details>
<summary><strong>A1.</strong></summary>

Because Base64 decoding restores the original raw bytes.

</details>

---

**Q2.**
What is the next step for viewing the result as human-readable text?

<details>
<summary><strong>A2.</strong></summary>

`decode()`

</details>

---

**Q3.**
Does analysis always end after Base64 decoding?

<details>
<summary><strong>A3.</strong></summary>

No. Inner transformations or wrappers such as XOR or hexadecimal may remain.

</details>

## Step 3 — Transformation Versus Wrapper

Distinguish the real transformation from the wrapper.

```python
plaintext = b"admin=true"
key = 0x23
cipher = bytes([x ^ key for x in plaintext])
token = base64.b64encode(cipher)
```

**Q1.**
Which operation performs the actual encryption-like transformation?

<details>
<summary><strong>A1.</strong></summary>

XOR

</details>

---

**Q2.**
What role does Base64 play?

<details>
<summary><strong>A2.</strong></summary>

It is a wrapper that converts raw ciphertext bytes into a printable
representation.

</details>

---

**Q3.**
Why does the token look like a printable string?

<details>
<summary><strong>A3.</strong></summary>

Because Base64 is applied as the outermost wrapper.

</details>

## Step 4 — Cookie Recovery

Identify where plaintext recovery occurs.

```python
raw = base64.b64decode(token)
recovered = bytes([x ^ key for x in raw])
```

**Q1.**
Why does Base64 decoding alone not produce plaintext?

<details>
<summary><strong>A1.</strong></summary>

Because the decoded result is still XOR-transformed ciphertext bytes.

</details>

---

**Q2.**
At which step does actual plaintext recovery occur?

<details>
<summary><strong>A2.</strong></summary>

At the XOR step that computes `cipher ^ key`.

</details>

---

**Q3.**
Why is the recovered result still `bytes`?

<details>
<summary><strong>A3.</strong></summary>

Because XOR operates on and returns bytes. Use `decode()` afterward if a text
interpretation is appropriate.

</details>

## Step 5 — Token State Classification

Classify the following values by state.

```python
A = b"admin=true"
B = base64.b64encode(A)
C = bytes([x ^ 0x23 for x in A])
D = base64.b64encode(C)
```

Possible states:

* raw plaintext bytes
* base64 wrapper
* cipher bytes
* printable token wrapper

**Q1.**
State of `A`:

<details>
<summary><strong>A1.</strong></summary>

raw plaintext bytes

</details>

---

**Q2.**
State of `B`:

<details>
<summary><strong>A2.</strong></summary>

base64 wrapper

</details>

---

**Q3.**
State of `C`:

<details>
<summary><strong>A3.</strong></summary>

cipher bytes

</details>

---

**Q4.**
State of `D`:

<details>
<summary><strong>A4.</strong></summary>

printable token wrapper

</details>

## Mini Task

Write the reverse sequence for the following token.

```python
token = base64.b64encode(bytes([x ^ 0x23 for x in b"admin=true"]))
```

Answer format:

```text
1.
2.
3.
```

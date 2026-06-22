# Data States

## Core Concept

In reverse analysis, the hardest mistake is often not “wrong decoding,”
but:

```text
misidentifying the current data state
```

The same visible value can belong to different semantic layers.

---

# Type and Meaning Are Different

Consider:

```python
x = b"68656c6c6f"
```

Type:

```text
bytes
```

Meaning:

```text
not raw plaintext bytes,
but bytes containing a printable hex wrapper
```

This is the central lesson:

```text
type alone is not enough
meaning also matters
```

---

# Wrapper States

Important states to distinguish:

## Raw bytes

Example:

```python
b"hello"
```

Actual content bytes.

---

## Printable wrapper bytes

Example:

```python
b"68656c6c6f"
```

Still `bytes`,
but semantically a wrapper around another layer.

---

## Human-readable wrapper

Example:

```python
"68656c6c6f"
```

String form of the wrapper.

---

# State Transitions

Example:

```python
x = b"68656c6c6f"
y = x.decode()
z = bytes.fromhex(y)
```

What happens:

* `x` is printable wrapper bytes
* `y` is the same content viewed as `str`
* `z` is the restored raw bytes

Important point:

```text
decode() changes representation
fromhex() changes semantic layer
```

---

# Predicting Before Running

A strong reverse habit is:

```text
predict first,
execute later
```

Why:

* it forces you to reason about states
* it reveals whether you understand the pipeline
* it prevents blind trial-and-error decoding

This becomes more important when wrappers stack.

---

# Closest to the Real Data

In a longer flow such as:

```text
plaintext
→ XOR
→ cipher bytes
→ hex
→ base64
→ token
```

the layer closest to the actual transformed data is:

```text
cipher bytes
```

The outer layers mainly exist to make transport, storage, or inspection easier.

---

# Why Wrapper Recognition Matters

If wrapper states are confused with real data states,
then:

* reverse order becomes wrong
* the wrong function is applied
* semantic progress is misunderstood

So a good analyst keeps asking:

```text
What is the current type?
What is the current meaning?
What layer am I actually looking at?
```

---

# Why This Session Matters

This session ties together the previous topics into one habit:

```text
track both type and semantic state
```

That habit becomes essential once tokens contain:

* multiple wrappers
* structured payloads
* nested encodings
* mixed printable and raw states

# QA

## Step 1 — Wrapper Versus Real Data

Determine whether the following value is actual data or a wrapper.

```python
x = b'68656c6c6f'
```

**Q1.**
Is `x` actual plaintext bytes or another form of representation?

<details>
<summary><strong>A1.</strong></summary>

Wrapper bytes representing the plaintext.

</details>

---

**Q2.**
What is the type returned by `x.decode()`?

<details>
<summary><strong>A2.</strong></summary>

str

</details>

---

**Q3.**
What does the value mean after `x.decode()`?

<details>
<summary><strong>A3.</strong></summary>

human-readable hex wrapper

</details>

## Step 2 — State Transition Recognition

Classify the state of each value in the following flow.

```python
x = b'68656c6c6f'
y = x.decode()
z = bytes.fromhex(y)
```

**Q1.**
What is the type of `y`?

<details>
<summary><strong>A1.</strong></summary>

str

</details>

---

**Q2.**
What is the type of `z`?

<details>
<summary><strong>A2.</strong></summary>

bytes

</details>

---

**Q3.**
What data state does `z` represent?

<details>
<summary><strong>A3.</strong></summary>

restored raw bytes

</details>

---

**Q4.**
Why is `fromhex()` required?

<details>
<summary><strong>A4.</strong></summary>

To restore actual bytes from the hexadecimal wrapper.

</details>

## Step 3 — Predict Before Execution

Predict the state shown by each output.

```python
x = b'414243'

print(x)
print(x.decode())
print(bytes.fromhex(x.decode()))
print(bytes.fromhex(x.decode()).decode())
```

**Q1.**
What does the first output show?

<details>
<summary><strong>A1.</strong></summary>

printable wrapper bytes

</details>

---

**Q2.**
What does the second output show?

<details>
<summary><strong>A2.</strong></summary>

human-readable hex string

</details>

---

**Q3.**
What does the third output show?

<details>
<summary><strong>A3.</strong></summary>

restored raw bytes

</details>

---

**Q4.**
What does the fourth output show?

<details>
<summary><strong>A4.</strong></summary>

human-readable plaintext

</details>

## Step 4 — Reverse Thinking

Explain the recovery order in the following structure.

```text
printable wrapper bytes
↓
decode()
↓
hex string
↓
fromhex()
↓
raw bytes
```

**Q1.**
Why is `decode()` required first?

<details>
<summary><strong>A1.</strong></summary>

Because the current value is wrapper content stored as bytes.

</details>

---

**Q2.**
Why must `fromhex()` come next?

<details>
<summary><strong>A2.</strong></summary>

Because the hexadecimal text must be converted back into actual bytes.

</details>

---

**Q3.**
What is the key skill demonstrated by this flow?

<details>
<summary><strong>A3.</strong></summary>

Reversing one layer at a time while distinguishing type from semantic state.

</details>

## Step 5 — State Classification

Classify the following values by state.

```python
A = b'hello'
B = '68656c6c6f'
C = b'68656c6c6f'
D = bytes.fromhex('68656c6c6f')
```

Possible states:

* raw bytes
* human-readable hex wrapper
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

human-readable hex wrapper

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

Explain the following flow in terms of type and meaning.

```python
import base64

x = b'hello'
a = x.hex()
b = a.encode()
c = base64.b64encode(b)
```

Answer format:

```text
x:
type:
meaning:

a:
type:
meaning:

b:
type:
meaning:

c:
type:
meaning:
```

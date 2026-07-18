---
Roadmap: Number Systems for Systems Programming
Phase: Phase 01 — Practical Number Representations
Session: Session 03
Title: Signed, Unsigned, Two's Complement, and Integer Limits
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-07-06
---

# Phase 01 — Session 03: Signed, Unsigned, Two's Complement, and Integer Limits

## Objective

Understand how the same bit pattern can represent different numeric meanings depending on signedness, integer width, and interpretation context.

The goal of this session was not arithmetic memorization. The goal was to recognize common signed and unsigned boundary patterns, observe fixed-width wraparound, and connect those observations to systems-level integer interpretation.

This session focused on:

- unsigned integer interpretation
- signed two's complement interpretation
- 8-bit and 32-bit integer boundaries
- wraparound behavior in fixed-width arithmetic
- masking with `0xff` and `0xffffffff`
- context-dependent meanings of values such as `0xff` and `0xffffffff`

---

## Learning Summary

A bit pattern does not carry a single fixed numeric meaning by itself. Its meaning depends on the interpretation context.

```text
raw bits
↓
type / width / context
↓
meaning
```

For example, the 8-bit pattern `11111111` can be read in multiple ways.

```text
0xff as unsigned 8-bit = 255
0xff as signed 8-bit   = -1
```

The same principle applies to 32-bit values.

```text
0xffffffff as unsigned 32-bit = 4294967295
0xffffffff as signed 32-bit   = -1
```

This distinction matters in C, binary protocols, reverse engineering, embedded registers, system call return values, masks, and sentinel values.

The core mental model is:

```text
bit pattern first
interpretation second
meaning last
```

---

## Key Concepts

- signed integer
- unsigned integer
- two's complement
- integer width
- 8-bit integer
- 32-bit integer
- fixed-width arithmetic
- wraparound
- overflow
- low bits
- bit mask
- sign bit
- sentinel value
- interpretation context

---

## Practical Observations

### Observation 01 — 8-bit Signed and Unsigned Interpretation

Given the following byte values:

```text
0x00
0x01
0x7f
0x80
0xff
```

Predicted interpretations:

```text
0x00 = unsigned 0,   signed 0
0x01 = unsigned 1,   signed 1
0x7f = unsigned 127, signed 127
0x80 = unsigned 128, signed -128
0xff = unsigned 255, signed -1
```

Explanation:

Unsigned 8-bit values use the full range as non-negative quantities.

```text
0x00 ~ 0xff
↓
0 ~ 255
```

Signed 8-bit two's complement splits the same 256 patterns into non-negative and negative ranges.

```text
0x00 ~ 0x7f
↓
0 ~ 127

0x80 ~ 0xff
↓
-128 ~ -1
```

The key boundary values are:

```text
0x7f = signed 8-bit maximum = 127
0x80 = signed 8-bit minimum = -128
0xff = signed 8-bit -1
```

---

### Observation 02 — 8-bit Wraparound Prediction

Predicted fixed-width 8-bit results:

```text
0xff + 1 = 0x00
0x00 - 1 = 0xff
0x7f + 1 = 0x80
0x80 - 1 = 0x7f
```

Explanation:

In an 8-bit space, only values from `0x00` through `0xff` fit. If an operation produces more than 8 bits, only the low 8 bits remain.

```text
0xff + 1
= 0x100
= 1 00000000₂
↓
low 8 bits
↓
0x00
```

```text
0x00 - 1
↓
wraps below zero in 8-bit space
↓
0xff
```

This is the basis for recognizing why `0xff` behaves like `-1` in signed 8-bit two's complement.

---

### Observation 03 — Signed Meaning of 8-bit Wraparound

The same 8-bit results were then interpreted as signed values.

```text
0x7f + 1 = 0x80
```

Signed interpretation:

```text
127 + 1 = -128
```

```text
0xff + 1 = 0x00
```

Signed interpretation:

```text
-1 + 1 = 0
```

```text
0x00 - 1 = 0xff
```

Signed interpretation:

```text
0 - 1 = -1
```

```text
0x80 - 1 = 0x7f
```

Signed interpretation:

```text
-128 - 1 = 127
```

The important separation is:

```text
operation result as bits
↓
signed or unsigned interpretation
↓
numeric meaning
```

Note: unsigned overflow in C is defined wraparound behavior. Signed integer overflow in C is undefined behavior. This session used two's complement bit-pattern reasoning for recognition and systems intuition.

---

### Observation 04 — Low 8 Bits with `& 0xff`

Command:

```bash
python3 - <<'PY'
values = [
    ("0xff + 1", 0xff + 1),
    ("0x00 - 1", 0x00 - 1),
    ("0x7f + 1", 0x7f + 1),
    ("0x80 - 1", 0x80 - 1),
]

for label, value in values:
    wrapped = value & 0xff
    print(label, "=", hex(value), "=> low 8 bits:", hex(wrapped))
PY
```

Observed result:

```text
0xff + 1 = 0x100 => low 8 bits: 0x0
0x00 - 1 = -0x1 => low 8 bits: 0xff
0x7f + 1 = 0x80 => low 8 bits: 0x80
0x80 - 1 = 0x7f => low 8 bits: 0x7f
```

Explanation:

`0xff` is a mask with the low 8 bits set.

```text
0xff = 11111111
```

Applying `value & 0xff` preserves only the low 8 bits.

```text
value
AND 00000000 00000000 11111111
↓
low 8 bits remain
```

This allows Python's unbounded integer arithmetic to be viewed through an 8-bit fixed-width lens.

---

### Observation 05 — Implementing `signed8`

A signed 8-bit interpretation rule was applied manually.

```text
0x00 ~ 0x7f → keep the value
0x80 ~ 0xff → subtract 0x100
```

Function:

```python
def signed8(value):
    value = value & 0xff
    if value >= 0x80:
        return value - 0x100
    return value
```

Command:

```bash
python3 - <<'PY'
def signed8(value):
    value = value & 0xff
    if value >= 0x80:
        return value - 0x100
    return value

for value in [0x00, 0x7f, 0x80, 0xff, 0xfe]:
    print(hex(value), "unsigned:", value, "signed:", signed8(value))
PY
```

Observed result:

```text
0x0 unsigned: 0 signed: 0
0x7f unsigned: 127 signed: 127
0x80 unsigned: 128 signed: -128
0xff unsigned: 255 signed: -1
0xfe unsigned: 254 signed: -2
```

Explanation:

Values below `0x80` remain in the non-negative signed range. Values from `0x80` through `0xff` are interpreted as negative by subtracting the 8-bit range size, `0x100`.

```text
0xfe
↓
unsigned value = 254
↓
254 - 256
↓
-2
```

---

### Observation 06 — 32-bit Signed and Unsigned Interpretation

Predicted interpretations:

```text
0x00000000 = unsigned 0,          signed 0
0x00000001 = unsigned 1,          signed 1
0x7fffffff = unsigned 2147483647, signed 2147483647
0x80000000 = unsigned 2147483648, signed -2147483648
0xffffffff = unsigned 4294967295, signed -1
```

Explanation:

The 32-bit pattern follows the same structure as the 8-bit pattern.

```text
8-bit:
0x7f = signed maximum
0x80 = signed minimum
0xff = -1
```

```text
32-bit:
0x7fffffff = signed maximum
0x80000000 = signed minimum
0xffffffff = -1
```

The size changes, but the recognition pattern stays the same.

---

### Observation 07 — Implementing `signed32`

The 8-bit signed interpretation function was generalized to 32-bit.

```python
def signed32(value):
    value = value & 0xffffffff
    if value >= 0x80000000:
        return value - 0x100000000
    return value
```

The structure matches `signed8`.

```text
signed8:
mask      = 0xff
sign edge = 0x80
range     = 0x100

signed32:
mask      = 0xffffffff
sign edge = 0x80000000
range     = 0x100000000
```

Command:

```bash
python3 - <<'PY'
def signed32(value):
    value = value & 0xffffffff
    if value >= 0x80000000:
        return value - 0x100000000
    return value

for value in [0x00000000, 0x00000001, 0x7fffffff, 0x80000000, 0xffffffff]:
    print(hex(value), "unsigned:", value, "signed:", signed32(value))
PY
```

Observed result:

```text
0x0 unsigned: 0 signed: 0
0x1 unsigned: 1 signed: 1
0x7fffffff unsigned: 2147483647 signed: 2147483647
0x80000000 unsigned: 2147483648 signed: -2147483648
0xffffffff unsigned: 4294967295 signed: -1
```

Explanation:

`value & 0xffffffff` restricts the value to a 32-bit space. Values from `0x80000000` through `0xffffffff` are then interpreted as negative by subtracting the 32-bit range size, `0x100000000`.

```text
0xffffffff
↓
unsigned value = 4294967295
↓
4294967295 - 4294967296
↓
-1
```

---

### Observation 08 — Context-Dependent Meaning of `0xffffffff`

The value `0xffffffff` was interpreted in several different contexts.

```text
0xffffffff as unsigned 32-bit = 4294967295
0xffffffff as signed 32-bit   = -1
0xffffffff as bit mask         = all 32 bits set
```

Explanation:

The underlying bit pattern is the same.

```text
11111111 11111111 11111111 11111111
```

The meaning changes because the interpretation context changes.

Possible meanings include:

- maximum `uint32_t` value
- signed `int32_t` value `-1`
- all-bits-on mask
- sentinel value
- invalid value marker
- error return convention

The correct interpretation requires checking the type, width, and use context.

---

## Commands / Code

```bash
python3 - <<'PY'
values = [
    ("0xff + 1", 0xff + 1),
    ("0x00 - 1", 0x00 - 1),
    ("0x7f + 1", 0x7f + 1),
    ("0x80 - 1", 0x80 - 1),
]

for label, value in values:
    wrapped = value & 0xff
    print(label, "=", hex(value), "=> low 8 bits:", hex(wrapped))
PY
```

Shows how `& 0xff` keeps only the low 8 bits of a value.

---

```python
def signed8(value):
    value = value & 0xff
    if value >= 0x80:
        return value - 0x100
    return value
```

Interprets a value as signed 8-bit two's complement.

---

```python
def signed32(value):
    value = value & 0xffffffff
    if value >= 0x80000000:
        return value - 0x100000000
    return value
```

Interprets a value as signed 32-bit two's complement.

---

```bash
python3 - <<'PY'
def signed32(value):
    value = value & 0xffffffff
    if value >= 0x80000000:
        return value - 0x100000000
    return value

for value in [0x00000000, 0x00000001, 0x7fffffff, 0x80000000, 0xffffffff]:
    print(hex(value), "unsigned:", value, "signed:", signed32(value))
PY
```

Shows common 32-bit signed and unsigned boundary interpretations.

---

## Connections

```text
raw bits
↓
integer width
↓
signed / unsigned interpretation
↓
systems meaning
```

This session connects directly to C programming.

```text
uint32_t
↓
0xffffffff = 4294967295
```

```text
int32_t
↓
0xffffffff = -1
```

It also connects to binary analysis and reverse engineering.

```text
hex dump
↓
byte pattern
↓
type inference
↓
meaning
```

It connects to cryptography and payload analysis because bytes often need to be preserved as raw patterns before being interpreted as numbers or text.

```text
0xff
↓
byte value
↓
mask / integer / sentinel / protocol field
```

It also connects to embedded systems, where registers and flags are often interpreted as fixed-width bit fields rather than ordinary decimal numbers.

---

## Common Misconceptions

### Misconception 01 — A Bit Pattern Has One Fixed Meaning

Incorrect:

```text
0xff always means 255.
```

Correct:

```text
0xff can mean 255 as unsigned 8-bit, -1 as signed 8-bit, or all bits set as a mask.
```

---

### Misconception 02 — Python Automatically Behaves Like Fixed-Width C Integers

Incorrect:

```text
Python 0xff + 1 automatically wraps to 0x00.
```

Correct:

```text
Python integers are not fixed-width by default.
Use a mask such as & 0xff to observe low 8-bit behavior.
```

---

### Misconception 03 — Signed and Unsigned Values Store Different Bits

Incorrect:

```text
Signed -1 and unsigned 255 must have different 8-bit storage.
```

Correct:

```text
In 8-bit two's complement, signed -1 and unsigned 255 share the same bit pattern: 0xff.
```

---

### Misconception 04 — `0xffffffff` Should Be Interpreted Immediately as a Decimal Number

Incorrect:

```text
0xffffffff means 4294967295, so that is the only correct interpretation.
```

Correct:

```text
0xffffffff must be interpreted according to width, signedness, and usage context.
```

---

### Misconception 05 — Exit, Error, or Sentinel Values Are Always Separate from Integer Representation

Incorrect:

```text
An error marker such as -1 is unrelated to raw bit patterns.
```

Correct:

```text
A sentinel such as -1 may appear as all bits set in fixed-width two's complement representation.
```

---

## Key Takeaways

- The same raw bits can have different meanings depending on type and context.
- Unsigned 8-bit values range from `0x00` to `0xff`, or `0` to `255`.
- Signed 8-bit values range from `0x80` to `0x7f`, or `-128` to `127`.
- `0x7f` is signed 8-bit maximum.
- `0x80` is signed 8-bit minimum.
- `0xff` is unsigned 8-bit `255`, signed 8-bit `-1`, or an all-bits-set mask.
- `0x7fffffff` is signed 32-bit maximum.
- `0x80000000` is signed 32-bit minimum.
- `0xffffffff` is unsigned 32-bit `4294967295`, signed 32-bit `-1`, or an all-bits-set mask.
- `& 0xff` keeps the low 8 bits.
- `& 0xffffffff` keeps the low 32 bits.
- In C, unsigned overflow is defined wraparound, while signed overflow is undefined behavior.
- Always ask which width, signedness, and context apply before assigning meaning to a bit pattern.

---

## Review Questions

### Q1. Why can the same bit pattern have different numeric meanings?

<details>
<summary>A</summary>

The same bit pattern can have different numeric meanings because the stored bits are interpreted according to the integer width and whether the type is signed or unsigned.

</details>

---

### Q2. What are the unsigned and signed 8-bit meanings of `0xff`?

<details>
<summary>A</summary>

As an unsigned 8-bit value, `0xff` means `255`. As a signed 8-bit two's complement value, it means `-1`.

</details>

---

### Q3. Why is `0x7f` the maximum signed 8-bit value?

<details>
<summary>A</summary>

`0x7f` is the maximum signed 8-bit value because its bit pattern is `01111111`: the sign bit is `0`, and all seven remaining value bits are `1`, giving `127`.

</details>

---

### Q4. Why is `0x80` the minimum signed 8-bit value?

<details>
<summary>A</summary>

`0x80` is the minimum signed 8-bit value because its bit pattern is `10000000`, which represents `-128` in 8-bit two's complement.

</details>

---

### Q5. What does `value & 0xff` do, and why was it useful in the Python experiment?

<details>
<summary>A</summary>

`value & 0xff` keeps only the lowest 8 bits of `value`. It was useful in Python because Python integers do not wrap automatically to 8 bits, so the mask simulated fixed-width 8-bit behavior.

</details>

---

### Q6. How does the `signed8` function convert values from `0x80` through `0xff` into negative numbers?

<details>
<summary>A</summary>

The `signed8` function first keeps the low 8 bits. If the value is at least `0x80`, it subtracts `0x100`, converting the unsigned range `128–255` into the signed range `-128–-1`.

</details>

---

### Q7. What are the signed and unsigned 32-bit meanings of `0xffffffff`?

<details>
<summary>A</summary>

As an unsigned 32-bit value, `0xffffffff` means `4294967295`. As a signed 32-bit two's complement value, it means `-1`.

</details>

---

### Q8. Why should `0xffffffff` not be interpreted immediately as only `4294967295`?

<details>
<summary>A</summary>

`0xffffffff` should not be interpreted immediately as only `4294967295` because its meaning depends on the integer width, signedness, and usage context. In 32 bits, it can mean unsigned `4294967295`, signed `-1`, or an all-bits-set mask.

</details>

---

### Q9. What is the relationship between `0xff`, `0xffffffff`, and the idea of all bits set?

<details>
<summary>A</summary>

`0xff` is all eight bits set in one byte, while `0xffffffff` is all 32 bits set in four bytes. Both represent the all-bits-set pattern for their respective widths.

</details>

---

### Q10. Why does C require extra caution when reasoning about signed overflow compared with unsigned overflow?

<details>
<summary>A</summary>

C requires extra caution because unsigned overflow has defined modulo wraparound behavior, while signed overflow is undefined behavior. Therefore, signed overflow cannot safely be assumed to wrap to the opposite end of the range.

</details>

---

## Next Session

Next:

```text
Phase 01
Session 04
```

Topic:

```text
Bitwise Operations, Masks, Flags, and Endianness
```

---
Roadmap: Number Systems for Systems Programming
Phase: Phase 01 — Practical Number Representations
Session: Session 01
Title: Binary, Hexadecimal, and Byte Recognition
Status: Completed
Review: Pending
ArchiveVersion: 2
Date:
---

# Phase 01 — Session 01: Binary, Hexadecimal, and Byte Recognition

## Objective

Understand how binary, hexadecimal, and byte-level representations relate to each other in practical systems work.

The goal of this session was not manual arithmetic. The goal was to recognize common byte patterns, distinguish raw data from representation, and begin reading hex dumps as evidence of actual byte values.

This session supports later work in:

- C programming
- Linux internals
- ELF analysis
- memory inspection
- packet analysis
- cryptography
- reverse engineering
- embedded systems
- payload and parser reasoning

---

## Learning Summary

A computer stores and processes data as bits, but humans usually inspect that data through representations such as hexadecimal, binary, decimal, or ASCII.

The key relationship is:

```text
1 hex digit = 4 bits
2 hex digits = 8 bits = 1 byte
````

This is why hexadecimal is common in systems programming. It maps cleanly to byte boundaries while staying much shorter than binary.

Examples:

```text
0xf        = 4 bits
0xff       = 1 byte
0xffff     = 2 bytes
0xffffffff = 4 bytes
```

The session also introduced the distinction between actual byte values and how tools display those values.

For example:

```text
raw byte: 0x30
ASCII interpretation: '0'
xxd hex view: 30
xxd ASCII view: 0
```

By contrast:

```text
raw byte: 0x00
ASCII interpretation: NUL
xxd hex view: 00
xxd ASCII view: .
```

The `.` in the ASCII view does not mean that a dot byte is stored. It means the byte is not printable as a normal ASCII character.

---

## Key Concepts

* bit
* byte
* nibble
* hexadecimal
* binary representation
* raw bytes
* hex dump
* ASCII interpretation
* printable and non-printable bytes
* NUL byte
* LF / newline
* offset
* representation vs actual data

---

## Practical Observations

### Observation 01 — Hex Digit Size

Prediction:

```text
0xf        = 4 bits
0xff       = 1 byte
0xffff     = 2 bytes
0xffffffff = 4 bytes
```

Observation:

The prediction was correct.

Explanation:

Each hexadecimal digit represents exactly 4 bits.

```text
hex 1 digit  = 4 bits
hex 2 digits = 8 bits = 1 byte
hex 4 digits = 16 bits = 2 bytes
hex 8 digits = 32 bits = 4 bytes
```

This makes hexadecimal useful for reading byte-sized data.

---

### Observation 02 — Byte Patterns

Prediction:

```text
0x00 = 0000 0000
0x01 = 0000 0001
0x0f = 0000 1111
0xf0 = 1111 0000
0xff = 1111 1111
```

Observation:

The prediction was correct.

Explanation:

Each hexadecimal digit maps to 4 bits.

```text
0 = 0000
1 = 0001
f = 1111
```

Therefore:

```text
0x0f = 0000 1111
0xf0 = 1111 0000
```

This also introduced the idea of a nibble.

```text
1 nibble = 4 bits
1 byte   = 2 nibbles = 8 bits
```

---

### Observation 03 — `xxd` Default Output

Command:

```bash
printf '\x00\x01\x0f\xf0\xff' | xxd
```

Observed output:

```text
00000000: 0001 0ff0 ff                             .....
```

Initial confusion:

The expected output was binary:

```text
00000000 00000001 00001111 11110000 11111111
```

Correct explanation:

The prediction described the actual bit patterns correctly, but `xxd` default output displays bytes in hexadecimal, not binary.

```text
raw bytes:
\x00 \x01 \x0f \xf0 \xff

xxd hex view:
00 01 0f f0 ff
```

The left side:

```text
00000000:
```

is an offset, not data.

The right side:

```text
.....
```

is the ASCII display area. The dots represent non-printable bytes.

---

### Observation 04 — `xxd -b` Binary Output

Command:

```bash
printf '\x00\x01\x0f\xf0\xff' | xxd -b
```

Observed output:

```text
00000000: 00000000 00000001 00001111 11110000 11111111  .....
```

Explanation:

`xxd -b` shows the same raw bytes in binary representation.

The data did not change.

Only the representation changed.

```text
raw bytes
   │
   ├─ xxd     → hex representation
   └─ xxd -b  → binary representation
```

---

### Observation 05 — ASCII Bytes for `ABC`

Prediction:

```text
A = 0x41
B = 0x42
C = 0x43
```

Command:

```bash
printf 'ABC' | xxd
printf 'ABC' | xxd -b
```

Observed output:

```text
xxd:
00000000: 4142 43                                  ABC

xxd -b:
00000000: 01000001 01000010 01000011              ABC
```

Explanation:

The same bytes can be interpreted in several ways.

```text
Character: A
Hex:       41
Binary:    01000001
Decimal:   65
ASCII:     A
```

The byte `0x41` did not become `A`. Rather, when interpreted through ASCII rules, `0x41` is displayed as `A`.

---

### Observation 06 — Character `0` vs NUL Byte

Prediction:

```text
printf '0'    → 0x30
printf '\x00' → 0x00
```

Commands:

```bash
printf '0' | xxd
printf '\x00' | xxd
```

Observed result:

```text
printf '0':
30

printf '\x00':
00
```

ASCII view difference:

```text
0x30 → 0
0x00 → .
```

Explanation:

The character `'0'` and the NUL byte are different.

```text
'0'  = 0x30 = 00110000
'\0' = 0x00 = 00000000
```

`0x30` is a printable ASCII character.

`0x00` is a non-printable zero byte.

---

### Observation 07 — String `"0A"` vs Byte `0x0a`

Prediction:

```text
printf '0A':
hex = 30 41
ASCII view = 0A

printf '\x0a':
hex = 0a
ASCII view = .
```

Explanation:

These are different:

```text
'0A'
= visible characters
= 2 bytes
= 0x30 0x41

'\x0a'
= one byte written by a hex escape
= 1 byte
= 0x0a
= LF / newline
```

The important distinction:

```text
"0a" = two visible characters
0x0a = one newline byte
```

---

### Observation 08 — Reading a Hex Dump

Given output:

```text
00000000: 3030 0a00  00..
```

Correct interpretation:

```text
offset:     00000000:
hex bytes:  30 30 0a 00
ASCII view: 00..
```

Byte-by-byte meaning:

```text
0x30 = character '0'
0x30 = character '0'
0x0a = LF / newline
0x00 = NUL byte
```

Answers:

```text
actual hex byte sequence: 30 30 0a 00
character '0' count: 2
NUL byte count: 1
newline byte count: 1
```

The ASCII view `00..` is not the actual stored byte sequence. The actual stored values are read from the hex byte area.

---

## Commands / Code

```bash
printf '\x00\x01\x0f\xf0\xff' | xxd
```

Displays raw bytes in hexadecimal.

---

```bash
printf '\x00\x01\x0f\xf0\xff' | xxd -b
```

Displays the same raw bytes in binary.

---

```bash
printf 'ABC' | xxd
```

Displays the ASCII bytes for `A`, `B`, and `C`.

---

```bash
printf 'ABC' | xxd -b
```

Displays the ASCII bytes for `A`, `B`, and `C` in binary.

---

```bash
printf '0' | xxd
```

Shows that the visible character `'0'` is byte `0x30`.

---

```bash
printf '\x00' | xxd
```

Shows a NUL byte, `0x00`.

---

```bash
printf '0A' | xxd
```

Shows two visible characters as two bytes:

```text
30 41
```

---

```bash
printf '\x0a' | xxd
```

Shows one newline byte:

```text
0a
```

---

## Connections

```text
Bits
↓
Bytes
↓
Hexadecimal
↓
Hex Dump
↓
ASCII Interpretation
↓
C Strings / ELF / Packets / Firmware / Payloads
```

This session connects directly to C strings:

```text
"0"
↓
0x30 0x00
↓
character '0' + terminating NUL byte
```

It also connects to binary analysis:

```text
hex dump
↓
raw byte observation
↓
file structure / memory layout / packet fields / firmware contents
```

The same skill will appear later when inspecting:

* ELF magic bytes
* memory dumps
* network packet payloads
* cryptographic byte strings
* C string termination
* binary protocol fields
* exploit payload bytes
* embedded firmware images

---

## Common Misconceptions

### Misconception 01 — `xxd` Shows Binary by Default

Incorrect:

```text
xxd shows bytes as 00000000-style binary values.
```

Correct:

```text
xxd shows bytes in hexadecimal by default.
xxd -b shows bytes in binary.
```

---

### Misconception 02 — Offset Is Data

Incorrect:

```text
00000000: is part of the byte sequence.
```

Correct:

```text
00000000: is the offset.
The actual byte values are shown after the colon.
```

---

### Misconception 03 — ASCII View Is the Actual Byte Sequence

Incorrect:

```text
The right side of xxd is the actual stored data.
```

Correct:

```text
The right side is a printable ASCII interpretation.
The actual byte values should be read from the hex area.
```

---

### Misconception 04 — `'0'` and `0x00` Are the Same

Incorrect:

```text
'0' = 0x00
```

Correct:

```text
'0'  = 0x30
0x00 = NUL byte
```

---

### Misconception 05 — `"0a"` and `0x0a` Are the Same

Incorrect:

```text
"0a" and 0x0a are the same.
```

Correct:

```text
"0a" = 0x30 0x61
0x0a = LF / newline byte
```

---

## Key Takeaways

* Hexadecimal is common because one hex digit maps to 4 bits.
* Two hex digits represent one byte.
* `xxd` displays raw bytes in hexadecimal by default.
* `xxd -b` displays raw bytes in binary.
* The left side of `xxd` output is an offset, not data.
* The right side of `xxd` output is an ASCII interpretation, not the source of truth.
* The character `'0'` is `0x30`.
* The NUL byte is `0x00`.
* The newline / LF byte is `0x0a`.
* The same raw byte can be interpreted as hex, binary, decimal, ASCII, or another structure depending on context.

---

## Review Questions

### Q1. Why is hexadecimal commonly used when inspecting bytes?

<details>
<summary>A</summary>

</details>

---

### Q2. How many bits are represented by one hexadecimal digit?

<details>
<summary>A</summary>

</details>

---

### Q3. What is the difference between `0xff`, `0xffff`, and `0xffffffff` in terms of byte size?

<details>
<summary>A</summary>

</details>

---

### Q4. In `xxd` output, what does the left-side value such as `00000000:` represent?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does `0x00` appear as `.` in the ASCII area of `xxd` output?

<details>
<summary>A</summary>

</details>

---

### Q6. What is the difference between the character `'0'` and the byte `0x00`?

<details>
<summary>A</summary>

</details>

---

### Q7. Why are `"0a"` and `0x0a` different?

<details>
<summary>A</summary>

</details>

---

### Q8. Given the hex dump `3030 0a00`, how many visible character `0` bytes, newline bytes, and NUL bytes are present?

<details>
<summary>A</summary>

</details>

---

## Next Session

Next:

```text
Phase 01
Session 02
```

Topic:

```text
Octal, Permissions, ASCII, and Text as Bytes
```

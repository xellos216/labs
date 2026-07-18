---
Roadmap: Number Systems for Systems Programming
Phase: Phase 01 — Practical Number Representations
Session: Session 04
Title: Bitwise Operations, Masks, Flags, and Endianness
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-07
---

# Phase 01 — Session 04: Bitwise Operations, Masks, Flags, and Endianness

## Objective

Understand how individual bits are used as switches, how masks and flags are represented and manipulated, and how byte order affects integer interpretation.

The goal of this session was to connect bitwise operations to real systems patterns such as Unix permissions, C flags, protocol fields, registers, masks, and memory byte order.

This session focused on:

- `&` as filtering or testing
- `|` as enabling bits
- `^` as toggling bits
- `~` as bit inversion
- `<<` and `>>` as position changes
- masks and flags
- bit numbering
- byte order and endianness

---

## Learning Summary

Bits can be treated as individual switches.

```text
bit
↓
switch
↓
mask / flag
↓
field extraction / permission / register / packet / memory
```

A mask marks which bit positions should be inspected or modified.

```text
mask bit = 1
↓
selected position

mask bit = 0
↓
unselected position
```

The main bitwise operations have distinct roles.

```text
&  = keep or test selected bits
|  = enable selected bits
^  = toggle selected bits
~  = invert bits
<< = move bits left
>> = move bits right
```

The session also introduced endianness as byte order, not bit order.

```text
0x12345678
↓
bytes: 12 34 56 78
```

Big-endian stores the highest-order byte first.

```text
12 34 56 78
```

Little-endian stores the lowest-order byte first.

```text
78 56 34 12
```

The stored bytes do not change during interpretation. The rule used to interpret them changes.

---

## Key Concepts

- bit
- switch
- mask
- flag
- bitwise AND
- bitwise OR
- bitwise XOR
- bitwise NOT
- left shift
- right shift
- bit index
- permission bits
- flag testing
- flag enabling
- flag clearing
- flag toggling
- byte sequence
- endianness
- little-endian
- big-endian

---

## Practical Observations

### Observation 01 — AND, OR, and XOR with a Mask

Given:

```text
value = 0b10101010
mask  = 0b00001111
```

Predicted results:

```text
value & mask = 0b00001010
value | mask = 0b10101111
value ^ mask = 0b10100101
```

Explanation:

AND keeps only positions selected by the mask.

```text
10101010
& 00001111
----------
00001010
```

OR enables positions selected by the mask.

```text
10101010
| 00001111
----------
10101111
```

XOR toggles positions selected by the mask.

```text
10101010
^ 00001111
----------
10100101
```

The key rule is:

```text
mask 1 = selected bit
mask 0 = unselected bit
```

---

### Observation 02 — Unix Permissions as Bit Flags

Permission bits can be represented as individual flags.

```text
r = 0b100 = 4
w = 0b010 = 2
x = 0b001 = 1
```

Predicted combinations:

```text
rw- = 0b110 = 6
r-x = 0b101 = 5
-wx = 0b011 = 3
rwx = 0b111 = 7
```

Explanation:

Permission values are combinations of bit flags.

```text
rw-
= r | w
= 100 | 010
= 110
= 6
```

```text
r-x
= r | x
= 100 | 001
= 101
= 5
```

This reframes `chmod 755` as bit-flag composition rather than memorized digits.

```text
755
↓
7       5       5
rwx     r-x     r-x
111     101     101
```

---

### Observation 03 — Testing Permission Bits with AND

Given:

```text
perm = 0b101
r    = 0b100
w    = 0b010
x    = 0b001
```

Predicted results:

```text
perm & r = 0b100 → permission present
perm & w = 0b000 → permission absent
perm & x = 0b001 → permission present
```

Explanation:

AND can test whether a flag is set.

```text
perm & flag != 0
↓
flag is set
```

```text
perm & flag == 0
↓
flag is not set
```

For `perm = 0b101`, read and execute are set, but write is not set.

---

### Observation 04 — Enabling a Bit with OR

Given:

```text
perm = 0b100
x    = 0b001
```

Predicted result:

```text
0b100 | 0b001 = 0b101
```

Meaning:

```text
r-- + x
↓
r-x
```

Explanation:

OR enables selected bits without clearing existing bits.

```text
100
| 001
-----
101
```

This is why OR is used to add a flag.

```text
value | flag
↓
enable flag
```

---

### Observation 05 — Clearing Bits with AND and NOT

Given:

```text
perm = 0b111
r    = 0b100
w    = 0b010
x    = 0b001
```

Predicted results:

```text
perm & ~r = 0b011 = -wx
perm & ~w = 0b101 = r-x
perm & ~x = 0b110 = rw-
```

Explanation:

To clear a bit, invert the flag and AND it with the value.

```text
w  = 010
~w = 101   # considering only the 3 permission bits
```

```text
111
& 101
-----
101
```

The selected bit is cleared and the other bits are preserved.

---

### Observation 06 — Toggling Bits with XOR

Given:

```text
perm = 0b110
x    = 0b001
```

Predicted result:

```text
perm ^ x = 0b111
```

Repeating the same operation:

```text
0b111 ^ 0b001 = 0b110
```

Explanation:

XOR toggles selected bits.

```text
0 ^ 1 = 1
1 ^ 1 = 0
0 ^ 0 = 0
1 ^ 0 = 1
```

Therefore:

```text
value ^ flag
↓
toggle flag
```

---

### Observation 07 — Shift Operations and Bit Masks

Initial prediction placed the masks one position too far to the right. The corrected mapping was:

```text
1 << 0 = 00000001 = 0x01
1 << 1 = 00000010 = 0x02
1 << 2 = 00000100 = 0x04
1 << 7 = 10000000 = 0x80
```

Explanation:

The value `1` already has bit 0 set.

```text
1 = 00000001
```

`1 << n` moves that set bit `n` positions to the left.

```text
1 << n
↓
mask with bit n set
```

Bit indexes are counted from the right, starting at zero.

```text
bit index: 7 6 5 4 3 2 1 0
binary:    0 0 0 0 0 0 0 1
                             ↑
                           bit 0
```

---

### Observation 08 — Building Permission Flags with Shifts

Flags can be built from bit positions.

```text
READ  = 1 << 2 = 0b100 = 4
WRITE = 1 << 1 = 0b010 = 2
EXEC  = 1 << 0 = 0b001 = 1
```

Given:

```text
perm = READ | EXEC
```

Predicted result:

```text
perm = 0b101 = 5 = r-x
```

Explanation:

Flags can be composed from named bit positions instead of memorized numeric constants.

```text
READ | EXEC
↓
100 | 001
↓
101
↓
r-x
```

---

### Observation 09 — Python Flag Observation

Command:

```bash
python3 - <<'PY'
READ  = 1 << 2
WRITE = 1 << 1
EXEC  = 1 << 0

perm = READ | EXEC

print("READ =", bin(READ), READ)
print("WRITE =", bin(WRITE), WRITE)
print("EXEC =", bin(EXEC), EXEC)
print("perm =", bin(perm), perm)

print("has READ:", bool(perm & READ))
print("has WRITE:", bool(perm & WRITE))
print("has EXEC:", bool(perm & EXEC))
PY
```

Observed result:

```text
READ = 0b100 4
WRITE = 0b10 2
EXEC = 0b1 1
perm = 0b101 5
has READ: True
has WRITE: False
has EXEC: True
```

Explanation:

Python's `bin()` does not preserve leading zeroes.

```text
0b010 = 0b10
0b001 = 0b1
```

The values are identical.

```text
0b010 = 2
0b10  = 2
```

The flag checks worked because `perm & FLAG` returns zero only when that flag is absent.

```text
perm = 0b101
READ = 0b100

perm & READ = 0b100
bool(0b100) = True
```

```text
perm = 0b101
WRITE = 0b010

perm & WRITE = 0b000
bool(0) = False
```

---

### Observation 10 — Byte Order and Endianness

Given the 32-bit value:

```text
0xaabbccdd
```

Byte sequence:

```text
aa bb cc dd
```

Predicted byte orders:

```text
big-endian:    aa bb cc dd
little-endian: dd cc bb aa
```

Explanation:

Endianness is byte order, not bit order.

```text
0xaabbccdd
↓
bytes: aa bb cc dd
```

Big-endian stores the highest-order byte first.

```text
aa bb cc dd
```

Little-endian stores the lowest-order byte first.

```text
dd cc bb aa
```

The byte values themselves are not bit-reversed.

---

### Observation 11 — Reading Bytes as Little-Endian or Big-Endian

Given memory bytes:

```text
78 56 34 12
```

Correct interpretation:

```text
little-endian 32-bit value = 0x12345678
big-endian 32-bit value    = 0x78563412
```

Explanation:

Little-endian treats the first byte as the lowest-order byte.

```text
78 56 34 12
↓ little-endian
0x12345678
```

Big-endian treats the first byte as the highest-order byte.

```text
78 56 34 12
↓ big-endian
0x78563412
```

A byte sequence and an integer value should be distinguished.

```text
byte sequence: 78 56 34 12
integer value: 0x12345678 or 0x78563412
```

---

### Observation 12 — Python `struct` Endianness Observation

Command:

```bash
python3 - <<'PY'
import struct

data = bytes.fromhex("dd cc bb aa")

little = struct.unpack("<I", data)[0]
big = struct.unpack(">I", data)[0]

print("bytes:", data.hex(" "))
print("little:", hex(little))
print("big:", hex(big))
PY
```

Observed result:

```text
bytes: dd cc bb aa
little: 0xaabbccdd
big: 0xddccbbaa
```

Explanation:

`data.hex(" ")` displays the actual byte sequence.

```text
dd cc bb aa
```

`struct.unpack("<I", data)` interprets those bytes as a little-endian unsigned 32-bit integer.

```text
dd cc bb aa
↓ little-endian
0xaabbccdd
```

`struct.unpack(">I", data)` interprets those bytes as a big-endian unsigned 32-bit integer.

```text
dd cc bb aa
↓ big-endian
0xddccbbaa
```

The bytes did not change. The interpretation rule changed.

---

### Observation 13 — Final Integration Check

Given:

```text
value = 0b10101100
mask  = 0b00001111
```

Correct results:

```text
value & mask = 0b00001100
value | mask = 0b10101111
value ^ mask = 0b10100011
```

The initial explanation for `value & 0xff` was corrected.

Incorrect interpretation:

```text
value & 0xff shows all enabled bits.
```

Correct interpretation:

```text
value & 0xff keeps only the low 8 bits.
```

Because `0xff` is an 8-bit mask:

```text
11111111
```

For an already 8-bit value, the result remains the same.

```text
10101100
& 11111111
----------
10101100
```

The endianness integration check was correct.

```text
bytes: 78 56 34 12
little-endian 32-bit value = 0x12345678
big-endian 32-bit value    = 0x78563412
```

---

## Commands / Code

```python
READ  = 1 << 2
WRITE = 1 << 1
EXEC  = 1 << 0
```

Defines permission flags from bit positions.

---

```python
perm = READ | EXEC
```

Enables the `READ` and `EXEC` flags.

---

```python
bool(perm & READ)
bool(perm & WRITE)
bool(perm & EXEC)
```

Tests whether specific flags are set.

---

```python
perm & ~WRITE
```

Clears the `WRITE` flag while preserving other flags.

---

```python
perm ^ EXEC
```

Toggles the `EXEC` flag.

---

```bash
python3 - <<'PY'
READ  = 1 << 2
WRITE = 1 << 1
EXEC  = 1 << 0

perm = READ | EXEC

print("READ =", bin(READ), READ)
print("WRITE =", bin(WRITE), WRITE)
print("EXEC =", bin(EXEC), EXEC)
print("perm =", bin(perm), perm)

print("has READ:", bool(perm & READ))
print("has WRITE:", bool(perm & WRITE))
print("has EXEC:", bool(perm & EXEC))
PY
```

Observes flag construction and flag testing in Python.

---

```bash
python3 - <<'PY'
import struct

data = bytes.fromhex("dd cc bb aa")

little = struct.unpack("<I", data)[0]
big = struct.unpack(">I", data)[0]

print("bytes:", data.hex(" "))
print("little:", hex(little))
print("big:", hex(big))
PY
```

Interprets the same byte sequence as little-endian and big-endian unsigned 32-bit integers.

---

## Connections

```text
bit
↓
flag
↓
mask
↓
field / permission / register / packet
```

This session connects directly to Unix permissions.

```text
r = 100
w = 010
x = 001
↓
chmod values
```

It connects to C programming.

```text
#define READ  (1 << 2)
#define WRITE (1 << 1)
#define EXEC  (1 << 0)
```

It connects to embedded systems and hardware registers.

```text
register value
↓
individual bit flags
↓
feature enabled / disabled
```

It connects to networking and protocol parsing.

```text
packet field
↓
bit masks
↓
flags and subfields
```

It connects to reverse engineering and binary analysis.

```text
memory bytes
↓
endianness
↓
integer interpretation
```

---

## Common Misconceptions

### Misconception 01 — OR Replaces the Whole Value

Incorrect:

```text
value | flag replaces the full value with the flag.
```

Correct:

```text
value | flag enables selected bits while preserving existing set bits.
```

---

### Misconception 02 — AND Means the Same Thing as Boolean AND Only

Incorrect:

```text
& only means logical true/false comparison.
```

Correct:

```text
& operates bit by bit and is commonly used for masking and flag testing.
```

---

### Misconception 03 — `1 << 0` Produces Zero

Incorrect:

```text
1 << 0 = 0
```

Correct:

```text
1 << 0 = 1
```

The starting value `1` already has bit 0 set.

---

### Misconception 04 — `bin()` Preserves Leading Zeroes

Incorrect:

```text
bin(0b010) prints 0b010.
```

Correct:

```text
bin(0b010) prints 0b10.
```

Leading zeroes are representation padding, not part of the numeric value.

---

### Misconception 05 — Endianness Reverses Bits Inside Each Byte

Incorrect:

```text
little-endian reverses every bit inside each byte.
```

Correct:

```text
endianness changes byte order, not bit order inside bytes.
```

---

### Misconception 06 — Byte Sequence and Integer Value Are the Same Display

Incorrect:

```text
bytes dd cc bb aa and integer 0xaabbccdd are the same kind of output.
```

Correct:

```text
bytes dd cc bb aa show storage order.
integer 0xaabbccdd shows the result of interpreting those bytes using a byte-order rule.
```

---

### Misconception 07 — `value & 0xff` Shows All Enabled Bits

Incorrect:

```text
value & 0xff means show every bit that is set in value.
```

Correct:

```text
value & 0xff keeps only the low 8 bits of value.
```

---

## Key Takeaways

- Bits can be treated as independent switches.
- A mask selects which bit positions matter.
- `&` keeps or tests selected bits.
- `|` enables selected bits.
- `^` toggles selected bits.
- `~` inverts bits, usually combined with `&` to clear flags.
- `1 << n` creates a mask with bit `n` set.
- Bit indexes are counted from the right, starting at zero.
- Unix permission digits are bit-flag combinations.
- `perm & flag` tests whether a permission or flag is present.
- `perm | flag` enables a permission or flag.
- `perm & ~flag` clears a permission or flag.
- `perm ^ flag` toggles a permission or flag.
- Endianness is byte order, not bit order.
- Little-endian stores the lowest-order byte first.
- Big-endian stores the highest-order byte first.
- The same bytes can produce different integer values depending on byte order.

---

## Review Questions

### Q1. What does a mask represent in bitwise operations?

<details>
<summary>A</summary>

A mask is a bit pattern that selects which bit positions should be tested, preserved, enabled, cleared, or toggled.

</details>

---

### Q2. What is the difference between `value & mask`, `value | mask`, and `value ^ mask`?

<details>
<summary>A</summary>

`value & mask` keeps or tests the selected bits, `value | mask` enables the selected bits, and `value ^ mask` toggles the selected bits.

</details>

---

### Q3. Why can Unix permissions such as `rwx` be represented as bit flags?

<details>
<summary>A</summary>

Unix permissions can be represented as bit flags because `r`, `w`, and `x` are independent yes/no states. They map to the three bits `100`, `010`, and `001`, with numeric values `4`, `2`, and `1`.

</details>

---

### Q4. How can `perm & flag` be used to test whether a flag is set?

<details>
<summary>A</summary>

If `perm & flag` produces a non-zero result, the flag is set. If it produces zero, the flag is not set.

</details>

---

### Q5. How do you enable, clear, and toggle a single bit flag?

<details>
<summary>A</summary>

Enable a flag with `value | flag`, clear it with `value & ~flag`, and toggle it with `value ^ flag`.

</details>

---

### Q6. Why does `1 << 7` produce `0x80` in an 8-bit view?

<details>
<summary>A</summary>

`1` is `00000001` in an 8-bit view. Shifting it left by seven positions produces `10000000`, which is `0x80`.

</details>

---

### Q7. Why does Python print `0b10` instead of `0b010`?

<details>
<summary>A</summary>

Python prints `0b10` instead of `0b010` because leading zeroes are not part of the numeric value, and `bin()` returns the shortest binary representation.

</details>

---

### Q8. What is the difference between a byte sequence and an integer value?

<details>
<summary>A</summary>

A byte sequence shows the bytes in storage order, while an integer value is the numeric result of interpreting those bytes according to a width and byte-order rule.

</details>

---

### Q9. Given bytes `78 56 34 12`, why does little-endian interpretation produce `0x12345678`?

<details>
<summary>A</summary>

Little-endian interpretation produces `0x12345678` because the first byte, `0x78`, is treated as the least significant byte, followed by `0x56`, `0x34`, and `0x12` as increasingly significant bytes.

</details>

---

### Q10. Why is endianness described as byte order rather than bit order?

<details>
<summary>A</summary>

Endianness is described as byte order because it determines the order of bytes in a multi-byte value. It does not reverse the bit order inside each byte.

</details>

---

## Next Session

Next:

```text
Phase 01
Session 05
```

Topic:

```text
Hex Dumps, Magic Values, Addresses, and Systems Recognition Review
```

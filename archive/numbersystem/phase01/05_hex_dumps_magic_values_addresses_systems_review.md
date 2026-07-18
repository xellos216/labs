---
Roadmap: Number Systems for Systems Programming
Phase: Phase 01 — Practical Number Representations
Session: Session 05
Title: Hex Dumps, Magic Values, Addresses, and Systems Recognition Review
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-08
---

# Phase 01 — Session 05: Hex Dumps, Magic Values, Addresses, and Systems Recognition Review

## Objective

Integrate the previous Phase 01 topics into practical recognition work:

- reading hex dumps as structured evidence
- recognizing file signatures and magic values
- separating byte sequences from integer values
- identifying address-looking values
- distinguishing ordinary values from system-context values
- reading basic `/proc/PID/maps` style memory mappings

The session emphasized recognition from evidence rather than memorizing isolated hexadecimal constants.

```text
hex value
↓
byte sequence
↓
representation context
↓
likely system meaning
```

---

## Learning Summary

A hex dump is not one flat string. It usually has separate fields.

```text
00000000: 7f45 4c46 0201 0100  .ELF....
```

This can be separated as:

```text
00000000:
= offset

7f45 4c46 0201 0100
= actual bytes

.ELF....
= ASCII helper view
```

The byte area is the primary evidence. The ASCII view is a helper representation.

```text
offset
↓
hex bytes
↓
ASCII helper view
```

A value can mean different things depending on context.

```text
0x00000000
```

Possible interpretations:

```text
integer zero
null pointer
cleared memory
empty field
```

The same reasoning applies to recognizable patterns.

```text
0x41414141
↓
41 41 41 41
↓
AAAA
↓
ASCII filler pattern
```

```text
0xdeadbeef
↓
recognizable debug or sentinel-looking value
```

---

## Key Concepts

- hex dump
- offset
- byte sequence
- ASCII view
- printable byte
- non-printable byte
- magic value
- file signature
- ELF header
- ASCII filler
- cleared bytes
- all bits set
- signed maximum
- unsigned maximum
- little-endian storage
- big-endian storage
- memory address-looking value
- process memory map
- file-backed mapping
- anonymous mapping
- stack region
- private mapping
- shared mapping
- executable region

---

## Practical Observations

### Observation 01 — Reading an ELF Magic Sequence

Given:

```text
00000000: 7f45 4c46 0201 0100  .ELF....
```

The first interpretation was mostly correct:

```text
offset: 00000000
ASCII view: display, not the source bytes
system context: ELF file header
```

The byte grouping needed correction.

`xxd` may group bytes visually as two-byte chunks.

```text
7f45 4c46
```

But byte-level recognition should split them into individual bytes.

```text
7f 45 4c 46
```

Correct classification:

```text
offset: 00000000
first four bytes: 7f 45 4c 46
ASCII view: .ELF
context: ELF file header
```

The ASCII helper view appears because:

```text
7f = non-printable byte → .
45 = ASCII E
4c = ASCII L
46 = ASCII F
```

Therefore:

```text
7f 45 4c 46
↓
.  E  L  F
↓
.ELF
```

The string `.ELF` is a display result. The actual bytes are `7f 45 4c 46`.

---

### Observation 02 — Common Hexadecimal Patterns

Given:

```text
1. 0x41414141
2. 0x00000000
3. 0xffffffff
4. 0xdeadbeef
```

Correct classification:

```text
1. 0x41414141
= ASCII pattern
= AAAA

2. 0x00000000
= zero / null / cleared value

3. 0xffffffff
= all bits set / -1 / max unsigned

4. 0xdeadbeef
= debug / sentinel-looking magic value
```

`0x41414141` is an ASCII pattern because:

```text
0x41 = ASCII A
```

Therefore:

```text
41 41 41 41
↓
A  A  A  A
↓
AAAA
```

`0xdeadbeef` is not an ASCII filler. It is a recognizable hex phrase often used as a debug marker, sentinel, poisoned value, or test value. Its exact meaning is context-dependent.

---

### Observation 03 — Byte Sequence, ASCII View, and Little-Endian Storage

Given:

```text
0x7f454c46
```

Correct byte sequence:

```text
7f 45 4c 46
```

ASCII view:

```text
.ELF
```

System context:

```text
ELF file header
```

If the 32-bit integer value `0x7f454c46` is stored in little-endian memory, the lowest-order byte is stored first.

```text
value:
0x7f454c46

highest to lowest bytes:
7f 45 4c 46

little-endian memory order:
46 4c 45 7f
```

This distinguishes integer notation from memory byte sequence notation.

```text
integer value: 0x7f454c46
memory bytes:  46 4c 45 7f
```

---

### Observation 04 — Address-Looking Values

Given:

```text
1. 0x00000000
2. 0x7fffffff
3. 0x7fffffffe000
4. 0x41414141
5. 0x00007ffff7dd0000
```

Correct classification:

```text
1. 0x00000000
= zero / null

2. 0x7fffffff
= signed 32-bit max-looking value

3. 0x7fffffffe000
= memory address-looking value

4. 0x41414141
= ASCII pattern

5. 0x00007ffff7dd0000
= memory address-looking value
```

The important distinction is not just length. It is context and shape.

```text
0x7fffffffe000
0x00007ffff7dd0000
```

These look like values that might appear in process memory maps, stack ranges, shared library mappings, or debugger output.

`0x7fffffff` is different. It is a well-known 32-bit signed maximum-looking value.

```text
0x7fffffff
= 2147483647
= max signed 32-bit integer
```

---

### Observation 05 — Reading a Stack Mapping

Given:

```text
7ffffffde000-7ffffffff000 rw-p 00000000 00:00 0 [stack]
```

Correct field breakdown:

```text
start address: 0x7ffffffde000
end address:   0x7ffffffff000
permissions:   rw-p
region:        [stack]
```

The permission field means:

```text
r = readable
w = writable
x = executable
p = private mapping
```

For this mapping:

```text
rw-p
```

The interpretation is:

```text
r = read allowed
w = write allowed
- = execute not allowed
p = private mapping
```

The corrected breakdown is:

```text
address range: 0x7ffffffde000-0x7ffffffff000
permission:    rw-p
mapping:       private, readable, writable, not executable
region:        stack
backing:       anonymous / special process memory region
```

`[stack]` is not a normal file path. It is a special process memory region label.

---

### Observation 06 — Reading a File-Backed Mapping

Given:

```text
555555554000-555555555000 r--p 00000000 08:01 123456 /bin/cat
```

Correct field breakdown:

```text
start address: 0x555555554000
end address:   0x555555555000
permissions:   r--p
file offset:   00000000
backing file:  /bin/cat
```

The permissions mean:

```text
r--p
↓
readable
not writable
not executable
private
```

Because a pathname appears at the end, this is file-backed memory.

```text
file-backed:
pathname present
example: /bin/cat
```

Anonymous or special mappings usually have no ordinary file path, or have labels such as:

```text
[heap]
[stack]
[anon:...]
```

---

### Observation 07 — Executable File-Backed Mapping

Given:

```text
555555555000-555555559000 r-xp 00001000 08:01 123456 /bin/cat
```

Correct field breakdown:

```text
start address: 0x555555555000
end address:   0x555555559000
permissions:   r-xp
file offset:   00001000
backing file:  /bin/cat
```

The permissions mean:

```text
r-xp
↓
readable
not writable
executable
private
```

The value `00001000` is not part of the permission field. It is the file offset.

```text
address range                  perms  offset    dev    inode   pathname
555555555000-555555559000      r-xp   00001000  08:01  123456  /bin/cat
```

The mapping looks like a code region because it has execute permission.

```text
r-xp
││││
│││└─ private
││└── executable
│└─── not writable
└──── readable
```

---

### Observation 08 — Comparing Two Mappings from the Same File

Given:

```text
A. 555555554000-555555555000 r--p 00000000 08:01 123456 /bin/cat
B. 555555555000-555555559000 r-xp 00001000 08:01 123456 /bin/cat
```

Correct comparison:

```text
1. Both are file-backed.
2. Both are connected to /bin/cat.
3. A is read-only and private.
4. B is read-execute and private.
5. B looks more like executable code because it has x permission.
6. A offset = 00000000.
7. B offset = 00001000.
```

A single file can be mapped into memory as multiple regions with different permissions.

```text
file
↓
segments
↓
memory mappings
↓
region-specific permissions
```

Example pattern:

```text
r--p
= read-only header or metadata-like region

r-xp
= executable code-like region

rw-p
= writable data-like region
```

This is a key systems observation: a loaded file is not necessarily one continuous memory region with one permission setting.

---

### Observation 09 — Integrated Recognition Set

Given:

```text
1. 7f 45 4c 46
2. 41 41 41 41
3. 00 00 00 00
4. ef be ad de
5. 555555555000-555555559000 r-xp /bin/cat
```

Correct classification:

```text
1. 7f 45 4c 46
= ELF magic

2. 41 41 41 41
= ASCII filler
= AAAA

3. 00 00 00 00
= zero / cleared bytes

4. ef be ad de
= little-endian representation of 0xdeadbeef

5. 555555555000-555555559000 r-xp /bin/cat
= file-backed executable memory region
```

The `0xdeadbeef` endianness connection is important.

```text
0xdeadbeef
```

Big-endian byte order:

```text
de ad be ef
```

Little-endian byte order:

```text
ef be ad de
```

Therefore, seeing this in a hex dump:

```text
ef be ad de
```

suggests:

```text
0xdeadbeef stored in little-endian memory
```

---

### Observation 10 — Final Integration Check

Given:

```text
1. 0x00000000
2. 0xffffffff
3. 0x41414141
4. de ad be ef
5. ef be ad de
6. 7f 45 4c 46
7. 555555554000-555555555000 r--p 00000000 08:01 123456 /bin/cat
8. 7ffffffde000-7ffffffff000 rw-p 00000000 00:00 0 [stack]
```

Correct classification:

```text
1. 0x00000000
= zero / null / cleared value

2. 0xffffffff
= all bits set / -1 / max unsigned

3. 0x41414141
= ASCII filler
= AAAA

4. de ad be ef
= 0xdeadbeef in big-endian byte order

5. ef be ad de
= 0xdeadbeef in little-endian byte order

6. 7f 45 4c 46
= ELF magic value
= .ELF

7. 555555554000-555555555000 r--p 00000000 08:01 123456 /bin/cat
= file-backed, read-only, private mapping of /bin/cat

8. 7ffffffde000-7ffffffff000 rw-p 00000000 00:00 0 [stack]
= private readable/writable stack mapping
```

The final answers showed stable recognition of:

- common magic bytes
- ASCII filler values
- cleared byte patterns
- endianness effects
- file-backed executable mappings
- stack mappings
- permission fields
- file offsets

---

## Commands / Code

This session was recognition-focused and did not require new shell commands. The following examples are relevant to reproduce similar observations locally.

Display the first bytes of an executable:

```bash
xxd -l 16 /bin/cat
```

Expected kind of pattern:

```text
00000000: 7f45 4c46 ...  .ELF...
```

Inspect memory mappings for the current shell process:

```bash
cat /proc/$$/maps | head
```

Look for fields like:

```text
address-range permissions offset device inode pathname
```

Example mapping shape:

```text
555555555000-555555559000 r-xp 00001000 08:01 123456 /path/to/file
```

---

## Connections

This session connects earlier Phase 01 topics into system recognition.

Binary and hexadecimal recognition:

```text
hex digits
↓
bytes
↓
ASCII view or integer interpretation
```

Signed and unsigned interpretation:

```text
0xffffffff
↓
unsigned: max 32-bit value
signed: -1
bits: all set
```

Bitwise and mask reasoning:

```text
permission field
↓
r--p / r-xp / rw-p
↓
capabilities of a memory region
```

Endianness:

```text
0xdeadbeef
↓
de ad be ef
↓
ef be ad de in little-endian memory
```

Unix and C systems:

```text
ELF file
↓
segments
↓
process memory mappings
↓
permissions and offsets
```

Embedded Linux and firmware analysis:

```text
firmware blob
↓
magic bytes
↓
file signatures
↓
packed filesystem or executable recognition
```

Debugging and reverse engineering:

```text
hex dump / GDB / proc maps
↓
classify values before interpreting behavior
```

---

## Common Misconceptions

### Misconception 01 — Visual Groups Are Always Byte Units

Incorrect:

```text
7f45 means one byte.
```

Correct:

```text
7f45 is two bytes when read as hex bytes:
7f 45
```

Hex dump tools may group bytes for readability. Byte-level analysis should split values into two-hex-digit bytes.

---

### Misconception 02 — ASCII View Is the Source Data

Incorrect:

```text
.ELF is the actual source data shown by xxd.
```

Correct:

```text
7f 45 4c 46 are the source bytes.
.ELF is the ASCII helper view.
```

The dot represents a non-printable byte.

---

### Misconception 03 — `0x41414141` Is a Debug Sentinel Like `0xdeadbeef`

Incorrect:

```text
0x41414141 is mainly a debug sentinel value.
```

Correct:

```text
0x41414141 is usually recognized as ASCII filler:
41 41 41 41 = AAAA
```

---

### Misconception 04 — `0xdeadbeef` Is an ASCII Filler

Incorrect:

```text
0xdeadbeef is an ASCII filler pattern.
```

Correct:

```text
0xdeadbeef is a recognizable magic-looking debug or sentinel value.
```

Its exact meaning depends on context.

---

### Misconception 05 — A Partial Address Is Enough

Incorrect:

```text
7fff or f000 is enough to identify the start or end address.
```

Correct:

```text
/proc/PID/maps address fields should be read as complete hex addresses.
```

Example:

```text
0x7ffffffde000-0x7ffffffff000
```

---

### Misconception 06 — `p` in `rw-p` Means Process

Incorrect:

```text
p = process
```

Correct:

```text
p = private mapping
```

The opposite style is usually `s`, meaning shared mapping.

```text
rw-p = read/write/private
rw-s = read/write/shared
```

---

### Misconception 07 — Offset Is Part of Permissions

Incorrect:

```text
r-xp 00001000 is the permission field.
```

Correct:

```text
r-xp is the permission field.
00001000 is the file offset.
```

---

### Misconception 08 — A File Maps into Memory as One Uniform Region

Incorrect:

```text
/bin/cat maps into memory once with one permission setting.
```

Correct:

```text
A file can map into multiple memory regions with different permissions and offsets.
```

Example:

```text
r--p offset 00000000
r-xp offset 00001000
rw-p offset ...
```

---

## Key Takeaways

- A hex dump should be read as fields, not as one string.
- The byte column is the primary evidence.
- The ASCII column is a helper view.
- Two hex digits represent one byte.
- `7f 45 4c 46` is ELF magic.
- `41 41 41 41` is ASCII filler for `AAAA`.
- `00 00 00 00` often suggests zero or cleared bytes.
- `ff ff ff ff` means all bits set in a 32-bit view.
- `0xffffffff` can mean max unsigned 32-bit or signed `-1` depending on interpretation.
- `0xdeadbeef` is a recognizable debug or sentinel-looking value.
- `ef be ad de` is `0xdeadbeef` stored in little-endian byte order.
- Memory-looking values should be interpreted with context, not just length.
- `/proc/PID/maps` lines contain address range, permissions, offset, device, inode, and optional pathname.
- `r--p`, `r-xp`, and `rw-p` encode memory access permissions.
- `p` means private mapping.
- A pathname usually indicates file-backed memory.
- `[stack]` indicates a special process memory region.
- A single file can appear as multiple mapped regions with different permissions.

---

## Review Questions

### Q1. In a hex dump line, what is the difference between the offset, byte column, and ASCII view?

<details>
<summary>A</summary>

The offset shows the position from the beginning of the data, the byte column shows the actual stored bytes, and the ASCII view shows a printable interpretation of those bytes.

</details>

---

### Q2. Why should `7f45 4c46` be split as `7f 45 4c 46` when doing byte-level analysis?

<details>
<summary>A</summary>

`7f45 4c46` should be split into `7f 45 4c 46` because two hexadecimal digits represent one byte. The visual grouping in `xxd` does not change the actual byte boundaries.

</details>

---

### Q3. Why does `7f 45 4c 46` appear as `.ELF` in an ASCII helper view?

<details>
<summary>A</summary>

`7f 45 4c 46` appears as `.ELF` because `0x7f` is a non-printable byte displayed as `.`, while `0x45`, `0x4c`, and `0x46` are interpreted as the printable ASCII characters `E`, `L`, and `F`.

</details>

---

### Q4. What does `0x41414141` suggest, and why?

<details>
<summary>A</summary>

`0x41414141` suggests the ASCII filler pattern `AAAA` because each byte `0x41` represents the character `A`.

</details>

---

### Q5. What are several possible meanings of `0x00000000` depending on context?

<details>
<summary>A</summary>

Depending on context, `0x00000000` can mean integer zero, a null pointer, cleared memory, or an empty field.

</details>

---

### Q6. Why can `0xffffffff` mean both max unsigned 32-bit and signed `-1`?

<details>
<summary>A</summary>

`0xffffffff` contains 32 bits all set to `1`. Interpreted as an unsigned 32-bit integer, it is `4294967295`; interpreted as a signed 32-bit two's complement integer, it is `-1`.

</details>

---

### Q7. What is the difference between `de ad be ef` and `ef be ad de`?

<details>
<summary>A</summary>

`de ad be ef` is the big-endian byte order of `0xdeadbeef`, while `ef be ad de` is the little-endian byte order of the same value.

</details>

---

### Q8. In a `/proc/PID/maps` style line, what does `r-xp` mean?

<details>
<summary>A</summary>

`r-xp` means the region is readable, executable, not writable, and privately mapped.

</details>

---

### Q9. Why is `/bin/cat` at the end of a mapping line evidence of file-backed memory?

<details>
<summary>A</summary>

`/bin/cat` at the end of the mapping line indicates that the memory region is backed by that file rather than being anonymous memory.

</details>

---

### Q10. Why can one file appear as multiple memory mappings with different permissions?

<details>
<summary>A</summary>

One file can appear as multiple memory mappings because different segments of the file are mapped separately, each with its own permissions and file offset.

</details>

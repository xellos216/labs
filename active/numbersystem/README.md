# Number Systems for Systems Programming Roadmap

## Objective

Build practical fluency with the number representations commonly encountered in systems programming, Linux, networking, embedded systems, reverse engineering, cryptography, and security.

This roadmap is not a mathematics track.

The goal is to recognize, interpret, and reason about values such as:

* `0xff`
* `0755`
* `0b11001010`
* `0x7fffffff`
* `0xdeadbeef`
* `0x7F454C46`

as they appear in real systems.

By the end of this roadmap, hexadecimal, binary, octal, byte values, memory addresses, bit masks, permissions, and encoded text should feel familiar enough that later topics do not require repeatedly relearning basic representation concepts.

---

## Philosophy

Number systems should not be studied as abstract arithmetic.

They should be studied as representations used by real systems.

Core principles:

* intuition over memorization
* recognition over lengthy manual conversion
* systems examples over abstract exercises
* observation before explanation
* byte-level reasoning
* practical pattern recognition
* long-term transferability

The guiding question is:

```text
Where would this appear in a real system?
```

Examples:

```text
0755

↓

Unix file permissions
```

```text
0x7F454C46

↓

ELF magic bytes
```

```text
0xff

↓

one full byte
```

```text
0x7fffffff

↓

maximum signed 32-bit integer
```

```text
0b11001010

↓

bit pattern, mask, packet field, register value
```

---

## Learning Method

This roadmap uses a compact hybrid structure.

Approximate ratio:

```text
Concept: 80%

Task: 20%
```

Each session follows this workflow:

```text
Recognize

↓

Interpret

↓

Observe

↓

Connect
```

Sessions should include:

* short conceptual explanation
* practical examples
* recognition exercises
* small CLI or C experiments when useful
* connections to existing systems topics

Manual conversion is used only when it improves understanding.

The main skill is not calculating values by hand.

The main skill is recognizing what representation a value is using and what it usually means in context.

---

## Lab Environment

Host system:

* Arch Linux

Primary workflow:

* zsh
* tmux
* neovim
* CLI-first tooling

Typical tools:

* Python 3 REPL
* C compiler
* `printf`
* `xxd`
* `hexdump`
* `od`
* `file`
* `readelf`
* `stat`
* `chmod`
* `ip`
* `tcpdump`
* `gdb` when useful

Experiments should remain:

* local
* reproducible
* observable
* reversible
* directly connected to systems understanding

---

## Typical Phase Structure

This roadmap intentionally contains one short phase.

```text
Representation Basics

↓

Bytes and Text

↓

Integers and Bit Patterns

↓

System-Level Interpretation

↓

Integrated Recognition Review
```

The purpose is to build a foundation, not a specialization.

After completion, number representations should be absorbed into the larger Labs curriculum rather than treated as a separate long-term subject.

---

## Phase 01 — Practical Number Representations

### Goal

Become comfortable reading and interpreting the number systems that appear in real systems work.

This phase builds the minimum durable foundation needed for C, Linux internals, networking, cryptography, embedded systems, reverse engineering, exploit development, and security tooling.

---

### Outcomes

After completing this phase, you should be able to:

* identify binary, decimal, octal, hexadecimal, ASCII, and basic Unicode representations
* explain why hexadecimal maps naturally to bytes and memory
* distinguish character data from byte values
* interpret common Unix permission values such as `0755` and `0644`
* explain signed and unsigned integer interpretation
* recognize two's complement patterns such as `0xff`, `0xffffffff`, and `0x7fffffff`
* reason about bitwise operations, flags, and masks
* identify common hexadecimal patterns in binaries, dumps, memory, and protocols
* explain endianness at the byte-order level
* inspect byte-level data using CLI tools
* connect numeric representations to real systems artifacts

---

### Typical Tools

* Python 3
* C compiler
* `printf`
* `xxd`
* `hexdump`
* `od`
* `file`
* `readelf`
* `stat`
* `chmod`
* `ip`
* `tcpdump`

---

### Example Labs

* compare decimal, binary, octal, and hexadecimal representations of the same value
* inspect ASCII text as bytes with `xxd`
* observe Unix file permissions as octal values
* compile a small C program and inspect integer sizes and overflow behavior
* inspect ELF magic bytes with `xxd` and `readelf`
* compare little-endian and big-endian byte order in memory
* interpret simple bit masks and flags
* recognize byte patterns in a small hex dump

---

### Session 01 — Binary, Hexadecimal, and Byte Recognition

Focus:

* binary as bit patterns
* hexadecimal as compact byte notation
* decimal as human-facing quantity
* why systems programmers read hex often
* recognizing nibbles, bytes, and common byte values

Core examples:

```text
0b11111111 = 0xff = one full byte
0x00       = all bits off
0xff       = all bits on
0x10       = 16 decimal
0x100      = 256 decimal
```

Where this appears:

* memory dumps
* packet fields
* register values
* binary files
* cryptographic bytes
* C integer output
* firmware images

Recognition targets:

* `0xff`
* `0x00`
* `0x10`
* `0x100`
* `0b10101010`
* `0b11110000`

---

### Session 02 — Octal, Permissions, ASCII, and Text as Bytes

Focus:

* octal as a compact permission representation
* Unix permissions as bit fields
* ASCII characters as byte values
* basic Unicode distinction
* text as encoded bytes, not magic symbols

Core examples:

```text
0755

↓

owner: read/write/execute
group: read/execute
other: read/execute
```

```text
'A' = 0x41
'a' = 0x61
'0' = 0x30
```

Where this appears:

* `chmod 755`
* `stat`
* shell scripts
* C character literals
* HTTP text
* protocol payloads
* hex dumps
* strings inside binaries

Recognition targets:

* `0755`
* `0644`
* `0x41`
* `0x20`
* `0x0a`
* `0x7f`

---

### Session 03 — Signed, Unsigned, Two's Complement, and Integer Limits

Focus:

* the same bits can have different meanings
* signed vs unsigned interpretation
* two's complement intuition
* integer boundaries
* overflow as representation behavior

Core examples:

```text
0xff

as unsigned 8-bit:

255

as signed 8-bit:

-1
```

```text
0x7fffffff

maximum signed 32-bit integer
```

```text
0xffffffff

unsigned 32-bit: 4294967295
signed 32-bit: -1
```

Where this appears:

* C integer types
* system calls
* return values
* binary protocols
* exploit development
* reverse engineering
* embedded registers
* file formats

Recognition targets:

* `0x7fffffff`
* `0x80000000`
* `0xffffffff`
* `0xff`
* `-1`
* `size_t`
* `int32_t`
* `uint32_t`

---

### Session 04 — Bitwise Operations, Masks, Flags, and Endianness

Focus:

* bits as switches
* masks as selective filters
* flags as stored yes/no states
* OR for enabling bits
* AND for testing bits
* XOR for difference or reversible transformation
* shifts as position changes
* endianness as byte order

Core examples:

```text
0b00000100

↓

one specific bit is set
```

```text
value & 0xff

↓

keep only the lowest byte
```

```text
little-endian memory:

0x12345678

stored as:

78 56 34 12
```

Where this appears:

* C bit flags
* Linux file mode bits
* network packet fields
* CPU registers
* embedded hardware registers
* cryptography
* protocol parsing
* reverse engineering
* memory inspection

Recognition targets:

* `&`
* `|`
* `^`
* `<<`
* `>>`
* `0xff`
* `0xffff`
* `0x80000000`
* little-endian byte order
* big-endian byte order

---

### Session 05 — Hex Dumps, Magic Values, Addresses, and Systems Recognition Review

Focus:

* reading hex dumps as structured evidence
* recognizing file signatures
* identifying memory-looking values
* distinguishing addresses from ordinary integers
* common hexadecimal patterns
* integrating previous sessions into real systems examples

Core examples:

```text
7f 45 4c 46

↓

ELF file header
```

```text
0x7F454C46

↓

same bytes interpreted as a hexadecimal value
```

```text
0xdeadbeef

↓

recognizable debug or sentinel pattern
```

```text
0x00000000

↓

null, zero, empty value, or cleared memory depending on context
```

Where this appears:

* ELF binaries
* firmware images
* memory maps
* GDB output
* packet captures
* reverse engineering
* exploit development
* crash analysis
* embedded debugging

Recognition targets:

* `0x7F454C46`
* `0xdeadbeef`
* `0xcafebabe`
* `0x00000000`
* `0x41414141`
* `0x7fffffff`
* `0x55`
* `0xaa`
* hex dump offsets
* memory addresses

Mini review task:

Given a mixed list of values, classify each one by likely representation and likely system context.

Example:

```text
0755
0xff
0x7F454C46
0b11001010
0x7fffffff
0xdeadbeef
0x41414141
0x0a
```

For each value, answer:

```text
What representation is this?

What does it likely mean?

Where might it appear in real systems?

What mistake could someone make when interpreting it?
```

---

## Final Outcome

After completing this roadmap, you should be able to read common numeric representations without stopping the main learning flow.

You should be able to:

* recognize binary, octal, decimal, and hexadecimal values in context
* understand why hexadecimal is common in systems programming
* read basic byte values in hex dumps
* interpret Unix permission values
* distinguish ASCII characters from their byte representation
* understand basic Unicode as a text encoding issue
* reason about signed and unsigned integer interpretation
* explain two's complement at a practical level
* recognize integer limit patterns
* use bitwise operations to understand flags and masks
* explain endianness as byte order
* identify common magic values and debug patterns
* connect numeric representations to memory, files, protocols, registers, and binaries

This roadmap should make future topics easier, especially:

* C Programming
* Linux Internals
* ELF Analysis
* Networking
* Cryptography
* Embedded Systems
* Reverse Engineering
* Exploit Development
* Firmware Analysis

---

## Core Mental Model

```text
Raw Bits
   │
   ▼
Grouped Bytes
   │
   ▼
Representation
Binary / Octal / Decimal / Hex / Text
   │
   ▼
Interpretation Context
Integer / Character / Address / Permission / Flag / Field
   │
   ▼
System Meaning
Memory / File / Protocol / Register / Binary / Permission
```

The same bits do not have one universal meaning.

Meaning comes from representation plus context.

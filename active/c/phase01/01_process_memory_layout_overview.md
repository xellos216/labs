# Process Memory Layout Overview

## Metadata

```yaml
Roadmap: C Programming
Phase: 01
Session: 01
Title: Process Memory Layout Overview
Status:
Review:
ArchiveVersion: 2
Date:
```

## Session Goal

Understand that a running C program is not just source code.

It becomes a process occupying multiple regions of memory.

By the end of this session, you should be able to explain:

* What a process is
* Why processes need memory
* What a process memory layout is
* The major memory regions of a running program
* Why understanding memory matters for Linux, Embedded Linux, and Firmware Analysis

---

# From Source Code to Process

Consider:

```c
#include <stdio.h>

int main(void)
{
    printf("Hello\n");
    return 0;
}
```

At rest:

```text
hello.c
```

After compilation:

```text
hello
```

After execution:

```text
running process
```

Question:

```text
Where does this process live?
```

Answer:

```text
Memory
```

---

# Mental Model

Think:

```text
Source Code
        ↓
Compiler
        ↓
Executable
        ↓
Loader
        ↓
Process
        ↓
Memory Layout
```

A running program becomes a memory structure managed by Linux.

---

# Core Idea

A process does not receive one giant block of memory.

Instead, Linux organizes memory into regions.

Typical layout:

```text
High Addresses

+------------------+
|      Stack       |
+------------------+

|                  |
|      Free        |
|     Space        |
|                  |

+------------------+
|       Heap       |
+------------------+

+------------------+
|      BSS         |
+------------------+

+------------------+
|      Data        |
+------------------+

+------------------+
|      Code        |
+------------------+

Low Addresses
```

---

# Code Segment

Contains:

```text
Compiled instructions
```

Example:

```c
printf("Hello");
```

After compilation:

```text
Machine instructions
```

These instructions live in:

```text
Code Segment
```

Also called:

```text
.text
```

---

# Data Segment

Contains:

```c
int count = 10;
```

Initialized global variables.

Example:

```c
int users = 100;
```

Value already exists before execution begins.

---

# BSS Segment

Contains:

```c
int count;
```

or

```c
static int count;
```

Uninitialized global or static variables.

Linux automatically initializes them to:

```text
0
```

---

# Heap

Used for:

```c
malloc()
calloc()
realloc()
```

Memory requested during runtime.

Example:

```c
char *buffer = malloc(1024);
```

The buffer lives in:

```text
Heap
```

---

# Stack

Used for:

```text
Function calls
Local variables
Function arguments
Return information
```

Example:

```c
void hello(void)
{
    int x = 10;
}
```

Variable:

```text
x
```

typically lives on the stack.

---

# Embedded Systems Connection

Many embedded vulnerabilities involve:

```text
Stack
Heap
```

Many firmware analyses involve:

```text
Memory regions
Executable layout
```

Many Linux internals concepts involve:

```text
Process memory
Virtual memory
Memory mapping
```

Understanding process memory is the foundation for:

```text
GDB
ELF
Assembly
Linux Internals
Firmware Analysis
Embedded Security
```

---

# Observation Habit

When looking at C code, begin asking:

```text
Where does this variable live?

Code?
Data?
BSS?
Heap?
Stack?
```

This question becomes increasingly important throughout the roadmap.

---

# Key Mental Model

```text
Process
=
Organized Memory Regions

Code
Data
BSS
Heap
Stack
```

A running program is not just executing instructions.

It is a structured memory layout managed by Linux.

---
# Review Questions

### Q1. What is a process?

<details>
<summary>A</summary>

A process is a running instance of a program managed by the Linux kernel

</details>

---

### Q2. What transforms source code into a running process?

<details>
<summary>A</summary>

The complier creates an executable, and the Linux loader creates a running process from it

</details>

---

### Q3. Why does a running process need memory?

<details>
<summary>A</summary>

A running process needs memory to store instructions, variables, function information, and runtime data

</details>

---

### Q4. What is a process memory layout?

<details>
<summary>A</summary>

Process memory layout is the organized arrangement of memory regions used by a running process

</details>

---

### Q5. Name the five major memory regions introduced in this session.

<details>
<summary>A</summary>

Heap, Stack, BSS, Data, Code

</details>

---

### Q6. What kind of information is stored in the code segment?

<details>
<summary>A</summary>

Compiled instructions

</details>

---

### Q7. What kind of variables typically live in the data segment?

<details>
<summary>A</summary>

Initialized global or static variables

</details>

---

### Q8. What kind of variables typically live in the BSS segment?

<details>
<summary>A</summary>

uninitialized global or static variables

</details>

---

### Q9. What is the purpose of the heap?

<details>
<summary>A</summary>

The heap stores memory dynamically allocated during runtime

</details>

---

### Q10. What is the purpose of the stack?

<details>
<summary>A</summary>

function call, local variables, function arguments, return information

</details>

---

### Q11. Where would memory allocated by malloc() typically live?

<details>
<summary>A</summary>

Heap

</details>

---

### Q12. Why is understanding process memory important for embedded systems?

<details>
<summary>A</summary>

Because embedded systems, firmware analysis, and many vulnerabilities involve understanding how memory is organized and used.

</details>

---

### Q13. When reading C code, what question should you begin asking about variables?

<details>
<summary>A</summary>

Where does this variable live?

</details>

---

### Q14. Complete the mental model:

```text
Process Memory Layout
=
________________
```

<details>
<summary>A</summary>

Organized Memory Regions

</details>

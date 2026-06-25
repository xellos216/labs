# Code Segment Observation

## Session Goal

Observe what actually exists inside the Code Segment of a running process.

By the end of this session, you should be able to explain:

* What the Code Segment contains
* Why machine instructions live in the Code Segment
* How Linux maps executable code into memory
* Why instructions and variables are stored separately
* How the Code Segment appears inside `/proc/<PID>/maps`

---

# Review

Previous session:

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

We also observed:

```bash
cat /proc/<PID>/maps
```

and saw:

```text
[heap]

[stack]

/path/to/executable
```

inside the process memory map.

---

# Core Question

Consider:

```c
#include <stdio.h>

int main(void)
{
    printf("Hello\n");
    return 0;
}
```

Question:

```text
Where does the actual program logic live?
```

Examples:

```text
printf()

return

function calls

machine instructions
```

Linux must place executable instructions somewhere.

That location is:

```text
Code Segment
```

---

# Mental Model

Think:

```text
Source Code
        ↓
Compiler
        ↓
Machine Instructions
        ↓
Code Segment
        ↓
CPU Executes
```

The CPU never executes C source code.

The CPU executes machine instructions stored in memory.

---

# Important Distinction

Variables:

```c
int x = 10;
```

are data.

Instructions:

```c
x++;
```

are actions.

Think:

```text
Data
=
Information

Code
=
Instructions
```

Linux stores them in different memory regions.

---

# Observation Exercise

Create:

```c
#include <stdio.h>
#include <unistd.h>

int main(void)
{
    printf("PID: %d\n", getpid());

    getchar();

    return 0;
}
```

Compile:

```bash
gcc -o code_demo code_demo.c
```

Run:

```bash
./code_demo
```

Keep it running.

---

# Prediction

Before continuing, predict:

```text
Which memory region contains:

printf()

main()

return
```

Why?

---

# Observation 1

Find the process:

```bash
cat /proc/<PID>/maps
```

Look for entries similar to:

```text
55ab12345000-55ab12346000 r-xp ...
```

Question:

```text
What might the x mean?
```

Hint:

```text
r = read
w = write
x = execute
```

---

# Observation 2

Inspect the executable:

```bash
readelf -S code_demo
```

Question:

```text
Can you find:

.text
```

section?

---

# Observation 3

Disassemble the program:

```bash
objdump -d code_demo
```

Observe:

```text
main:
```

and the instructions below it.

Example:

```text
push
mov
call
leave
ret
```

Question:

```text
Where are these instructions stored while the program is running?
```

---

# Key Observation

The Code Segment contains:

```text
Machine Instructions
```

Not:

```text
Variables
```

Not:

```text
Heap Data
```

Not:

```text
Function Arguments
```

The CPU fetches instructions from the Code Segment and executes them.

---

# Embedded Systems Connection

Firmware imagess contain:

```text
Code
Data
Configuration
Filesystems
```

Understanding which bytes represent:

```text
Instructions
```

versus

```text
Data
```

is fundamental for:

```text
ELF Analysis
Firmware Analysis
Assembly
Reverse Engineering
Embedded Security
```

---

# Observation Habit

When looking at a binary, ask:

```text
Which bytes are:

Instructions?

Which bytes are:

Data?
```

This distinction becomes critical later.

---

# Key Mental Model

```text
Code Segment
=
Executable Machine Instructions

CPU
↓
Fetch
↓
Decode
↓
Execute
```

The CPU executes instructions from the Code Segment.

---

# QA

**Q1.**

What is stored in the Code Segment?

<details>
<summary><strong>A1.</strong></summary>

</details>

---

**Q2.**

Does the CPU execute C source code directly?

<details>
<summary><strong>A2.</strong></summary>

</details>

---

**Q3.**

What transforms C source code into machine instructions?

<details>
<summary><strong>A3.</strong></summary>

</details>

---

**Q4.**

Why are variables not stored in the Code Segment?

<details>
<summary><strong>A4.</strong></summary>

</details>

---

**Q5.**

Complete:

```text
Data
=
__________

Code
=
__________
```

<details>
<summary><strong>A5.</strong></summary>

</details>

---

**Q6.**

What permission typically identifies executable memory in `/proc/<PID>/maps`?

<details>
<summary><strong>A6.</strong></summary>

</details>

---

**Q7.**

What does the `x` permission mean in a memory mapping?

<details>
<summary><strong>A7.</strong></summary>

</details>

---

**Q8.**

Which tool can display ELF sections?

<details>
<summary><strong>A8.</strong></summary>

</details>

---

**Q9.**

Which ELF section commonly contains executable code?

<details>
<summary><strong>A9.</strong></summary>

</details>

---

**Q10.**

Which tool can disassemble a binary into assembly instructions?

<details>
<summary><strong>A10.</strong></summary>

</details>

---

**Q11.**

Name three assembly instructions you observed during this session.

<details>
<summary><strong>A11.</strong></summary>

</details>

---

**Q12.**

Where do machine instructions live while a program is running?

<details>
<summary><strong>A12.</strong></summary>

</details>

---

**Q13.**

Why is distinguishing code from data important in firmware analysis?

<details>
<summary><strong>A13.</strong></summary>

</details>

---

**Q14.**

Complete the mental model:

```text
Code Segment
=
________________
```

<details>
<summary><strong>A14.</strong></summary>

</details>

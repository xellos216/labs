# BSS Segment Observation

## Metadata

```yaml
Roadmap: C Programming
Phase: 01
Session: 04
Title: BSS Segment Observation
Status:
Review:
ArchiveVersion: 2
Date:
```

## Session Goal

Observe how uninitialized global variables are stored and why the BSS segment exists.

By the end of this session, you should be able to explain:

- What the BSS segment contains
- Why `.bss` exists separately from `.data`
- The difference between `PROGBITS` and `NOBITS`
- Why BSS reduces executable size
- How uninitialized global variables appear during program execution

---

# Review

Previous sessions established:

```text
.text
↓
Code Segment
↓
r-xp
↓
Machine Instructions
```

and

```text
.data
↓
Data Segment
↓
rw-p
↓
Initialized Global Variables
```

---

# Core Question

Consider:

```c
int global_b;
```

Question:

```text
Where is this variable stored?

Code
Data
BSS
Heap
Stack
```

---

# Prediction

Consider:

```c
int global_a = 10;
int global_b;
```

Questions:

```text
What value should global_b have before main() changes it?

Why?
```

---

# Observation 1

Create:

```c
#include <stdio.h>

int global_a = 10;
int global_b;

int main(void)
{
    printf("%d %d\n", global_a, global_b);
}
```

Observe:

```text
global_b
```

Question:

```text
Why is the value already zero?
```

---

# Observation 2

Inspect ELF sections:

```bash
readelf -S test | grep -E '\.data|\.bss'
```

Example:

```text
.data   PROGBITS
.bss    NOBITS
```

Question:

```text
Why does .data use PROGBITS while .bss uses NOBITS?
```

---

# Observation 3

Create:

```c
#include <stdio.h>

char big_data[10000000] = {1};
char big_bss[10000000];

int main(void)
{
    getchar();
}
```

Compile:

```bash
gcc test.c -o test
```

Observe file size:

```bash
ls -lh test
```

Question:

```text
Why is the executable around 10 MB?
```

---

# Observation 4

Remove the initialized array:

```c
#include <stdio.h>

char big_bss[10000000];

int main(void)
{
    getchar();
}
```

Compile again:

```bash
gcc test.c -o test
```

Observe:

```bash
ls -lh test
```

Question:

```text
Why did the executable become much smaller?
```

---

# Observation 5

Observe the running program:

```c
#include <stdio.h>
#include <unistd.h>

char big_bss[10000000];

int main(void)
{
    printf("PID: %d\n", getpid());
    printf("big_bss address: %p\n", (void *)big_bss);
    printf("big_bss[0]: %d\n", big_bss[0]);

    getchar();

    return 0;
}
```

Inspect memory:

```bash
cat /proc/<PID>/maps | grep '/test'
```

Question:

```text
Which mapping contains big_bss?
```

---

# Why BSS Exists

Suppose we declare:

```c
char buffer[10000000];
```

If every zero byte were stored inside the executable,

```text
Executable Size
≈
10 MB
```

Instead, ELF stores only:

```text
Reserve 10 MB

Initialize with zeros at runtime
```

This keeps executables much smaller.

---

# .data vs .bss

Initialized global variable:

```c
int global_a = 10;
```

```text
↓

.data

↓

PROGBITS

↓

Actual bytes stored inside ELF
```

---

Uninitialized global variable:

```c
int global_b;
```

```text
↓

.bss

↓

NOBITS

↓

Only size information stored inside ELF

↓

Zero-initialized when the program starts
```

---

# Embedded Systems Connection

Firmware often contains many global variables representing:

```text
Device State
Buffers
Flags
Configuration
Runtime Objects
```

Large zero-initialized objects are typically placed in:

```text
.bss
```

to reduce firmware image size.

Understanding BSS helps explain:

- Embedded firmware layouts
- Boot-time memory initialization
- RAM usage
- ELF analysis

---

# Observation Habit

When reading C code, ask:

```text
Is this variable initialized?

Yes
↓

.data

No
↓

.bss
```

---

# Key Mental Model

```text
Initialized Global Variable
        │
        ▼
.data
(PROGBITS)
        │
        ▼
Actual bytes stored in ELF
```

```text
Uninitialized Global Variable
        │
        ▼
.bss
(NOBITS)
        │
        ▼
Only size information stored
        │
        ▼
Zero-filled when the process starts
```

# Review Questions

### Q1. What kind of variables are typically stored in the BSS segment?

<details>
<summary>A</summary>

</details>

---

### Q2. Why is `int global_b;` stored in `.bss` instead of `.data`?

<details>
<summary>A</summary>

</details>

---

### Q3. What does `NOBITS` mean?

<details>
<summary>A</summary>

</details>

---

### Q4. Why does `.bss` reduce executable size?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does `char big_data[10000000] = {1};` make the executable much larger?

<details>
<summary>A</summary>

</details>

---

### Q6. Why does `char big_bss[10000000];` not significantly increase executable size?

<details>
<summary>A</summary>

</details>

---

### Q7. What value does an uninitialized global variable have when the program starts?

<details>
<summary>A</summary>

</details>

---

### Q8. Complete:

```text
Uninitialized Global Variable
↓
__________
↓
NOBITS
```

<details>
<summary>A</summary>

</details>

---

### Q9. Complete:

```text
.bss
↓
Only __________ information is stored in the ELF file.
```

<details>
<summary>A</summary>

</details>

---

### Q10. What initializes the BSS region before `main()` begins?

<details>
<summary>A</summary>

</details>

---

### Q11. Which tool shows that `.bss` is marked as `NOBITS`?

<details>
<summary>A</summary>

</details>

---

### Q12. Explain the difference between `.data` and `.bss` in one or two sentences.

<details>
<summary>A</summary>

</details>

# Phase 01 - Session 06

## Metadata

```yaml
Roadmap: C Programming / Embedded Linux, Firmware Analysis & IoT Systems
Phase: 01
Session: 06
Title: Stack Growth Observation
Status: Completed
Review: Pending
Date: 2026-06-30
```

---

# Objective

Observe how stack addresses change as function calls become deeper.

This session focuses on stack growth direction, stack frame size, stack frame return behavior, and the relationship between nested function calls and local variable addresses.

---

# Learning Summary

A C program begins execution from `main()`, but the full execution path follows the chain of function calls.

In this session, nested calls were observed:

```text
main()
↓
func1()
↓
func2()
↓
func3()
```

The observed local variable addresses decreased as the calls became deeper. This supports the model that, on this Linux x86-64 environment, the stack grows toward lower addresses.

However, the address difference between stack frames is not always fixed. When one function contained a larger local array, the address gap around that function became larger. This showed that stack frame size depends on the function structure, local variables, alignment, compiler behavior, and ABI rules.

A final experiment showed that after a nested function returns, execution resumes in the caller's stack frame. Local variables observed after the nested call appeared near other variables from the same caller frame, not near the returned callee frame.

---

# Key Concepts

- Stack growth
- Stack frame
- Nested function call
- Caller
- Callee
- Return to caller frame
- Local variable address
- Frame size
- Alignment
- Function execution flow

---

# Practical Observations

## Observation 1: Nested Calls Move Toward Lower Addresses

### Prediction

As function calls become deeper, local variable addresses should become lower because the stack usually grows downward on Linux x86-64.

### Code

```c
#include <stdio.h>

void func3(void)
{
    int c = 300;
    printf("func3 &c = %p\n", (void *)&c);
}

void func2(void)
{
    int b = 200;
    printf("func2 &b = %p\n", (void *)&b);

    func3();
}

void func1(void)
{
    int a = 100;
    printf("func1 &a = %p\n", (void *)&a);

    func2();
}

int main(void)
{
    int m = 0;
    printf("main  &m = %p\n", (void *)&m);

    func1();

    return 0;
}
```

### Observation

Observed output:

```text
main  &m = 0x7ffc950671a4
func1 &a = 0x7ffc95067184
func2 &b = 0x7ffc95067164
func3 &c = 0x7ffc95067144
```

Address differences:

```text
main  → func1 : 0x20 = 32 bytes
func1 → func2 : 0x20 = 32 bytes
func2 → func3 : 0x20 = 32 bytes
```

### Explanation

The actual execution order was determined by function calls, not by the order in which functions were written in the source file.

```text
main()
↓
func1()
↓
func2()
↓
func3()
```

As each function was called, a new stack frame was created at a lower address.

```text
High Address

main frame
  m = 0x...71a4

func1 frame
  a = 0x...7184

func2 frame
  b = 0x...7164

func3 frame
  c = 0x...7144

Low Address
```

This supports the model that the stack grows toward lower addresses in this environment.

---

## Observation 2: Stack Frame Size Can Change

### Prediction

Adding a larger local variable to `func2()` should increase the size of the stack frame around `func2()`.

### Code

```c
#include <stdio.h>

void func3(void)
{
    int c = 300;
    printf("func3 &c = %p\n", (void *)&c);
}

void func2(void)
{
    char buffer[100];
    int b = 200;

    printf("func2 buffer = %p\n", (void *)buffer);
    printf("func2 &b     = %p\n", (void *)&b);

    func3();
}

void func1(void)
{
    int a = 100;
    printf("func1 &a = %p\n", (void *)&a);

    func2();
}

int main(void)
{
    int m = 0;
    printf("main &m = %p\n", (void *)&m);

    func1();

    return 0;
}
```

### Observation

Observed output:

```text
main &m        = 0x7ffcdcf157b4
func1 &a       = 0x7ffcdcf15794
func2 buffer   = 0x7ffcdcf15710
func2 &b       = 0x7ffcdcf1570c
func3 &c       = 0x7ffcdcf156e4
```

Address differences:

```text
main  → func1       : 0x20 = 32 bytes
func1 → func2 buffer: 0x84 = 132 bytes
buffer → b          : 0x04 = 4 bytes
b → func3           : 0x28 = 40 bytes
```

### Explanation

The `main → func1` gap remained 32 bytes because `func1()` stayed structurally similar to the first experiment.

The `func1 → func2` gap became larger because `func2()` now contained:

```c
char buffer[100];
```

This required more stack space.

This observation corrected an overgeneralization:

```text
Incorrect:
Stack always moves down by 32 bytes per function call.

Correct:
Stack grows toward lower addresses, but each frame size can vary.
```

Stack frame size can be affected by:

- local variable size
- arrays
- alignment
- padding
- saved registers
- compiler behavior
- ABI rules

---

## Observation 3: Returning from a Callee Restores the Caller Frame

### Prediction

After `func3()` returns, execution should resume inside `func2()`'s stack frame. Therefore, a local variable observed after the call to `func3()` should appear near `func2()`'s other local variables.

### Code

```c
#include <stdio.h>

void func3(void)
{
    int c = 300;
    printf("func3 &c = %p\n", (void *)&c);
}

void func2(void)
{
    int b = 200;
    printf("func2 &b = %p\n", (void *)&b);

    func3();

    int after = 222;
    printf("func2 after &after = %p\n", (void *)&after);
}

void func1(void)
{
    int a = 100;
    printf("func1 &a = %p\n", (void *)&a);

    func2();

    int after = 111;
    printf("func1 after &after = %p\n", (void *)&after);
}

int main(void)
{
    int m = 0;
    printf("main &m = %p\n", (void *)&m);

    func1();

    int after = 999;
    printf("main after &after = %p\n", (void *)&after);

    return 0;
}
```

### Observation

Observed output:

```text
main &m                = 0x7fff64a2b0e0
func1 &a               = 0x7fff64a2b0c0
func2 &b               = 0x7fff64a2b0a0
func3 &c               = 0x7fff64a2b084
func2 after &after     = 0x7fff64a2b0a4
func1 after &after     = 0x7fff64a2b0c4
main after &after      = 0x7fff64a2b0e4
```

### Explanation

During the nested call:

```text
main()
↓
func1()
↓
func2()
↓
func3()
```

the stack moved toward lower addresses.

When `func3()` returned, its stack frame was no longer active. Execution resumed inside `func2()`.

Therefore:

```text
func2 &b            = 0x...b0a0
func2 after &after  = 0x...b0a4
```

appeared near each other because both belong to the `func2()` frame.

Similarly:

```text
func1 &a            = 0x...b0c0
func1 after &after  = 0x...b0c4
```

belong to the `func1()` frame.

And:

```text
main &m             = 0x...b0e0
main after &after   = 0x...b0e4
```

belong to the `main()` frame.

The key conclusion:

```text
When a called function returns,
execution goes back to the caller's stack frame.
```

---

# Commands / Code

Compile without optimization:

```bash
gcc -O0 test.c -o test
```

Compile with debug information for future GDB inspection:

```bash
gcc -O0 -g test.c -o test
```

Run the program:

```bash
./test
```

---

# Connections

## Previous Sessions

```text
Session 05
Stack Fundamentals
↓
Local variables exist in stack frames
↓
Function return ends local variable lifetime
↓
Stack space can be reused
```

## Current Session

```text
Nested function calls
↓
New stack frames
↓
Lower addresses
↓
Stack growth observation
```

## Future Sessions

```text
Session 07
Function Call Frames
↓
Caller / callee relationship
↓
Return address
↓
Saved frame pointer
↓
GDB frame inspection
```

This session prepares for understanding function call frames, return addresses, frame pointers, and later stack-based memory corruption concepts.

---

# Common Misconceptions

## Misconception 1

```text
The order of function definitions determines execution order.
```

Correction:

```text
Execution order is determined by the call chain starting from main().
```

Example:

```text
main()
↓
func1()
↓
func2()
↓
func3()
```

even if the functions are written in another order in the source file.

---

## Misconception 2

```text
Stack always moves down by exactly 32 bytes per function call.
```

Correction:

```text
The stack may grow toward lower addresses, but the frame size is not fixed.

Frame size depends on function structure, local variables, alignment, compiler behavior, and ABI rules.
```

---

## Misconception 3

```text
A new stack frame is created for every local variable declaration.
```

Correction:

```text
A stack frame is created for a function call.

Local variables are placed inside that function's stack frame.
```

---

## Misconception 4

```text
After a nested function returns, new local variables are placed near the returned function's frame.
```

Correction:

```text
After a callee returns, execution resumes in the caller's frame.

Local variables observed afterward belong to the caller's frame.
```

---

# Key Takeaways

- Function execution begins from `main()`.
- Function definition order does not determine execution order.
- The call chain determines which functions execute.
- Each function call creates a stack frame.
- In this environment, deeper function calls appeared at lower addresses.
- Stack frame size is not fixed.
- Larger local variables can increase stack frame size.
- Local variables are placed inside their own function's stack frame.
- When a callee returns, execution resumes in the caller's frame.
- Address observations provide evidence for stack growth and frame return behavior.

---

# Review Questions

### Q1. What determines the actual execution order of functions in a C program?

<details>
<summary>A</summary>

</details>

---

### Q2. In the nested call experiment, what evidence showed that the stack grew toward lower addresses?

<details>
<summary>A</summary>

</details>

---

### Q3. Why is it incorrect to conclude that stack frames always differ by 32 bytes?

<details>
<summary>A</summary>

</details>

---

### Q4. What factors can affect stack frame size?

<details>
<summary>A</summary>

</details>

---

### Q5. What is the difference between a caller and a callee?

<details>
<summary>A</summary>

</details>

---

### Q6. After `func3()` returns to `func2()`, why does `func2 after` appear near `func2 &b` instead of near `func3 &c`?

<details>
<summary>A</summary>

</details>

---

### Q7. Why is it incorrect to say that a new stack frame is created for every local variable declaration?

<details>
<summary>A</summary>

</details>

---

### Q8. Complete the model:

```text
Function call
↓
__________ created
↓
Local variables placed inside it
↓
Function return
↓
Return to caller frame
```

<details>
<summary>A</summary>

</details>

---

### Q9. How does this session prepare for studying function call frames in GDB?

<details>
<summary>A</summary>

</details>

---

# Next Session

```yaml
Phase: 01
Session: 07
Title: Function Call Frames
```

Next topic:

```text
Observe function call frames more explicitly, including caller/callee relationships and how GDB displays stack frames.
```

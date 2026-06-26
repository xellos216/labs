# Phase 01 - Session 05

## Metadata

```yaml
Roadmap: C Programming / Embedded Linux, Firmware Analysis & IoT Systems
Phase: 01
Session: 05
Title: Stack Fundamentals
Status: Completed
Review: Pending
Date: 2026-06-27
```

---

# Objective

Understand how local variables exist on the stack, how stack frames are created during function calls, and why using the address of a local variable after its function has returned is unsafe.

This session connects local variable lifetime, stack frame reuse, and dangling pointer behavior.

---

# Learning Summary

A local variable declared inside a function is created inside that function's stack frame.

When a function is called, a new stack frame is created. On common Linux x86-64 systems, stack frames usually appear at lower addresses as calls go deeper. When the function returns, its stack frame is no longer valid.

The memory is not necessarily erased. Instead, the stack space may be reused by a later function call. This means a pointer may still contain the old address, but that address no longer safely represents the original local variable.

A key observation from this session was that two different local variables from two different functions used the exact same stack address when the functions were called sequentially. This demonstrated stack frame reuse directly.

---

# Key Concepts

- Stack
- Stack frame
- Local variable
- Function call
- Function return
- Variable lifetime
- Stack reuse
- Dangling pointer
- Undefined behavior
- Address reuse

---

# Practical Observations

## Observation 1: Local Variables Are Stored on the Stack

### Prediction

A local variable declared inside a function should exist on the stack, not in Data or BSS.

Initial misconception corrected:

```text
Incorrect:
A variable with an initial value belongs to Data.

Correct:
A local variable belongs to the Stack, even if it has an initial value.
```

The Data/BSS distinction applies to global or static storage variables, not ordinary local variables.

### Code

```c
#include <stdio.h>

void func(void)
{
    int x = 100;
    printf("&x = %p\n", (void *)&x);
}

int main(void)
{
    int y = 200;

    printf("&y = %p\n", (void *)&y);

    func();

    return 0;
}
```

### Observation

Example output:

```text
&y = 0x7ffde3cdab94
&x = 0x7ffde3cdab74
```

### Explanation

`y` is a local variable in `main()`.

`x` is a local variable in `func()`.

Both variables are stored on the stack, but they belong to different stack frames.

The address of `x` was lower than the address of `y`, matching the common model that the stack grows toward lower addresses on Linux x86-64.

```text
High Address

main stack frame
└── y

func stack frame
└── x

Low Address
```

---

## Observation 2: Sequential Function Calls Can Reuse the Same Stack Address

### Prediction

If `func1()` returns before `func2()` is called, the stack space used by `func1()` may be reused by `func2()`.

### Code

```c
#include <stdio.h>

void func1(void)
{
    int x = 100;
    printf("func1 &x = %p\n", (void *)&x);
}

void func2(void)
{
    int z = 300;
    printf("func2 &z = %p\n", (void *)&z);
}

int main(void)
{
    func1();
    func2();

    return 0;
}
```

### Observation

Observed output:

```text
func1 &x = 0x7ffdfff18204
func2 &z = 0x7ffdfff18204
```

### Explanation

`x` and `z` are not the same variable.

They used the same address because the stack frame used by `func1()` was no longer active when `func2()` was called.

```text
func1()
↓
stack frame created
↓
x uses address 0x...
↓
func1() returns
↓
func1 stack frame is no longer valid

func2()
↓
new stack frame created
↓
z reuses address 0x...
```

This shows that stack memory is reused across function calls.

---

## Observation 3: Pointer to a Returned Local Variable Becomes Unsafe

### Prediction

If a function stores the address of its local variable in a global pointer, that pointer may still contain the address after the function returns.

However, the pointed-to object is no longer valid.

### Code

```c
#include <stdio.h>

int *p;

void func1(void)
{
    int x = 100;
    p = &x;

    printf("func1 &x = %p\n", (void *)&x);
    printf("func1 = %d\n", x);
}

void func2(void)
{
    int z = 300;

    printf("func2 &z = %p\n", (void *)&z);
    printf("func2 z = %d\n", z);
}

int main(void)
{
    func1();

    printf("main *p after func1 = %d\n", *p);

    func2();

    printf("main *p after func2 = %d\n", *p);

    return 0;
}
```

### Observation

Observed output:

```text
func1 &x = 0x7ffefb6fb4d4
func1 = 100
main *p after func1 = 100
func2 &z = 0x7ffefb6fb4d4
func2 z = 300
main *p after func2 = 300
```

### Explanation

The pointer `p` kept the address where `x` had existed.

After `func1()` returned, `x`'s lifetime ended. The address value still remained in `p`, but it no longer safely referred to a valid `x`.

When `func2()` was called, its local variable `z` reused the same stack address.

Therefore, `*p` appeared to change from `100` to `300`.

```text
p did not remember "x".

p only remembered an address.

That address was later reused by another stack frame.
```

This is an example of a dangling pointer.

---

# Commands / Code

Compile without optimization:

```bash
gcc -O0 test.c -o test
```

Use `-O0` to reduce compiler optimizations so stack behavior remains easier to observe.

Compile with debug information when preparing for GDB:

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
Code Segment
↓
Machine instructions
```

```text
Data Segment
↓
Initialized global/static variables
```

```text
BSS Segment
↓
Uninitialized global/static variables
```

```text
Stack
↓
Local variables and function call state
```

---

## Future Sessions

```text
Stack Fundamentals
↓
Stack Growth Observation
↓
Function Call Frames
↓
Function Arguments in Memory
↓
Pointer Tracing
↓
GDB Memory Inspection
```

This session prepares for observing stack growth, function frames, pointer lifetime, and memory inspection with GDB.

---

# Common Misconceptions

## Misconception 1

```text
A variable with an initial value belongs to Data.
```

Correction:

```text
Only initialized global/static variables usually belong to Data.

Ordinary local variables belong to Stack, even if they have initial values.
```

---

## Misconception 2

```text
If a pointer still has an address, the pointed-to value is still valid.
```

Correction:

```text
A pointer can keep an address even after the object at that address has ended its lifetime.

The address value may remain, but using it is unsafe.
```

---

## Misconception 3

```text
When a function returns, its stack memory is erased.
```

Correction:

```text
The stack frame becomes invalid, but the memory is not necessarily erased.

The same stack space may later be reused by another function call.
```

---

# Key Takeaways

- Local variables are stored in stack frames.
- Function calls create new stack frames.
- Function returns make the function's local variables invalid.
- Stack memory can be reused by later function calls.
- A pointer to a returned local variable is a dangling pointer.
- The pointer may still contain an address, but that address no longer safely represents the original object.
- Observed address reuse is evidence of stack frame reuse.

---

# Review Questions

### Q1. Where is an ordinary local variable usually stored?

<details>
<summary>A</summary>

</details>

---

### Q2. Why is `int x = 100;` inside a function stored on the Stack rather than in Data?

<details>
<summary>A</summary>

</details>

---

### Q3. What is a stack frame?

<details>
<summary>A</summary>

</details>

---

### Q4. What happens to a function's local variables when the function returns?

<details>
<summary>A</summary>

</details>

---

### Q5. Why can two different local variables from two different functions have the same address?

<details>
<summary>A</summary>

</details>

---

### Q6. What is a dangling pointer?

<details>
<summary>A</summary>

</details>

---

### Q7. Why is using a pointer to a returned local variable unsafe?

<details>
<summary>A</summary>

</details>

---

### Q8. In the observed experiment, why did `*p` change from `100` to `300`?

<details>
<summary>A</summary>

</details>

---

### Q9. Complete the model:

```text
Local Variable
↓
__________
↓
Function executes
↓
Function returns
↓
Variable lifetime ends
```

<details>
<summary>A</summary>

</details>

---

### Q10. How does this session prepare for studying stack overflows and function call frames later?

<details>
<summary>A</summary>

</details>

---

# Next Session

```yaml
Phase: 01
Session: 06
Title: Stack Growth Observation
```

Next topic:

```text
Observe how stack addresses change across nested function calls and build a clearer model of stack growth direction.
```

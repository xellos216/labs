# Phase 01 - Session 08

## Metadata

```yaml
Roadmap: C Programming / Embedded Linux, Firmware Analysis & IoT Systems
Phase: 01
Session: 08
Title: Function Arguments In Memory
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-07-05
```

---

# Objective

Understand how C function arguments are passed, where they can be observed during function execution, and why ordinary arguments and pointer arguments behave differently.

This session connects C-level argument passing with stack frames, register-based calling conventions, and pointer-based modification of caller-owned objects.

---

# Learning Summary

Previous sessions established that function calls create stack frames and that each frame contains local state and return information. This session extended that model to function arguments.

At the C language level, function arguments are passed by value. When `add(a, b)` is called, the values of `a` and `b` are copied into the callee's parameters `x` and `y`. The caller's variables and the callee's parameters are separate objects in separate stack frames.

This was observed by printing addresses:

```text
main &a      = 0x7ffd5593f160, a      = 10
main &b      = 0x7ffd5593f164, b      = 20
add  &x      = 0x7ffd5593f13c, x      = 10
add  &y      = 0x7ffd5593f138, y      = 20
add  &result = 0x7ffd5593f144, result = 30
```

The addresses showed that `a` and `x` were not the same variable, even though they held the same value. The deeper `add()` frame appeared at lower stack addresses than the caller's `main()` frame.

The session then used GDB disassembly to observe the lower-level mechanism. On x86-64 Linux, the first two `int` arguments were passed through `%edi` and `%esi`, and then stored into the callee's stack frame.

Finally, the session distinguished passing an integer value from passing an address value. `change(&a)` still passes by value, but the value being copied is the address of `a`. Because the callee receives a copy of the caller's address, dereferencing that pointer can modify the original object.

---

# Key Concepts

- Function arguments
- Function parameters
- Pass by value
- Stack frame
- Caller frame
- Callee frame
- Register argument passing
- `%edi`
- `%esi`
- `%rbp`-relative addressing
- Pointer argument
- Address value
- Dereference
- Object identity versus value equality

---

# Practical Observations

## Observation 1: Parameters Are Separate Objects in the Callee Frame

### Prediction

The initial prediction was that `x` and `y` might belong to the `main()` frame because the values originate from the call site.

This was corrected during the session.

### Code

```c
#include <stdio.h>

void add(int x, int y)
{
    int result = x + y;

    printf("add  &x      = %p, x      = %d\n", (void *)&x, x);
    printf("add  &y      = %p, y      = %d\n", (void *)&y, y);
    printf("add  &result = %p, result = %d\n", (void *)&result, result);
}

int main(void)
{
    int a = 10;
    int b = 20;

    printf("main &a      = %p, a      = %d\n", (void *)&a, a);
    printf("main &b      = %p, b      = %d\n", (void *)&b, b);

    add(a, b);

    return 0;
}
```

### Observation

```text
main &a      = 0x7ffd5593f160, a      = 10
main &b      = 0x7ffd5593f164, b      = 20
add  &x      = 0x7ffd5593f13c, x      = 10
add  &y      = 0x7ffd5593f138, y      = 20
add  &result = 0x7ffd5593f144, result = 30
```

### Explanation

`a` and `x` had equal values but different addresses. `b` and `y` also had equal values but different addresses.

This supports the model:

```text
main frame
  a = 10
  b = 20

add(a, b)
  ↓ values copied

add frame
  x = 10
  y = 20
  result = 30
```

The callee parameters are not the caller's variables. They are separate objects in the callee's execution context.

---

## Observation 2: Modifying Copied Parameters Does Not Modify Caller Variables

### Prediction

The corrected prediction was that changing `x` and `y` inside `add()` would not modify `a` and `b` in `main()`.

### Code

```c
#include <stdio.h>

void add(int x, int y)
{
    printf("add before: x = %d, y = %d\n", x, y);

    x = 999;
    y = 888;

    printf("add after : x = %d, y = %d\n", x, y);
}

int main(void)
{
    int a = 10;
    int b = 20;

    printf("main before: a = %d, b = %d\n", a, b);

    add(a, b);

    printf("main after : a = %d, b = %d\n", a, b);

    return 0;
}
```

### Observation

```text
main before: a = 10, b = 20
add before: x = 10, y = 20
add after : x = 999, y = 888
main after : a = 10, b = 20
```

### Explanation

Only the callee's local parameter objects changed.

```text
x = 999
```

changed `x` in the `add()` frame.

It did not change `a` in the `main()` frame.

This confirmed:

```text
a and x are not aliases.
b and y are not aliases.
```

---

## Observation 3: GDB Shows Register-Based Argument Passing

### Procedure

Compile without optimization and include debug information:

```bash
gcc -O0 -g test.c -o test
```

Start GDB:

```bash
gdb ./test
```

Disassemble `add`:

```gdb
disassemble add
```

### Observation

Relevant instructions from `add`:

```asm
0x0000000000001139 <+0>:  push %rbp
0x000000000000113a <+1>:  mov  %rsp,%rbp
0x000000000000113d <+4>:  sub  $0x10,%rsp
0x0000000000001141 <+8>:  mov  %edi,-0x4(%rbp)
0x0000000000001144 <+11>: mov  %esi,-0x8(%rbp)
```

### Explanation

On this x86-64 Linux environment, the first two `int` arguments were passed using registers:

```text
first int argument  → %edi
second int argument → %esi
```

Then `add()` stored those register values into its own stack frame:

```text
%edi → -0x4(%rbp)  // x
%esi → -0x8(%rbp)  // y
```

This connects the C-level model with the observed low-level behavior:

```text
C view:
a value → x
b value → y

Assembly view:
a value → %edi → add frame storage for x
b value → %esi → add frame storage for y
```

---

## Observation 4: `main` Loads Argument Values Before Calling `add`

### Procedure

Disassemble `main`:

```gdb
disassemble main
```

### Observation

Relevant instructions from `main`:

```asm
0x0000000000001198 <+8>:  movl $0xa,-0x8(%rbp)
0x000000000000119f <+15>: movl $0x14,-0x4(%rbp)

0x00000000000011c2 <+50>: mov -0x4(%rbp),%edx
0x00000000000011c5 <+53>: mov -0x8(%rbp),%eax
0x00000000000011c8 <+56>: mov %edx,%esi
0x00000000000011ca <+58>: mov %eax,%edi
0x00000000000011cc <+60>: call 0x1139 <add>
```

### Explanation

The first two instructions stored local values in the `main()` frame:

```text
0xa  = 10 → a
0x14 = 20 → b
```

Before calling `add`, the values were moved into argument registers:

```text
b value → %edx → %esi
a value → %eax → %edi
```

Then `call add` transferred control to `add()`.

This reinforced the distinction between object identity and value movement:

```text
a itself did not become x.
a's value moved into the first argument path.

b itself did not become y.
b's value moved into the second argument path.
```

---

## Observation 5: `%rbp`-Relative Addresses Depend on the Current Frame

### Corrected Misconception

Both `main` and `add` used addresses such as `-0x8(%rbp)` or `-0x4(%rbp)`, but those expressions did not refer to the same frame.

### Explanation

`%rbp` is frame-relative.

```text
main frame
  main's rbp
  -0x8(%rbp) = a

add frame
  add's rbp
  -0x4(%rbp) = x
```

The same textual offset pattern does not imply the same variable, because the base pointer belongs to the currently active function frame.

---

## Observation 6: Passing an Address Allows the Callee to Modify the Caller Object

### Prediction

The initial prediction was that `change(&a)` would not modify `a`, because C passes arguments by value.

This prediction was corrected.

C still passes by value, but the copied value is the address of `a`.

### Code

```c
#include <stdio.h>

void change(int *p)
{
    printf("change p  = %p\n", (void *)p);
    printf("change *p = %d\n", *p);

    *p = 999;

    printf("change *p after = %d\n", *p);
}

int main(void)
{
    int a = 10;

    printf("main &a before = %p\n", (void *)&a);
    printf("main a before  = %d\n", a);

    change(&a);

    printf("main &a after  = %p\n", (void *)&a);
    printf("main a after   = %d\n", a);

    return 0;
}
```

### Observation

```text
main &a before = 0x7ffcd0336204
main a before  = 10
change p       = 0x7ffcd0336204
change *p      = 10
change *p after = 999
main &a after  = 0x7ffcd0336204
main a after   = 999
```

### Explanation

`change(&a)` passed the address of `a` by value.

```text
main frame
  a = 10
  &a = 0x7ffcd0336204

change(&a)
  ↓ address value copied

change frame
  p = 0x7ffcd0336204
```

Because `p` contained the address of `a`, dereferencing `p` accessed the original object:

```text
*p = 999
↓
write 999 into the memory location of main's a
```

The result was:

```text
main a after = 999
```

---

## Observation 7: Changing the Pointer Variable Is Different from Changing the Pointee

### Prediction

For this code:

```c
void change(int *p)
{
    p = NULL;
}
```

The correct prediction was that `a` would remain unchanged.

### Explanation

`p = NULL` changes the local pointer variable `p` inside the `change()` frame.

It does not change `a`.

```text
p = NULL
→ change the pointer variable p
→ main's a is unaffected

*p = 999
→ change the object pointed to by p
→ if p contains &a, main's a changes
```

Final distinction:

```text
p
=
address value stored in the pointer variable

*p
=
the object located at the address stored in p
```

---

# Commands / Code

Compile with debugging information and no optimization:

```bash
gcc -O0 -g test.c -o test
```

Run the program:

```bash
./test
```

Start GDB:

```bash
gdb ./test
```

Disassemble `add`:

```gdb
disassemble add
```

Disassemble `main`:

```gdb
disassemble main
```

Key assembly pattern for `add(int x, int y)`:

```asm
mov %edi,-0x4(%rbp)
mov %esi,-0x8(%rbp)
```

Key assembly pattern before `add(a, b)`:

```asm
mov %edx,%esi
mov %eax,%edi
call <add>
```

Pointer modification pattern:

```c
change(&a);
```

passes an address value.

```c
*p = 999;
```

modifies the object pointed to by that address.

```c
p = NULL;
```

modifies only the local pointer variable.

---

# Connections

## Previous Sessions

```text
Session 05
Stack Fundamentals
↓
Local variables live inside stack frames
```

```text
Session 06
Stack Growth Observation
↓
Deeper calls appear at lower stack addresses
```

```text
Session 07
Function Call Frames
↓
Function calls preserve return information and frame state
```

## Current Session

```text
Function arguments
↓
Value copying
↓
Register argument passing
↓
Callee frame storage
↓
Pointer-based access to caller objects
```

## Future Sessions

```text
Session 09
Pointer Tracing Fundamentals
↓
Trace pointer values, addresses, and dereferenced objects more directly
```

```text
Later memory corruption reasoning
↓
Pointers and addresses are data values
↓
Incorrect address use can corrupt or access unintended memory
```

---

# Common Misconceptions

## Misconception 1

```text
If add(a, b) is called, a becomes x and b becomes y.
```

Correction:

```text
a and b do not become x and y.
Their values are copied into x and y.
```

---

## Misconception 2

```text
Function parameters are stored in the caller's frame because the caller supplies the values.
```

Correction:

```text
The caller supplies values, but the callee parameters are callee-side objects.
```

---

## Misconception 3

```text
If two variables have the same value, they are the same variable.
```

Correction:

```text
Value equality is not object identity.
Different objects can contain the same value.
```

---

## Misconception 4

```text
If two functions both use -0x8(%rbp), they refer to the same variable.
```

Correction:

```text
%rbp is frame-relative. Each function frame has its own base pointer.
```

---

## Misconception 5

```text
Passing a pointer means C is no longer pass by value.
```

Correction:

```text
C still passes by value. The copied value is an address value.
```

---

## Misconception 6

```text
p = NULL and *p = 999 both modify the same thing.
```

Correction:

```text
p = NULL modifies the local pointer variable.
*p = 999 modifies the object pointed to by p.
```

---

# Key Takeaways

- C function arguments are passed by value.
- Passing `int` copies the integer value.
- Passing `int *` copies an address value.
- The caller's variable and the callee's parameter are separate objects.
- Equal values do not mean identical variables.
- On x86-64 Linux, early integer arguments are commonly passed through registers such as `%edi` and `%esi`.
- A callee may store register arguments into its own stack frame.
- `%rbp`-relative locations are relative to the current function frame.
- `p` is a pointer variable containing an address value.
- `*p` is the object located at the address stored in `p`.
- Changing `p` does not modify the original object.
- Changing `*p` can modify the original object if `p` points to it.

---

# Review Questions

### Q1. What does it mean that C function arguments are passed by value?

<details>
<summary>A</summary>

</details>

---

### Q2. Why are `a` in `main()` and `x` in `add()` not the same variable, even when both contain `10`?

<details>
<summary>A</summary>

</details>

---

### Q3. What observation showed that `a` and `x` were separate objects?

<details>
<summary>A</summary>

</details>

---

### Q4. Why did changing `x = 999` inside `add()` not change `a` inside `main()`?

<details>
<summary>A</summary>

</details>

---

### Q5. In the observed x86-64 disassembly, what roles did `%edi` and `%esi` play?

<details>
<summary>A</summary>

</details>

---

### Q6. Why does `-0x8(%rbp)` in `main()` not necessarily refer to the same object as `-0x8(%rbp)` in another function?

<details>
<summary>A</summary>

</details>

---

### Q7. If C passes arguments by value, why can `change(&a)` modify `a`?

<details>
<summary>A</summary>

</details>

---

### Q8. What is the difference between `p = NULL` and `*p = 999`?

<details>
<summary>A</summary>

</details>

---

### Q9. Complete the model:

```text
add(a, b)
↓
__________ are copied
↓
add frame receives x and y
```

<details>
<summary>A</summary>

</details>

---

### Q10. How does this session prepare for pointer tracing in Session 09?

<details>
<summary>A</summary>

</details>

---

# Next Session

```yaml
Phase: 01
Session: 09
Title: Pointer Tracing Fundamentals
```

Next topic:

```text
Trace pointer variables, stored address values, and dereferenced objects through running C programs.
```

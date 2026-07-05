# Phase 01 - Session 07

## Metadata

```yaml
Roadmap: C Programming / Embedded Linux, Firmware Analysis & IoT Systems
Phase: 01
Session: 07
Title: Function Call Frames
Status: Completed
Review: Pending
ArchiveVersion: 2
Date: 2026-07-03
```

---

# Objective

Understand what a function call frame contains beyond local variables.

This session focuses on how a called function returns to its caller, how GDB displays call frames, and how `call`, `saved rip`, and `ret` relate to function execution.

---

# Learning Summary

Previous sessions showed that local variables live inside stack frames and that nested function calls move deeper into lower stack addresses.

This session extended that model by observing that a stack frame contains more than local variables. A function must also preserve enough execution state to return to the correct location after it finishes.

Using GDB, the call chain was observed directly:

```text
func2()
↑
func1()
↑
main()
```

`backtrace` showed the active function and its callers. `info frame` showed frame addresses and `saved rip` values. The `saved rip` value was then compared with the disassembly of `func1()`, confirming that the saved return address points to the instruction immediately after the `call func2` instruction.

The key conclusion is:

```text
call
↓
save return address
↓
jump to callee
↓
callee runs
↓
ret
↓
return to saved address
```

---

# Key Concepts

- Function call frame
- Stack frame
- Caller
- Callee
- Return address
- saved rip
- rip
- call instruction
- ret instruction
- backtrace
- GDB frame inspection
- Disassembly
- Instruction pointer

---

# Practical Observations

## Observation 1: Function Calls Need Return Information

### Prediction

When `func2()` finishes, the program must know where inside `func1()` to continue execution.

The correct prediction was:

```text
Stack somewhere stores return-location information.
```

### Code

```c
#include <stdio.h>

void func2(void)
{
    int b = 200;
    printf("func2 &b = %p\n", (void *)&b);
}

void func1(void)
{
    int a = 100;
    printf("func1 &a = %p\n", (void *)&a);

    func2();

    printf("func1 after func2\n");
}

int main(void)
{
    int m = 0;
    printf("main &m = %p\n", (void *)&m);

    func1();

    return 0;
}
```

### Explanation

A function frame does not only contain local variables.

It may also contain information required for function call and return behavior, including:

```text
local variables
saved frame pointer
saved return address / saved rip
alignment space
compiler or ABI-required state
```

The important concept from this observation is:

```text
return address
=
the instruction address to resume at after the current function returns
```

---

## Observation 2: GDB Backtrace Shows the Call Chain

### Procedure

Compile with debugging information:

```bash
gcc -O0 -g test.c -o test
```

Run GDB:

```bash
gdb ./test
```

Inside GDB:

```gdb
break func2
run
backtrace
```

### Observation

Observed `backtrace` output:

```text
#0  func2 () at test.c:3
#1  0x00005555555551e7 in func1 () at test.c:12
#2  0x000055555555524b in main () at test.c:21
```

### Explanation

The actual call chain was:

```text
main()
↓
func1()
↓
func2()
```

GDB displays the current frame first, then walks back toward the callers:

```text
func2()
↑
func1()
↑
main()
```

Therefore:

```text
#0 = current function
#1 = caller of current function
#2 = caller's caller
```

---

## Observation 3: `info frame` Shows Frame Address and saved rip

### Procedure

Inside GDB at the `func2` breakpoint:

```gdb
info frame
```

### Observation

Observed output included:

```text
Stack level 0, frame at 0x7ffffffffdc80:
rip = 0x555555555161 in func2 (test.c:3); saved rip = 0x5555555551e7
called by frame at 0x7ffffffffdca0
```

### Explanation

The current frame was `func2`.

```text
rip = current instruction address
saved rip = address to return to when func2 finishes
```

The saved return address:

```text
saved rip = 0x5555555551e7
```

points back into `func1()`, because `func1()` called `func2()`.

This confirmed the model:

```text
func2 frame
↓
saved rip points to func1's next instruction
```

---

## Observation 4: Caller Frames Have Higher Addresses

### Procedure

Move through GDB frames:

```gdb
frame 1
info frame

frame 2
info frame
```

### Observation

Observed frame addresses:

```text
frame 0, func2: frame at 0x7ffffffffdc80
frame 1, func1: frame at 0x7ffffffffdca0
frame 2, main : frame at 0x7ffffffffdcc0
```

Address order:

```text
0x...dc80 < 0x...dca0 < 0x...dcc0
```

### Explanation

The deeper function call, `func2()`, had the lower frame address.

Caller frames appeared at higher addresses:

```text
High Address

main frame   0x...dcc0
func1 frame  0x...dca0
func2 frame  0x...dc80

Low Address
```

This matched the previous stack-growth model:

```text
Deeper calls
↓
Lower stack addresses

Returning toward callers
↓
Higher stack addresses
```

---

## Observation 5: saved rip Points to the Instruction After `call`

### Procedure

Return to frame 0 and disassemble `func1`:

```gdb
frame 0
disassemble func1
```

### Observation

Relevant disassembly:

```text
0x5555555551e2 <+57>: call 0x555555555159 <func2>
0x5555555551e7 <+62>: lea  0xe34(%rip),%rax
```

Previously observed saved return address:

```text
saved rip = 0x5555555551e7
```

### Explanation

`0x...51e2` is the address of the `call func2` instruction inside `func1`.

`0x...51e7` is the address of the next instruction after the call.

The saved return address is not the address of the `call` instruction itself. It is the address where execution should resume after `func2()` returns.

```text
0x...51e2: call func2
           ↓
           save 0x...51e7 as return address
           ↓
           jump to func2

func2 runs

ret
↓
return to 0x...51e7
```

This directly confirmed the `call` and `ret` relationship.

---

# Commands / Code

Compile with no optimization and debug symbols:

```bash
gcc -O0 -g test.c -o test
```

Start GDB:

```bash
gdb ./test
```

Set a breakpoint at `func2`:

```gdb
break func2
```

Run the program:

```gdb
run
```

Show the call chain:

```gdb
backtrace
```

Inspect the current frame:

```gdb
info frame
```

Move to a caller frame:

```gdb
frame 1
```

Inspect another frame:

```gdb
frame 2
```

Disassemble a function:

```gdb
disassemble func1
```

---

# Connections

## Previous Sessions

```text
Session 05
Stack Fundamentals
↓
Local variables live inside stack frames
↓
Stack space can be reused
```

```text
Session 06
Stack Growth Observation
↓
Nested calls move toward lower addresses
↓
Returning resumes the caller's frame
```

## Current Session

```text
Function call frame
↓
Caller / callee relationship
↓
saved rip
↓
return address
↓
GDB frame inspection
```

## Future Sessions

```text
Session 08
Function Arguments In Memory
↓
Arguments and calling convention
↓
Registers and stack argument behavior
```

```text
Later:
Assembly Foundations
↓
call / ret
↓
Function prologue / epilogue
```

```text
Later:
Memory Corruption Foundations
↓
Return address corruption concepts
↓
Stack overflow reasoning
```

---

# Common Misconceptions

## Misconception 1

```text
A stack frame only contains local variables.
```

Correction:

```text
A stack frame can contain local variables, saved frame information, saved return addresses, alignment space, and compiler or ABI-required state.
```

---

## Misconception 2

```text
The CPU automatically remembers function names to return after a call.
```

Correction:

```text
The program returns using saved execution addresses, not function names.
```

---

## Misconception 3

```text
saved rip points to the call instruction itself.
```

Correction:

```text
saved rip points to the instruction after the call instruction.
```

---

## Misconception 4

```text
rip and saved rip are the same thing.
```

Correction:

```text
rip is the current instruction address.

saved rip is the return address used when the current function returns.
```

---

## Misconception 5

```text
func1's saved rip is for returning from func2() back to func1().
```

Correction:

```text
func1's saved rip is for returning from func1() back to main().

func2's saved rip is for returning from func2() back to func1().
```

---

# Key Takeaways

- A function call frame contains more than local variables.
- A function must know where to return after it finishes.
- `backtrace` shows the current function and its callers.
- `info frame` shows frame information such as frame address and saved rip.
- `rip` is the current instruction pointer.
- `saved rip` is the saved return address.
- `call` stores the address of the next instruction as the return address.
- `ret` returns to the saved return address.
- The saved return address points to the caller's next instruction after the call.
- Caller frames appear higher in the stack than deeper callee frames in this environment.

---

# Review Questions

### Q1. What does `backtrace` show in GDB?

<details>
<summary>A</summary>

</details>

---

### Q2. What is the difference between a caller and a callee?

<details>
<summary>A</summary>

</details>

---

### Q3. What is `rip`?

<details>
<summary>A</summary>

</details>

---

### Q4. What is `saved rip`?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does a function call frame need more than local variables?

<details>
<summary>A</summary>

</details>

---

### Q6. In the observed disassembly, why was `saved rip` equal to the instruction after `call func2`?

<details>
<summary>A</summary>

</details>

---

### Q7. Why is it incorrect to say that `saved rip` points to the `call` instruction itself?

<details>
<summary>A</summary>

</details>

---

### Q8. In GDB, why does `backtrace` show `func2`, then `func1`, then `main`?

<details>
<summary>A</summary>

</details>

---

### Q9. Complete the model:

```text
call
↓
__________ saved
↓
callee executes
↓
ret
↓
return to saved address
```

<details>
<summary>A</summary>

</details>

---

### Q10. How does understanding `saved rip` prepare for later stack overflow reasoning?

<details>
<summary>A</summary>

</details>

---

# Next Session

```yaml
Phase: 01
Session: 08
Title: Function Arguments In Memory
```

Next topic:

```text
Observe how function arguments are passed and where they appear during function execution.
```

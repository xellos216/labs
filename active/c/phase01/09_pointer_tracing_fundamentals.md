# Phase 01 - Session 09

## Metadata

```yaml
Roadmap: C Programming / Embedded Linux, Firmware Analysis & IoT Systems
Phase: 01
Session: 09
Title: Pointer Tracing Fundamentals
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-08
```

---

# Objective

Understand how pointer variables store address values, how dereferencing follows those address values, and how pointer values behave when copied, reassigned, and passed through function calls.

This session focuses on tracing:

```text
&a
p
&p
*p
q = p
int **pp
*pp
**pp
```

The goal is to distinguish pointer variables, the address values they store, and the objects reached through dereferencing.

---

# Learning Summary

Previous sessions established that C function arguments are passed by value. Session 08 showed that passing `int` copies an integer value, while passing `int *` copies an address value.

This session extended that model into pointer tracing.

The first experiment confirmed that:

```text
p == &a
*p == a
&p != &a
```

`p` stores the address of `a`, but `p` itself is a separate variable with its own address.

The next experiment showed that assigning a new address to a pointer changes only the pointer variable's stored address value:

```text
p = &b
```

After this assignment, `p` no longer points to `a`; it points to `b`. The address of the pointer variable itself, `&p`, remains unchanged.

The session then traced copying one pointer into another:

```c
int *q = p;
```

This copies the current address value stored in `p` into `q`. It does not create a permanent connection between `p` and `q`. Later changes to `p` do not automatically change `q`.

Finally, pointer behavior was traced across function calls. Passing `int *p` to a function copies the pointer value. Reassigning the callee's local pointer parameter does not change the caller's pointer variable. To change the caller's pointer variable itself, the function needs the address of that pointer variable, using `int **pp`.

The final distinction was:

```text
int *p
=
used to modify the int object pointed to by p

int **pp
=
used to modify the pointer variable p itself
```

---

# Key Concepts

- Pointer variable
- Address value
- Dereference
- Object identity
- Pointer reassignment
- Pointer copy
- Caller frame
- Callee frame
- Pass by value
- Pointer parameter
- Pointer-to-pointer
- `int *`
- `int **`
- `p`
- `&p`
- `*p`
- `pp`
- `*pp`
- `**pp`

---

# Practical Observations

## Observation 1: `p`, `&p`, and `*p` Are Different

### Prediction

For this code:

```c
int a = 10;
int *p = &a;
```

The correct predictions were:

```text
&a and p are equal.
&p and &a are different.
*p prints the value of a.
```

### Code

```c
#include <stdio.h>

int main(void)
{
    int a = 10;
    int *p = &a;

    printf("a  = %d\n", a);
    printf("&a = %p\n", (void *)&a);

    printf("p  = %p\n", (void *)p);
    printf("&p = %p\n", (void *)&p);

    printf("*p = %d\n", *p);

    return 0;
}
```

### Observation

The output showed the same address for `&a` and `p`, a different address for `&p`, and the value `10` for `*p`.

```text
&a = 0x...f8c
p  = 0x...f8c
&p = 0x...f90
*p = 10
```

### Explanation

`p` stores the address of `a`.

`&p` is the address of the pointer variable `p` itself.

`*p` follows the address stored in `p` and reads the value at that location.

```text
&p        &a
 │         │
 ▼         ▼
[p] ---> [a]
        value 10
```

Key model:

```text
p == &a
*p == a
&p != &a
```

---

## Observation 2: Reassigning a Pointer Changes What It Points To

### Prediction

For this operation:

```c
p = &b;
```

The correct predictions were:

```text
p becomes equal to &b.
&p does not change.
*p = 999 modifies b, not a.
```

### Code

```c
#include <stdio.h>

int main(void)
{
    int a = 10;
    int b = 20;
    int *p = &a;

    printf("before\n");
    printf("&a = %p, a = %d\n", (void *)&a, a);
    printf("&b = %p, b = %d\n", (void *)&b, b);
    printf("&p = %p, p = %p, *p = %d\n", (void *)&p, (void *)p, *p);

    p = &b;

    printf("after p = &b\n");
    printf("&a = %p, a = %d\n", (void *)&a, a);
    printf("&b = %p, b = %d\n", (void *)&b, b);
    printf("&p = %p, p = %p, *p = %d\n", (void *)&p, (void *)p, *p);

    *p = 999;

    printf("after *p = 999\n");
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}
```

### Observation

The output showed:

```text
before:
p == &a
*p == 10

p = &b after:
p == &b
*p == 20

*p = 999 after:
a == 10
b == 999
```

### Explanation

`p = &b` changes the address value stored inside `p`.

It does not move the pointer variable itself. `&p` remains the address of the pointer variable.

After `p` is changed to `&b`, dereferencing `p` reaches `b`.

```text
Initial:
[p] ---> [a: 10]
[b: 20]
```

```text
After p = &b:
[a: 10]
[p] ---> [b: 20]
```

```text
After *p = 999:
[a: 10]
[p] ---> [b: 999]
```

---

## Observation 3: `q = p` Copies the Current Pointer Value

### Prediction

For this code:

```c
int *p = &a;
int *q = p;
```

The initial prediction correctly identified that `q == &a` immediately after assignment.

The incorrect prediction was that later changing `p` would also change `q`.

### Code

```c
#include <stdio.h>

int main(void)
{
    int a = 10;
    int b = 20;

    int *p = &a;
    int *q = p;

    printf("initial\n");
    printf("&a = %p, a = %d\n", (void *)&a, a);
    printf("&b = %p, b = %d\n", (void *)&b, b);
    printf("&p = %p, p = %p, *p = %d\n", (void *)&p, (void *)p, *p);
    printf("&q = %p, q = %p, *q = %d\n", (void *)&q, (void *)q, *q);

    p = &b;

    printf("after p = &b\n");
    printf("p = %p, *p = %d\n", (void *)p, *p);
    printf("q = %p, *q = %d\n", (void *)q, *q);

    *q = 777;

    printf("after *q = 777\n");
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}
```

### Observation

The output showed:

```text
initial:
p == &a
q == &a

p = &b after:
p == &b
q == &a

*q = 777 after:
a == 777
b == 20
```

### Explanation

`q = p` copies the address value currently stored in `p` into `q`.

It does not permanently link the two pointer variables.

```text
Initial:
[p] ---> [a: 10]
[q] ----^
[b: 20]
```

```text
After p = &b:
[q] ---> [a: 10]
[p] ---> [b: 20]
```

Because `q` still pointed to `a`, `*q = 777` modified `a`.

Key correction:

```text
q = p
=
copy p's current address value into q

q = p
!=
make q follow future changes to p
```

---

## Observation 4: Reassigning a Pointer Parameter Does Not Change the Caller Pointer

### Prediction

The incorrect prediction was that passing `main`'s pointer variable into a function and then assigning the parameter would change the caller's pointer.

### Code

```c
#include <stdio.h>

void move_pointer(int *p, int *target)
{
    printf("inside before\n");
    printf("&p      = %p, p      = %p, *p      = %d\n", (void *)&p, (void *)p, *p);
    printf("&target = %p, target = %p, *target = %d\n", (void *)&target, (void *)target, *target);

    p = target;

    printf("inside after p = target\n");
    printf("&p      = %p, p      = %p, *p      = %d\n", (void *)&p, (void *)p, *p);
}

int main(void)
{
    int a = 10;
    int b = 20;
    int *p = &a;

    printf("main before\n");
    printf("&a = %p, a = %d\n", (void *)&a, a);
    printf("&b = %p, b = %d\n", (void *)&b, b);
    printf("&p = %p, p = %p, *p = %d\n", (void *)&p, (void *)p, *p);

    move_pointer(p, &b);

    printf("main after\n");
    printf("&p = %p, p = %p, *p = %d\n", (void *)&p, (void *)p, *p);
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}
```

### Observation

The output showed:

```text
main before:
main p == &a

inside before:
callee p == &a
target == &b

inside after p = target:
callee p == &b

main after:
main p == &a
a == 10
b == 20
```

### Explanation

The caller's pointer variable and the callee's pointer parameter are separate variables in separate stack frames.

They initially contain the same address value, but they are not the same object.

```text
main frame:
  p ---> a

move_pointer frame:
  p      ---> a
  target ---> b
```

After `p = target` inside the function:

```text
main frame:
  p ---> a

move_pointer frame:
  p      ---> b
  target ---> b
```

When the function returns, the callee frame is removed. The caller's `p` remains unchanged.

---

## Observation 5: `int **pp` Allows a Function to Change the Caller Pointer

### Prediction

The correct conclusion after correction was:

```text
&p is the address of main's pointer variable p.
pp receives main's &p.
*pp = target changes main's p.
```

### Code

```c
#include <stdio.h>

void move_pointer(int **pp, int *target)
{
    printf("inside before\n");
    printf("&pp = %p, pp = %p, *pp = %p, **pp = %d\n",
           (void *)&pp, (void *)pp, (void *)*pp, **pp);
    printf("target = %p, *target = %d\n", (void *)target, *target);

    *pp = target;

    printf("inside after *pp = target\n");
    printf("&pp = %p, pp = %p, *pp = %p, **pp = %d\n",
           (void *)&pp, (void *)pp, (void *)*pp, **pp);
}

int main(void)
{
    int a = 10;
    int b = 20;
    int *p = &a;

    printf("main before\n");
    printf("&a = %p, a = %d\n", (void *)&a, a);
    printf("&b = %p, b = %d\n", (void *)&b, b);
    printf("&p = %p, p = %p, *p = %d\n", (void *)&p, (void *)p, *p);

    move_pointer(&p, &b);

    printf("main after\n");
    printf("&p = %p, p = %p, *p = %d\n", (void *)&p, (void *)p, *p);
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}
```

### Observation

The output showed:

```text
main before:
p == &a

inside before:
pp == &p
*pp == p == &a
**pp == *p == 10
target == &b

inside after *pp = target:
pp == &p
*pp == p == &b
**pp == *p == 20

main after:
p == &b
*p == 20
a == 10
b == 20
```

### Explanation

`pp` stores the address of the caller's pointer variable `p`.

```text
pp ---> p ---> a
```

`*pp = target` modifies the caller's pointer variable itself.

```text
Before:
pp ---> p ---> a

target ---> b
```

```text
After *pp = target:
pp ---> p ---> b
```

This changes what `p` points to. It does not change the integer values of `a` or `b`.

---

## Observation 6: `*pp = target` and `**pp = 999` Modify Different Things

### Prediction

The correct final prediction was:

```text
If p points to a, **pp = 999 changes a.
If p later points to b, **pp = 999 changes b.
```

### Code

```c
#include <stdio.h>

void change_value(int **pp)
{
    **pp = 999;
}

int main(void)
{
    int a = 10;
    int b = 20;
    int *p = &a;

    change_value(&p);

    printf("a = %d\n", a);
    printf("b = %d\n", b);

    p = &b;

    change_value(&p);

    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}
```

### Observation

The output showed:

```text
a = 999
b = 20

a = 999
b = 999
```

### Explanation

`*pp = target` changes the pointer variable `p`.

```text
*pp = target
=
p = target
```

`**pp = 999` changes the object currently pointed to by `p`.

```text
**pp = 999
=
*p = 999
```

If `p` points to `a`, `**pp = 999` modifies `a`.

If `p` points to `b`, `**pp = 999` modifies `b`.

---

# Commands / Code

Compile with no optimization and debug symbols:

```bash
gcc -O0 -g test.c -o test
```

Run the compiled program:

```bash
./test
```

Print an object's address:

```c
printf("&a = %p\n", (void *)&a);
```

Print a pointer variable's stored address value:

```c
printf("p = %p\n", (void *)p);
```

Print a pointer variable's own address:

```c
printf("&p = %p\n", (void *)&p);
```

Print the object reached by dereferencing a pointer:

```c
printf("*p = %d\n", *p);
```

Trace a pointer-to-pointer:

```c
printf("pp = %p, *pp = %p, **pp = %d\n",
       (void *)pp, (void *)*pp, **pp);
```

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
Session 07
Function Call Frames
↓
Caller and callee frames are separate execution contexts
```

```text
Session 08
Function Arguments In Memory
↓
C arguments are passed by value
Pointer arguments copy address values
```

## Current Session

```text
Pointer tracing
↓
Address values
↓
Dereference
↓
Pointer copy
↓
Pointer reassignment
↓
Pointer-to-pointer
```

## Future Sessions

```text
Session 10
Heap Fundamentals
↓
Pointers refer to dynamically allocated objects
```

```text
Later memory corruption reasoning
↓
Incorrect pointer values can access or modify unintended memory
```

```text
Embedded and firmware analysis
↓
Pointers model memory-mapped structures, buffers, and device-facing data
```

---

# Common Misconceptions

## Misconception 1

```text
p and &p are the same thing.
```

Correction:

```text
p is the address value stored inside the pointer variable.
&p is the address of the pointer variable itself.
```

---

## Misconception 2

```text
If q = p, q is permanently connected to p.
```

Correction:

```text
q = p copies the current address value stored in p. Later changes to p do not automatically change q.
```

---

## Misconception 3

```text
Passing a pointer to a function lets the function reassign the caller's pointer variable.
```

Correction:

```text
Passing int * copies an address value. Reassigning the callee's local pointer parameter does not change the caller's pointer variable.
```

---

## Misconception 4

```text
int **pp is needed whenever a function wants to modify the value pointed to by p.
```

Correction:

```text
int *p is enough to modify the int object pointed to by p. int **pp is needed to modify the caller's pointer variable itself.
```

---

## Misconception 5

```text
*pp = target and **pp = 999 modify the same thing.
```

Correction:

```text
*pp = target modifies the pointer variable p. **pp = 999 modifies the int object currently pointed to by p.
```

---

# Key Takeaways

- A pointer variable stores an address value.
- `p` is the address value stored in the pointer variable.
- `&p` is the address of the pointer variable itself.
- `*p` is the object reached by following the address stored in `p`.
- `p = &b` changes the address value stored in `p`.
- `p = &b` does not change the address of the pointer variable itself.
- `q = p` copies the current pointer value.
- `q = p` does not make `q` follow future changes to `p`.
- Function pointer parameters are still passed by value.
- Reassigning a callee's `int *p` parameter does not change the caller's pointer variable.
- To change a caller's pointer variable, pass its address: `&p`.
- `int **pp` points to an `int *` pointer variable.
- `*pp = target` changes what `p` points to.
- `**pp = 999` changes the int object currently pointed to by `p`.

---

# Review Questions

### Q1. What is stored inside a pointer variable?

<details>
<summary>A</summary>

</details>

---

### Q2. What is the difference between `p`, `&p`, and `*p`?

<details>
<summary>A</summary>

</details>

---

### Q3. Why is `p == &a` true after `int *p = &a;`?

<details>
<summary>A</summary>

</details>

---

### Q4. Why does `p = &b` not change `&p`?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does `q = p` not make `q` follow future changes to `p`?

<details>
<summary>A</summary>

</details>

---

### Q6. In a function parameter `void f(int *p)`, why does `p = target;` not change the caller's pointer variable?

<details>
<summary>A</summary>

</details>

---

### Q7. When is `int **pp` needed?

<details>
<summary>A</summary>

</details>

---

### Q8. What is the difference between `*pp = target;` and `**pp = 999;`?

<details>
<summary>A</summary>

</details>

---

### Q9. Complete the model:

```text
pp
↓
__________
↓
int object
```

<details>
<summary>A</summary>

</details>

---

### Q10. How does pointer tracing prepare for heap allocation in the next session?

<details>
<summary>A</summary>

</details>

---

# Next Session

```yaml
Phase: 01
Session: 10
Title: Heap Fundamentals
```

Next topic:

```text
Understand dynamically allocated objects and how pointers refer to heap memory.
```

# Phase 01 - Session 10

## Metadata

```yaml
Roadmap: C Programming / Embedded Linux, Firmware Analysis & IoT Systems
Phase: 01
Session: 10
Title: Heap Fundamentals
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-14
```

---

# Objective

Understand why heap allocation exists, how heap-object lifetime differs from
stack-object lifetime, and how pointers relate to dynamically allocated
objects.

This session also introduces the failure modes that appear when allocation and
lifetime are managed incorrectly:

- dangling pointers
- use-after-free
- double free
- memory leaks
- stale aliases to freed storage

---

# Learning Summary

A normal local variable belongs to a function's stack frame. Its lifetime ends
when that function returns. Returning the address of such a local variable does
not extend its lifetime; it produces a pointer to an object that no longer
exists.

Heap allocation solves a different lifetime problem. `malloc()` requests
storage that is independent of the current function's stack frame. A function
may return the resulting address, and the allocated object remains alive after
the function returns.

That longer lifetime is not automatic. The program must eventually call
`free()` with the allocated address. `free()` ends the lifetime of the dynamic
object, but it does not automatically clear every pointer that contains the old
address.

The central model is:

```text
Stack object
→ lifetime tied to function call and return
→ managed automatically

Heap object
→ lifetime begins with dynamic allocation
→ lifetime ends when the program calls free()
→ managed explicitly by the program
```

---

# Key Concepts

- stack lifetime
- heap lifetime
- dynamic allocation
- `malloc()`
- `free()`
- allocation failure
- `NULL`
- dangling pointer
- use-after-free
- double free
- memory leak
- pointer alias
- allocator reuse
- object lifetime
- memory mapping

---

# Practical Observations

## Observation 1: Returning a Local Variable Address Is Unsafe

### Prediction

The initial prediction was that returning a local variable's address would be
safe because the numeric address remains available after the function returns.

### Code

```c
#include <stdio.h>

int *make_value(void)
{
    int x = 10;

    return &x;
}

int main(void)
{
    int *p = make_value();

    printf("%d\n", *p);
    return 0;
}
```

### Observation

`x` belongs to `make_value()`'s stack frame. When the function returns, `x`'s
lifetime ends even if its old address value is copied into `p`.

### Explanation

An address value remaining in a pointer does not prove that a valid object
still exists at that address.

```text
make_value() running:

p will receive → [x: 10]

make_value() returned:

x lifetime ended
p contains the old address
p is dangling
```

Dereferencing `p` after the return is undefined behavior.

---

## Observation 2: Heap Storage Survives Function Return

### Prediction

The learner correctly predicted that a value allocated with `malloc()` remains
valid after the allocating function returns.

### Code

```c
#include <stdio.h>
#include <stdlib.h>

int *make_value(void)
{
    int *p = malloc(sizeof(int));

    if (p == NULL) {
        return NULL;
    }

    *p = 10;
    return p;
}

int main(void)
{
    int *p = make_value();

    if (p == NULL) {
        fprintf(stderr, "allocation failed\n");
        return 1;
    }

    printf("%d\n", *p);

    free(p);
    return 0;
}
```

### Observation

The local pointer variable inside `make_value()` belongs to the stack, but the
allocated `int` object does not belong to that stack frame.

```text
During make_value():

Stack:
[p] ─────→ Heap:
          [10]

After make_value() returns:

local p removed
returned address copied into main's pointer
Heap object remains alive
```

### Explanation

`malloc()` creates a dynamic object whose lifetime is independent of the
calling function's stack frame. The object remains alive until it is released
with `free()`.

---

## Observation 3: Allocation Failure Must Be Checked

### Prediction

The learner correctly predicted that `malloc()` returns `NULL` when allocation
fails.

### Explanation

This pattern is unsafe:

```c
int *p = malloc(sizeof(int));
*p = 10;
```

If allocation fails, dereferencing `p` is invalid. Check the result before use:

```c
int *p = malloc(sizeof(int));

if (p == NULL) {
    return 1;
}

*p = 10;
```

---

## Observation 4: `free()` Ends the Object Lifetime

### Prediction

The initial prediction was that reading through `p` after `free(p)` would be
safe because the heap storage had already been returned.

### Explanation

The opposite is true. Returning the storage ends the lifetime of the allocated
object.

```c
free(p);
printf("%d\n", *p);
```

The second line is a use-after-free and has undefined behavior.

```text
free(p)
→ allocated object lifetime ends
→ p may still contain the old address
→ p becomes dangling
```

A common cleanup pattern is:

```c
free(p);
p = NULL;
```

Setting `p` to `NULL` does not undo an earlier error. It only makes later
accidental reuse of that particular pointer easier to detect.

---

## Observation 5: Freeing the Same Object Twice Is Invalid

### Prediction

The learner correctly predicted that calling `free(p)` twice is unsafe.

### Code

```c
free(p);
free(p);
```

### Explanation

The first call ends the dynamic object's lifetime. Passing the same stale
address to `free()` again attempts to release an object that has already been
released. This is a double free and has undefined behavior.

`free(NULL)` is safe and performs no operation, which is one reason the
following pattern is useful:

```c
free(p);
p = NULL;
```

---

## Observation 6: Replacing the Last Pointer Causes a Memory Leak

### Prediction

The learner correctly predicted that assigning `NULL` to the only pointer does
not free the allocated object.

### Code

```c
int *p = malloc(sizeof(int));

if (p == NULL) {
    return 1;
}

*p = 10;
p = NULL;
```

### Explanation

`p = NULL` changes only the pointer variable. It does not end the lifetime of
the allocated object.

```text
Before:

p ─────→ Heap object

After p = NULL:

p ─────→ NULL

Heap object still allocated
but its address has been lost
```

This is a memory leak.

Correct order:

```c
free(p);
p = NULL;
```

Incorrect order:

```c
p = NULL;
free(p);
```

The second form calls `free(NULL)` and leaves the original object allocated.

---

## Observation 7: All Aliases Become Dangling After `free()`

### Prediction

The initial prediction was that a copied pointer would remain valid after the
original pointer was passed to `free()`.

### Code

```c
int *p = malloc(sizeof(int));

if (p == NULL) {
    return 1;
}

int *q = p;

free(p);
p = NULL;
```

### Observation

`p` and `q` initially contain the same address value. `free(p)` ends the
lifetime of the one heap object that both pointers referred to.

After cleanup:

```text
p = NULL
q = old address of the freed object
```

### Explanation

`free()` releases the dynamic object, not one particular pointer variable.
Every pointer that still contains the old address becomes stale.

```text
Before free():

p ───┐
     ├──→ Heap object
q ───┘

After free(p):

Heap object lifetime ended
p and q both contain stale addresses

After p = NULL:

p → NULL
q → dangling pointer
```

---

## Observation 8: Heap and Stack Addresses Occupy Different Mappings

### Code

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int global_value = 10;

int main(void)
{
    int local_value = 20;
    int *heap_value = malloc(sizeof(int));

    if (heap_value == NULL) {
        return 1;
    }

    *heap_value = 30;

    printf("PID: %d\n", getpid());
    printf("&global_value = %p\n", (void *)&global_value);
    printf("&local_value  = %p\n", (void *)&local_value);
    printf("heap_value    = %p\n", (void *)heap_value);
    printf("&heap_value   = %p\n", (void *)&heap_value);

    getchar();

    free(heap_value);
    return 0;
}
```

### Observation

The program output and `/proc/<PID>/maps` showed:

```text
&global_value
→ writable executable mapping

&local_value
→ [stack]

heap_value
→ [heap]

&heap_value
→ [stack]
```

The exact process identifiers and addresses were environment-specific and are
not preserved in this public archive.

### Explanation

The pointer variable and the object it points to are separate objects in
separate regions.

```text
Data:
[global_value: 10]

Stack:
[local_value: 20]
[heap_value] ───────────┐
                        │
                        ▼
Heap:
[30]
```

Therefore:

```text
heap_value
→ address of the allocated heap object

&heap_value
→ address of the local pointer variable in the stack frame
```

---

## Observation 9: `free()` Does Not Necessarily Remove the Heap Mapping

### Prediction

The learner correctly predicted that freeing one allocation does not require
the complete `[heap]` mapping to disappear.

### Explanation

`/proc/<PID>/maps` shows virtual-memory mappings. It does not show whether every
individual allocator block is currently in use.

```text
free(heap_value)
→ ends that dynamic object's lifetime
→ returns its block to the allocator
→ allocator may keep the block for reuse
→ [heap] mapping may remain visible
```

The allocator decides how to manage and reuse freed blocks. The program decides
when to call `free()`.

---

## Observation 10: A Freed Block May Be Reused

### Prediction

The learner correctly predicted that a later allocation of the same size could
receive the same address as an earlier freed allocation.

### Code

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *p = malloc(sizeof(int));

    if (p == NULL) {
        return 1;
    }

    printf("p = %p\n", (void *)p);

    free(p);

    int *q = malloc(sizeof(int));

    if (q == NULL) {
        return 1;
    }

    printf("q = %p\n", (void *)q);

    free(q);
    return 0;
}
```

### Observation

In the observed run, `p` and `q` printed the same numeric address.

### Explanation

The allocator reused a block that had become available after `free(p)`.

```text
first malloc()
→ object A created in block X

free(p)
→ object A lifetime ends
→ block X becomes reusable

second malloc()
→ object B created
→ allocator selects block X again
```

The same address does not mean the same object lifetime continued.

```text
same storage address
≠
same object
```

The pointer returned by the second allocation should be used to access the new
object.

---

# Commands / Code

Compile without optimization and include debug symbols:

```bash
gcc -O0 -g test.c -o test
```

Run the program:

```bash
./test
```

Inspect the process mappings while it is paused:

```bash
cat /proc/<PID>/maps
```

Allocate one `int` object:

```c
int *p = malloc(sizeof(int));
```

Check allocation success:

```c
if (p == NULL) {
    return 1;
}
```

End the allocated object's lifetime:

```c
free(p);
```

Clear the local pointer after release:

```c
free(p);
p = NULL;
```

---

# Connections

```text
Session 05
Stack Fundamentals
↓
local objects belong to stack frames
```

```text
Session 09
Pointer Tracing Fundamentals
↓
pointer variables store addresses
aliases copy address values
```

```text
Session 10
Heap Fundamentals
↓
dynamic objects have explicit lifetimes
```

```text
Session 11
malloc() Observation
↓
observe allocation behavior in more detail
```

This model also supports later reasoning about:

- resource ownership
- memory leaks
- use-after-free vulnerabilities
- double-free vulnerabilities
- heap corruption
- firmware and embedded memory management

---

# Common Misconceptions

## Misconception 1

```text
Returning a local variable's address keeps the local variable alive.
```

Correction:

The function return ends the local object's lifetime. Only the numeric address
value is copied.

---

## Misconception 2

```text
free(p) makes p automatically become NULL.
```

Correction:

`free()` ends the dynamic object's lifetime. Pointer variables may still retain
the stale address.

---

## Misconception 3

```text
A copied pointer remains valid after the original pointer is freed.
```

Correction:

All aliases refer to the same allocated object. When that object's lifetime
ends, every stale alias becomes dangling.

---

## Misconception 4

```text
p = NULL frees the object that p previously pointed to.
```

Correction:

It changes only the pointer variable. If no other pointer retains the address,
the allocated object becomes unreachable and leaks.

---

## Misconception 5

```text
If /proc/<PID>/maps still shows [heap], free() failed.
```

Correction:

`maps` reports mappings, not the allocation status of individual allocator
blocks.

---

## Misconception 6

```text
If two allocations return the same address, they are the same object.
```

Correction:

A freed block can be reused for a new object with a separate lifetime.

---

# Key Takeaways

- Stack-object lifetime is tied to function calls and returns.
- Returning a local variable's address creates a dangling pointer.
- `malloc()` creates dynamic storage independent of a function stack frame.
- `malloc()` returns `NULL` when allocation fails.
- The program must explicitly end a dynamic object's lifetime with `free()`.
- Reading or writing through a pointer after `free()` is use-after-free.
- Freeing the same dynamic object twice is a double free.
- Assigning `NULL` before `free()` can lose the only address and cause a leak.
- `free()` affects the allocated object and therefore invalidates all stale
  aliases to it.
- A pointer variable may live on the stack while pointing to an object on the
  heap.
- Heap mappings and individual allocator blocks are different levels of memory
  management.
- A later allocation may reuse the same address for a new object.

---

# Review Questions

### Q1. Why is returning the address of an ordinary local variable unsafe?

<details>
<summary>A</summary>

</details>

---

### Q2. How does the lifetime of a heap object differ from the lifetime of a stack object?

<details>
<summary>A</summary>

</details>

---

### Q3. Why must a `malloc()` return value be checked before dereferencing it?

<details>
<summary>A</summary>

</details>

---

### Q4. What happens to a pointer variable when the object it points to is freed?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does setting `p = NULL` not release the allocated object?

<details>
<summary>A</summary>

</details>

---

### Q6. If `p` and `q` point to the same heap object, what happens to `q` after `free(p)`?

<details>
<summary>A</summary>

</details>

---

### Q7. Why can `/proc/<PID>/maps` remain unchanged after one allocation is freed?

<details>
<summary>A</summary>

</details>

---

### Q8. What does it demonstrate when a later `malloc()` returns the same address as a freed allocation?

<details>
<summary>A</summary>

</details>

---

### Q9. Why does the same numeric address not necessarily identify the same C object over time?

<details>
<summary>A</summary>

</details>

---

### Q10. Explain who decides when a heap object should be freed and who manages the reusable block afterward.

<details>
<summary>A</summary>

</details>

---

# Next Session

```yaml
Phase: 01
Session: 11
Title: malloc() Observation
```

Next topic:

```text
Observe malloc() behavior, returned addresses, and allocator-managed storage in
more detail.
```

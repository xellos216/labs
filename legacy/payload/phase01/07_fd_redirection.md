# File Descriptor Redirection

## Standard Descriptors

| FD | Stream | Default target |
|---|---|---|
| `0` | stdin | terminal input |
| `1` | stdout | terminal output |
| `2` | stderr | terminal output |

Stdout and stderr may appear on the same terminal while remaining independent
streams.

```sh
echo ok
ls /no/such/path
```

The first writes to FD 1; the second normally reports its error on FD 2.

## Redirect One Stream

```sh
command >stdout.txt
command 2>stderr.txt
```

## Redirect Both Streams

```sh
command >all.txt 2>&1
```

`2>&1` duplicates FD 1's current destination onto FD 2.

```sh
command &>all.txt
```

This Bash shorthand redirects both streams.

## Descriptor Duplication

```text
2>&1
```

means:

```text
make FD 2 point where FD 1 points now
```

It does not mean "send stderr to a file named 1."

## Ordering Example

```sh
command >out 2>&1
```

```text
FD 1 -> out
FD 2 -> current FD 1 -> out
```

Reversing the order changes the graph.

## Review

1. A descriptor is a process-local integer reference to an open resource.
2. Identical display destinations do not make stdout and stderr identical.
3. Redirection rewires descriptors before the program runs.
4. Descriptor duplication copies a destination at that point in the order.
5. Analyze redirection as an FD graph.

# QA

**Q1.**
What are file descriptors `0`, `1`, and `2` normally used for?

<details>
<summary><strong>A1.</strong></summary>

FD 0 is stdin, FD 1 is stdout, and FD 2 is stderr. They are conventional
process I/O channels.

</details>

---

**Q2.**
Why are stdout and stderr still different if both appear on the terminal?

<details>
<summary><strong>A2.</strong></summary>

They are separate descriptors that happen to point to the same display by
default. Redirection can move one without moving the other.

</details>

---

**Q3.**
What does `2>&1` mean in descriptor terms?

<details>
<summary><strong>A3.</strong></summary>

It makes FD 2 point to the same destination that FD 1 points to at that point
in the redirection order.

</details>

---

**Q4.**
Why is redirection best analyzed as a graph?

<details>
<summary><strong>A4.</strong></summary>

Because the important question is which process descriptor points to which
kernel object or file. The graph makes stream destinations and ordering
effects explicit.

</details>

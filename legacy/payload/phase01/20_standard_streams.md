# Standard Streams

## Core Streams

Processes normally begin with:

| FD | Name | Purpose |
|---|---|---|
| `0` | stdin | Input |
| `1` | stdout | Normal output |
| `2` | stderr | Diagnostic output |

A file descriptor is an integer reference in a process's descriptor table.
It may point to a file, terminal, socket, pipe, or another kernel object.

## Default Terminal Flow

```text
terminal keyboard -> process FD 0
process FD 1      -> terminal display
process FD 2      -> terminal display
```

Sharing a display does not merge stdout and stderr.

## Rewiring

```sh
command <input.txt
command >output.txt
command 2>errors.txt
producer | consumer
```

The shell rewires descriptors before executing the process.

## Buffering

Programs may buffer output differently depending on whether the destination
is a terminal, file, or pipe. This can change when output becomes visible
without changing which stream is used.

## Review

1. Standard streams are conventional process I/O channels.
2. File descriptors are process-local references.
3. Redirection changes descriptor targets.
4. A pipe links descriptors across processes.
5. Visible output timing may be affected by buffering.

# QA

**Q1.**
What are the three standard streams?

<details>
<summary><strong>A1.</strong></summary>

They are stdin on FD 0, stdout on FD 1, and stderr on FD 2.

</details>

---

**Q2.**
Why does sharing the terminal not merge stdout and stderr?

<details>
<summary><strong>A2.</strong></summary>

They are separate descriptors that may point to the same terminal. The shared
destination does not make the streams identical.

</details>

---

**Q3.**
When does the shell rewire descriptors?

<details>
<summary><strong>A3.</strong></summary>

The shell rewires descriptors before executing the target process, based on
redirection and pipeline syntax.

</details>

---

**Q4.**
Why can buffering change what the user observes?

<details>
<summary><strong>A4.</strong></summary>

Programs may buffer output differently for terminals, files, and pipes. This
can change when output becomes visible without changing which stream is used.

</details>

# Pipe Data Flow

## Producer and Consumer

```sh
echo hello | cat
```

The shell connects:

```text
echo stdout (FD 1)
-> pipe
-> cat stdin (FD 0)
```

`echo` and `cat` do not communicate through shell variables or command
arguments. They exchange bytes through a kernel pipe.

## Endpoints

A pipe has:

- a write end
- a read end

The shell assigns the relevant ends to process descriptors and closes unused
copies. EOF reaches the reader after all write ends are closed.

## Flow Control

Pipe capacity is finite:

- a fast producer may block when the pipe is full
- a consumer may block while waiting for input
- closing the reader can cause the writer to receive `SIGPIPE`

## Stream Selection

Only stdout enters a normal pipe:

```sh
command | consumer
```

Include stderr explicitly:

```sh
command 2>&1 | consumer
```

## Review

1. `|` creates a data-flow edge.
2. It links producer FD 1 to consumer FD 0.
3. The kernel transports bytes between processes.
4. Descriptor closure determines EOF behavior.
5. Pipe backpressure coordinates producer and consumer speed.

# QA

**Q1.**
What actually moves through a pipe?

<details>
<summary><strong>A1.</strong></summary>

Bytes move through a kernel pipe. The producer and consumer do not exchange
shell variables or command arguments.

</details>

---

**Q2.**
What descriptors are normally connected by `producer | consumer`?

<details>
<summary><strong>A2.</strong></summary>

The producer's stdout, FD 1, is connected to the consumer's stdin, FD 0.

</details>

---

**Q3.**
Why does closing unused pipe ends matter?

<details>
<summary><strong>A3.</strong></summary>

EOF reaches the reader only after all write ends are closed. Extra open
copies can keep the reader waiting unexpectedly.

</details>

---

**Q4.**
What can happen if the reader closes while the writer still writes?

<details>
<summary><strong>A4.</strong></summary>

The writer can receive `SIGPIPE` or get a broken-pipe error because the read
side of the pipe is gone.

</details>

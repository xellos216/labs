# Pipe Basics

## Core Model

A pipe connects one process's stdout to another process's stdin:

```sh
echo hello | cat
```

```text
echo FD 1
-> pipe write end
-> pipe read end
-> cat FD 0
```

The `|` token is parser syntax, not an argument passed to either command.

## Pipe Versus File Redirection

```sh
echo hello > output.txt
echo hello | cat
```

Both replace the stdout destination of `echo`.

- File redirection targets a file.
- A pipe targets another process's stdin.

## Process Setup

The shell generally:

1. Creates the pipe.
2. Creates processes for pipeline commands.
3. Rewires their descriptors.
4. Closes unused pipe ends.
5. Starts execution.

## Commands That Ignore Stdin

```sh
ping -c 1 localhost | whoami
```

The pipe is created, but `whoami` does not need stdin. The upstream output
may therefore be unread and discarded after the pipe closes.

## Stderr

An ordinary pipe carries stdout only:

```sh
command | consumer
```

Redirect stderr first when both streams should enter the pipe:

```sh
command 2>&1 | consumer
```

## Review

1. A pipe is a kernel data channel.
2. It links FD 1 of the producer to FD 0 of the consumer.
3. Pipeline commands normally run as separate processes.
4. Stderr is not piped unless explicitly redirected.
5. Parser syntax determines the process and descriptor graph.

# QA

**Q1.**
What descriptor connection does a normal pipe create?

<details>
<summary><strong>A1.</strong></summary>

It connects the producer's stdout, FD 1, to the consumer's stdin, FD 0,
through a kernel pipe.

</details>

---

**Q2.**
Why is `|` not visible to either command as an argument?

<details>
<summary><strong>A2.</strong></summary>

`|` is shell parser syntax. The shell uses it to construct a pipeline and
does not include it in either command's argv.

</details>

---

**Q3.**
What happens if the consumer ignores stdin?

<details>
<summary><strong>A3.</strong></summary>

The pipe may still be created, but the consumer does not read the data. The
producer's output can become unread and may be discarded or trigger pipe
closure behavior.

</details>

---

**Q4.**
How can stderr be included in a pipe?

<details>
<summary><strong>A4.</strong></summary>

Redirect stderr to stdout before the pipe, for example `command 2>&1 |
consumer`.

</details>

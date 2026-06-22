# Process Lifecycle

## External Command Execution

A Unix shell commonly executes an external program through a flow similar to:

```text
parse command
-> fork child
-> configure descriptors and environment
-> exec program
-> parent waits or continues
-> collect exit status
```

Implementation details vary, but the process distinction is fundamental.

## Fork

`fork()` creates a child process based on the parent:

- inherited environment
- inherited open descriptors
- inherited working directory
- separate process identity and mutable state

## Exec

An `exec` function replaces the current process image with a new program. The
PID normally remains the same across the replacement.

## Wait and Exit

The child terminates with an exit status. A foreground shell waits and records
that status:

```sh
command
echo "$?"
```

If the parent never reaps a terminated child, the child remains a zombie
entry until collected.

## Review

1. `fork` creates a new process.
2. `exec` replaces a process image.
3. The child inherits state but later changes are isolated.
4. The parent commonly waits for foreground work.
5. Exit status connects child completion to shell control flow.

# QA

**Q1.**
What is the usual shell flow for running an external command?

<details>
<summary><strong>A1.</strong></summary>

The shell parses the command, forks a child, configures descriptors and
environment, execs the program in the child, and then waits or continues
depending on foreground or background execution.

</details>

---

**Q2.**
What does `fork()` create?

<details>
<summary><strong>A2.</strong></summary>

It creates a child process based on the parent, with inherited state such as
environment, descriptors, and working directory, but separate mutable state
afterward.

</details>

---

**Q3.**
What does `exec` change?

<details>
<summary><strong>A3.</strong></summary>

It replaces the current process image with a new program. The PID normally
remains the same across that replacement.

</details>

---

**Q4.**
Why does a zombie process exist?

<details>
<summary><strong>A4.</strong></summary>

A terminated child remains as a zombie entry until its parent collects its
exit status with a wait operation.

</details>

# Job Control

## Foreground and Background

Foreground execution:

```sh
sleep 10
```

The shell waits before returning the prompt.

Background execution:

```sh
sleep 10 &
```

The shell starts the job and returns the prompt without an immediate wait.

## Jobs

A shell job may contain one process or an entire pipeline.

```sh
jobs
fg %1
bg %1
```

Job identifiers are shell-level objects and are different from kernel PIDs.

## Terminal Control

The foreground process group owns normal terminal input. Background jobs that
try to read from the terminal may be stopped.

Common interactive controls:

```text
Ctrl-C -> SIGINT to foreground process group
Ctrl-Z -> SIGTSTP to foreground process group
```

## Output Ordering

Background jobs can write while the shell or other jobs are also writing, so
output may be interleaved.

## Review

1. `&` requests background execution.
2. The shell does not immediately wait for a background job.
3. A job can represent a pipeline process group.
4. Foreground ownership controls terminal interaction.
5. Concurrency makes output ordering nondeterministic.

# QA

**Q1.**
What does `&` request from the shell?

<details>
<summary><strong>A1.</strong></summary>

It requests background execution. The shell starts the job and returns the
prompt without immediately waiting for it to finish.

</details>

---

**Q2.**
How is a shell job different from a PID?

<details>
<summary><strong>A2.</strong></summary>

A job is a shell-level object that may represent one process or a whole
pipeline. A PID identifies one kernel process.

</details>

---

**Q3.**
Why can a background job be stopped when it reads from the terminal?

<details>
<summary><strong>A3.</strong></summary>

Normal terminal input belongs to the foreground process group. A background
job that tries to read from it may be stopped by job-control behavior.

</details>

---

**Q4.**
Why can background output appear mixed with the prompt?

<details>
<summary><strong>A4.</strong></summary>

The shell and background jobs run concurrently and may write to the same
terminal, so output ordering is not deterministic.

</details>

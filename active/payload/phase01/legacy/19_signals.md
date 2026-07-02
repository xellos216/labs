# Signals

## Definition

A signal is an asynchronous control notification delivered to a process or
process group by the kernel.

```sh
kill -TERM <pid>
kill -KILL <pid>
```

`kill` sends signals; it does not always terminate a process.

## Common Signals

| Signal | Typical meaning |
|---|---|
| `SIGINT` | Interactive interrupt |
| `SIGTERM` | Request graceful termination |
| `SIGKILL` | Immediate kernel termination |
| `SIGSTOP` | Uncatchable stop |
| `SIGCONT` | Continue a stopped process |
| `SIGHUP` | Terminal loss or reload convention |

## Handling

A process may:

- accept the default action
- ignore some signals
- install a handler

`SIGKILL` and `SIGSTOP` cannot be caught or ignored.

## Process Groups

Interactive shells send terminal-generated signals to the foreground process
group, allowing a whole pipeline to be interrupted together.

## Review

1. Signals carry control events, not ordinary stream data.
2. The kernel identifies targets by PID or process group.
3. `SIGTERM` allows cleanup; `SIGKILL` does not.
4. Signal delivery and final process behavior are separate.
5. Job control relies on signals and process groups.

# QA

**Q1.**
What kind of information does a signal carry?

<details>
<summary><strong>A1.</strong></summary>

A signal carries an asynchronous control event, not ordinary stdin, stdout,
or stderr data.

</details>

---

**Q2.**
Why does `kill` not always mean a process will terminate?

<details>
<summary><strong>A2.</strong></summary>

`kill` sends a signal. The target may handle, ignore, or default-handle that
signal, depending on the signal and process behavior.

</details>

---

**Q3.**
Why is `SIGTERM` different from `SIGKILL`?

<details>
<summary><strong>A3.</strong></summary>

`SIGTERM` requests graceful termination and can allow cleanup. `SIGKILL` is
forced by the kernel and cannot be caught or ignored.

</details>

---

**Q4.**
Why do interactive shells signal a process group?

<details>
<summary><strong>A4.</strong></summary>

A foreground job may be a pipeline with multiple processes. Signaling the
foreground process group lets terminal actions affect the whole job.

</details>

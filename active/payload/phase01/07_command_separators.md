# Session 07 — Command Separators

## Metadata

```yaml
Roadmap: Payload Construction & Parser Reasoning
Phase: 01
Session: 07
Title: Command Separators
Status:
Review:
ArchiveVersion: 2
Date:
```

## Exit Status

Every command returns an integer status:

```sh
true
echo "$?"   # 0

false
echo "$?"   # nonzero
```

Convention:

```text
0       -> success
nonzero -> failure or another condition
```

Exit status is independent of visible stdout or stderr.

## Conditional Operators

```sh
cmd1 && cmd2
```

Run `cmd2` only when `cmd1` succeeds.

```sh
cmd1 || cmd2
```

Run `cmd2` only when `cmd1` fails.

```sh
cmd1 ; cmd2
```

Run `cmd2` regardless of `cmd1`'s status.

## Lists

```sh
test -f config && echo found || echo missing
```

This is concise but is not always equivalent to a full `if` statement. If
the middle command fails, the final `||` branch can run.

## Injection Relevance

The choice of separator changes execution conditions:

```text
;  unconditional next command
&& next command after success
|| next command after failure
```

## Review

1. `$?` reports the most recent foreground pipeline's status.
2. Success does not require visible output.
3. Failure does not require stderr.
4. `&&` and `||` create status-dependent control flow.
5. Parser structure and process result are separate layers.

# Review Questions

### Q1. What does exit status `0` conventionally mean?

<details>
<summary>A</summary>

It conventionally means success. A nonzero status indicates failure or some
other command-specific condition.

</details>

---

### Q2. How does `cmd1 && cmd2` decide whether to run `cmd2`?

<details>
<summary>A</summary>

`cmd2` runs only if `cmd1` exits successfully with status `0`.

</details>

---

### Q3. How does `cmd1 || cmd2` decide whether to run `cmd2`?

<details>
<summary>A</summary>

`cmd2` runs only if `cmd1` exits with a nonzero status.

</details>

---

### Q4. Why is `a && b || c` not always the same as a full `if` statement?

<details>
<summary>A</summary>

If `a` succeeds but `b` fails, the `|| c` branch can still run. The status of
the middle command participates in the list.

</details>

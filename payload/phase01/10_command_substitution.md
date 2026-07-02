# Session 10 — Command Substitution

## Metadata

```yaml
Roadmap: Payload Construction & Parser Reasoning
Phase: 01
Session: 10
Title: Command Substitution
Status:
Review:
ArchiveVersion: 2
Date:
```

## Core Model

Command substitution runs an inner command before the outer command:

```sh
echo "$(whoami)"
```

```text
parse substitution
-> execute inner command
-> capture stdout
-> remove trailing newlines
-> insert result
-> execute outer command
```

Both forms perform substitution:

```sh
$(command)
`command`
```

Prefer `$(...)` because it is easier to read and nest.

## Token Boundaries

Substitution does not automatically create a new argument:

```sh
echo$(whoami)
```

If `whoami` prints `alice`, the resulting token may be:

```text
echoalice
```

Use an explicit boundary when a separate argument is required:

```sh
echo "$(whoami)"
```

## Quote Behavior

```sh
'$(id)'   # literal text
"$(id)"   # command substitution executes
```

Single quotes suppress substitution. Double quotes preserve substitution but
keep the resulting text in one argument.

## Output Versus Side Effect

Substitution captures stdout, but the inner command may also have side
effects. Stderr is not captured unless redirected.

```sh
value=$(command 2>&1)
```

## Injection Context

In vulnerable shell construction, a value such as `$(id)` can execute even
when command separators are blocked, provided the parser reaches a context
where substitution is active.

Always track:

```text
HTTP decoding
-> application string construction
-> shell quote state
-> expansion
-> final execution
```

## Review

1. Command substitution is processed before the outer command executes.
2. Its stdout is inserted at the original position.
3. Quote state determines whether substitution is active.
4. Inserted output may join an existing token.
5. Execution and visible output are separate observations.

# Review Questions

### Q1. When does command substitution run relative to the outer command?

<details>
<summary>A</summary>

It runs before the outer command executes. The shell executes the inner
command, captures its stdout, inserts that text, and then continues building
the outer command.

</details>

---

### Q2. Why can `echo$(whoami)` become a different command name?

<details>
<summary>A</summary>

Command substitution does not automatically create an argument boundary. If
`whoami` prints `alice`, the source can become one token such as
`echoalice`.

</details>

---

### Q3. Why does `'$(id)'` not execute while `"$(id)"` does?

<details>
<summary>A</summary>

Single quotes protect the text literally and suppress substitution. Double
quotes still allow command substitution, while keeping the substituted result
inside one argument.

</details>

---

### Q4. What stream is captured by command substitution by default?

<details>
<summary>A</summary>

Only stdout is captured by default. Stderr remains separate unless it is
explicitly redirected, for example with `2>&1`.

</details>

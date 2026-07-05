# Session 09 — Variable Expansion

## Metadata

```yaml
Roadmap: Payload Construction & Parser Reasoning
Phase: 01
Session: 09
Title: Variable Expansion
Status:
Review:
ArchiveVersion: 2
Date:
```

## Shell Variables and Environment

A shell variable exists in the current shell:

```sh
NAME=alice
```

It becomes part of the process environment after export:

```sh
export NAME
```

or:

```sh
export NAME=alice
```

## Child Inheritance

Child processes inherit a copy of the parent's environment:

```sh
export TEST=value
sh -c 'printf "%s\n" "$TEST"'
```

Changes made by the child do not propagate back to the parent.

## Per-Command Assignment

```sh
MODE=test command
```

This adds `MODE=test` to the environment of that command without permanently
exporting it in the current shell.

## Inspection

```sh
env
printenv
printf '%s\n' "$PATH"
```

Do not print secrets casually; environments can contain credentials or
tokens.

## Security Relevance

Environment variables influence:

- executable lookup through `PATH`
- locale and parser behavior
- library loading
- configuration and credentials

Privileged programs should construct a controlled environment instead of
trusting arbitrary inherited values.

## Review

1. A shell variable is not automatically exported.
2. `export` includes a variable in future child environments.
3. Children inherit copies, not shared mutable state.
4. Per-command assignments have limited scope.
5. Environment data crosses a process trust boundary.

# Review Questions

### Q1. When does a shell variable become part of a child process environment?

<details>
<summary>A</summary>

After it is exported. A plain shell variable stays in the current shell unless
`export` marks it for inheritance by future child processes.

</details>

---

### Q2. Why do child changes not propagate back to the parent shell?

<details>
<summary>A</summary>

The child inherits a copy of the environment. Mutating that copy does not
modify the parent's shell state.

</details>

---

### Q3. What is the scope of `MODE=test command`?

<details>
<summary>A</summary>

`MODE=test` is placed in the environment for that command invocation. It does
not permanently export `MODE` in the current shell.

</details>

---

### Q4. Why are environment variables security-relevant?

<details>
<summary>A</summary>

They can influence command lookup, locale behavior, library loading,
configuration, and credentials. Inherited environment values cross a process
trust boundary.

</details>

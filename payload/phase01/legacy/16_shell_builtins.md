# Shell Builtins

## Definition

A builtin executes inside the shell process rather than as a separate
external executable.

Inspect commands with:

```sh
type cd
type printf
type /bin/pwd
```

## Why Builtins Exist

Some operations must change the current shell's state:

```sh
cd /tmp
export NAME=value
unset NAME
alias ll='ls -l'
```

An external child process cannot change its parent's working directory or
environment.

## Builtin Versus External Command

Some names have both forms:

```sh
printf
/usr/bin/printf
```

Their options or behavior may differ.

Force builtin or external-style resolution with:

```sh
builtin printf '%s\n' test
command printf '%s\n' test
```

## Subshell Effect

```sh
(cd /tmp; pwd)
pwd
```

`cd` changes the subshell's state, not the parent shell's state.

## Review

1. Builtins run in the shell's execution context.
2. State-changing commands must affect the current shell.
3. External children cannot directly mutate parent state.
4. The same command name may have builtin and external implementations.
5. Resolution and process context determine persistent effects.

# QA

**Q1.**
What makes a command a shell builtin?

<details>
<summary><strong>A1.</strong></summary>

A builtin is implemented by the shell and executes in the shell process
context instead of requiring a separate external executable.

</details>

---

**Q2.**
Why must commands like `cd` and `export` be builtins?

<details>
<summary><strong>A2.</strong></summary>

They need to change the current shell's state. An external child process
cannot directly change its parent's working directory or environment.

</details>

---

**Q3.**
Why can `printf` and `/usr/bin/printf` behave differently?

<details>
<summary><strong>A3.</strong></summary>

One may be a shell builtin and the other an external program. Their options,
edge cases, or implementation details may differ.

</details>

---

**Q4.**
Why does `cd` inside `( ... )` not persist?

<details>
<summary><strong>A4.</strong></summary>

The parentheses create a subshell context. `cd` changes that subshell's
directory, not the parent shell's directory.

</details>

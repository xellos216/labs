# Subshells

## Core Model

Parentheses create a subshell environment:

```sh
(cd /tmp; pwd)
pwd
```

The directory change occurs in the child environment and does not change the
parent shell's working directory.

## State Isolation

```sh
VAR=outer
(VAR=inner; echo "$VAR")
echo "$VAR"
```

Output:

```text
inner
outer
```

The child begins with inherited state, then modifies its own copy.

## Grouping Without a Subshell

```sh
{ cd /tmp; pwd; }
```

Brace grouping runs in the current shell. Required syntax includes spaces and
a terminating semicolon or newline.

## Command Substitution

```sh
value=$(pwd)
```

Command substitution also executes in a subshell-like environment and
captures stdout.

## Process Perspective

```text
parent shell
-> create child execution environment
-> run grouped commands
-> collect status/output
-> parent state remains
```

## Review

1. `( ... )` creates process-state isolation.
2. Child changes to variables and cwd do not normally persist in the parent.
3. `{ ...; }` groups commands without that isolation.
4. Subshell stdout and exit status can still affect the parent.
5. Distinguish process state from textual grouping.

# QA

**Q1.**
Why does `(cd /tmp; pwd)` not change the parent shell's directory?

<details>
<summary><strong>A1.</strong></summary>

The parentheses create a subshell environment. `cd` changes that child
environment, and the parent shell keeps its original working directory.

</details>

---

**Q2.**
How is `{ cd /tmp; pwd; }` different from `(cd /tmp; pwd)`?

<details>
<summary><strong>A2.</strong></summary>

Brace grouping runs in the current shell context, while parentheses create
subshell state isolation.

</details>

---

**Q3.**
What state does a child environment inherit?

<details>
<summary><strong>A3.</strong></summary>

It starts with inherited state such as variables, environment, working
directory, and file descriptors, but later mutations are isolated from the
parent.

</details>

---

**Q4.**
How can a subshell still affect the parent command line?

<details>
<summary><strong>A4.</strong></summary>

Its stdout and exit status can be observed by the parent shell, for example
through command substitution or conditional execution.

</details>

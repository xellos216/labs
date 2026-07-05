# Redirection Parsing

## Core Model

Redirection operators are shell syntax, not ordinary command arguments.

```sh
echo hello > output.txt
```

The shell:

1. Parses `>`.
2. Opens `output.txt`.
3. Connects stdout to that file.
4. Executes `echo` with only `hello` as its user argument.

## Common Operators

| Syntax | Effect |
|---|---|
| `> file` | Replace file with stdout |
| `>> file` | Append stdout |
| `< file` | Read stdin from file |
| `2> file` | Redirect stderr |
| `2>&1` | Point stderr at stdout's current target |

## No-Space Forms

Whitespace is not required around redirection syntax:

```sh
echo hello>output.txt
cat</etc/passwd
```

The lexer recognizes the operator boundary.

## Ordering Matters

```sh
command >out 2>&1
```

Both stdout and stderr go to `out`.

```sh
command 2>&1 >out
```

Stderr first points to the old stdout target; stdout is then redirected to
`out`. The destinations can differ.

## Observation Checklist

```text
Which descriptor changes?
What is its new target?
When is the target opened?
Which redirections are applied first?
What argv reaches the process?
```

## Review

1. Redirection is parsed before process execution.
2. Operators are removed from the process argument list.
3. Redirection changes data flow, not merely text.
4. `cat</etc/passwd` works without reconstructing `cat /etc/passwd`.
5. Left-to-right ordering affects descriptor duplication.

# QA

**Q1.**
Why is `>` not passed as an ordinary argument to `echo`?

<details>
<summary><strong>A1.</strong></summary>

`>` is shell syntax. The shell consumes it while building the execution plan,
opens the target file, rewires stdout, and removes the operator from argv.

</details>

---

**Q2.**
Why can `cat</etc/passwd` work without spaces?

<details>
<summary><strong>A2.</strong></summary>

The shell lexer can recognize redirection operators at token boundaries even
without surrounding whitespace. The operator is syntax, not part of the
filename argument.

</details>

---

**Q3.**
Why do `command >out 2>&1` and `command 2>&1 >out` differ?

<details>
<summary><strong>A3.</strong></summary>

Redirections are applied left to right. `2>&1` duplicates FD 1's current
target at that moment, so changing FD 1 before or after the duplication can
produce different descriptor graphs.

</details>

---

**Q4.**
What should be tracked when analyzing a redirection?

<details>
<summary><strong>A4.</strong></summary>

Track which descriptor changes, what it points to after the change, when the
target is opened, and which argv remains after shell syntax is removed.

</details>

# Session 11 — Globbing and Filename Expansion

## Metadata

```yaml
Roadmap: Payload Construction & Parser Reasoning
Phase: 01
Session: 11
Title: Globbing and Filename Expansion
Status:
Review:
ArchiveVersion: 2
Date:
```

## Core Model

Globbing is pathname expansion performed by the shell before program
execution.

```sh
printf '%s\n' *.txt
```

The program receives matching filenames, not the literal `*.txt`, when
matches exist.

## Common Patterns

| Pattern | Meaning |
|---|---|
| `*` | Any string |
| `?` | One character |
| `[abc]` | One listed character |
| `[a-z]` | One character in a range |

## Quoting

```sh
echo *.txt    # expanded
echo "*.txt"  # literal
echo \*.txt   # literal
```

## No-Match Behavior

Behavior depends on the shell and options:

- Bash normally leaves the pattern literal.
- `nullglob` removes unmatched patterns.
- `failglob` reports an error.
- zsh commonly reports no matches unless configured otherwise.

## Security Relevance

Attacker-controlled filenames can become arguments after expansion. Filenames
beginning with `-` may then be interpreted as options by a command.

Safer patterns include:

```sh
command -- ./*
```

## Review

1. `*` is parser syntax until quoting makes it literal.
2. Expansion occurs before execution.
3. Matches become separate argv entries.
4. No-match behavior is shell-specific.
5. Pathname expansion can alter command meaning and option parsing.

# Review Questions

### Q1. Who expands `*.txt`, the shell or the program?

<details>
<summary>A</summary>

The shell expands it before program execution. The program normally receives
matching pathnames, not the literal pattern.

</details>

---

### Q2. How can `*.txt` be passed literally?

<details>
<summary>A</summary>

Quote or escape the glob metacharacter, for example `"*.txt"` or `\*.txt`.

</details>

---

### Q3. Why does no-match behavior matter?

<details>
<summary>A</summary>

Different shells and options handle unmatched patterns differently. The
pattern may remain literal, disappear, or raise an error.

</details>

---

### Q4. Why can attacker-controlled filenames affect command meaning?

<details>
<summary>A</summary>

Expanded filenames become argv entries. A filename beginning with `-` can be
interpreted as an option unless the command is protected with patterns such
as `-- ./...`.

</details>

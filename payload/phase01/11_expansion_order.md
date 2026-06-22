# Expansion Order

## Core Model

The shell transforms source text before executing a command.

A useful simplified sequence is:

```text
parse shell syntax
-> parameter, command, and arithmetic expansion
-> field splitting
-> pathname expansion
-> quote removal
-> redirection setup
-> execution
```

Exact shell rules are context-dependent, but execution happens after the
relevant expansions.

## Parameter Expansion

```sh
NAME=alice
echo "$NAME"
```

The value is inserted before `echo` runs.

## Command Substitution

```sh
echo "$(whoami)"
```

The inner command runs first, and its stdout is reinserted into the outer
command.

## Field Splitting

Unquoted expansion may create multiple fields:

```sh
VALUE='one two'
printf '<%s>\n' $VALUE
```

Quoted expansion remains one argument:

```sh
printf '<%s>\n' "$VALUE"
```

## Pathname Expansion

After eligible field splitting, glob patterns may expand into matching
pathnames:

```sh
printf '%s\n' *.txt
```

## Review

1. Expansion occurs before command execution.
2. Quote context controls later splitting and globbing.
3. Substitution output is reinserted into the command.
4. The final argv may differ significantly from the source text.
5. Analyze intermediate parser states rather than only the typed command.

# QA

**Q1.**
Why can final argv differ from the command text the user typed?

<details>
<summary><strong>A1.</strong></summary>

The shell expands variables and substitutions, may split fields, may expand
globs, removes quotes, and then executes the resulting command.

</details>

---

**Q2.**
Why does quoting affect field splitting and globbing?

<details>
<summary><strong>A2.</strong></summary>

Quote context marks text as protected. Quoted expansion stays one argument
and does not undergo the same later splitting and pathname expansion.

</details>

---

**Q3.**
When does command substitution output become part of the outer command?

<details>
<summary><strong>A3.</strong></summary>

The inner command runs during expansion. Its stdout is reinserted before the
outer command is executed.

</details>

---

**Q4.**
Why is it useful to analyze intermediate parser states?

<details>
<summary><strong>A4.</strong></summary>

Intermediate states show where text changes meaning: variable values appear,
fields split, globs expand, and operators are separated from argv.

</details>

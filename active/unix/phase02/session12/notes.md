# Session12 Notes

## Core Idea

Globbing is performed by the shell before the command runs.

`find` performs filesystem traversal itself.

This session focused on distinguishing:

```text
Shell
→ pathname expansion
```

from:

```text
find
→ filesystem search
```

---

## Task1

Run:

```bash
*.log
```

Observed result in zsh:

```text
zsh: no matches found: *.log
```

Meaning:

```text
Shell tried to expand *.log
→ no matching file existed in the current directory
→ zsh returned an error
→ no command was executed
```

Pattern:

```text
unquoted glob
→ shell expansion
```

---

## Task2

Compare:

```bash
echo *.log
```

and:

```bash
find . -name "*.log"
```

Difference:

```text
echo *.log
```

```text
Shell interprets *.log first
→ matching filenames are passed to echo
```

```text
find . -name "*.log"
```

```text
Shell preserves "*.log"
→ find receives the pattern
→ find performs matching
```

Pattern:

```text
unquoted glob
→ shell expansion
```

```text
quoted pattern
→ passed to program
```

---

## Task3

Run:

```bash
echo logs/*.log
```

Output:

```text
logs/access.log logs/debug.log logs/error.log
```

Explanation:

```text
Shell expands logs/*.log before echo runs.
```

`echo` does not search for files.

It only receives arguments that the shell already expanded.

Pattern:

```text
directory-specific glob
→ pathname expansion
→ command arguments
```

---

## Task4

Run:

```bash
echo app/*
```

Output:

```text
app/config.py app/main.py app/readme.md
```

Meaning:

```text
* expands to all matching pathnames inside app/
```

Pattern:

```text
directory/*
→ all entries directly inside directory
```

---

## Task5

Compare:

```bash
echo logs/*.log
```

and:

```bash
find logs -name "*.log"
```

| Item | `echo logs/*.log` | `find logs -name "*.log"` |
|---|---|---|
| Interpreter | Shell | find |
| Pattern handling | Shell expands before command runs | find receives pattern and matches files |
| Recursion | No | Yes |
| Scope | Direct path pattern | Filesystem traversal |
| Best use | Simple known path matching | Recursive search and filtering |

---

## Notes

### Shell Globbing

Globbing means:

```text
Shell pattern
→ matching pathnames
```

Example:

```bash
echo logs/*.log
```

Shell converts this into something like:

```bash
echo logs/access.log logs/debug.log logs/error.log
```

before `echo` executes.

---

### `*`

`*` means:

```text
match zero or more characters in one pathname component
```

Example:

```bash
logs/*.log
```

Matches:

```text
logs/access.log
logs/debug.log
logs/error.log
```

Does not recursively search deeper directories by default.

---

### zsh No-Match Behavior

In zsh, when a glob pattern matches nothing:

```bash
echo *.log
```

may produce:

```text
zsh: no matches found: *.log
```

This means:

```text
The shell failed before the command received arguments.
```

This is different from `find`, where the command runs and simply returns no matching paths.

---

### Quoting Prevents Shell Expansion

Unquoted:

```bash
find . -name *.log
```

Risk:

```text
Shell may expand *.log before find sees it.
```

Quoted:

```bash
find . -name "*.log"
```

Correct:

```text
Shell passes *.log literally to find.
find performs the matching.
```

Pattern:

```text
quote patterns when the target program should interpret them
```

---

### Glob vs find

Use glob when:

```text
files are in a known location
matching is simple
recursion is not needed
```

Example:

```bash
cat logs/*.log
```

Use `find` when:

```text
recursive search is needed
conditions are needed
metadata filtering is needed
batch processing is needed
```

Example:

```bash
find logs -name "*.log"
```

---

## Common Patterns

```text
Shell glob
→ command arguments
```

```text
directory/*.ext
→ match files directly under directory
```

```text
find path -name "*.ext"
→ recursive search
```

```text
quoted pattern
→ program interprets pattern
```

```text
unquoted pattern
→ shell interprets pattern
```

---

## Mental Model

Command line processing happens in stages.

```text
You type command

↓

Shell parses command line

↓

Shell expands globs

↓

Command receives final arguments

↓

Command executes
```

For glob:

```text
logs/*.log

↓

Shell

↓

logs/access.log logs/debug.log logs/error.log

↓

echo receives arguments
```

For find:

```text
find logs -name "*.log"

↓

Shell preserves "*.log"

↓

find receives pattern

↓

find searches filesystem
```

Most important takeaway:

```text
A glob is not interpreted by the command.

It is usually interpreted by the shell before the command starts.
```

The key question is:

```text
Who should interpret the pattern?

Shell
or
the program?
```

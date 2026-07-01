# Session13 Notes

## Core Idea

Recursive text replacement should be done in three stages.

```text
inspect
→ replace
→ verify
```

The important point is not `sed -i` alone.

The important point is controlling the target files before modifying them.

---

## Task1

Print files containing `dev`

```bash
find . -type f -exec grep -l "dev" {} +
```

Pattern:

```text
find
→ all files
→ grep matching files
```

`grep -l` prints only filenames that contain the matched string.

---

## Task2

Print only `ENV=dev` lines from `.conf` files

```bash
find . -type f -name "*.conf" -exec grep -H "ENV=dev" {} +
```

Pattern:

```text
find
→ select .conf files
→ inspect matching lines
```

`grep -H` prints the filename with the matching line.

Example output:

```text
./app/main.conf:ENV=dev
./app/worker.conf:ENV=dev
./config/service.conf:ENV=dev
```

---

## Task3

Replace `ENV=dev` with `ENV=prod` only in `.conf` files

```bash
find . -type f -name "*.conf" -exec sed -i 's/ENV=dev/ENV=prod/' {} +
```

Pattern:

```text
find
→ select target files
→ sed -i replacement
```

Important constraint:

```text
Only .conf files should be modified.
```

Document files such as `.md` and `.txt` should not be changed.

---

## Task4

Verify `.conf` files were changed

```bash
find . -type f -name "*.conf" -exec grep -H "ENV=prod" {} +
```

Also verify document files still contain `dev`

```bash
find . -type f \( -name "*.txt" -o -name "*.md" \) -exec grep -H "dev" {} +
```

Pattern:

```text
verify changed files
+
verify untouched files
```

A safe replacement workflow checks both:

```text
what changed
```

and:

```text
what should not have changed
```

---

## Task5

Inspect all files containing `debug`

```bash
find . -type f -exec grep -H "debug" {} +
```

Replace `LOG_LEVEL=debug` with `LOG_LEVEL=info` only in `.conf` files

```bash
find . -type f -name "*.conf" -exec sed -i 's/LOG_LEVEL=debug/LOG_LEVEL=info/' {} +
```

Verify `.conf` files changed

```bash
find . -type f -name "*.conf" -exec grep -H "LOG_LEVEL=info" {} +
```

Verify document files still contain `debug`

```bash
find . -type f \( -name "*.txt" -o -name "*.md" \) -exec grep -H "debug" {} +
```

Pattern:

```text
inspect
→ replace selected files
→ verify modified files
→ verify excluded files
```

---

## Notes

### `sed -i`

`sed -i` edits files in place.

Example:

```bash
sed -i 's/OLD/NEW/' file
```

Meaning:

```text
replace OLD with NEW inside file
and save the change to the same file
```

Because it modifies files directly, it should usually be preceded by inspection.

---

### Safe Replacement Pattern

Before replacing:

```bash
find . -type f -name "*.conf" -exec grep -H "TARGET" {} +
```

Replace:

```bash
find . -type f -name "*.conf" -exec sed -i 's/OLD/NEW/' {} +
```

After replacing:

```bash
find . -type f -name "*.conf" -exec grep -H "NEW" {} +
```

Then verify excluded files if needed:

```bash
find . -type f \( -name "*.txt" -o -name "*.md" \) -exec grep -H "OLD" {} +
```

---

### Why Group `-name` Conditions

Command:

```bash
find . -type f \( -name "*.txt" -o -name "*.md" \) -exec grep -H "debug" {} +
```

Logical meaning:

```text
-type f AND (name is *.txt OR name is *.md)
```

The parentheses group the two filename conditions into one unit.

Without grouping, the `-o` condition can change how the rest of the expression applies.

---

### Why `\(` and `\)` Are Escaped

Parentheses have meaning to the shell.

So they are escaped:

```bash
\(
\)
```

This prevents the shell from interpreting them first.

The escaped parentheses are passed to `find`.

---

### `-o`

`-o` means OR inside a `find` expression.

Example:

```bash
-name "*.txt" -o -name "*.md"
```

Meaning:

```text
name matches *.txt
OR
name matches *.md
```

Common grouped form:

```bash
\( -name "*.txt" -o -name "*.md" \)
```

---

## Common Mistake

Incorrect attempt:

```bash
find . -type f -exec grep -l "debug" {} + -exec sed -i 's/LOG_LEVEL=debug/LOG_LEVEL=info/' + find . -type f -exec grep -H "LOG_LEVEL=info" {} +
```

Problems:

```text
multiple find commands are incorrectly chained
```

```text
sed -i lacks {}
```

```text
target file type is not restricted
```

Correct approach:

```text
Do not force inspect, replace, and verify into one command.
Separate the workflow into clear stages.
```

---

## Common Patterns

```text
find
→ grep -l
```

```text
find
→ grep -H
```

```text
find
→ sed -i
```

```text
inspect
→ replace
→ verify
```

```text
target files
→ excluded files
```

```text
-type f AND (name A OR name B)
```

---

## Mental Model

Unsafe replacement:

```text
replace first
→ hope the target was correct
```

Safe replacement:

```text
find target files
→ inspect matching lines
→ replace only selected files
→ verify changed files
→ verify excluded files
```

Most important takeaway:

```text
Recursive replacement is a filesystem selection problem before it is a sed problem.
```

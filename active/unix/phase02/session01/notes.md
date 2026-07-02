# Session01 Notes

## Core Idea

`find` discovers files.

Most multi-file workflows follow:

```text
find
→ pass filenames
→ process contents
→ aggregate results
```

## Task1

Print all `.log` file paths

<details>
<summary><strong>Answer</strong></summary>

```bash
find . -name "*.log"
```

</details>

## Task2

Count all ERROR lines across log files

<details>
<summary><strong>Answer</strong></summary>

```bash
find . -name "*.log" | xargs cat | grep ERROR | wc -l
```

</details>

Pattern:

```text
find → merge contents → filter → count
```

## Task3

Print filenames containing ERROR

<details>
<summary><strong>Answer</strong></summary>

```bash
find . -name "*.log" -exec grep -l ERROR {} +
```

</details>

Pattern:

```text
find → content check → return filenames
```

## Task4

Count all `.tmp` files

<details>
<summary><strong>Answer</strong></summary>

```bash
find . -name "*.tmp" | wc -l
```

</details>

Pattern:

```text
find → count
```

## Task5

Count total lines across log files

<details>
<summary><strong>Answer</strong></summary>

```bash
find . -name "*.log" | xargs cat | wc -l
```

</details>

Pattern:

```text
find → merge contents → aggregate
```

## Notes

* `find` = recursive file discovery
* `-name "*.log"` = filename filtering
* `xargs` = convert stdin into command arguments
* `grep ERROR` = content filtering
* `grep -l ERROR` = print filenames containing matches
* `wc -l` = count lines
* `-exec command {} +` = run a command on many discovered files
* listing files and counting files are different operations
* matching lines and counting matches are different operations

### Basic Multi-file Workflow

```text
find
→ select files
→ process contents
→ summarize results
```

### Common Patterns

```text
find → count
```

```text
find → grep → count
```

```text
find → content check → filenames
```

```text
find → merge contents → aggregate
```

### Safer Form

```bash
find . -name "*.log" -print0 | xargs -0 grep ERROR
```

Reason:

```text
Handles filenames containing spaces safely.
```

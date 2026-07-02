# Session11 Notes

## Core Idea

`find` is not limited to discovering files.

It can also execute commands on matched files.

General workflow:

```text
find
→ match files
→ execute command
```

---

## Task1

Print all log files

```bash
find . -name "*.log"
```

Pattern:

```text
find
→ file discovery
```

---

## Task2

Copy all log files

```bash
find . -name "*.log" -exec cp {} backup/ \;
```

Pattern:

```text
find
→ file discovery
→ action
```

---

## Task3

Verify copied files

```bash
find backup -name "*.log"
```

Pattern:

```text
verification
```

---

## Task4

Move all text files

```bash
find . -name "*.txt" -exec mv {} archive/ \;
```

Pattern:

```text
find
→ action
```

---

## Task5

Compare `\;` and `+`

Single execution per file:

```bash
find . -exec COMMAND {} \;
```

Batch execution:

```bash
find . -exec COMMAND {} +
```

Pattern:

```text
find
→ action
```

---

## Notes

### Placeholder `{}`

`{}` is replaced by the pathname currently matched by `find`.

Example:

```bash
find . -name "*.log" -exec cp {} backup/ \;
```

Behaves like:

```text
cp file1 backup/
cp file2 backup/
cp file3 backup/
```

---

### `\;`

```bash
find . -exec COMMAND {} \;
```

Meaning:

```text
One command execution
per matched file.
```

Characteristics:

- One process per file
- Simple
- Less efficient for large numbers of files

---

### `+`

```bash
find . -exec COMMAND {} +
```

Meaning:

```text
Collect many matched files

↓

Execute one command
```

Example:

```bash
cp file1 file2 file3 backup/
```

Characteristics:

- Fewer processes
- Better performance
- Preferred when the command accepts multiple input files

---

### `\;` vs `+`

`\;`

```text
file1

↓

COMMAND

↓

file2

↓

COMMAND

↓

file3

↓

COMMAND
```

`+`

```text
file1
file2
file3

↓

COMMAND
```

---

### Observation

Copy:

```bash
cp
```

Result:

```text
Source remains
Destination receives a copy
```

Move:

```bash
mv
```

Result:

```text
Source disappears
Destination now owns the file
```

---

## Common Patterns

```text
find
→ discovery
```

```text
find
→ action
```

```text
find
→ action
→ verification
```

```text
find
→ one-file execution
```

```text
find
→ batch execution
```

---

## Mental Model

Until Session10:

```text
find

↓

Observe
```

Session11:

```text
find

↓

Modify
```

Current reasoning model:

```text
Which files?

↓

What action?

↓

Per file
or
Batch?

↓

Verify result
```

Most important takeaway:

```text
find is not only a search tool.

It is a batch-processing tool.
```

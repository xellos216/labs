# Session02 Notes

## Core Idea

Phase01 focused on processing fields inside a file.

Phase02 focuses on treating many files as a dataset.

```text
many files
→ discover
→ extract metadata
→ sort/filter
→ summarize
```

---

## Task1

Print all file paths

<details>
<summary><strong>Answer</strong></summary>

```bash
find . -type f
```

</details>

Pattern:

```text
find → discover files
```

---

## Task2

Count all `.log` files

<details>
<summary><strong>Answer</strong></summary>

```bash
find . -type f -name "*.log" | wc -l
```

</details>

Pattern:

```text
find → filter → count
```

---

## Task3

Print filenames only

<details>
<summary><strong>Answer</strong></summary>

```bash
find . -type f -name "*.log" | awk -F/ '{print $NF}'
```

</details>

Pattern:

```text
find → path processing → projection
```

Notes:

```text
$NF = last field
-F/ = split path by /
```

---

## Task4

Print file size and filename

<details>
<summary><strong>Answer</strong></summary>

```bash
find . -type f -exec stat -c "%s %n" {} \;
```

</details>

Pattern:

```text
find → metadata extraction
```

Notes:

```text
%s = file size (bytes)
%n = filename/path
```

---

## Task5

Print the largest file

<details>
<summary><strong>Answer</strong></summary>

```bash
find . -type f -exec stat -c "%s %n" {} \; |
sort -k1 -nr |
head -n 1 |
awk '{print $2}'
```

</details>

Pattern:

```text
find
→ metadata extraction
→ preserve size field
→ numeric sort
→ projection
```

---

## Notes

### File Discovery

```bash
find . -type f
```

```text
-type f = regular file
-type d = directory
```

---

### Metadata Extraction

```bash
stat file.txt
```

Useful fields:

```text
size
permissions
owner
timestamps
```

Compact output:

```bash
stat -c "%s %n"
```

---

### Preserve Sort Key

Wrong:

```bash
find ...
| awk '{print $2}'
| sort -nr
```

Reason:

```text
Size information is lost before sorting.
```

Correct:

```bash
find ...
| stat ...
| sort ...
| awk ...
```

Pattern:

```text
preserve fields
→ sort
→ projection
```

---

### Common Patterns

```text
find → count
```

```text
find → filter → count
```

```text
find → metadata extraction
```

```text
find → metadata extraction → sort
```

```text
find → metadata extraction → sort → projection
```

---

## Mental Model

Think in two questions:

```text
1. Which files?
2. What information about those files?
```

Typical workflow:

```text
find
→ discover files
→ extract metadata
→ sort/filter
→ summarize
```

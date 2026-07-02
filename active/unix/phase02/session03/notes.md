# Session03 Notes

## Core Idea

Multi-file analysis is usually:

```text
find files
→ inspect contents
→ aggregate results
```

Instead of asking:

```text
What is inside this file?
```

ask:

```text
What pattern exists across many files?
```

---

## Task1

Print all `.log` file paths

```bash
find . -type f -name "*.log"
```

Pattern:

```text
find → discover files
```

---

## Task2

Count all 404 entries

```bash
find . -name "*.log" |
xargs cat |
grep "404" |
wc -l
```

Pattern:

```text
find
→ merge contents
→ filter
→ count
```

---

## Task3

Print files containing 404

```bash
find . -name "*.log" -exec grep -l "404" {} +
```

Pattern:

```text
find
→ content check
→ return filenames
```

Notes:

```text
grep -l
= print filenames containing matches
```

---

## Task4

Count total log lines

```bash
find . -name "*.log" |
xargs cat |
wc -l
```

Pattern:

```text
find
→ merge contents
→ aggregate
```

Alternative:

```bash
find . -name "*.log" -exec cat {} +
```

---

## Task5

Print file with the most 404 entries

```bash
find . -name "*.log" -exec grep -H -c "404" {} \; |
awk -F: '{print $2, $1}' |
sort -k1 -nr |
head -n 1 |
awk '{print $2}'
```

Pattern:

```text
find
→ per-file count
→ preserve count
→ numeric sort
→ projection
```

---

## Notes

### Per-file Analysis

```bash
grep -c "404" file.log
```

Output:

```text
count only
```

Example:

```text
2
```

---

### Include Filename

```bash
grep -H -c "404" file.log
```

Output:

```text
count + filename
```

Example:

```text
file.log:2
```

---

### Preserve Sort Key

Wrong:

```bash
grep ...
| awk ...
| sort
```

after removing the count.

Reason:

```text
Sort key is lost.
```

Correct:

```bash
grep ...
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

### File-level vs Content-level Analysis

Content-level:

```bash
grep "404"
```

Returns:

```text
matching lines
```

File-level:

```bash
grep -l "404"
```

Returns:

```text
filenames
```

Count-level:

```bash
grep -c "404"
```

Returns:

```text
number of matches
```

---

## Common Patterns

```text
find → filter → count
```

```text
find → content check → filenames
```

```text
find → merge contents → aggregate
```

```text
find → per-file count
```

```text
find → per-file count → sort
```

```text
find → per-file count → sort → projection
```

---

## Mental Model

Three levels of analysis:

```text
Line
→ File
→ Directory
```

Examples:

```text
grep
→ line analysis
```

```text
grep -c
→ file analysis
```

```text
find + grep
→ directory-wide analysis
```

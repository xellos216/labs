# Session04 Notes

## Core Idea

Treat all files as one dataset.

```text
many files
→ extract values
→ merge values
→ aggregate
```

Instead of:

```text
Which file contains 404?
```

ask:

```text
How many 404s exist overall?
```

---

## Task1

Count total log lines

```bash
find . -name "*.log" -exec cat {} + | wc -l
```

Pattern:

```text
find
→ merge contents
→ aggregate
```

---

## Task2

Count all 404 entries

```bash
find . -name "*.log" -exec cat {} + |
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

Count all 500 entries

```bash
find . -name "*.log" -exec cat {} + |
grep "500" |
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

## Task4

Count occurrences of every status code

```bash
find . -name "*.log" -exec cat {} + |
sort |
uniq -c
```

Pattern:

```text
find
→ merge values
→ sort
→ uniq -c
```

Output:

```text
5 200
4 404
3 500
```

---

## Task5

Print most common status code

```bash
find . -name "*.log" -exec cat {} + |
sort |
uniq -c |
sort -k1 -nr |
head -n 1 |
awk '{print $2}'
```

Pattern:

```text
preserve count
→ numeric sort
→ projection
```

---

## Notes

### uniq Requires Sorting

Wrong:

```bash
cat file |
uniq -c
```

Reason:

```text
uniq only works on adjacent lines.
```

Correct:

```bash
cat file |
sort |
uniq -c
```

Pattern:

```text
sort
→ uniq -c
```

---

### Counting vs Aggregation

Count one value:

```bash
grep "404" | wc -l
```

Result:

```text
404 count only
```

Aggregate everything:

```bash
sort |
uniq -c
```

Result:

```text
count all values
```

---

### Preserve Count Field

Wrong:

```bash
uniq -c |
awk '{print $2}' |
sort
```

Reason:

```text
Count information is lost.
```

Correct:

```bash
uniq -c |
sort -k1 -nr |
awk '{print $2}'
```

Pattern:

```text
preserve count
→ sort
→ projection
```

---

## Common Patterns

```text
find → merge contents
```

```text
find → merge contents → count
```

```text
find → merge values → sort → uniq -c
```

```text
find → merge values → sort → uniq -c → sort
```

```text
find → merge values → sort → uniq -c → sort → projection
```

---

## Mental Model

Three aggregation levels:

```text
Line
→ File
→ Dataset
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
sort | uniq -c
→ dataset analysis
```

The most common Phase02 workflow so far:

```text
find
→ merge values
→ aggregate
→ rank
```

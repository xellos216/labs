# Session07 Notes

## Core Idea

Files have metadata as well as contents.

```text
file
├─ contents
└─ metadata
```

Examples of metadata:

```text
size
owner
permissions
timestamps
path
```

This session focuses on:

```text
find
→ metadata extraction
→ filter
→ rank
```

---

## Task1

Print file size and path

```bash
find . -type f -name "*.log" -exec stat -c '%s %n' {} \;
```

Pattern:

```text
find
→ metadata extraction
```

Output:

```text
6 ./app1/access.log
12 ./app2/access.log
...
```

---

## Task2

Print the largest log file

```bash
find . -type f -name "*.log" -exec stat -c '%s %n' {} \; |
sort -nr |
head -1 |
awk '{print $2}'
```

Pattern:

```text
metadata extraction
→ sort descending
→ projection
```

---

## Task3

Print the smallest log file

```bash
find . -type f -name "*.log" -exec stat -c '%s %n' {} \; |
sort -n |
head -1 |
awk '{print $2}'
```

Pattern:

```text
metadata extraction
→ sort ascending
→ projection
```

---

## Task4

Print the largest 3 log files

```bash
find . -type f -name "*.log" -exec stat -c '%s %n' {} \; |
sort -nr |
head -3 |
awk '{print $2}'
```

Pattern:

```text
metadata extraction
→ ranking
→ top N
→ projection
```

---

## Task5

Print empty log files

```bash
find . -type f -name "*.log" -exec stat -c '%s %n' {} \; |
awk '$1 == 0 {print $2}'
```

Pattern:

```text
metadata extraction
→ metadata filtering
```

---

## Notes

### stat Output Format

```bash
stat -c '%s %n'
```

Meaning:

```text
%s = file size (bytes)
%n = file path
```

Output:

```text
size path
```

Example:

```text
12 ./app2/access.log
```

---

### Metadata as Fields

After:

```bash
stat -c '%s %n'
```

Think:

```text
$1 = size
$2 = path
```

Example:

```text
12 ./app2/access.log
```

becomes:

```text
$1 → 12
$2 → ./app2/access.log
```

---

### Preserve Sort Key

Wrong:

```bash
awk '{print $2}'
sort -nr
```

Reason:

```text
Size field was removed.
```

Correct:

```bash
sort -nr
awk '{print $2}'
```

Pattern:

```text
preserve size
→ sort
→ projection
```

---

### Ranking

Largest:

```bash
sort -nr
```

Smallest:

```bash
sort -n
```

Top N:

```bash
sort -nr |
head -N
```

Pattern:

```text
metric
→ ranking
→ top N
```

---

### Metadata Filtering

Empty files:

```bash
awk '$1 == 0'
```

Files larger than 10 bytes:

```bash
awk '$1 > 10'
```

Files smaller than 100 bytes:

```bash
awk '$1 < 100'
```

Pattern:

```text
metadata extraction
→ metadata filtering
```

---

## Common Patterns

```text
find
→ metadata extraction
```

```text
find
→ metadata extraction
→ filter
```

```text
find
→ metadata extraction
→ sort
```

```text
find
→ metadata extraction
→ sort
→ projection
```

```text
find
→ metadata extraction
→ ranking
→ top N
```

```text
find
→ metadata extraction
→ ranking
→ projection
```

---

## Mental Model

Phase02 progression:

```text
find
→ discover files
```

↓

```text
find
→ content analysis
```

↓

```text
find
→ aggregation
```

↓

```text
find
→ ranking
```

↓

```text
find
→ metadata ranking
```

Current reasoning model:

```text
Which files?
→ Which metadata?
→ How to compare?
→ How to rank?
```

Most important takeaway:

```text
stat output is just another dataset.
```

Once metadata becomes fields:

```text
extract
→ filter
→ sort
→ aggregate
→ rank
```

works exactly like log analysis.

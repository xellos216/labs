# Session06 Notes

## Core Idea

Compare files using metrics.

```text
many files
→ measure each file
→ compare results
→ rank
```

Instead of:

```text
How many 404s exist overall?
```

ask:

```text
Which file has the most 404s?
```

---

## Task1

Print line counts for each file

```bash
find . -name "*.log" -exec wc -l {} \;
```

Pattern:

```text
find
→ per-file metric
```

Example:

```text
5 ./web1/access.log
4 ./web2/access.log
4 ./web3/access.log
3 ./archive/old.log
```

---

## Task2

Print 404 counts per file

```bash
find . -name "*.log" -exec grep -H -c "^404" {} \; |
awk -F: '{print $2, $1}'
```

Pattern:

```text
find
→ per-file count
```

Example:

```text
2 ./web1/access.log
3 ./web2/access.log
0 ./web3/access.log
1 ./archive/old.log
```

---

## Task3

Print file with the most 404 entries

```bash
find . -name "*.log" -exec grep -H -c "^404" {} \; |
awk -F: '{print $2, $1}' |
sort -nr |
head -n 1 |
awk '{print $2}'
```

Pattern:

```text
per-file metric
→ sort
→ projection
```

---

## Task4

Print file with the most 500 entries

```bash
find . -name "*.log" -exec grep -H -c "^500" {} \; |
awk -F: '{print $2, $1}' |
sort -nr |
head -n 1 |
awk '{print $2}'
```

Pattern:

```text
per-file metric
→ sort
→ projection
```

---

## Task5

Print all files tied for the highest

404 + 500 count

```bash
find . -name "*.log" -exec grep -E -H -c "^(404|500)" {} \; |
awk -F: '{print $2, $1}' |
sort -nr |
awk '
NR==1 {max=$1}
$1==max {print $2}
'
```

Pattern:

```text
per-file metric
→ sort
→ tie handling
→ projection
```

---

## Notes

### Per-file Metrics

Examples:

```bash
wc -l file.log
```

```bash
grep -c "^404" file.log
```

```bash
grep -c "^500" file.log
```

Each produces:

```text
one number per file
```

---

### Preserve Metric Before Sorting

Wrong:

```bash
awk '{print $2}'
sort -nr
```

Reason:

```text
Metric was removed before sorting.
```

Correct:

```bash
count
→ sort
→ projection
```

Example:

```bash
grep -H -c "^404" ...
| awk -F: '{print $2, $1}'
| sort -nr
| awk '{print $2}'
```

---

### Ranking Pattern

Most common workflow:

```text
metric
→ sort
→ top result
```

Example:

```bash
sort -nr |
head -n 1
```

---

### Handling Ties

Problem:

```text
web1 = 3
web2 = 3
archive = 3
```

Using:

```bash
head -n 1
```

returns only one result.

To keep all winners:

```bash
awk '
NR==1 {max=$1}
$1==max
'
```

Pattern:

```text
find maximum
→ print all equal values
```

---

## Common Patterns

```text
find → per-file metric
```

```text
find → per-file metric → sort
```

```text
find → per-file metric → sort → projection
```

```text
find → per-file metric → top result
```

```text
find → per-file metric → tie handling
```

```text
find → per-file metric → ranking
```

---

## Mental Model

Phase02 progression:

```text
Session01
find → process files
```

```text
Session02
find → metadata extraction
```

```text
Session03
find → content analysis
```

```text
Session04
find → dataset aggregation
```

```text
Session05
find → filtering
```

```text
Session06
find → per-file metrics → ranking
```

Current reasoning model:

```text
Which files?
→ Which metric?
→ How to compare?
→ How to rank?
```

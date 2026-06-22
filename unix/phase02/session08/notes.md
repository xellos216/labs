# Session08 Notes

## Core Idea

Classification is a common filesystem analysis technique.

Instead of:

```text
Analyze every file individually
```

group files by a shared property:

```text
extension
owner
permission
directory
```

and then calculate statistics.

General workflow:

```text
find
→ classification key extraction
→ aggregation
```

---

## Task1

Print all file paths

```bash
find . -type f
```

Pattern:

```text
find
→ file discovery
```

---

## Task2

Count files by extension

```bash
find . -type f |
awk -F. '{print $NF}' |
sort |
uniq -c
```

Pattern:

```text
path
→ extension extraction
→ aggregation
```

Output:

```text
2 py
2 log
2 md
2 tar
```

---

## Task3

Print the most common extension(s)

```bash
find . -type f |
awk -F. '{print $NF}' |
sort |
uniq -c |
sort -nr |
awk '
NR==1 {max=$1}
$1==max {print $2}
'
```

Pattern:

```text
classification
→ aggregation
→ ranking
→ tie handling
```

---

## Task4

Calculate total size of all log files

```bash
find . -name "*.log" -exec stat -c '%s' {} \; |
awk '{sum += $1} END {print sum}'
```

Pattern:

```text
metadata extraction
→ aggregation
```

---

## Task5

Calculate total size by extension

```bash
find . -type f -exec stat -c '%s %n' {} \; |
awk '
{
    n = split($2, a, ".")
    ext = a[n]
    sum[ext] += $1
}
END {
    for (ext in sum)
        print sum[ext], ext
}'
```

Pattern:

```text
metadata extraction
→ classification
→ metric aggregation
```

---

## Notes

### Classification Keys

Examples:

```text
extension
owner
permission
directory
status code
user
```

A classification key creates groups.

Example:

```text
main.py
config.py
```

↓

```text
py
```

---

### Extracting Extensions

Path:

```text
./app/main.py
```

Command:

```bash
awk -F. '{print $NF}'
```

Result:

```text
py
```

Notes:

```text
$NF = last field
```

Useful because paths can contain different numbers of dots.

---

### Aggregation

Count groups:

```bash
sort |
uniq -c
```

Pattern:

```text
classification
→ aggregation
```

Example:

```text
2 py
2 log
2 md
2 tar
```

---

### Ranking Groups

Most common extension:

```bash
sort -nr
```

Pattern:

```text
aggregate
→ rank
```

Example:

```text
5 log
3 py
2 md
```

---

### Tie Handling

Wrong:

```bash
head -1
```

Only returns one result.

Correct:

```bash
awk '
NR==1 {max=$1}
$1==max
'
```

Pattern:

```text
find max
→ print all equal values
```

---

### Metric Aggregation

Count files:

```bash
uniq -c
```

Sum sizes:

```bash
sum[key] += value
```

Pattern:

```text
classification
→ metric aggregation
```

Examples:

```text
extension → file count
```

```text
extension → total size
```

```text
owner → file count
```

```text
owner → total size
```

---

## Common Patterns

```text
find
→ classification
→ aggregation
```

```text
find
→ classification
→ aggregation
→ ranking
```

```text
find
→ classification
→ aggregation
→ tie handling
```

```text
find
→ metadata extraction
→ aggregation
```

```text
find
→ metadata extraction
→ classification
→ aggregation
```

```text
find
→ metadata extraction
→ classification
→ metric aggregation
```

---

## Mental Model

A file can be viewed as:

```text
file
├─ content
├─ metadata
└─ category
```

Phase02 progression:

```text
file discovery
→ content analysis
→ aggregation
→ ranking
→ metadata analysis
→ classification
```

Current reasoning model:

```text
Which files?
→ Which category?
→ Which metric?
→ How to aggregate?
→ How to rank?
```

Most important takeaway:

```text
Classification converts many files
into meaningful groups.
```

Once a classification key is extracted:

```text
count
sum
average
ranking
```

all become possible.

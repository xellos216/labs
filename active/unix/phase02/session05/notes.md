# Session05 Notes

## Core Idea

Filtering happens at multiple levels.

```text
files
→ lines
→ values
→ aggregation
```

Instead of processing everything:

```text
find
→ process all files
```

we can narrow the scope:

```text
find
→ filename filtering
→ content filtering
→ aggregation
```

---

## Task1

Count all log files

```bash
find . -type f -name "*.log" | wc -l
```

Pattern:

```text
find
→ file filtering
→ count
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
→ content filtering
→ count
```

---

## Task3

Count lines from access logs only

```bash
find . -name "access.log" -exec cat {} + |
wc -l
```

Pattern:

```text
find
→ filename filtering
→ aggregate
```

---

## Task4

Count 404 OR 500 entries

```bash
find . -name "*.log" -exec cat {} + |
awk '$1 == "404" || $1 == "500"' |
wc -l
```

Pattern:

```text
find
→ content filtering
→ OR condition
→ count
```

---

## Task5

Find the most common HTTP status code

```bash
find . \( -name "access.log" -o -name "old.log" \) -exec cat {} + |
awk '{print $1}' |
sort |
uniq -c |
sort -k1 -nr |
head -n 1 |
awk '{print $2}'
```

Pattern:

```text
filename filtering
→ value extraction
→ aggregation
→ ranking
```

---

## Notes

### Filename Filtering

Single filename:

```bash
find . -name "access.log"
```

Single extension:

```bash
find . -name "*.log"
```

Multiple names:

```bash
find . \( -name "access.log" -o -name "old.log" \)
```

Meaning:

```text
access.log OR old.log
```

---

### Content Filtering

Using grep:

```bash
grep "404"
```

Using awk:

```bash
awk '$1 == "404"'
```

Both:

```text
filter lines
```

---

### OR Conditions

Using grep:

```bash
grep -E "404|500"
```

Using awk:

```bash
awk '$1 == "404" || $1 == "500"'
```

Meaning:

```text
404 OR 500
```

---

### Filtering Levels

File level:

```bash
find . -name "*.log"
```

Line level:

```bash
grep "404"
```

Value level:

```bash
awk '{print $1}'
```

Dataset level:

```bash
sort | uniq -c
```

---

## Common Patterns

```text
find
→ filename filtering
→ aggregation
```

```text
find
→ content filtering
→ count
```

```text
find
→ filename filtering
→ content filtering
```

```text
find
→ filename filtering
→ value extraction
→ aggregation
```

```text
find
→ filename filtering
→ value extraction
→ aggregation
→ ranking
```

---

## Mental Model

When solving a problem, ask:

```text
1. Which files?
2. Which lines?
3. Which values?
4. What summary?
```

Typical workflow:

```text
find
→ select files
→ select lines
→ extract values
→ aggregate
→ rank
```

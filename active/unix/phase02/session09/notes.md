# Session09 Notes

## Core Idea

Real-world analysis often ends with a report.

```text
find
→ analyze
→ aggregate
→ summarize
→ report
```

The goal is not just finding information.

The goal is producing useful summaries.

---

## Task1

Count log files

```bash
find . -type f -name "*.log" | wc -l
```

Pattern:

```text
find
→ count
```

---

## Task2

Generate status code statistics

```bash
find . -type f -name "*.log" -exec cat {} + |
sort |
uniq -c
```

Pattern:

```text
find
→ merge values
→ aggregate
```

Example:

```text
5 200
5 404
4 500
```

---

## Task3

Count files containing 404

```bash
find . -type f -name "*.log" -exec grep -l "^404" {} + |
wc -l
```

Pattern:

```text
find
→ file filtering
→ count
```

---

## Task4

Find the largest file

```bash
find . -type f -exec stat -c '%s %n' {} \; |
sort -nr |
head -1 |
awk '{print $2}'
```

Pattern:

```text
metadata extraction
→ ranking
→ projection
```

---

## Task5

Generate a summary report

```bash
log_files=$(find . -type f -name "*.log" | wc -l)

total_404=$(
find . -type f -name "*.log" -exec cat {} + |
grep "^404" |
wc -l
)

total_500=$(
find . -type f -name "*.log" -exec cat {} + |
grep "^500" |
wc -l
)

empty_files=$(
find . -type f -name "*.log" -exec stat -c '%s %n' {} \; |
awk '$1 == 0 {count++} END {print count}'
)

printf 'LOG_FILES=%s\nTOTAL_404=%s\nTOTAL_500=%s\nEMPTY_FILES=%s\n' \
"$log_files" \
"$total_404" \
"$total_500" \
"$empty_files"
```

Pattern:

```text
metric calculation
→ variable capture
→ reporting
```

---

## Notes

### Command Substitution

Capture command output:

```bash
count=$(wc -l file.txt)
```

Pattern:

```text
command
→ variable
```

Useful for:

```text
reports
automation
comparisons
conditions
```

---

### Reporting

Human-readable output:

```bash
echo "TOTAL_404=$count"
```

Structured output:

```bash
printf 'TOTAL_404=%s\n' "$count"
```

Pattern:

```text
metric
→ label
→ output
```

---

### Report-Oriented Thinking

Before:

```text
How many 404s?
```

After:

```text
TOTAL_404=5
```

Before:

```text
How many empty logs?
```

After:

```text
EMPTY_FILES=1
```

The report answers questions directly.

---

### Aggregation vs Reporting

Aggregation:

```bash
sort |
uniq -c
```

Output:

```text
5 404
4 500
```

Reporting:

```bash
printf 'TOTAL_404=%s\n' "$count"
```

Output:

```text
TOTAL_404=5
```

Pattern:

```text
analysis
→ aggregation
→ reporting
```

---

### Building Metrics

Common metrics:

```text
file count
line count
error count
empty files
largest file
most common value
```

Each metric follows:

```text
find
→ extract
→ aggregate
```

---

## Common Patterns

```text
find
→ count
```

```text
find
→ aggregate
```

```text
find
→ ranking
```

```text
find
→ metric extraction
```

```text
metric
→ variable capture
```

```text
metric
→ reporting
```

```text
analysis
→ aggregation
→ reporting
```

---

## Mental Model

Phase02 progression:

```text
find
→ discovery
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
→ classification
```

↓

```text
find
→ reporting
```

Current reasoning model:

```text
Which files?
→ Which metric?
→ How to aggregate?
→ How should it be reported?
```

Most important takeaway:

```text
Analysis becomes useful
when it is transformed into a report.
```

General workflow:

```text
find
→ extract
→ aggregate
→ summarize
→ report
```

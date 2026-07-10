# Session15 Notes

## Core Idea

Session15 was the final review checkpoint for Phase02.

The goal was not to learn new commands.

The goal was to verify whether the main Phase02 patterns were stable:

```text
file discovery
→ safe filename transport
→ content aggregation
→ file ranking
→ metadata ranking
→ safe replacement
→ report generation
```

The three main review targets were:

```text
safe handling of filenames with spaces
max ranking with owner preservation
size-first metadata sorting
```

---

## Task1

Print all `.log` files.

```bash
find . -type f -name "*.log"
```

Pattern:

```text
find
→ recursive file discovery
```

This includes files with spaces in the path, such as:

```text
./logs/error log.log
```

---

## Task2

Count total lines from all `.log` files safely.

Correct form:

```bash
find . -type f -name "*.log" -print0 |
xargs -0 cat |
wc -l
```

Pattern:

```text
find -print0
→ xargs -0
→ cat
→ wc -l
```

Important shell detail:

```text
A pipeline can be split across lines after a pipe.
```

Good:

```bash
find . -type f -name "*.log" -print0 |
xargs -0 cat |
wc -l
```

Fragile:

```bash
find . -type f -name "*.log" -print0 | xargs -0 cat
| wc -l
```

The pipe should remain syntactically connected to the next command.

---

## Task3

Aggregate status-code-like first fields.

```bash
find . -type f -name "*.log" -exec cat {} \; |
awk '$1 ~ /^[0-9]+$/ {print $1}' |
sort |
uniq -c
```

Stricter 3-digit version:

```bash
find . -type f -name "*.log" -exec cat {} \; |
awk '$1 ~ /^[0-9][0-9][0-9]$/ {print $1}' |
sort |
uniq -c
```

Pattern:

```text
find
→ merge content
→ extract numeric first field
→ sort
→ uniq -c
```

This prevents non-status text such as `database`, `timeout`, or report text from being counted.

---

## Task4

Find the `.log` file with the most `404` entries.

First observe the intermediate data:

```bash
find . -type f -name "*.log" -exec grep -H -c "404" {} \;
```

Example shape:

```text
./logs/access.log:2
./logs/error log.log:1
./app/app.log:0
./archive/old.log:2
```

Correct `awk` max form:

```bash
find . -type f -name "*.log" -exec grep -H -c "404" {} \; |
awk -F: '$2 > max { max=$2; file=$1 } END { print file }'
```

Pattern:

```text
file:count
→ compare count
→ save count and filename
→ print saved filename
```

Important correction:

```awk
$2 > max { max=$2; file=$1 } END { print file }
```

When the maximum value changes, save both:

```text
the maximum value
and
the file that produced it
```

Do not print `$1` at `END` unless it was explicitly saved. At `END`, `$1` may refer to the last processed record, not the maximum record.

---

## Task5

Print the largest three `.log` files by size.

Correct form:

```bash
find . -type f -name "*.log" -exec stat -c "%s %n" {} \; |
sort -nr |
head -3
```

Pattern:

```text
find
→ stat
→ size path
→ numeric reverse sort
→ top 3
```

Important correction:

```text
The sort key must come first.
```

Wrong shape:

```bash
stat -c "%n %s"
```

This produces:

```text
path size
```

Correct shape:

```bash
stat -c "%s %n"
```

This produces:

```text
size path
```

Then `sort -nr` can sort by size correctly.

---

## Task6

Replace `ENV=dev` with `ENV=prod` only in `.conf` files.

Inspect before replacement:

```bash
find . -type f -name "*.conf" -exec grep -H "ENV=dev" {} +
```

Replace:

```bash
find . -type f -name "*.conf" -exec sed -i 's/ENV=dev/ENV=prod/g' {} +
```

Verify changed files:

```bash
find . -type f -name "*.conf" -exec grep -H "ENV=prod" {} +
```

Verify excluded report file:

```bash
grep -H "ENV=prod" reports/summary.txt
```

Expected result:

```text
no output
```

Alternative verification:

```bash
grep -H "404" reports/summary.txt
```

This confirms the original report file still exists and still contains its expected content.

Pattern:

```text
inspect
→ replace selected files
→ verify changed files
→ verify excluded files
```

---

## Task7

Generate a final report.

Correct form:

```bash
log_files=$(find . -type f -name "*.log" | wc -l)

total_lines=$(
  find . -type f -name "*.log" -print0 |
  xargs -0 cat |
  wc -l
)

total_404=$(
  find . -type f -name "*.log" -print0 |
  xargs -0 grep -h "404" |
  wc -l
)

top_404_file=$(
  find . -type f -name "*.log" -exec grep -H -c "404" {} \; |
  awk -F: '$2 > max { max=$2; file=$1 } END { print file }'
)

largest_log=$(
  find . -type f -name "*.log" -exec stat -c "%s %n" {} \; |
  sort -nr |
  head -1 |
  cut -d' ' -f2-
)

config_env=$(grep '^ENV=' ./app/config.conf)

printf 'LOG_FILES=%s\n' "$log_files"
printf 'TOTAL_LINES=%s\n' "$total_lines"
printf 'TOTAL_404=%s\n' "$total_404"
printf 'TOP_404_FILE=%s\n' "$top_404_file"
printf 'LARGEST_LOG=%s\n' "$largest_log"
printf 'CONFIG_ENV=%s\n' "$config_env"
```

Pattern:

```text
compute value
→ store in variable
→ print structured report
```

---

## Notes

### Safe Filename Transport

Unsafe:

```bash
find . -type f -name "*.log" | xargs cat
```

Safe:

```bash
find . -type f -name "*.log" -print0 |
xargs -0 cat
```

Mental model:

```text
newline-separated paths
→ fragile with unusual names

null-separated paths
→ safer for path transport
```

---

### Max Ranking

Incorrect pattern:

```awk
$2 > max { max=$2 } END { print $1 }
```

Problem:

```text
The max value is saved,
but the object that produced it is not saved.
```

Correct pattern:

```awk
$2 > max { max=$2; file=$1 } END { print file }
```

Mental model:

```text
ranking needs both metric and owner
```

---

### Size-First Sorting

Incorrect:

```bash
stat -c "%n %s" | sort -nr
```

Correct:

```bash
stat -c "%s %n" | sort -nr
```

Mental model:

```text
sort reads fields from left to right

therefore:

metric first
object second
```

---

### Paths with Spaces

Fragile:

```bash
awk '{print $2}'
```

Safer for `size path` output:

```bash
cut -d' ' -f2-
```

Example:

```text
42 ./logs/error log.log
```

`cut -d' ' -f2-` preserves:

```text
./logs/error log.log
```

---

### Report Variables

Common syntax mistake:

```bash
log_files=$(find . -type f -name "*.log" | wc -l
```

Correct:

```bash
log_files=$(find . -type f -name "*.log" | wc -l)
```

Pattern:

```text
$(...)
must be closed
```

---

### Replacement Verification

A replacement task is incomplete if only the changed files are checked.

Safe verification checks both:

```text
included target files
and
excluded non-target files
```

For example:

```bash
find . -type f -name "*.conf" -exec grep -H "ENV=prod" {} +
```

confirms the intended target changed.

```bash
grep -H "ENV=prod" reports/summary.txt
```

should produce no output, confirming the excluded report file was not modified.

---

## Common Mistakes

### Mistake 1

Pipeline line break disconnected from the pipe.

Fragile:

```bash
command1
| command2
```

Better:

```bash
command1 |
command2
```

---

### Mistake 2

Sorting `file size` instead of `size file`.

Incorrect:

```bash
stat -c "%n %s" | sort -nr
```

Correct:

```bash
stat -c "%s %n" | sort -nr
```

---

### Mistake 3

Using `head` before ranking.

Incorrect:

```bash
grep -H -c "404" ... | head -2
```

This does not calculate the maximum.

Correct:

```text
count per file
→ compare counts
→ select maximum
```

---

### Mistake 4

Using `$1` at `END` without saving the intended record.

Incorrect:

```awk
$2 > max { max=$2; file=$1 } END { print $1 }
```

Correct:

```awk
$2 > max { max=$2; file=$1 } END { print file }
```

---

### Mistake 5

Using `awk '{print $2}'` for paths that may contain spaces.

Fragile:

```bash
awk '{print $2}'
```

Safer:

```bash
cut -d' ' -f2-
```

---

## Phase02 Review Result

Stable patterns:

```text
find-based discovery
recursive content aggregation
status-code extraction
sed replacement workflow
basic report generation
```

Needs reinforcement:

```text
safe filename transport
max ranking with owner preservation
metadata sorting by metric
path handling when filenames contain spaces
script syntax accuracy
```

---

## Mental Model

Phase02 final model:

```text
files
→ pathnames
→ content
→ fields
→ metadata
→ metrics
→ ranked objects
→ modifications
→ verification
→ reports
```

Most important takeaway:

```text
Unix multi-file work is not just command usage.

It is controlled data flow across pathnames, lines, fields, metadata, and generated reports.
```

# Session14 Notes

## Core Idea

Phase02 combines multiple Unix patterns into one workflow.

```text
select files
→ inspect content
→ aggregate data
→ rank files
→ modify safely
→ verify
→ report
```

The important skill is not remembering one command.

The important skill is choosing the correct pipeline shape for the problem.

---

## Task1

Print all `.log` files.

```bash
find . -name "*.log"
```

Better restricted form:

```bash
find . -type f -name "*.log"
```

Pattern:

```text
find
→ recursive file discovery
```

This includes filenames with spaces, such as:

```text
./web2/error log.log
```

---

## Task2

Count all lines from `.log` files safely.

```bash
find . -name "*.log" -print0 |
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

This preserves filenames containing spaces.

---

## Task3

Aggregate HTTP-like status codes.

```bash
find . -name "*.log" -exec cat {} \; |
awk '$1 ~ /^[0-9]+$/ {print $1}' |
sort |
uniq -c
```

Stricter 3-digit status-code form:

```bash
find . -name "*.log" -exec cat {} \; |
awk '$1 ~ /^[0-9][0-9][0-9]$/ {print $1}' |
sort |
uniq -c
```

Pattern:

```text
find
→ merge content
→ select numeric first field
→ sort
→ count
```

This excludes non-status lines such as:

```text
DEBUG
database
timeout
```

---

## Task4

Find the `.log` file with the most `404` entries.

Correct variable-based form:

```bash
find . -name "*.log" -exec grep -H -c "404" {} \; |
awk -F: '$2 > max { max = $2; file = $1 } END { print file }'
```

Sort-based form:

```bash
find . -name "*.log" -exec grep -H -c "404" {} \; |
awk -F: '{print $2, $1}' |
sort -nr |
head -1 |
awk '{print $2}'
```

Pattern:

```text
find
→ per-file count
→ preserve count and filename
→ select maximum
```

Important correction:

```awk
$2 > max { max = $2; file = $1 } END { print file }
```

The filename must be saved when the maximum value is updated.

---

## Task5

Print the largest three `.log` files with size.

```bash
find . -name "*.log" -exec stat -c '%s %n' {} \; |
sort -nr |
head -3
```

Pattern:

```text
find
→ stat metadata
→ size first
→ numeric reverse sort
→ top N
```

Important correction:

```text
Use '%s %n', not '%n %s', when sorting by size.
```

The sortable value should appear first.

---

## Task6

Replace `ENV=dev` with `ENV=prod` only in `.conf` files.

Inspect before replacement:

```bash
find . -name "*.conf" -exec grep -H "ENV=dev" {} \;
```

Replace:

```bash
find . -name "*.conf" -exec sed -i 's/ENV=dev/ENV=prod/g' {} +
```

Verify changed files:

```bash
find . -name "*.conf" -exec grep -H "ENV=prod" {} \;
```

Verify excluded document files:

```bash
find . -type f \( -name "*.md" -o -name "*.txt" \) -exec grep -H "dev" {} +
```

Pattern:

```text
inspect
→ replace selected files
→ verify changed files
→ verify excluded files
```

---

## Task7

Replace `LOG_LEVEL=debug` with `LOG_LEVEL=info` only in `.conf` files.

Inspect before replacement:

```bash
find . -name "*.conf" -exec grep -H "LOG_LEVEL=debug" {} \;
```

Replace:

```bash
find . -name "*.conf" -exec sed -i 's/LOG_LEVEL=debug/LOG_LEVEL=info/g' {} +
```

Verify changed files:

```bash
find . -name "*.conf" -exec grep -H "LOG_LEVEL=info" {} \;
```

Verify document files still contain `debug`:

```bash
find . -type f \( -name "*.md" -o -name "*.txt" \) -exec grep -H "debug" {} +
```

Pattern:

```text
config files
→ modified

document files
→ unchanged
```

---

## Task8

Generate final report.

```bash
log_files=$(find . -name '*.log' | wc -l)

total_lines=$(
  find . -name '*.log' -print0 |
  xargs -0 cat |
  wc -l
)

total_404=$(
  find . -name '*.log' -exec grep -h '404' {} \; |
  wc -l
)

top_404_file=$(
  find . -name '*.log' -exec grep -H -c '404' {} \; |
  awk -F: '$2 > max { max=$2; file=$1 } END { print file }'
)

largest_log=$(
  find . -name '*.log' -exec stat -c '%s %n' {} \; |
  sort -nr |
  head -1 |
  cut -d' ' -f2-
)

config_env=$(grep '^ENV=' ./api/config.conf)
config_log_level=$(grep '^LOG_LEVEL=' ./api/config.conf)

printf 'LOG_FILES=%s\n' "$log_files"
printf 'TOTAL_LINES=%s\n' "$total_lines"
printf 'TOTAL_404=%s\n' "$total_404"
printf 'TOP_404_FILE=%s\n' "$top_404_file"
printf 'LARGEST_LOG=%s\n' "$largest_log"
printf 'CONFIG_ENV=%s\n' "$config_env"
printf 'CONFIG_LOG_LEVEL=%s\n' "$config_log_level"
```

Pattern:

```text
compute metrics
→ store in variables
→ print structured report
```

---

## Notes

### Safe Filename Handling

Unsafe when filenames may contain spaces:

```bash
find . -name "*.log" | xargs cat
```

Safe:

```bash
find . -name "*.log" -print0 |
xargs -0 cat
```

Pattern:

```text
null-separated pathnames
→ safe argument passing
```

---

### Ranking with awk

Incorrect pattern:

```awk
$2 > max { max = $2 } END { print $1 }
```

Problem:

```text
END-time $1 is not necessarily the file that produced max.
```

Correct pattern:

```awk
$2 > max { max = $2; file = $1 } END { print file }
```

Pattern:

```text
when max changes
→ save both value and owner
```

---

### Ranking with sort

For numeric ranking, put the numeric value first.

```bash
stat -c '%s %n'
```

Then sort numerically in reverse order:

```bash
sort -nr
```

Pattern:

```text
metric first
→ object second
→ sort by metric
```

---

### Handling Paths with Spaces

This is fragile:

```bash
awk '{print $2}'
```

when the second field is a pathname that may contain spaces.

Safer for output like:

```text
49 ./web2/error log.log
```

Use:

```bash
cut -d' ' -f2-
```

Meaning:

```text
print everything after the first space
```

---

### Replacement Safety

Unsafe replacement mindset:

```text
replace first
→ check later
```

Safe replacement mindset:

```text
inspect target
→ replace target
→ verify changed target
→ verify excluded files
```

For recursive replacement, the hard part is usually not `sed`.

The hard part is selecting the correct files.

---

## Common Patterns

```text
find
→ file discovery
```

```text
find -print0
→ xargs -0
→ safe content processing
```

```text
find
→ cat
→ awk
→ sort
→ uniq -c
```

```text
find
→ grep -H -c
→ ranking
```

```text
find
→ stat
→ sort -nr
→ top N
```

```text
find
→ grep
→ sed -i
→ grep
```

```text
variables
→ printf report
```

---

## Common Mistakes

### Mistake 1

Printing `$1` at `END` after calculating a max.

Incorrect:

```awk
$2 > max { max=$2; file=$1 } END { print $1 }
```

Correct:

```awk
$2 > max { max=$2; file=$1 } END { print file }
```

---

### Mistake 2

Sorting file metadata by filename instead of size.

Incorrect:

```bash
stat -c '%n %s' | sort
```

Correct:

```bash
stat -c '%s %n' | sort -nr
```

---

### Mistake 3

Using `$2` for paths that may contain spaces.

Fragile:

```bash
awk '{print $2}'
```

Safer:

```bash
cut -d' ' -f2-
```

---

### Mistake 4

Typo in command name.

Incorrect:

```bash
gre
```

Correct:

```bash
grep
```

---

## Mental Model

Phase02 workflow:

```text
Which files?

↓

How should filenames be transported?

↓

Which content or metadata should be extracted?

↓

What field must be preserved?

↓

Is this analysis or modification?

↓

If modifying, how will the result be verified?

↓

How should the result be reported?
```

Most important takeaway:

```text
Multi-file Unix work is a data-flow problem.

Files, lines, fields, metadata, and pathnames must be selected and preserved deliberately.
```

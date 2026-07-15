# Phase 03 Session 01 — HTTP Access Log Analysis

## Objective

Analyze an HTTP access log as a stream of structured events.

The session focused on:

* filtering events by HTTP status
* extracting fields from log records
* grouping repeated values
* ranking frequent IP addresses and paths
* aggregating requests into minute-level time buckets
* producing a compact shell report

## Sample Log Structure

A log entry had the following form:

```text
192.168.0.12 - - [10/Jul/2026:09:00:07 +0900] "POST /login HTTP/1.1" 401 128 "/login" "Mozilla/5.0"
```

With the default whitespace field separator:

```text
$1  = client IP
$4  = timestamp prefix
$6  = HTTP method with opening quote
$7  = request path
$8  = HTTP version with closing quote
$9  = HTTP status code
$10 = response size
```

The field positions depend on the log format. They are not universal properties of HTTP logs.

## Core Analysis Pattern

The reusable log-analysis flow was:

```text
Filter relevant events
→ Extract the meaningful field
→ Sort identical values together
→ Count each group
→ Rank or present the result
```

Typical pipeline:

```bash
awk 'condition {print field}' access.log |
  sort |
  uniq -c |
  sort -nr
```

## Count Total Requests

```bash
wc -l < access.log
```

This counts all log records.

Using input redirection avoids an unnecessary `cat` process and prints only the count.

## Filter by Status Code

Print all `401 Unauthorized` responses:

```bash
awk '$9 == 401' access.log
```

Print all client and server errors:

```bash
awk '$9 >= 400 && $9 < 600' access.log
```

Using the status-code field is safer than searching for strings such as:

```bash
grep '401' access.log
```

A plain string search may match `401` somewhere other than the status field.

## Count a Specific Status

```bash
awk '$9 == 401' access.log | wc -l
```

This counts all events whose status field is exactly `401`.

The condition-only form is equivalent to:

```bash
awk '$9 == 401 {print}' access.log
```

When an `awk` condition is true and no action is given, the default action is to print the whole record.

## Find the IP Producing the Most 401 Responses

```bash
awk '$9 == 401 {print $1}' access.log |
  sort |
  uniq -c |
  sort -nr |
  head -n1
```

Result:

```text
4 192.168.0.12
```

Pipeline meaning:

```text
Select 401 events
→ Extract client IPs
→ Place identical IPs next to each other
→ Count each IP
→ Sort by count descending
→ Select the highest-ranked result
```

## Count Requests by Path

```bash
awk '{print $7}' access.log |
  sort |
  uniq -c |
  sort -nr
```

Top result:

```text
6 /login
```

The first `sort` is required because `uniq -c` counts only adjacent identical lines.

Without sorting, the same path may appear as several separate groups if its requests are scattered throughout the log.

## Extract Minute-Level Time Buckets

The original timestamp field looked like:

```text
[10/Jul/2026:09:00:01
```

Extract the hour and minute:

```bash
awk '{print $4}' access.log |
  awk -F: '{print $2 ":" $3}'
```

Output:

```text
09:00
09:00
09:00
09:00
09:01
...
```

Here, the second `awk` uses `:` as its field separator:

```text
$1 = [10/Jul/2026
$2 = 09
$3 = 00
$4 = 01
```

## Count Requests per Minute

```bash
awk '{print $4}' access.log |
  awk -F: '{print $2 ":" $3}' |
  sort |
  uniq -c
```

Result:

```text
4 09:00
2 09:01
2 09:02
2 09:03
1 09:04
2 09:05
1 09:06
```

This converts individual events into minute-level buckets and counts the number of requests in each bucket.

## Integrated Report

```bash
total_request=$(wc -l < access.log)

error_request=$(
  awk '$9 >= 400 && $9 < 600' access.log |
    wc -l
)

top_error=$(
  awk '$9 >= 400 && $9 < 600 {print $1}' access.log |
    sort |
    uniq -c |
    sort -nr |
    head -n1
)

top_path=$(
  awk '{print $7}' access.log |
    sort |
    uniq -c |
    sort -nr |
    head -n1
)

printf \
  'Total requests: %s\nError requests: %s\nTop error IP: %s\nTop path: %s\n' \
  "$total_request" \
  "$error_request" \
  "$top_error" \
  "$top_path"
```

Expected result:

```text
Total requests: 15
Error requests: 9
Top error IP:       4 192.168.0.12
Top path:       6 /login
```

`uniq -c` pads the count with leading spaces. Those spaces remain when the complete line is stored in a variable.

## Corrected Mistakes

### Counting the Entire Stream Instead of Each Group

Incorrect:

```bash
awk '$9 == 401 {print $1}' access.log |
  wc -l |
  sort -nr |
  head -n1
```

`wc -l` reduces the entire stream to one number. It cannot retain the relationship between each IP and its frequency.

Correct mental model:

```text
wc -l
→ one count for the complete input stream

sort | uniq -c
→ one count for each distinct value
```

### Using `uniq -c` Without Sorting

Incorrect:

```bash
awk '{print $7}' access.log |
  uniq -c
```

`uniq` does not search the whole input for matching values. It combines only consecutive identical lines.

Correct:

```bash
awk '{print $7}' access.log |
  sort |
  uniq -c
```

### Matching Status Codes as Arbitrary Strings

Fragile:

```bash
grep '200' access.log
```

This searches the entire record and may match `200` outside the status field.

Structured filtering:

```bash
awk '$9 == 200' access.log
```

### Excluding 5xx Errors Accidentally

Incomplete error range:

```bash
awk '$9 >= 400 && $9 < 500' access.log
```

This includes only `4xx` client errors.

Complete client-and-server error range:

```bash
awk '$9 >= 400 && $9 < 600' access.log
```

### Printing a Summary Instead of the Matching Log Events

A task asking for `401` log entries requires filtering the original records:

```bash
awk '$9 == 401' access.log
```

Filtering a previously generated summary line does not return the underlying events.

### Using `echo` for Structured Multi-Line Output

Potentially inconsistent:

```bash
echo "line1\nline2"
```

Backslash handling by `echo` can vary.

Preferred:

```bash
printf 'line1\nline2\n'
```

`printf` has explicit and predictable formatting behavior.

## Reusable Command Patterns

Count all records:

```bash
wc -l < file
```

Filter by a numeric field:

```bash
awk '$field >= lower && $field < upper' file
```

Count values:

```bash
awk '{print field}' file |
  sort |
  uniq -c
```

Rank values by frequency:

```bash
awk '{print field}' file |
  sort |
  uniq -c |
  sort -nr
```

Select the most frequent value:

```bash
awk '{print field}' file |
  sort |
  uniq -c |
  sort -nr |
  head -n1
```

Generate a stable report:

```bash
printf 'Label: %s\n' "$value"
```

## Final Mental Model

An access log is not merely text to search.

It is a stream of structured event records:

```text
Event records
→ Field-aware filtering
→ Field extraction
→ Grouping
→ Aggregation
→ Ranking or timeline
→ Operational observation
```

The important distinction is:

```text
Text matching asks:
“Does this string occur somewhere?”

Structured parsing asks:
“What value does this event contain in the field that represents status,
client, path, or time?”
```

Reliable log analysis depends on understanding the record structure before composing the pipeline.

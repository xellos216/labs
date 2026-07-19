# Session02 Notes

## Core Idea

Authentication logs contain events with similar meanings but variable field
positions.

The main problem was not simply finding text.

The goal was to identify stable relationships inside each event:

```text
Failed password
→ authentication failure

Accepted
→ authentication success

sudo[PID]
→ privilege-elevation event
```

Some fields moved because optional words appeared in the log.

```text
Failed password for invalid user admin from 192.0.2.10
Failed password for root from 192.0.2.10
```

The reusable parsing model was:

```text
select event type
→ find a stable token
→ extract a field relative to that token
→ aggregate or correlate events
```

---

## Task1

Count authentication event types.

```bash
failed_count=$(grep -c 'Failed password' auth.log)
accepted_count=$(grep -c 'Accepted' auth.log)
sudo_count=$(grep -c 'sudo\[' auth.log)

printf '%s\n' \
  "Failed: $failed_count" \
  "Accepted: $accepted_count" \
  "Sudo: $sudo_count"
```

Dataset result:

```text
Failed: 11
Accepted: 4
Sudo: 4
```

Pattern:

```text
event signature
→ grep -c
→ event count
```

Using the complete event signature is safer than searching for a broad word.

For example:

```bash
grep -c 'Failed password' auth.log
```

is more specific than:

```bash
grep -c 'Failed' auth.log
```

---

## Task2

Count failed authentication attempts by source IP.

```bash
grep 'Failed password' auth.log |
awk '{
  for (i = 1; i <= NF; i++) {
    if ($i == "from") {
      print $(i + 1)
      break
    }
  }
}' |
sort |
uniq -c |
sort -nr
```

Dataset result:

```text
6 192.0.2.10
3 203.0.113.30
2 192.0.2.11
```

Pattern:

```text
Failed password events
→ find "from"
→ print the following field
→ group by IP
→ rank by frequency
```

The IP was not extracted using a fixed field number.

Instead, it was identified by this relationship:

```text
from → source IP
```

This remains valid across both failure formats:

```text
invalid user admin from 192.0.2.10
root from 192.0.2.10
```

---

## Task3

Count failed authentication attempts by username.

```bash
grep 'Failed password' auth.log |
awk '{
  for (i = 1; i <= NF; i++) {
    if ($i == "from") {
      print $(i - 1)
      break
    }
  }
}' |
sort |
uniq -c |
sort -nr
```

Dataset result:

```text
4 admin
2 root
1 test
1 postgres
1 oracle
1 guest
1 deploy
```

The username was identified by this relationship:

```text
username → immediately before "from"
```

Examples:

```text
invalid user admin from
             admin ← username

for root from
    root ← username
```

Searching only for the token `user` would miss entries such as:

```text
Failed password for root from ...
```

because that event does not contain the word `user`.

---

## Task4

Count successful SSH authentication by username.

```bash
grep 'Accepted' auth.log |
awk '{
  for (i = 1; i <= NF; i++) {
    if ($i == "for") {
      print $(i + 1)
      break
    }
  }
}' |
sort |
uniq -c |
sort -nr
```

Dataset result:

```text
2 analyst
1 operator
1 deploy
```

Pattern:

```text
Accepted event
→ find "for"
→ print the following field
→ group by username
```

The authentication method may change:

```text
Accepted publickey for analyst
Accepted password for operator
```

The relationship remains stable:

```text
for → authenticated username
```

---

## Task5

Count successful SSH authentication by source IP.

```bash
grep 'Accepted' auth.log |
awk '{
  for (i = 1; i <= NF; i++) {
    if ($i == "from") {
      print $(i + 1)
      break
    }
  }
}' |
sort |
uniq -c |
sort -nr
```

Dataset result:

```text
2 198.51.100.20
1 203.0.113.40
1 192.0.2.11
```

The same token-relative extraction rule used for failures also applies to
successful SSH events:

```text
from → source IP
```

---

## Task6

Count failed authentication attempts by minute.

```bash
grep 'Failed password' auth.log |
awk '{
  minute = substr($3, 1, 5)
  print minute
}' |
sort |
uniq -c
```

Dataset result:

```text
3 09:00
2 09:01
1 09:02
1 09:03
2 09:04
1 09:05
1 09:06
```

The original time field was:

```text
09:00:01
```

The expression:

```awk
substr($3, 1, 5)
```

produced:

```text
09:00
```

Pattern:

```text
individual timestamps
→ normalize to minute buckets
→ group equal buckets
→ count events per minute
```

The final output remained in chronological order.

A final `sort -nr` was not used because the objective was timeline
observation, not frequency ranking.

---

## Task7

Extract complete commands from sudo events.

```bash
grep 'sudo\[' auth.log |
awk '{
  command_pos = index($0, "COMMAND=")

  if (command_pos)
    print substr($0, command_pos + 8)
}'
```

Dataset result:

```text
/usr/bin/systemctl status sshd
/usr/bin/id
/usr/bin/journalctl -u sshd
/usr/bin/systemctl restart app.service
```

A single field number was insufficient because a command may contain
arguments and spaces.

For example:

```text
COMMAND=/usr/bin/systemctl restart app.service
```

The parser therefore operated on the complete record, `$0`.

Pattern:

```text
complete log record
→ find marker position
→ print everything after marker
```

`index()` returned the starting position of `COMMAND=`.

`COMMAND=` is eight characters long, so:

```awk
substr($0, command_pos + 8)
```

started immediately after the marker.

---

## Task8

Count sudo events by invoking user.

```bash
grep 'sudo\[' auth.log |
awk '{print $6}' |
sort |
uniq -c |
sort -nr
```

Dataset result:

```text
2 analyst
1 operator
1 deploy
```

In this specific log format:

```text
$5 = sudo[PID]:
$6 = invoking user
$7 = :
```

This task used a fixed field because the supplied sudo records had a stable
prefix.

The rule is format-specific.

If the syslog prefix changes, the field number may also change.

---

## Task9

Find the IP that produced the most failed authentication attempts.

```bash
top_failed_ip=$(
  grep 'Failed password' auth.log |
  awk '{
    for (i = 1; i <= NF; i++) {
      if ($i == "from") {
        print $(i + 1)
        break
      }
    }
  }' |
  sort |
  uniq -c |
  sort -nr |
  head -n1 |
  awk '{print $2}'
)
```

Inspect every event involving that IP:

```bash
grep "$top_failed_ip" auth.log
```

Dataset result:

```text
192.0.2.10
```

Observation:

```text
192.0.2.10 generated six failed authentication events.
No Accepted event from that IP appeared in the supplied log interval.
```

Important ranking sequence:

```text
group values
→ count groups
→ sort by count
→ select first result
```

Incorrect sequence:

```bash
sort |
uniq -c |
head -n1
```

This selects the first IP in lexical order, not necessarily the IP with the
largest count.

Correct sequence:

```bash
sort |
uniq -c |
sort -nr |
head -n1
```

---

## Task10

Find IP addresses that appeared in both failed and successful SSH events.

```bash
failed_accepted_ips=$(
  comm -12 \
    <(
      grep 'Failed password' auth.log |
      awk '{
        for (i = 1; i <= NF; i++) {
          if ($i == "from") {
            print $(i + 1)
            break
          }
        }
      }' |
      sort -u
    ) \
    <(
      grep 'Accepted' auth.log |
      awk '{
        for (i = 1; i <= NF; i++) {
          if ($i == "from") {
            print $(i + 1)
            break
          }
        }
      }' |
      sort -u
    )
)
```

Dataset result:

```text
192.0.2.11
```

Inspect the correlated events:

```bash
grep '192.0.2.11' auth.log
```

Timeline:

```text
09:00:04 Failed password for invalid user test
09:06:03 Failed password for invalid user deploy
09:06:20 Accepted publickey for deploy
```

Verified observation:

```text
The same IP produced two failed attempts and later one successful
public-key authentication.
```

This does not prove that an intrusion succeeded.

Possible explanations include:

```text
normal user error
automation using multiple account names
misconfigured deployment tooling
malicious authentication attempts
```

The log alone establishes correlation:

```text
same source IP
→ failed authentication
→ later successful authentication
```

Additional evidence would be required to determine intent or compromise.

---

## Integrated Report

```bash
failed_attempts=$(grep -c 'Failed password' auth.log)

accepted_attempts=$(grep -c 'Accepted' auth.log)

top_failed_ip=$(
  grep 'Failed password' auth.log |
  awk '{
    for (i = 1; i <= NF; i++) {
      if ($i == "from") {
        print $(i + 1)
        break
      }
    }
  }' |
  sort |
  uniq -c |
  sort -nr |
  head -n1
)

failed_accepted_ips=$(
  comm -12 \
    <(
      grep 'Failed password' auth.log |
      awk '{
        for (i = 1; i <= NF; i++) {
          if ($i == "from") {
            print $(i + 1)
            break
          }
        }
      }' |
      sort -u
    ) \
    <(
      grep 'Accepted' auth.log |
      awk '{
        for (i = 1; i <= NF; i++) {
          if ($i == "from") {
            print $(i + 1)
            break
          }
        }
      }' |
      sort -u
    )
)

top_failed_user=$(
  grep 'Failed password' auth.log |
  awk '{
    for (i = 1; i <= NF; i++) {
      if ($i == "from") {
        print $(i - 1)
        break
      }
    }
  }' |
  sort |
  uniq -c |
  sort -nr |
  head -n1
)

top_sudo_user=$(
  grep 'sudo\[' auth.log |
  awk '{print $6}' |
  sort |
  uniq -c |
  sort -nr |
  head -n1
)

printf '%s\n' \
  "Failed attempts: $failed_attempts" \
  "Accepted attempts: $accepted_attempts" \
  "Top failed IP: $top_failed_ip" \
  "Failed-then-accepted IPs: $failed_accepted_ips" \
  "Top failed user: $top_failed_user" \
  "Top sudo user: $top_sudo_user"
```

Dataset result:

```text
Failed attempts: 11
Accepted attempts: 4
Top failed IP:       6 192.0.2.10
Failed-then-accepted IPs: 192.0.2.11
Top failed user:       4 admin
Top sudo user:       2 analyst
```

Pattern:

```text
compute individual observations
→ store results in shell variables
→ correlate selected event sets
→ print a structured report
```

`uniq -c` pads count values with leading spaces.

Those spaces remain when the entire result line is stored in a variable.

---

## Notes

### Fixed Fields Versus Relative Fields

A fixed field is appropriate when the record format is stable.

Example:

```bash
grep 'sudo\[' auth.log |
awk '{print $6}'
```

A relative field is safer when optional tokens change the field positions.

Example:

```awk
if ($i == "from")
  print $(i + 1)
```

Mental model:

```text
stable format
→ fixed field may be sufficient

variable format
→ locate semantic marker
→ extract relative field
```

---

### Token-Relative Parsing

The most reusable relationships from this session were:

```text
Failed username
→ field before "from"

Source IP
→ field after "from"

Accepted username
→ field after "for"
```

This approach asks:

```text
Which token defines the meaning of the nearby value?
```

rather than:

```text
Which numbered field happened to contain the value in one example?
```

---

### Whole-Record Substring Extraction

Field extraction loses the spaces between later command arguments.

For values that occupy the rest of the record, use `$0`.

```awk
marker_pos = index($0, "COMMAND=")
print substr($0, marker_pos + 8)
```

Pattern:

```text
marker
→ character position
→ remaining substring
```

---

### Ranking Requires Explicit Metric Sorting

This is not sufficient:

```bash
sort |
uniq -c |
head -n1
```

After `uniq -c`, the records must be sorted by the count.

```bash
sort |
uniq -c |
sort -nr |
head -n1
```

Mental model:

```text
grouping
→ counting
→ metric sorting
→ top selection
```

---

### `comm` Requires Sorted Inputs

`comm` compares two sorted streams line by line.

```bash
comm -12 sorted_file_a sorted_file_b
```

Options:

```text
-1 → suppress values unique to the first input
-2 → suppress values unique to the second input
-3 → suppress common values
```

Therefore:

```bash
comm -12
```

prints only common values.

The session used process substitution:

```bash
comm -12 <(pipeline_a) <(pipeline_b)
```

This allowed `comm` to consume pipeline outputs as file-like inputs without
creating temporary files.

Each input used:

```bash
sort -u
```

which combines:

```text
sort
→ uniq
```

---

### Observation Versus Interpretation

Observed:

```text
192.0.2.11 appeared in both failed and successful authentication events.
```

Reasonable interpretation:

```text
The source deserves additional investigation.
```

Unsupported conclusion:

```text
The source definitely compromised the host.
```

Incident-oriented analysis should preserve this boundary:

```text
log evidence
→ verified relationship
→ possible explanations
→ further evidence required
```

---

## Common Mistakes

### Mistake 1

Using different capitalization when storing and reading shell variables.

Incorrect:

```bash
sudo=$(grep -c 'sudo\[' auth.log)
printf '%s\n' "$Sudo"
```

Shell variable names are case-sensitive.

Correct:

```bash
sudo_count=$(grep -c 'sudo\[' auth.log)
printf '%s\n' "$sudo_count"
```

---

### Mistake 2

Supplying a filename to `awk` after piping filtered input.

Incorrect:

```bash
grep 'Failed password' auth.log |
awk '{print}' auth.log
```

The explicit `auth.log` argument causes `awk` to read the file directly.

Correct:

```bash
grep 'Failed password' auth.log |
awk '{print}'
```

Pattern:

```text
command | awk 'program'
→ awk reads standard input

awk 'program' file
→ awk reads file
```

---

### Mistake 3

Starting a new line with a disconnected pipe.

Incorrect:

```bash
command1
| command2
```

Correct:

```bash
command1 |
command2
```

The pipe must remain syntactically connected to the preceding command.

---

### Mistake 4

Searching only for `user` when extracting failed usernames.

Incomplete:

```awk
if ($i == "user")
  print $(i + 1)
```

This handles:

```text
invalid user admin
```

but misses:

```text
for root from
```

Correct relationship:

```awk
if ($i == "from")
  print $(i - 1)
```

---

### Mistake 5

Using `head` before sorting the counts.

Incorrect:

```bash
sort |
uniq -c |
head -n1
```

Correct:

```bash
sort |
uniq -c |
sort -nr |
head -n1
```

---

### Mistake 6

Using commas when a value must contain no separator spaces.

This:

```awk
print $1, ":", $2
```

uses `OFS` between every argument and produces:

```text
09 : 00
```

Concatenation produces:

```awk
print $1 ":" $2
```

Result:

```text
09:00
```

---

### Mistake 7

Using frequency sorting when chronological order is required.

Frequency ranking:

```bash
sort |
uniq -c |
sort -nr
```

Timeline aggregation:

```bash
sort |
uniq -c
```

The final sort depends on the question:

```text
most frequent first
or
time order
```

---

### Mistake 8

Misspelling a variable name.

Stored:

```bash
failed_accpeted=$(...)
```

Read:

```bash
printf '%s\n' "$failed_accepted"
```

The names refer to different variables.

Use a single descriptive name consistently:

```bash
failed_accepted_ips=$(...)
```

---

## Reusable Patterns

Count a specific event:

```bash
grep -c 'event signature' log_file
```

Extract a value after a marker:

```bash
awk '{
  for (i = 1; i <= NF; i++)
    if ($i == "marker")
      print $(i + 1)
}'
```

Extract a value before a marker:

```bash
awk '{
  for (i = 1; i <= NF; i++)
    if ($i == "marker")
      print $(i - 1)
}'
```

Extract everything after a string marker:

```bash
awk '{
  marker_pos = index($0, "MARKER=")

  if (marker_pos)
    print substr($0, marker_pos + length("MARKER="))
}'
```

Rank values:

```bash
extract_values |
sort |
uniq -c |
sort -nr
```

Select the highest-ranked value:

```bash
extract_values |
sort |
uniq -c |
sort -nr |
head -n1
```

Find values common to two event sets:

```bash
comm -12 \
  <(first_pipeline | sort -u) \
  <(second_pipeline | sort -u)
```

Aggregate events by minute:

```bash
filter_events |
awk '{print substr($3, 1, 5)}' |
sort |
uniq -c
```

---

## Final Mental Model

Authentication-log analysis is a sequence of transformations.

```text
raw authentication events
→ classify event type
→ identify semantic markers
→ extract users, IPs, times, or commands
→ aggregate repeated values
→ rank suspicious concentrations
→ correlate failure and success timelines
→ separate evidence from interpretation
```

The central lesson was:

```text
do not depend on accidental field positions
when the log contains optional tokens

instead:

find a stable semantic marker
→ extract the surrounding value
```

Observability becomes incident-oriented analysis when separate event streams
are correlated:

```text
failed authentication
+
successful authentication
+
source identity
+
time order
↓
investigation candidate
```

Correlation identifies what deserves investigation.

It does not by itself prove intent or compromise.

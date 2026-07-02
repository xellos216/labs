# Session04 Notes

## Setup
```bash
mkdir -p app db

for i in {1..10}; do echo "INFO user$((i%3)) ok" > app/app$i.log; done
for i in {1..10}; do echo "ERROR user$((i%3)) fail" > db/db$i.log; done

find . -type f
```

## Task1
Print lines containing "ERROR" from all files

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep "ERROR" */*.log'
awk  'awk "/ERROR/" */*.log'
```

</details>

## Task2
Print lines containing "ERROR" in ./db

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep "ERROR" db/*.log'
awk  'awk "/ERROR/" db/*.log'
```

</details>

## Task3
Extract "user" from all logs

<details>
<summary><strong>Answer</strong></summary>

```bash
awk  'awk "{print \$2}" */*.log'
```

</details>

## Task4
Count occurrences per user across all logs

<details>
<summary><strong>Answer</strong></summary>

```bash
awk  'awk "{print \$2}" */*.log | sort | uniq -c | sort -nr'
```

</details>

## Task5
Count occurrences per user in ERROR logs

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep -h "ERROR" */*.log | awk "{print \$2}" | sort | uniq -c | sort -nr'
awk  'awk "\$1 == \"ERROR\" {print \$2}" */*.log | sort | uniq -c | sort -nr'
```

</details>

## Pattern
- find → grep → awk → sort → uniq -c
- multi-file → filter → extract → count

## Notes
- */*.log = all .log files in subdirectories
- grep -h = suppress filename output
- awk "$1 == \"ERROR\"" = conditional filtering
- awk "{print $2}" = extract the user field
- sort | uniq -c = basic counting pattern

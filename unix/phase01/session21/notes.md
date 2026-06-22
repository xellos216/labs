# Session21 Notes

## Setup
```bash
mkdir -p monitor

cat <<EOF > monitor/events.log
nginx ERROR worker_crash
nginx INFO reload
mysql ERROR connection_fail
sshd WARN auth_retry
redis INFO snapshot
mysql WARN slow_query
EOF

cat monitor/events.log
````

## Task1

Print lines where level is WARN

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$2 == \"WARN\"" monitor/events.log'
```

</details>

## Task2

Extract events only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$3}" monitor/events.log'
```

</details>

## Task3

Count events per service

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" monitor/events.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract events where level is ERROR and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$2 == \"ERROR\" {print \$3}" monitor/events.log | sort | uniq'
```

</details>

## Task5

Extract events where level is WARN or ERROR, then sort by service descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$2 == \"WARN\" || \$2 == \"ERROR\" {print \$1, \$3}" monitor/events.log | sort -k1 -r | awk "{print \$2}"'
```

</details>

## Pattern

* OR condition → preserve sort key → projection
* event/service log parsing

## Notes

* $1 = service
* $2 = level
* $3 = event
* awk "$2 == "WARN" || $2 == "ERROR"" = OR condition filtering
* Each comparison in an OR condition must be written completely
* sort -k1 -r = reverse sort by first field
* keep sort key field until sorting finishes
* final projection after sorting
* uniq = deduplicate
* uniq -c = count
* journalctl / monitoring log parsing basics

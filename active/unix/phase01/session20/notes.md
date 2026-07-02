# Session20 Notes

## Setup
```bash
mkdir -p services

cat <<EOF > services/status.log
nginx active running
mysql failed stopped
sshd active running
docker inactive dead
redis failed stopped
nginx active running
EOF

cat services/status.log
````

## Task1

Print lines where state is failed

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$2 == \"failed\"" services/status.log'
```

</details>

## Task2

Extract service names only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" services/status.log'
```

</details>

## Task3

Count entries per state

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" services/status.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract service names where status is running and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 == \"running\" {print \$1}" services/status.log | sort | uniq'
```

</details>

## Task5

Extract service names where state is failed or inactive, then sort by state descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$2 == \"failed\" || \$2 == \"inactive\" {print \$1, \$2}" services/status.log | sort -k2 -r | awk "{print \$1}"'
```

</details>

## Pattern

* OR condition → preserve sort key → projection
* service state parsing

## Notes

* $1 = service
* $2 = state
* $3 = status
* state != status
* awk "$2 == "failed" || $2 == "inactive"" = OR condition filtering
* Each comparison in an OR condition must be written completely
* sort -k2 -r = reverse sort by second field
* keep sort key field until sorting finishes
* final projection after sorting
* uniq = deduplicate
* uniq -c = count
* systemctl/service monitoring style parsing basics

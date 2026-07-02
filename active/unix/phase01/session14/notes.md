# Session14

## Setup
```bash
mkdir -p service

cat <<EOF > service/journal.log
May01 nginx INFO started
May01 nginx ERROR failed
May02 sshd INFO login
May02 mysql ERROR crash
May03 nginx INFO reload
May03 mysql INFO recovered
EOF

cat service/journal.log
````

## Task1

Print lines where level is ERROR

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep "ERROR" service/journal.log'

awk 'awk "\$3 == \"ERROR\"" service/journal.log'
```

</details>

## Task2

Extract service names only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" service/journal.log'
```

</details>

## Task3

Count entries per service

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" service/journal.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract service names where level is INFO and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 == \"INFO\" {print \$2}" service/journal.log | sort | uniq'
```

</details>

## Task5

Extract service names where level is ERROR, then count

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 == \"ERROR\" {print \$2}" service/journal.log | sort | uniq -c | sort -nr'
```

</details>

## Pattern

* condition → extract → count
* awk status filtering

## Notes

* $1 = date
* $2 = service
* $3 = level
* $4 = message
* awk "$3 == "ERROR"" = status/level filtering
* uniq = deduplicate
* uniq -c = count
* sort -nr = descending numeric sort
* filter first → extract second → aggregate last
* journalctl/systemctl style parsing basics

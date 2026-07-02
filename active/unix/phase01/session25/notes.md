# Phase01 Final Review Notes

## Setup
```bash
mkdir -p review

cat <<EOF > review/system.log
nginx ERROR 500
nginx INFO 200
mysql WARN 300
sshd INFO 100
redis ERROR 700
mysql ERROR 600
EOF

cat review/system.log
````

## Field Structure

```text
$1 = service
$2 = level
$3 = value
```

## Task1

Print ERROR logs only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$2 == \"ERROR\"" review/system.log'
```

</details>

## Task2

Extract service names only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" review/system.log'
```

</details>

## Task3

Count entries per level

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" review/system.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract service names where value is greater than or equal to 500 and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 500 {print \$1}" review/system.log | sort | uniq'
```

</details>

## Task5

Extract service names where level is WARN or ERROR, then sort by value descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$2 == \"WARN\" || \$2 == \"ERROR\" {print \$1, \$3}" review/system.log | sort -k2 -nr | awk "{print \$1}"'
```

</details>

## Task6

Extract service names from ERROR logs, then count occurrences

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$2 == \"ERROR\" {print \$1}" review/system.log | sort | uniq -c | sort -nr'
```

</details>

## Task7

Extract service names where value is greater than or equal to 300, then sort by value descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 300 {print \$1, \$3}" review/system.log | sort -k2 -nr | awk "{print \$1}"'
```

</details>

## Task8

Extract service names from WARN or ERROR logs, then remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$2 == \"WARN\" || \$2 == \"ERROR\" {print \$1}" review/system.log | sort | uniq'
```

</details>

## Phase01 Core Pattern

```text
filter
→ extract
→ preserve fields
→ sort
→ projection
```

## Phase01 Mastered Concepts

* grep line filtering
* awk field extraction
* numeric filtering
* AND conditions
* OR conditions
* sort
* sort -k
* uniq
* uniq -c
* projection timing
* sort key preservation
* pipeline composition

## Notes

* filter first
* extract only what is needed
* keep sort key fields until sorting finishes
* project final output after sorting
* uniq = deduplicate
* uniq -c = count
* OR conditions require complete comparisons

```bash
a == x || a == y
```

* sort -kN selects the sorting field
* sort -nr performs numeric reverse sorting

## Phase01 Outcome

```text
field reasoning
→ filtering
→ extraction
→ counting
→ sorting
→ projection
```

Phase01 Complete.

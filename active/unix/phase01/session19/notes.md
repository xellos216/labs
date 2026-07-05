# Session19 Notes

## Setup
```bash
mkdir -p security

cat <<EOF > security/auth.log
INFO alice login
WARN bob password_fail
ERROR alice sudo_fail
INFO charlie login
ERROR bob sudo_fail
WARN alice password_fail
EOF

cat security/auth.log
````

## Task1

Print lines where level is ERROR

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$1 == \"ERROR\"" security/auth.log'
```

</details>

## Task2

Extract usernames only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" security/auth.log'
```

</details>

## Task3

Count entries per level

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" security/auth.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract usernames where action is password_fail and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 == \"password_fail\" {print \$2}" security/auth.log | sort | uniq'
```

</details>

## Task5

Extract usernames where level is WARN or ERROR, then sort by level descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$1 == \"WARN\" || \$1 == \"ERROR\" {print \$1, \$2}" security/auth.log | sort -k1 -r | awk "{print \$2}"'
```

</details>

## Pattern

* multi-condition → preserve sort key → projection
* security/auth log parsing

## Notes

* $1 = level
* $2 = username
* $3 = action
* awk "$1 == "WARN" || $1 == "ERROR"" = OR condition filtering
* Each comparison in an OR condition must be written completely
* sort -k1 -r = reverse sort by first field
* keep sort key field until sorting finishes
* final projection after sorting
* uniq = deduplicate
* uniq -c = count
* auth.log / sudo log style parsing basics

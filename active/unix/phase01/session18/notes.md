# Session18 Notes

## Setup
```bash
mkdir -p web

cat <<EOF > web/access.log
GET /index 200 nginx
POST /login 500 nginx
GET /admin 403 nginx
GET /index 200 apache
POST /upload 500 apache
GET /health 200 nginx
EOF

cat web/access.log
````

## Task1

Print lines where status code is 500

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep "500" web/access.log'

awk 'awk "\$3 == 500" web/access.log'
```

</details>

## Task2

Extract URL paths only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" web/access.log'
```

</details>

## Task3

Count requests per web server

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$4}" web/access.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract URL paths where status code is greater than or equal to 400 and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 400 {print \$2}" web/access.log | sort | uniq'
```

</details>

## Task5

Extract URL paths where status code is greater than or equal to 400, then sort by status code descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 400 {print \$2, \$3}" web/access.log | sort -k2 -nr | awk "{print \$1}"'
```

</details>

## Pattern

* numeric filtering → preserve sort key → final projection
* HTTP-style log parsing

## Notes

* $1 = method
* $2 = path
* $3 = status
* $4 = server
* awk "$3 >= 400" = numeric status filtering
* sort -k2 -nr = numeric reverse sort by second field
* keep sort key field until sorting finishes
* final projection after sorting
* uniq = deduplicate
* uniq -c = count
* nginx/apache access.log style parsing basics

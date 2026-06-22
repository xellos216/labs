# Session22 Notes

## Setup
```bash
mkdir -p runtime

cat <<EOF > runtime/process.log
nginx worker 12 running
nginx master 3 sleeping
mysql worker 40 running
sshd listener 1 idle
redis worker 25 running
mysql backup 15 stopped
EOF

cat runtime/process.log
````

## Task1

Print lines where status is running

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$4 == \"running\"" runtime/process.log'
```

</details>

## Task2

Extract roles only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" runtime/process.log'
```

</details>

## Task3

Count processes per service

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" runtime/process.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract roles where CPU usage is greater than or equal to 10 and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 10 {print \$2}" runtime/process.log | sort | uniq'
```

</details>

## Task5

Extract roles where status is running, then sort by CPU usage descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$4 == \"running\" {print \$2, \$3}" runtime/process.log | sort -k2 -nr | awk "{print \$1}"'
```

</details>

## Pattern

* status filter → preserve numeric key → projection
* runtime/process parsing

## Notes

* $1 = service
* $2 = role
* $3 = cpu
* $4 = status
* awk "$4 == "running"" = status filtering
* awk "$3 >= 10" = numeric filtering
* sort -k2 -nr = numeric reverse sort by second field
* keep sort key field until sorting finishes
* final projection after sorting
* uniq = deduplicate
* uniq -c = count
* ps/top/htop style parsing basics

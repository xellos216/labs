# Session16 Notes

## Setup
```bash
mkdir -p process

cat <<EOF > process/top.log
root nginx 5 120
root sshd 1 30
alice firefox 40 900
bob vim 2 50
alice python 25 300
bob chrome 60 1100
EOF

cat process/top.log
````

## Task1

Print lines where CPU usage is greater than or equal to 30

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 30" process/top.log'
```

</details>

## Task2

Extract process names only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" process/top.log'
```

</details>

## Task3

Count processes per user

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" process/top.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract process names where MEM usage is greater than or equal to 500 and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$4 >= 500 {print \$2}" process/top.log | sort | uniq'
```

</details>

## Task5

Extract process names where CPU usage is greater than or equal to 20, then sort by CPU usage descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 20 {print \$2, \$3}" process/top.log | sort -k2 -nr | awk "{print \$1}"'
```

</details>

## Pattern

* numeric filter → preserve field → numeric sort
* projection timing

## Notes

* $1 = user
* $2 = process
* $3 = cpu
* $4 = mem
* awk "$3 >= 20" = numeric filtering
* sort -k2 -nr = numeric reverse sort by second field
* projection timing = keep sort key field until sorting finishes
* extract final target field after sorting
* uniq = deduplicate
* uniq -c = count

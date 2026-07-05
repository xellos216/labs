# Session23 Notes

## Setup
```bash
mkdir -p capacity

cat <<EOF > capacity/usage.log
rootfs / 72
homefs /home 91
datafs /data 55
backupfs /backup 97
tmpfs /tmp 12
varfs /var 83
EOF

cat capacity/usage.log
````

## Task1

Print lines where usage is greater than or equal to 90

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 90" capacity/usage.log'
```

</details>

## Task2

Extract mount paths only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" capacity/usage.log'
```

</details>

## Task3

Count entries per filesystem

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" capacity/usage.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract mount paths where usage is greater than or equal to 80 and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 80 {print \$2}" capacity/usage.log | sort | uniq'
```

</details>

## Task5

Extract mount paths where usage is greater than or equal to 80, then sort by usage descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 80 {print \$2, \$3}" capacity/usage.log | sort -k2 -nr | awk "{print \$1}"'
```

</details>

## Pattern

* numeric filter → preserve sort key → projection
* filesystem capacity parsing

## Notes

* $1 = filesystem
* $2 = mount path
* $3 = usage
* awk "$3 >= 80" = numeric filtering
* sort -k2 -nr = numeric reverse sort by second field
* keep sort key field until sorting finishes
* final projection after sorting
* uniq = deduplicate
* uniq -c = count
* filter → preserve fields → sort → projection
* df -h / filesystem usage parsing basics

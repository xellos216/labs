# Session15

## Setup
```bash
mkdir -p storage

cat <<EOF > storage/fs.log
ext4 / 70
ext4 /home 92
xfs /data 55
tmpfs /run 15
ext4 /var 88
xfs /backup 95
EOF

cat storage/fs.log
````

## Task1

Print lines where usage is greater than or equal to 90

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 90" storage/fs.log'
```

</details>

## Task2

Extract filesystem types only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" storage/fs.log'
```

</details>

## Task3

Count entries per filesystem type

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" storage/fs.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract ext4 mount paths and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$1 == \"ext4\" {print \$2}" storage/fs.log | sort | uniq'
```

</details>

## Task5

Extract mount paths where usage is greater than or equal to 80, then sort by usage descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 80 {print \$2, \$3}" storage/fs.log | sort -k2 -nr | awk "{print \$1}"'
```

</details>

## Pattern

* numeric filtering → extract → numeric sort
* condition → print multiple fields

## Notes

* $1 = filesystem type
* $2 = mount path
* $3 = usage
* awk "$3 >= 80" = numeric filtering
* sort -k2 -nr = numeric reverse sort by second field
* sort key field must remain until sorting finishes
* extract final target field after sorting
* uniq = deduplicate
* uniq -c = count

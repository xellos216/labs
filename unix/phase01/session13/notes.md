# Session13 Notes

## Setup
```bash
mkdir -p disk

cat <<EOF > disk/usage.log
root /var 80
root /home 40
alice /home/alice 95
bob /srv 60
alice /tmp 20
bob /home/bob 90
EOF

cat disk/usage.log
````

## Task1

Print lines where usage is greater than or equal to 80

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 80" disk/usage.log'
```

</details>

## Task2

Extract mount paths only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" disk/usage.log'
```

</details>

## Task3

Count mount entries per user

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" disk/usage.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract mount paths where usage is greater than or equal to 80 and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 80 {print \$2}" disk/usage.log | sort | uniq'
```

</details>

## Task5

Extract alice mount paths and sort by usage descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$1 == \"alice\"" disk/usage.log | sort -k3 -nr'

awk-path 'awk "\$1 == \"alice\"" disk/usage.log | sort -k3 -nr | awk "{print \$2}"'
```

</details>

## Pattern

* condition → extract → numeric sort
* filter → print field → sort -nr

## Notes

* $1 = user
* $2 = mount path
* $3 = usage
* awk "$3 >= 80" = numeric condition filtering
* sort -nr = numeric reverse sort
* sort -k3 -nr = sort by third field descending
* uniq = deduplicate
* uniq -c = count
* filter first → extract second → sort last

```
:contentReference[oaicite:0]{index=0}
```

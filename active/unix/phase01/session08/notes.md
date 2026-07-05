# Session08 Notes

## Setup
```bash
mkdir -p reports

cat <<EOF > reports/sales.txt
2026-05-01 alice book 3
2026-05-01 bob pen 10
2026-05-02 alice pen 5
2026-05-02 charlie book 2
2026-05-03 bob book 1
2026-05-03 alice notebook 4
EOF

cat reports/sales.txt
```

## Task1
Print lines containing "alice"

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep "alice" reports/sales.txt'
awk 'awk "\$2 == \"alice\"" reports/sales.txt'
```

</details>

## Task2
Extract product names only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$3}" reports/sales.txt'
```

</details>

## Task3
Count occurrences per product

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$3}" reports/sales.txt | sort | uniq -c | sort -nr'
```

</details>

## Task4
Print lines where sales are greater than or equal to 3

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$4 >= 3" reports/sales.txt'
```

</details>

## Task5
Extract usernames from book sales records and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 == \"book\" {print \$2}" reports/sales.txt | sort | uniq'
```

</details>

## Pattern

- filter → extract → count
- condition → print field → sort → uniq

## Notes

- $1 = date
- $2 = username
- $3 = product
- $4 = quantity
- awk "$4 >= 3" = numeric conditional filtering
- uniq = remove duplicates
- uniq -c = count occurrences
- sort | uniq = basic deduplication pattern

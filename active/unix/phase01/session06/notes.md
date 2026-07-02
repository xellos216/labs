# Session06 Notes

## Setup
```bash
mkdir -p logs

cat <<EOF > logs/access.log
2026-05-01 GET /index 200
2026-05-01 POST /login 500
2026-05-02 GET /admin 403
2026-05-02 GET /index 200
2026-05-03 POST /upload 500
2026-05-03 GET /index 200
EOF

cat logs/access.log
```

## Task1
Print lines with 500 errors

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'find . -name "*.log" -print0 | xargs -0 cat | grep 500'
awk 'find . -name "*.log" -print0 | xargs -0 awk "$4 == 500"'
```

</details>

## Task2
Extract URLs

<details>
<summary><strong>Answer</strong></summary>

```bash
cut 'find . -name "*.log" -print0 | xargs -0 cat | cut -d" " -f3'
awk 'find . -name "*.log" -print0 | xargs -0 awk "{print \$3}"'
```

</details>

## Task3
Count requests per status code

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'find . -name "*.log" -print0 | xargs -0 awk "{print \$4}" | sort | uniq -c | sort -nr'
```

</details>

## Task4
Extract GET request URLs and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'find . -name "*.log" -print0 | xargs -0 awk "\$2 == \"GET\" {print \$3}" | sort | uniq'
```

</details>

## Task5
Extract dates with 500 errors and count occurences

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'find . -name "*.log" -print0 | xargs -0 awk "\$4 == 500 {print \$1}" | sort | uniq -c'
```

</details>

## Pattern
- filter → extract → deduplicate → count
- awk condition → print field → sort → uniq

## Notes
- $1 = date
- $2 = METHOD
- $3 = URL
- $4 = status code
- awk "$4 == 500" = status-code filtering
- awk "{print $3}" = extract the URL
- sort | uniq = remove duplicates
- sort | uniq -c = count occurrences

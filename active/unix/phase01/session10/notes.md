# Session10 Notes

## Setup
```bash
mkdir -p logs

cat <<EOF > logs/auth.log
May01 ssh login success alice
May01 ssh login failed bob
May02 ssh login failed alice
May02 ssh login success charlie
May03 ssh login failed david
May03 ssh login success alice
EOF

cat logs/auth.log
```

## Task1
Print lines containing "failed"

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep "failed" logs/auth.log'
awk 'awk "\$4 == \"failed\"" logs/auth.log'
```

</details>

## Task2
Extract usernames only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$5}" logs/auth.log'
```

</details>

## Task3
Count occurrences per status(success/failed)

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$4}" logs/auth.log | sort | uniq -c | sort -nr'
```

</details>

## Task4
Extract usernames from failed logins and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$4 == \"failed\" {print \$5}" logs/auth.log | sort | uniq'
```

</details>

## Task5
Count failed logins per date

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$4 == \"failed\" {print \$1}" logs/auth.log | sort | uniq -c'
```

</details>

## Pattern

- filter → extract → deduplicate
- condition → print field → count

## Notes

- $1 = date
- $2 = protocol
- $3 = action
- $4 = status
- $5 = username
- uniq = remove duplicates
- uniq -u = values that appear only once
- uniq -c = count occurrences
- filter first, then print only the required fields

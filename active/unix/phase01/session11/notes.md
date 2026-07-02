# Session11 Notes

## Setup
```bash
mkdir -p proc

cat <<EOF > proc/ps.log
root nginx 120
root sshd 30
alice firefox 450
bob vim 20
alice python 200
bob chrome 500
EOF

cat proc/ps.log
```

## Task1
Print line containing "alice"

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$1 == \"alice\"" proc/ps.log'
```

</details>

## Task2
Extract process names only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" proc/ps.log'
```

</details>

## Task3
Count processes per user

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" proc/ps.log | sort | uniq -c | sort -nr'
```

</details>

## Task4
Print lines where memory usage (field 3) is greater than or equal to 100

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 100" proc/ps.log'
```

</details>

## Task5
Extract process names where memory usage (field 3) is greater than or equal to 100 and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 100 {print \$2}" proc/ps.log | sort | uniq'
awk-count 'awk "\$3 >= 100 {print \$2}" proc/ps.log | sort | uniq -c'
```

</details>

## Pattern
- condition → numeric compare → extract
- filter → print field → uniq

## Notes
- $1 = user
- $2 = process
- $3 = memory
- =  → assignment
- == → comparison
- awk "$3 >= 100" = numeric conditional filtering
- uniq = deduplicate
- uniq -c = count
- filter first → extract second

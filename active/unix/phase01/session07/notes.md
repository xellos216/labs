# Session07 Notes

## Setup
```bash
mkdir -p data

cat <<EOF > data/users.txt
alice:admin:active
bob:user:inactive
charlie:user:active
david:admin:inactive
eve:user:active
EOF

cat data/users.txt
```

## Task1
Print lines containing "active"

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep ":active$" data/users.txt'

awk 'awk -F":" "\$3 == \"active\"" data/users.txt'
```

</details>

## Task2
Exctract "username" only

<details>
<summary><strong>Answer</strong></summary>

```bash
cut 'cut -d":" -f1 data/users.txt'

awk 'awk -F":" "{print \$1}" data/users.txt'
```

</details>

## Task3
Replace ":" with spaces

<details>
<summary><strong>Answer</strong></summary>

```bash
sed 'sed "s/:/ /g" data/users.txt'
```

</details>

## Task4
Count occurances per role(admin/user)

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk -F":" "{print \$2}" data/users.txt | sort | uniq -c | sort -nr'
```

</details>

## Task5
Extract usernames from inactive users and convert them to uppercase

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep ":inactive$" data/users.txt | cut -d":" -f1 | tr "a-z" "A-Z"'

awk 'awk -F":" "\$3 == \"inactive\" {print \$1}" data/users.txt | tr "a-z" "A-Z"'
```

</details>

## Pattern
- extract → transform → count
- cut/awk → sed/tr → sort → uniq

## Notes
- $1 = username
- $2 = role
- $3 = status
- sed "s/:/ /g" = string replacement
- tr "a-z" "A-Z" = convert to uppercase
- grep active can also match inactive
- awk field conditions are safer for structured data

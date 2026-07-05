# Session05 Notes

## Setup
```bash
mkdir -p web api

for i in {1..5}; do echo "GET /index$i 200" > web/web$i.log; done
for i in {1..5}; do echo "POST /login$i 500" > api/api$i.log; done

find . -name "*.log"
```

## Task1
Print the contents of all .log files

<details>
<summary><strong>Answer</strong></summary>

```bash
find 'find . -name "*.log" -exec cat {} \;'
xargs 'find . -name "*.log" | xargs cat'
xargs-safe 'find . -name "*.log" -print0 | xargs -0 cat'
```

</details>

## Task2
Print lines containing "500"

<details>
<summary><strong>Answer</strong></summary>

```bash
xargs-safe 'find . -name "*.log" -print0 | xargs -0 cat | grep 500'
awk 'find . -name "*.log" -print0 | xargs -0 awk "$3 == 500"'
```

</details>

## Task3
Extract URL paths

<details>
<summary><strong>Answer</strong></summary>

```bash
cut 'find . -name "*.log" -print0 | xargs -0 cat | cut -d" " -f2'
awk 'find . -name "*.log" -print0 | xargs -0 awk "{print \$2}"'
```

</details>

## Task4
Count requests per HTTP method(GET/POST)

<details>
<summary><strong>Answer</strong></summary>

```bash
cut 'find . -name "*.log" -print0 | xargs -0 cat | cut -d" " -f1 | sort | uniq -c | sort -nr'
awk 'find . -name "*.log" -print0 | xargs -0 awk "{print \$1}" | sort | uniq -c | sort -nr'
```

</details>

## Task5
Extract and sort URLs from 500 error requests

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'find . -name "*.log" -print0 | xargs -0 cat | grep 500 | awk "{print \$2}" | sort'
awk 'find . -name "*.log" -print0 | xargs -0 awk "$3 == 500 {print \$2}" | sort'
```

</details>

## Pattern

- find → xargs → filter → extract
- find → xargs → awk → sort → uniq -c

## Notes

- find = file discovery
- xargs = pass input as command arguments
- -print0 + xargs -0 = safely handle filenames containing spaces
- awk "$3 == 500" = conditional filtering
- awk "{print $2}" = extract the URL
- sort | uniq -c = core counting pattern

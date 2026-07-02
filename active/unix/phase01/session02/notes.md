# Session02 Notes

## Setup
```bash
seq 1 40 | awk '{printf "user%d %s %dms\n", $1%4, ($1%2?"GET":"POST"), int(rand()*200)}' > access.log
cat access.log
```

## Task1
Print GET requests

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep GET access.log'
awk  'awk "$2 == \"GET\"" access.log'
```

</details>

## Task2
Extract the latency value (remove "ms")

<details>
<summary><strong>Answer</strong></summary>

```bash
awk  'awk "{sub(\"ms\",\"\",$3); print $3}" access.log'
```

</details>

## Task3
Print requests where latency is 100 or greater

<details>
<summary><strong>Answer</strong></summary>

```bash
awk  'awk "$3+0 >= 100" access.log'
```

</details>

## Task4
Count requests per user

<details>
<summary><strong>Answer</strong></summary>

```bash
awk  'awk "{print $1}" access.log | sort | uniq -c | sort -nr'
```

</details>

## Task5
For GET requests with latency >= 100, count requests per user

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep GET access.log | awk "$3+0 >= 100 {print $1}" | sort | uniq -c | sort -nr'
awk  'awk "$2 == \"GET\" && $3+0 >= 100 {print $1}" access.log | sort | uniq -c | sort -nr'
```

</details>

## Pattern
- filter → transform → extract → count

## Notes
- $3+0 converts a string to a number
- grep = line filtering / awk = structured processing
- sort | uniq -c is a recurring pattern

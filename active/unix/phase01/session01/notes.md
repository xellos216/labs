# Session01 Notes

## Setup
```bash
seq 1 30 | awk '{printf "user%d,action%d,%d\n", $1%5, $1%3, int(rand()*100)}' > log.txt
cat log.txt
```

## Task1
Print lines containing "action1"

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep action1 log.txt'
awk  'awk -F"," "$2 == \"action1\"" log.txt'
```

</details>

## Task2
Extract the user from each line

<details>
<summary><strong>Answer</strong></summary>

```bash
cut  'cut -d"," -f1 log.txt'
awk  'awk -F"," "{print $1}" log.txt'
```

</details>

## Task3
Count occurrences per user

<details>
<summary><strong>Answer</strong></summary>

```bash
cut  'cut -d"," -f1 log.txt | sort | uniq -c | sort -nr'
awk  'awk -F"," "{print $1}" log.txt | sort | uniq -c | sort -nr'
```

</details>

## Task4
Print lines where the third value is 50 or greater

<details>
<summary><strong>Answer</strong></summary>

```bash
awk  'awk -F"," "$3 >= 50" log.txt'
```

</details>

## Task5
Find the most frequent user

<details>
<summary><strong>Answer</strong></summary>

```bash
awk  'awk -F"," "$2 == \"action1\" && $3 >= 50 {print $1}" log.txt | sort | uniq -c | sort -nr'
```

</details>

## Pattern
- filter → extract → count
- extract → sort → uniq -c → sort

## Notes
- cut = simple field extraction
- awk = conditional and field processing
- use "" for string comparisons
- sort | uniq -c is the core counting pattern

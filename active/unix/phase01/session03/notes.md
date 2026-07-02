# Session03 Notes

## Setup
```bash
mkdir -p file

for i in {1..10}; do
  echo "error user$((i%3)) code$((i%2))" > file/file$(printf "%02d" "$i").log
done

find file -name "*.log" | sort | xargs cat
```

## Task1
Print lines countaining "error" from all .log files

<details>
<summary><strong>Answer</strong></summary>

```bash
grep error file/*.log
awk '/error/' file/*.log
```

</details>

## Task2
Extract users from all files

<details>
<summary><strong>Answer</strong></summary>

```bash
grep user file/*.log
awk '{print $2}' file/*.log
```

</details>

## Task3
Count occurrences per user

<details>
<summary><strong>Answer</strong></summary>

```bash
grep user file/*.log | awk '{print $2}' | sort | uniq -c | sort -nr
awk '{print $2}' file/*.log | sort | uniq -c | sort -nr
```

</details>

## Task4
Print lines containing "code1"

<details>
<summary><strong>Answer</strong></summary>

```bash
grep code1 file/*.log
awk '$3 == "code1"' file/*.log
```

</details>

## Task5
Count users inlines containing "code1"

<details>
<summary><strong>Answer</strong></summary>

```bash
grep code1 file/*.log | awk '{print $2}' | sort | uniq -c | sort -nr
awk '$3 == "code1" {print $2}' file/*.log | sort | uniq -c | sort -nr
```

</details>

## Pattern
- multi-file → filter → extract → count
- file/*.log → grep/awk → awk → sort → uniq -c → sort

## Notes
- file/*.log processes multiple files at once
- grep = line filtering
- awk = field-based processing
- sort | uniq -c = basic counting pattern

# Session09 Notes

## Setup
```bash
mkdir -p metrics

cat <<EOF > metrics/cpu.log
server1 cpu=20 mem=30
server2 cpu=85 mem=70
server3 cpu=40 mem=90
server1 cpu=95 mem=50
server2 cpu=60 mem=40
server3 cpu=88 mem=95
EOF

cat metrics/cpu.log
```

## Task1
Print lines where CPU usage is greater than or equal to 80

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{split(\$2,a,\"=\"); if (a[2] >= 80) print}" metrics/cpu.log'
```

</details>

## Task2
Extract server name only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" metrics/cpu.log'
```

</details>

## Task3
Count occurrences per server

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" metrics/cpu.log | sort | uniq -c | sort -nr'
```

</details>

## Task4
Extract memory values only

<details>
<summary><strong>Answer</strong></summary>

```bash
cut 'awk "{print \$3}" metrics/cpu.log | cut -d"=" -f2'
awk 'awk "{split(\$3,a,\"=\"); print a[2]}" metrics/cpu.log'
```

</details>

## Task5
Extract server names where CPU usage is greater than or equal to 80 and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{split(\$2,a,\"=\"); if (a[2] >= 80) print \$1}" metrics/cpu.log | sort | uniq'
awk-count 'awk "{split(\$2,a,\"=\"); if (a[2] >= 80) print \$1}" metrics/cpu.log | sort | uniq -c'
```

</details>

## Pattern

- field → split("=") → compare → extract
- key=value → cleanup → filter → count

## Notes

- $1 = server
- $2 = cpu=value
- $3 = mem=value
- split(field,array,"=") = split on "="
- a[1] = key / a[2] = value
- uniq = remove duplicates
- uniq -c = count occurrences

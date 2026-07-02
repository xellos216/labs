# Session17 Notes

## Setup
```bash
mkdir -p socket

cat <<EOF > socket/ss.log
tcp LISTEN nginx 80
tcp ESTABLISHED nginx 443
tcp ESTABLISHED sshd 22
udp LISTEN dns 53
tcp LISTEN mysql 3306
tcp ESTABLISHED nginx 443
EOF

cat socket/ss.log
````

## Task1

Print lines where state is ESTABLISHED

<details>
<summary><strong>Answer</strong></summary>

```bash
grep 'grep "ESTABLISHED" socket/ss.log'

awk 'awk "\$2 == \"ESTABLISHED\"" socket/ss.log'
```

</details>

## Task2

Extract service names only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$3}" socket/ss.log'
```

</details>

## Task3

Count entries per state

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" socket/ss.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract service names where protocol is tcp and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$1 == \"tcp\" {print \$3}" socket/ss.log | sort | uniq'
```

</details>

## Task5

Extract service names where state is ESTABLISHED, then sort by port descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$2 == \"ESTABLISHED\" {print \$3, \$4}" socket/ss.log | sort -k2 -nr | awk "{print \$1}"'
```

</details>

## Pattern

* multi-condition → preserve field → numeric sort
* projection after sorting

## Notes

* $1 = protocol
* $2 = state
* $3 = service
* $4 = port
* awk "$2 == "ESTABLISHED"" = state filtering
* sort -k2 -nr = numeric reverse sort by second field
* keep sort key field until sorting finishes
* final projection after sorting
* uniq = deduplicate
* uniq -c = count
* ss/netstat style parsing basics

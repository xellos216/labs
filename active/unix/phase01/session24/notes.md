# Session24 Notes

## Setup
```bash
mkdir -p network

cat <<EOF > network/ports.log
tcp nginx 80 LISTEN
tcp nginx 443 LISTEN
tcp sshd 22 LISTEN
udp dns 53 LISTEN
tcp mysql 3306 LISTEN
tcp nginx 443 ESTABLISHED
EOF

cat network/ports.log
````

## Task1

Print lines where state is LISTEN

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$4 == \"LISTEN\"" network/ports.log'
```

</details>

## Task2

Extract service names only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$2}" network/ports.log'
```

</details>

## Task3

Count entries per protocol

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" network/ports.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract service names where port is greater than or equal to 100 and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 >= 100 {print \$2}" network/ports.log | sort | uniq'
```

</details>

## Task5

Extract service names where state is LISTEN, then sort by port descending

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$4 == \"LISTEN\" {print \$2, \$3}" network/ports.log | sort -k2 -nr | awk "{print \$1}"'
```

</details>

## Pattern

* status filter → preserve sort key → numeric sort → projection
* network socket parsing

## Notes

* $1 = protocol
* $2 = service
* $3 = port
* $4 = state
* awk "$4 == "LISTEN"" = state filtering
* awk "$3 >= 100" = numeric filtering
* sort -k2 -nr = numeric reverse sort by second field
* keep sort key field until sorting finishes
* final projection after sorting
* uniq = deduplicate
* uniq -c = count
* filter → preserve fields → sort → projection
* ss -tulpn / netstat style parsing basics

# Session12

## Setup
```bash
mkdir -p net

cat <<EOF > net/connections.log
tcp 22 LISTEN sshd
tcp 80 LISTEN nginx
tcp 443 ESTABLISHED nginx
udp 53 LISTEN dns
tcp 22 ESTABLISHED sshd
tcp 3306 LISTEN mysql
EOF

cat net/connections.log
````

## Task1

Print lines where state is LISTEN

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 == \"LISTEN\"" net/connections.log'
```

</details>

## Task2

Extract service names only

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$4}" net/connections.log'
```

</details>

## Task3

Count connections per protocol

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "{print \$1}" net/connections.log | sort | uniq -c | sort -nr'
```

</details>

## Task4

Extract service names where state is ESTABLISHED and remove duplicates

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$3 == \"ESTABLISHED\" {print \$4}" net/connections.log | sort | uniq'
```

</details>

## Task5

Extract service names where protocol is tcp and state is LISTEN, then count

<details>
<summary><strong>Answer</strong></summary>

```bash
awk 'awk "\$1 == \"tcp\" && \$3 == \"LISTEN\" {print \$4}" net/connections.log | sort | uniq -c | sort -nr'
```

</details>

## Pattern

* multiple conditions → extract → count
* awk AND condition

## Notes

* $1 = protocol
* $2 = port
* $3 = state
* $4 = service
* awk "$1 == "tcp" && $3 == "LISTEN"" = AND condition filtering
* uniq = deduplicate
* uniq -c = count
* filter first → extract second
* ss -tulpn style parsing basics

```text
:contentReference[oaicite:0]{index=0}
```

# Service Guessing

## Session Goal

Understand that port numbers provide service hints, not proof.

Extend the scanner to display a common service guess next to each port.

## Core Idea

```text
Open Port
↓
Port Number
↓
Common Service Guess
````

Example:

```text
22   -> SSH
80   -> HTTP
443  -> HTTPS
```

This is only a guess.

Real confirmation requires banner grabbing or protocol behavior observation.

## Current Scanner

Current output:

```text
127.0.0.1:22 closed
127.0.0.1:80 closed
127.0.0.1:443 closed
127.0.0.1:4212 open
```

New target output:

```text
127.0.0.1:22 closed ssh
127.0.0.1:80 closed http
127.0.0.1:443 closed https
127.0.0.1:4212 open unknown
```

## New Concept: Dictionary

A dictionary maps one value to another.

```python
common_ports = {
    22: "ssh",
    80: "http",
    443: "https",
}
```

Think:

```text
Port Number
↓
Service Guess
```

## Lookup

```python
service = common_ports.get(port, "unknown")
```

Meaning:

```text
If port exists in dictionary:
    return service name

If port does not exist:
    return "unknown"
```

## Build Plan

Add this near the top:

```python
common_ports = {
    21: "ftp",
    22: "ssh",
    53: "dns",
    80: "http",
    443: "https",
    3306: "mysql",
    5432: "postgresql",
    6379: "redis",
    8000: "http-alt",
    8080: "http-alt",
}
```

Inside `scan_port()`:

```python
service = common_ports.get(port, "unknown")
```

Then change output from:

```python
print(f"{host}:{port} open")
```

to:

```python
print(f"{host}:{port} open {service}")
```

Do the same for `closed` and `timeout`.

## Prediction

Before editing, predict:

```python
common_ports = {
    22: "ssh",
    80: "http",
    443: "https",
}

print(common_ports.get(22, "unknown"))
print(common_ports.get(4212, "unknown"))
```

Expected output:

```text
?
?
```

## QA

**Q1.**

What does service guessing add to the scanner?

<details>
<summary><strong>A1.</strong></summary>

</details>

---

**Q2.**

Why is `22 -> ssh` only a guess, not proof?

<details>
<summary><strong>A2.</strong></summary>

</details>

---

**Q3.**

What does a Python dictionary store?

<details>
<summary><strong>A3.</strong></summary>

</details>

---

**Q4.**

What does this return?

```python
common_ports.get(443, "unknown")
```

<details>
<summary><strong>A4.</strong></summary>

</details>

---

**Q5.**

What does this return if `4212` is not in the dictionary?

```python
common_ports.get(4212, "unknown")
```

<details>
<summary><strong>A5.</strong></summary>

</details>

---

**Q6.**

What is the difference between service guessing and banner grabbing?

<details>
<summary><strong>A6.</strong></summary>

</details>

---

**Q7.**

Complete:

```text
Port Number
↓
Common Service ______
```

<details>
<summary><strong>A7.</strong></summary>

</details>

---

**Q8.**

In one sentence, explain why service guessing is useful but limited.

<details>
<summary><strong>A8.</strong></summary>

</details>


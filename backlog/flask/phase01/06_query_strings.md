# Session 06 Notes

## Query Strings

A query string provides additional data in a URL.

Example:

```text
/search?q=flask
```

Contains:

- Path → `/search`
- Query String → `q=flask`

---

## Route Matching

Flask matches routes using:

Method + Path

Example:

```text
GET /search?q=flask
GET /search?page=2
```

Both match:

```python
@app.route("/search")
```

Because the Path is the same.

---

## request.path

```python
request.path
```

Returns the requested path.

Example:

```text
/search
```

---

## request.args

```python
request.args
```

Returns query string parameters.

Example:

```text
/search?q=flask&page=2
```

Behaves similarly to:

```python
{
    "q": "flask",
    "page": "2"
}
```

Internally Flask uses an ImmutableMultiDict.

---

## request.args.get()

```python
request.args.get("q")
```

Returns:

```text
flask
```

from:

```text
/search?q=flask
```

---

## Default Values

```python
request.args.get("q", "")
```

If `q` does not exist:

```python
""
```

is returned.

Example:

```text
/search
```

↓

```python
request.args.get("q", "")
```

↓

```text
""
```

---

## Observation

```text
/search?q=flask
```

↓

```python
request.path
```

↓

```text
/search
```

---

```python
request.args
```

↓

```python
{"q": "flask"}
```

---

```text
/search?page=2
```

↓

```python
request.path
```

↓

```text
/search
```

---

```python
request.args
```

↓

```python
{"page": "2"}
```

---

## Security Insight

Query string values are client-controlled.

Users can modify:

```text
?q=flask
?page=2
?id=100
```

before the request reaches the server.

Servers must validate and handle missing or unexpected values safely.

---

# Flask Web Security Foundations
## Phase 01
### Session 06

**Q1.**
What is a query string?

<details>
<summary>A1.</summary>

</details>

---

**Q2.**
What is the difference between a URL path and a query string?

<details>
<summary>A2.</summary>

</details>

---

**Q3.**
What does `request.path` return?

<details>
<summary>A3.</summary>

</details>

---

**Q4.**
What does `request.args` contain?

<details>
<summary>A4.</summary>

</details>

---

**Q5.**
What does `request.args.get("q")` return when the URL is:

```text
/search?q=flask
```

<details>
<summary>A5.</summary>

</details>

---

**Q6.**
What happens when `request.args.get("q")` is called but `q` does not exist?

<details>
<summary>A6.</summary>

</details>

---

**Q7.**
What is the purpose of providing a default value to `.get()`?

<details>
<summary>A7.</summary>

</details>

---

**Q8.**
Do query string values affect Flask route matching?

<details>
<summary>A8.</summary>

</details>

---

**Q9.**
Why should a server not blindly trust query string values?

<details>
<summary>A9.</summary>

</details>

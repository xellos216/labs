# Session 03 Notes

## HTTP Request Structure

HTTP Request

- Request Line
- Headers
- Body (optional)

---

## Request Line

Example:

GET /about HTTP/1.1

Contains:

- Method
- Path
- HTTP Version

---

## Flask Request Object

```python
request.method
```

Returns the HTTP method.

```python
request.path
```

Returns the requested path.

```python
request.headers
```

Returns request headers.

---

## Observation

Headers can be viewed and inspected inside Flask.

Custom headers can be sent with curl.

---

## Security Insight

HTTP headers are client-supplied data.

Servers should validate important information and avoid blindly trusting header values.

---

# Flask Web Security Foundations
## Phase 01
### Session 03

**Q1.**
What are the main components of an HTTP request?

<details>
<summary>A1.</summary>

Request Line, Headers, Body(optional)

</details>

---

**Q2.**
What information does `request.method` provide?

<details>
<summary>A2.</summary>

HTTP method

</details>

---

**Q3.**
What information does `request.path` provide?

<details>
<summary>A3.</summary>

HTTP path

</details>

---

**Q4.**
What is the difference between a Request Line and HTTP Headers?

<details>
<summary>A4.</summary>

Request line contains: method, path, http version
headers version: host, user-agent, accept, custom headers

</details>

---

**Q5.**
What does `request.headers` contain?

<details>
<summary>A5.</summary>

All HTTP headers

</details>

---

**Q6.**
Can a user modify HTTP headers?

<details>
<summary>A6.</summary>

Yes

</details>

---

**Q7.**
Why should a server not blindly trust header values?

<details>
<summary>A7.</summary>

Because headers are supplied by the client, they can be modified before reaching the server.

</details>

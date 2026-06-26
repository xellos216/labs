# Session 01 Notes

## Core Model

Browser
→ HTTP Request
→ Flask
→ HTTP Response
→ Browser Rendering

---

## Request

Client asks for a resource.

Example:

GET /

---

## Response

Server returns data.

Example:

200 OK

Hello Flask

---

## Flask Route

```python
@app.route("/")
```

Maps a URL path to a Python function.

---

## Observation

```bash
curl http://127.0.0.1:5000
```

Creates an HTTP request.

Flask receives the request and generates a response.

---

## Security Insight

Clients do not receive Python source code.

Clients only receive the server's response.

Server-side code remains on the server.

---

# Flask Web Security Foundations
## Phase 01
### Session 01

**Q1.** What does a browser send first when communicating with a web server?

<details>
<summary>A1.</summary>

HTTP Request

</details>

---

**Q2.** What is the difference between an HTTP Request and an HTTP Response?

<details>
<summary>A2.</summary>

HTTP Request: client -> server, HTTP Response: server -> client

</details>

---

**Q3.** What does `@app.route("/")` mean in Flask?

<details>
<summary>A3.</summary>

Maps a URL path to a Python function

</details>

---

**Q4.** What happens inside Flask when a browser visits `http://127.0.0.1:5000`?

<details>
<summary>A4.</summary>

The browser sends a GET / request.

Flask receives the request.

Flask executes the home() function.

home() returns "Hello Flask".

Flask creates an HTTP Response.

The browser receives the response.

</details>

---

**Q5.** What does each part of the following Flask log output mean?

`GET / HTTP/1.1 200`

<details>
<summary>A5.</summary>

GET -> HTTP method

/ -> request path

HTTP/1.1 -> HTTP version

200 -> response status code

</details>

---

**Q6.** Does the browser receive Python source code directly?

<details>
<summary>A6.</summary>

No, it does not receive it directly.

</details>

---

**Q7.** What does the browser actually receive?

<details>
<summary>A7.</summary>

Hello Response

</details>

---

**Q8.** Why is server code not directly exposed to the client?

<details>
<summary>A8.</summary>

Python code runs inside the server process. The browser sends an HTTP request to the server and only receives the HTTP response produced by that execution. Therefore, server code is not directly exposed.

</details>

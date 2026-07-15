# Session 05

## HTTP Methods

Methods describe the intent of a request.

---

## GET

Typically used for:

- Reading
- Viewing
- Retrieving resources

Example:

```http
GET /about HTTP/1.1
```

---

## POST

Typically used for:

- Sending data
- Submitting forms
- Creating resources

Example:

```http
POST /login HTTP/1.1
```

---

## Flask Route Methods

```python
@app.route("/submit", methods=["POST"])
```

Allows only POST requests.

---

## Route Selection

Flask matches:

Method + Path

Example:

GET /login

is different from

POST /login

---

## Common Status Code

405 METHOD NOT ALLOWED

Path exists.

Method is not allowed.

---

## Observation

```bash
curl http://127.0.0.1:5000/submit
```

↓

```http
HTTP/1.1 405 METHOD NOT ALLOWED
```

---

```bash
curl -X POST http://127.0.0.1:5000/submit
```

↓

```text
Method: POST
Submitted
```

---

## Security Insight

HTTP methods are client-controlled.

Clients can choose:

- GET
- POST
- PUT
- DELETE

Servers must validate both:

- Method
- Path

and should not assume clients behave as expected.

---

# QA

**Q1.**
What is the main purpose of the GET method?

<details>
<summary>A1.</summary>

</details>

---

**Q2.**
What is the main purpose of the POST method?

<details>
<summary>A2.</summary>

</details>

---

**Q3.**
How does Flask choose a route when methods are involved?

<details>
<summary>A3.</summary>

</details>

---

**Q4.**
Why does a GET request to a POST-only route fail?

<details>
<summary>A4.</summary>

</details>

---

**Q5.**
What does HTTP 405 Method Not Allowed mean?

<details>
<summary>A5.</summary>

</details>

---

**Q6.**
Can a client choose which HTTP method to send?

<details>
<summary>A6.</summary>

</details>

---

**Q7.**
Why should a server not blindly assume clients will use the expected method?

<details>
<summary>A7.</summary>

</details>

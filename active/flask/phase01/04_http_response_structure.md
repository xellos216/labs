# Session 04 Notes

## HTTP Response Structure

HTTP Response

- Status Line
- Headers
- Body

---

## Status Line

Example:

HTTP/1.1 200 OK

Contains:

- HTTP Version
- Status Code
- Status Message

---

## Response Headers

Example:

Content-Type: text/html

Describe the response.

---

## Response Body

The actual content returned to the client.

Example:

Hello Flask

---

## Observation

```bash
curl -i http://127.0.0.1:5000
```

Displays:

- Status Line
- Headers
- Body

---

## Common Status Codes

200 OK

Request succeeded.

404 NOT FOUND

Route does not exist.

500 INTERNAL SERVER ERROR

Server-side failure.

---

## Security Insight

Status codes reveal information about server behavior.

Clients can learn whether a resource exists or whether an error occurred.

---

# Flask Web Security Foundations
## Phase 01
### Session 04

**Q1.**
What are the main components of an HTTP response?

<details>
<summary>A1.</summary>
Status line, Headers, Body</details>

---

**Q2.**
What information does the Status Line contain?

<details>
<summary>A2.</summary>

HTTP version, Status code, Status message</details>

---

**Q3.**
What is the purpose of Response Headers?

<details>
<summary>A3.</summary>
Response headers describe the response.
Content-type, Content-length, Server, Date</details>


---

**Q4.**
What is the Response Body?

<details>
<summary>A4.</summary>
The actual content returned to the client.</details>


---

**Q5.**
What does `curl -i` show that a normal browser page usually hides?

<details>
<summary>A5.</summary>
Status Line, Headers, Body</details>


---

**Q6.**
Why does Flask return a 404 response for an unknown route?

<details>
<summary>A6.</summary>
Flask has no route matching the requested path.</details>


---

**Q7.**
Does a browser receive only the response body?

<details>
<summary>A7.</summary>

The browser receives: Status Line, Headers, Body</details>

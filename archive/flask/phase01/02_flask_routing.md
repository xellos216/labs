# Session 02 Notes

## Routing

Routing maps URL paths to Python functions.

Example:

/ → home()

/about → about()

/contact → contact()

---

## Route Decorator

```python
@app.route("/about")
```

Registers a URL path.

---

## URL Mapping

Path
→ Function

Flask uses the request path to decide which function to execute.

---

## Observation

```http
GET /about HTTP/1.1
```

Contains:

- Method
- Path
- HTTP Version

---

## Security Insight

URL paths are user-controlled.

A user can manually request:

/admin
/profile
/settings

The server must decide whether access is allowed.

---

# Flask Web Security Foundations
## Phase 01
### Session 02

**Q1.**
Why does Flask need routing?

<details>
<summary>A1.</summary>

Routing maps URL paths to Python function

</details>

---

**Q2.**
What does `@app.route("/about")` mean?

<details>
<summary>A2.</summary>

When an /about request comes in, execute the about() function.

</details>

---

**Q3.**
What information in an HTTP request helps Flask choose a route?

<details>
<summary>A3.</summary>

Path

</details>

---

**Q4.**
When a browser requests `/contact`, which function should Flask execute?

<details>
<summary>A4.</summary>

contact()

</details>

---

**Q5.**
What is URL mapping?

<details>
<summary>A5.</summary>

Path -> Function,

Flask uses the request path to decide which function to execute.

</details>

---

**Q6.**
Can a user request any URL path manually?

<details>
<summary>A6.</summary>

URL paths are user-controlled

</details>

---

**Q7.**
Why is user-controlled URL access important for security?

<details>
<summary>A7.</summary>

Users can manually request routes that developers did not intend them to access.

Therefore the server must verify whether access is allowed.

</details>

# HTTP

## Metadata

```yaml
Roadmap: Networking
Phase: 01
Session: 09
Title: HTTP
Status:
Review:
ArchiveVersion: 2
Date:
```

## Why HTTP Exists

DNS finds addresses.

IP identifies machines.

Routing finds paths.

TCP provides reliable delivery.

HTTP provides rules for requesting and delivering web resources.

## Core Problem

After reaching a server:

How does a client ask for specific content?

HTTP solves this problem.

## Mental Model

TCP = Reliable Pipe

HTTP = Request/Response Rules

## Request

A request asks for a resource.

Examples:

GET /

GET /index.html

GET /images/logo.png

## Response

A response contains:

- status information
- headers
- content

## Common Status Codes

200 = Success

404 = Resource not found

500 = Server error

## Observation Principle

Before memorizing status codes, ask:

- What did the client request?
- What did the server understand?
- Why did the server respond that way?

# Review Questions

### Q1. What problem does HTTP solve?

<details>
<summary>A</summary>

HTTP provides rules for requesting and delivering web resouces.

</details>

---

### Q2. Why are DNS, IP, Routing, and TCP insufficient for web communication?

<details>
<summary>A</summary>

DNS, IP, Routing, and TCP can establish communication, but they do not define how web resources should be requested or delivered.

</details>

---

### Q3. What is an HTTP request?

<details>
<summary>A</summary>

method, path, headers

</details>

---

### Q4. What is an HTTP response?

<details>
<summary>A</summary>

status code, headers, content

</details>

---

### Q5. Why does a browser need to specify a path such as "/"?

<details>
<summary>A</summary>

Without a path, the server would not know which resource the client wants.

</details>

---

### Q6. Why might a server return a 404 response?

<details>
<summary>A</summary>

A server returns a 404 response when the requested resource does not exist.

</details>

---

### Q7. Why is HTTP often described as a request/response protocol?

<details>
<summary>A</summary>

Because HTTP is structured around a client sending a request and a server returning a response.

The sever usually does not send content by itself  first; it responds to what the client asked for.

</details>

---

### Q8. How does HTTP relate to the networking concepts learned previously?

<details>
<summary>A</summary>

HTTP uses DNS, IP, Routing, and TCP to reach a server, then defines how web resources are requested and delivered.

</details>

# Flask Web Security Foundations

---

# Philosophy

This roadmap uses Flask as a learning laboratory for:

- HTTP understanding
- Request/Response flow
- Browser behavior
- Server-side processing
- Authentication concepts
- Session management
- Input handling
- Web security fundamentals

Goal:

Understand normal web behavior first.

Then learn:

- Why vulnerabilities happen
- What assumptions developers make
- How attackers abuse those assumptions
- How to design safer applications

Practice environment:

- Local machine only
- Flask
- Python
- Browser
- curl
- Developer Tools
- SQLite

---

# Phase 01
## HTTP and Flask Fundamentals

Goal:

Understand how browsers communicate with Flask.

---

### Session 01
What happens when a browser sends a request to Flask?

Topics:

- Request
- Response
- Flask server
- curl
- HTTP observation

---

### Session 02
What is a Route and why does URL mapping exist?

Topics:

- URL paths
- Routing
- Multiple routes
- Request targeting

---

### Session 03
What is actually inside an HTTP request?

Topics:

- Method
- Path
- Headers
- Body

Observation:

- Browser request
- curl request

---

### Session 04
Understanding HTTP responses

Topics:

- Status codes
- Headers
- Response body

Codes:

- 200
- 301
- 302
- 403
- 404
- 500

---

### Session 05
GET vs POST

Topics:

- Safe requests
- State-changing requests
- Form submission

Security preview:

- Why method confusion matters

---

### Session 06
Observing Flask request objects

Topics:

- request.method
- request.path
- request.headers

---

### Session 07
Building a request inspector

Project:

Create a page that displays:

- Method
- Path
- Headers
- User-Agent

Security observation:

- User-controlled metadata

---

### Session 08
Phase Review

Mini Project:

HTTP Observation Lab

---

# Phase 02
## Templates and User Input

Goal:

Understand how user data reaches server code.

---

### Session 01
Introduction to Templates

Topics:

- Jinja2
- HTML rendering
- Dynamic pages

---

### Session 02
Variables inside templates

Topics:

- Template rendering
- Context passing

---

### Session 03
Receiving URL parameters

Topics:

- Query strings
- request.args

Examples:

```text
/search?q=test
```

---

### Session 04
Route parameters

Topics:

```text
/user/alice
```

```python
@app.route("/user/<name>")
```

---

### Session 05
HTML Forms

Topics:

- Input fields
- Form submission
- Browser behavior

---

### Session 06
Handling POST data

Topics:

- request.form
- User input processing

---

### Session 07
Building a local message board

Features:

- Submit message
- Display messages

---

### Session 08
Phase Review

Mini Project:

Simple Guestbook

---

# Phase 03
## Cookies and Sessions

Goal:

Understand state in web applications.

---

### Session 01
Why HTTP is stateless

Topics:

- Request independence
- Stateless design

---

### Session 02
Cookies

Topics:

- Set-Cookie
- Browser storage

Observation:

Developer Tools

---

### Session 03
Flask cookies

Topics:

- set_cookie()
- get_cookie()

---

### Session 04
Sessions

Topics:

- session object
- User state

---

### Session 05
Tracking a visitor

Project:

Visit counter

---

### Session 06
Login state simulation

Topics:

- Logged-in user
- Session tracking

---

### Session 07
Session lifecycle

Topics:

- Creation
- Modification
- Expiration

---

### Session 08
Phase Review

Mini Project:

State Tracking Lab

---

# Phase 04
## Authentication Fundamentals

Goal:

Understand how login systems work.

---

### Session 01
What is authentication?

Topics:

- Identity
- Credentials

---

### Session 02
Building a local login form

Topics:

- Username
- Password

---

### Session 03
Authentication flow

Topics:

- Login request
- Validation
- Session creation

---

### Session 04
Protected routes

Topics:

- Access control

---

### Session 05
Logout flow

Topics:

- Session destruction

---

### Session 06
Role concepts

Topics:

- User
- Admin

---

### Session 07
Building a complete local login system

---

### Session 08
Phase Review

Mini Project:

Authentication Lab

---

# Phase 05
## Database Fundamentals

Goal:

Understand persistence.

---

### Session 01
Why databases exist

Topics:

- Memory vs storage

---

### Session 02
SQLite introduction

Topics:

- Tables
- Rows
- Columns

---

### Session 03
Flask + SQLite

Topics:

- Database connections

---

### Session 04
Creating users

Topics:

- Insert
- Select

---

### Session 05
Displaying records

Topics:

- Dynamic rendering

---

### Session 06
Updating records

Topics:

- CRUD

---

### Session 07
Deleting records

Topics:

- Data lifecycle

---

### Session 08
Phase Review

Mini Project:

User Management System

---

# Phase 06
## Security Foundations

Goal:

Understand why vulnerabilities happen.

No exploitation focus.

Understanding focus.

---

### Session 01
Trust boundaries

Topics:

- Client
- Server

---

### Session 02
Input validation

Topics:

- Expected input
- Unexpected input

---

### Session 03
Authentication mistakes

Topics:

- Missing checks
- Logic flaws

---

### Session 04
Authorization basics

Topics:

- Identity
- Permissions

---

### Session 05
IDOR concepts

Topics:

- Object ownership
- Resource access

Normal behavior first

---

### Session 06
Session security concepts

Topics:

- Session trust
- Session misuse

---

### Session 07
Security review lab

Topics:

- Finding weak assumptions

---

### Session 08
Phase Review

Mini Project:

Secure vs Insecure Design Comparison

---

# Phase 07
## XSS Foundations

Goal:

Understand browser-side trust.

---

### Session 01
How browsers render HTML

---

### Session 02
User input in pages

---

### Session 03
Template rendering behavior

---

### Session 04
Escaping

Topics:

- Why escaping exists

---

### Session 05
Unsafe rendering concepts

Topics:

- Trust mistakes

---

### Session 06
Stored vs Reflected concepts

High-level understanding only

---

### Session 07
Safe output handling

---

### Session 08
Phase Review

Mini Project:

Input Rendering Lab

---

# Phase 08
## SQL Injection Foundations

Goal:

Understand query construction.

---

### Session 01
How SQL queries work

---

### Session 02
Building queries safely

---

### Session 03
Parameterized queries

---

### Session 04
Unsafe query construction

Conceptual analysis

---

### Session 05
Input interpretation

Topics:

- Data vs commands

---

### Session 06
Database trust boundaries

---

### Session 07
Secure query design

---

### Session 08
Phase Review

Mini Project:

Database Security Lab

---

# Phase 09
## Authorization and IDOR

Goal:

Understand resource ownership.

---

### Session 01
User-owned resources

---

### Session 02
Profile pages

---

### Session 03
Object identifiers

---

### Session 04
Authorization checks

---

### Session 05
Ownership validation

---

### Session 06
Designing safer routes

---

### Session 07
Resource access review

---

### Session 08
Phase Review

Mini Project:

Access Control Lab

---

# Phase 10
## Flask Security Review Project

Goal:

Combine everything learned.

---

### Session 01
Architecture review

---

### Session 02
Request flow review

---

### Session 03
Authentication review

---

### Session 04
Session review

---

### Session 05
Database review

---

### Session 06
Input handling review

---

### Session 07
Security review

---

### Session 08
Final Project

Secure Local Flask Portal

Features:

- Login
- Sessions
- SQLite
- Templates
- User Profiles
- Access Control
- Input Validation
- Logging

Final Outcome:

You can explain:

- Browser → Server communication
- HTTP requests
- Routing
- Forms
- Cookies
- Sessions
- Authentication
- Authorization
- XSS fundamentals
- SQL Injection fundamentals
- IDOR fundamentals
- Secure design principles

before moving into larger frameworks or dedicated web-security labs.

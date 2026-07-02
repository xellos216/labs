# Final Review

## Goal

Validate that the complete Phase01 mental model exists.

The objective is not remembering commands.

The objective is reasoning about:

```text
input
↓
parser
↓
execution graph
↓
process graph
↓
FD graph
↓
runtime behavior
```

---

# Core Mental Models

## Model 1 — Parser World

Parser responsibilities:

```text
tokenization
expansion
syntax recognition
execution graph construction
```

Examples:

```text
|
>
&
quotes
variables
$( )
```

Important:

```text
parser
≠
execution
```

---

## Model 2 — Process World

Process responsibilities:

```text
fork
exec
wait
signals
ownership
lifecycle
```

Important:

```text
process
≠
command text
```

Commands become processes.

---

## Model 3 — FD World

FD responsibilities:

```text
stdin
stdout
stderr
pipe
redirection
```

Important:

```text
FD
=
communication path
```

---

## Model 4 — Runtime World

Runtime responsibilities:

```text
execution
data flow
signals
termination
```

Examples:

```text
SIGINT
SIGTERM
SIGKILL
SIGPIPE
```

Important:

```text
runtime
begins after exec
```

---

# Integration Example

Command:

```bash
cat file.txt | grep root > out.txt
```

Parser graph:

```text
pipeline
+
redirection
```

Process graph:

```text
cat
→ grep
```

FD graph:

```text
cat FD1
→ pipe
→ grep FD0

grep FD1
→ out.txt
```

Runtime:

```text
concurrent execution
data flow
process exit
```

---

# Phase01 Final Summary

Phase01 progression:

```text
input
→ tokenization
→ expansion
→ parser decisions
→ execution graph
→ pipe creation
→ FD rewiring
→ fork
→ exec
→ running processes
→ data flow
→ signals
→ exit
```

---

# What Phase01 Was Really About

Not:

```text
learning shell commands
```

But:

```text
understanding
how text becomes behavior
```

---

# Phase02 Preview

Phase02 focus:

```text
filter evasion
payload mutation
parser confusion
encoding tricks
blacklist bypass
```

Phase02 assumes the Phase01 model is stable.

Without Phase01:

```text
payloads
=
magic strings
```

With Phase01:

```text
payloads
=
parser manipulation
```

---

# Final Question

Whenever you see a payload, ask:

```text
What parser sees this?

What execution graph is created?

What processes will exist?

How will FDs be connected?

What runtime behavior will occur?
```

# QA

## Parser and Execution Graph

Consider:

```sh
printf '%s\n' "$HOME" | grep home >result.txt 2>errors.txt &
```

**Q1. What syntax does the parser identify?**

<details>
<summary><strong>A1.</strong></summary>
'', "", |, >, 2>, &


</details>

---

**Q2. What execution structure is created?**

<details>
<summary><strong>A2.</strong></summary>
printf -> grep 
</details>

---

**Q3. Why are `|` and `>` not string arguments?**

<details>
<summary><strong>A3.</strong></summary>
Because they are parser syntax that changes the execution structure.

'|' creates a pipeline.

'>' changes the stdout target.</details>

---

## Process Count

Consider:

```sh
cat input.txt | grep token | wc -l
```

**Q4. How many command processes are expected?**

<details>
<summary><strong>A4.</strong></summary>
3

</details>

---

**Q5. Draw the process graph.**

<details>
<summary><strong>A5.</strong></summary>
cat -> grep -> wc
</details>

---

**Q6. Why distinguish the parser graph from the process graph?**

<details>
<summary><strong>A6.</strong></summary>
Because they represent different layers.
The parser graph describes command structure.
The process graph describes the actual running processes.


</details>

---

## Descriptor Flow

**Q7. Which descriptor normally enters a pipe?**

<details>
<summary><strong>A7.</strong></summary>
FD1

</details>

---

**Q8. Which descriptor normally receives pipe data?**

<details>
<summary><strong>A8.</strong></summary>
FD0

</details>

---

**Q9. Does stderr enter a normal pipe automatically?**

<details>
<summary><strong>A9.</strong></summary>
No.
stderr(FD2) does not automatically enter a normal pipe.
By default, stderr is usually connected to the terminal.


</details>

---

## Resolution and State

**Q10. Why can `cd` change the current shell but an external child cannot?**

<details>
<summary><strong>A10.</strong></summary>
Because changes made in a child process cannot propagate back to the parent shell.
The current working directory belongs to the parent shell's execution context.


</details>

---

**Q11. Why can a command name resolve differently across environments?**

<details>
<summary><strong>A11.</strong></summary>
Because command resolution depends on the environment.
PATH, aliases, functions, and builtins can all affect how a command name is resolved.

</details>

---

**Q12. Why should verification use explicit command paths and controlled environments?**

<details>
<summary><strong>A12.</strong></summary>
Because explicit paths remove resolution ambiguity.
Using absolute paths helps avoid differences caused by PATH, aliases functions, or builtins.

</details>

---

## Final Mental Model

```text
parse
-> expand
-> split and glob
-> resolve commands
-> create pipes and redirections
-> create processes
-> execute
-> observe streams, signals, and status
```

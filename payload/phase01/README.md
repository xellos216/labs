# Phase01

## Goal

Validate that the complete Phase01 mental model exists.

The objective is not remembering commands.

The objective is understanding how text becomes behavior.

---

# The Full Model

```text
input
→ parser
→ expansion
→ parser decisions
→ execution graph
→ pipe creation
→ FD rewiring
→ fork
→ exec
→ runtime execution
→ signals
→ termination
```

---

# 1. Input

Input is raw user-controlled text.

Example:

```sh
cat file.txt | grep root > out.txt
```

At this stage nothing has executed yet.

Important:

```text
input
≠
command execution
```

The parser must first interpret the text.

---

# 2. Parser

The shell parses the input and identifies structure.

Example:

```sh
cat file.txt | grep root > out.txt
```

The parser identifies:

```text
cat
file.txt
|
grep
root
>
out.txt
```

Important parser syntax:

```text
|
>
&
;
quotes
$( )
```

Important:

```text
parser syntax
≠
command arguments
```

Parser syntax changes execution structure.

---

# 3. Expansion

The shell expands:

```text
variables
command substitutions
globs
```

Examples:

```sh
echo "$HOME"
echo $(whoami)
echo *.txt
```

Expansion produces:

```text
variable values
captured command output
filename matches
```

Important:

```text
expansion
happens before execution
```

---

# 4. Parser Decisions

The parser decides which execution structure to build.

Example:

```sh
echo hello | wc -c
```

Creates:

```text
pipeline structure
```

Example:

```sh
echo hello > out.txt
```

Creates:

```text
redirection structure
```

Important:

```text
payloads modify parser decisions
```

This idea becomes critical in Phase02.

---

# 5. Execution Graph

Parser decisions produce an execution graph.

Example:

```sh
cat file.txt | grep root > out.txt
```

Execution graph:

```text
cat
→ grep

grep stdout
→ out.txt
```

Important:

```text
process graph
≠
FD graph
```

They are different layers.

---

# 6. Pipe Creation

For pipelines, the shell creates pipe objects before execution.

Example:

```sh
echo hello | wc -c
```

The shell creates:

```text
pipe write end
pipe read end
```

Important:

```text
pipe
≠
simple connection
```

A pipe is:

```text
kernel-managed buffer
```

used for inter-process communication.

---

# 7. FD Rewiring

The shell changes file descriptor targets before execution.

Default:

```text
FD0 stdin  ← terminal
FD1 stdout → terminal
FD2 stderr → terminal
```

Pipeline:

```text
echo FD1
→ pipe write end

wc FD0
← pipe read end
```

Redirection:

```text
grep FD1
→ out.txt
```

Important:

```text
processes do not know about files or pipes directly
```

Processes only:

```text
read(FD)
write(FD)
```

The shell decides where those descriptors point.

---

# 8. Fork

The shell creates child processes.

```text
shell
→ fork
→ child
```

The child inherits:

```text
environment
cwd
FD table
```

Important:

```text
inheritance
≠
shared mutable state
```

Changes in the child do not automatically affect the parent.

---

# 9. Exec

The child process is replaced with the target program.

Example:

```text
child
→ exec(/bin/grep)
→ grep
```

Important:

```text
fork
=
create process

exec
=
replace process image
```

The PID remains the same.

---

# 10. Runtime Execution

After exec, the actual program runs.

Example:

```sh
yes | head -n 1
```

Runtime:

```text
yes running
head running
```

Data flow:

```text
yes FD1
→ pipe
→ head FD0
```

Important:

```text
pipeline
=
concurrent process graph
```

Not sequential execution.

---

# 11. Signals

Signals are runtime control messages.

Examples:

```text
SIGINT
SIGTERM
SIGKILL
SIGPIPE
```

Examples:

```text
Ctrl+C
→ SIGINT

kill PID
→ SIGTERM

kill -9 PID
→ SIGKILL
```

Important:

```text
signals
≠
parser syntax
```

Signals operate on running processes.

---

# 12. Termination

Processes eventually terminate.

Exit status:

```text
0
=
success

non-zero
=
failure
```

The shell collects termination information using:

```text
wait()
```

Important:

```text
visible output
≠
exit status
```

A command may succeed without output.

A command may fail while producing output.

---

# Integration Example

Command:

```sh
cat file.txt | grep root > out.txt
```

Parser World:

```text
pipeline
redirection
```

Process Graph:

```text
cat
→ grep
```

FD Graph:

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

# Phase02 Preparation

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

Phase02 focuses on:

```text
filter
↓
parser
↓
execution
```

The key questions become:

```text
What does the filter see?

What does the parser see?

What actually executes?
```

---

# Final Mental Model

Whenever you see a payload, ask:

```text
What parser sees this?

What execution graph is created?

What processes will exist?

How will FDs be connected?

What runtime behavior will occur?
```

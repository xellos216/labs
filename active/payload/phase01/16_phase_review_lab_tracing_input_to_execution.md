# Session 16 — Phase Review Lab — Tracing Input to Execution

## Metadata

```yaml
Roadmap: Payload Construction & Parser Reasoning
Phase: 01
Session: 16
Title: Phase Review Lab — Tracing Input to Execution
Status:
Review:
ArchiveVersion: 2
Date:
```

## Integrated Shell Model

Analyze shell input through these layers:

```text
source text
-> quoting and parsing
-> expansions
-> field splitting and globbing
-> redirection and pipeline graph
-> command resolution
-> process creation
-> descriptor wiring
-> execution, signals, and exit status
```

## Example

```sh
printf '%s\n' "$HOME" | grep home >result.txt 2>errors.txt &
```

Questions to ask:

1. Which text is protected by quotes?
2. Which expansions occur?
3. Which tokens are shell syntax?
4. How many commands and pipes exist?
5. Where do stdin, stdout, and stderr point?
6. How are command names resolved?
7. Does the shell wait?
8. Which status can later be observed?

## Parser Graph

```text
pipeline
├── printf command
└── grep command
    ├── stdout -> result.txt
    └── stderr -> errors.txt
```

## Process Graph

```text
printf process FD 1
-> pipe
-> grep process FD 0

grep FD 1 -> result.txt
grep FD 2 -> errors.txt
```

The trailing `&` makes the pipeline a background job.

## Security Perspective

Injection vulnerabilities arise when attacker-controlled data crosses from a
data position into shell grammar. Filtering one character class is weak
because shell grammar provides multiple boundary, expansion, and redirection
mechanisms.

## Final Review

- Separate parser state from process state.
- Separate command arguments from operators.
- Track descriptor targets explicitly.
- Distinguish visible output from execution and exit status.
- Treat command resolution and environment as security inputs.

# Review Questions

### Q1. Why should shell input be analyzed in layers?

<details>
<summary>A</summary>

Each layer can change meaning: quotes affect parsing, expansions change text,
splitting and globbing change argv, redirections change descriptors, and
execution creates runtime behavior.

</details>

---

### Q2. In `printf '%s\n' "$HOME" | grep home >result.txt 2>errors.txt &`, what parser structures are present?

<details>
<summary>A</summary>

The command contains quoting, parameter expansion, a pipeline, stdout and
stderr redirections, and background execution.

</details>

---

### Q3. What descriptor graph does the example create around `grep`?

<details>
<summary>A</summary>

`grep` receives stdin from the pipe, writes stdout to `result.txt`, and writes
stderr to `errors.txt`.

</details>

---

### Q4. Why is filtering one character class a weak injection defense?

<details>
<summary>A</summary>

Shell grammar has many mechanisms for changing interpretation, including
quoting, expansion, redirection, separators, and command resolution. Blocking
one character class rarely removes all grammar paths.

</details>

# Pipeline Processes

## Process Graph

```sh
producer | filter | consumer
```

This is not one command passing through three textual stages. It is a process
graph:

```text
producer process
-> pipe
-> filter process
-> pipe
-> consumer process
```

## Shell Preparation

Before execution, the shell generally:

1. Parses pipeline syntax.
2. Creates the required pipes.
3. Creates command processes.
4. Connects descriptors to pipe ends.
5. Closes unused descriptors.
6. Waits according to foreground or background mode.

## Exit Status

By default, many shells report the final command's status for a pipeline.
Bash's `pipefail` option changes this behavior:

```sh
set -o pipefail
```

Then a failing earlier stage can make the pipeline fail.

## Builtins in Pipelines

Pipeline components may execute in child contexts, so state changes may not
persist:

```sh
printf '/tmp\n' | read directory
```

Behavior varies by shell and options.

## Review

1. A pipeline is both parser structure and process graph.
2. Each command generally has its own execution context.
3. Pipes must exist before useful descriptor wiring.
4. Pipeline status policy is shell-dependent.
5. State-changing builtins in pipelines require careful context analysis.

# QA

**Q1.**
Why is `producer | filter | consumer` a process graph?

<details>
<summary><strong>A1.</strong></summary>

Each stage generally runs in its own execution context, and pipes connect the
stdout of one process to the stdin of the next.

</details>

---

**Q2.**
What must the shell prepare before the pipeline can run usefully?

<details>
<summary><strong>A2.</strong></summary>

It must parse the pipeline, create pipes, create command processes, wire
descriptors to pipe ends, and close unused descriptors.

</details>

---

**Q3.**
Why can pipeline exit status be surprising?

<details>
<summary><strong>A3.</strong></summary>

Many shells report the final command's status by default. Options such as
Bash `pipefail` can make earlier stage failures affect the pipeline status.

</details>

---

**Q4.**
Why are builtins in pipelines context-sensitive?

<details>
<summary><strong>A4.</strong></summary>

Pipeline components may run in child contexts. A state-changing builtin such
as `read` or `cd` may therefore not modify the parent shell.

</details>

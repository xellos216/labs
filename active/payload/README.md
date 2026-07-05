# Payload Construction & Parser Reasoning Roadmap

## Objective

Build a rigorous mental model for how controlled input moves through parsers,
changes meaning and produces observable behavior.

This roadmap focuses on:

- parser boundaries
- execution-flow reasoning
- input constraints and mutation
- observable side effects
- SQL and filesystem interpretation
- type and serialization behavior
- multi-parser data flows
- small, inspectable analysis tools

The objective is not to memorize payload strings.

The objective is to predict how an input will be interpreted at every stage.

---

# Scope & Ethics

All exercises must remain:

- local or explicitly authorized
- isolated from production systems
- reproducible
- observable
- reversible
- limited to intentionally vulnerable training targets

Do not use this roadmap for unauthorized access, indiscriminate scanning,
persistence or disruption.

Every practical exercise should record:

```text
Input
  ↓
Expected Interpretation
  ↓
Observed Behavior
  ↓
Explanation
  ↓
Cleanup
```

---

# Philosophy

Payload construction should not be studied as:

- memorized strings
- a collection of CTF tricks
- blind tool usage
- unexplained filter bypasses

Instead, model the complete interpretation path:

```text
Input
  │
  ▼
Decoding and Normalization
  │
  ▼
Parser Decisions
  │
  ▼
Execution or Data Access
  │
  ▼
Observable Behavior
```

Core principles:

- understand the parser before changing the input
- distinguish data from syntax
- observe before automating
- mutate one constraint at a time
- treat failures as evidence
- preserve ethical and technical scope

---

# Learning Method

Each phase uses a fixed 16-session curriculum so that learning continues in a
stable order across separate study sessions.

## Concept Sessions

Build accurate models of parsing, normalization, execution and trust
boundaries.

## Observation Sessions

Use small local harnesses to inspect tokens, arguments, paths, queries, types
and side effects.

## Hands-on Sessions

Change one input property at a time, predict the result and compare that
prediction with observable behavior.

Typical workflow:

```text
Model

↓

Predict

↓

Test Locally

↓

Observe

↓

Revise

↓

Explain
```

---

# Lab Environment

Host system:

- Arch Linux

Primary workflow:

- zsh
- tmux
- neovim
- Python 3
- CLI-first tooling

Preferred lab boundaries:

- local parser harnesses
- disposable containers
- virtual machines
- intentionally vulnerable applications
- authorized training platforms

Use generated test data and loopback-only services whenever practical.

---

# Typical Phase Structure

Every phase contains exactly 16 sessions.

```text
Session 01–04
Parser and Execution Models

↓

Session 05–08
Direct Observation

↓

Session 09–12
Constraints and Reasoning

↓

Session 13–15
Integrated Analysis and Tooling

↓

Session 16
Phase Review Lab
```

---

# Phase 01 — Shell Parsing & Command Injection Foundations

## Goal

Understand how shell input becomes tokens, expansions, execution structures
and observable process behavior.

---

## Outcomes

After completing this phase, you should be able to:

- distinguish raw input from executed commands
- explain shell tokenization, quoting and expansion
- model pipelines, redirection and command substitution
- trace arguments and file descriptors into child processes
- identify where untrusted data crosses into shell syntax

---

## Typical Tools

- POSIX shell
- Bash
- Python 3
- `printf`
- `set -x`
- `strace`
- local argument-printing harnesses

---

## Example Labs

- compare raw strings with parsed arguments
- observe quoting and word splitting
- trace pipeline and redirection setup
- inspect expansion order
- map input to a local process and file-descriptor graph

---

### Session 01

Input Is Not Execution

---

### Session 02

Shell Tokens and Grammar

---

### Session 03

Commands, Arguments and Syntax

---

### Session 04

Execution Graphs

---

### Session 05

Whitespace and Word Splitting

---

### Session 06

Single and Double Quotes

---

### Session 07

Command Separators

---

### Session 08

Pipelines and Redirection

---

### Session 09

Variable Expansion

---

### Session 10

Command Substitution

---

### Session 11

Globbing and Filename Expansion

---

### Session 12

Expansion Order and Reinterpretation

---

### Session 13

Processes, Arguments and File Descriptors

---

### Session 14

Locating the Shell Trust Boundary

---

### Session 15

Building a Local Shell Parser Harness

---

### Session 16

Phase Review Lab — Tracing Input to Execution

---

# Phase 02 — Filter Evasion & Payload Mutation

## Goal

Understand why input filters and downstream parsers disagree, and reason about
constraint-driven input mutation without relying on memorized strings.

---

## Outcomes

After completing this phase, you should be able to:

- distinguish filtering from parsing
- explain normalization and canonicalization order
- identify weaknesses in blacklist-based validation
- reason about quote, separator and whitespace constraints
- compare rejected and accepted inputs using controlled local tests

---

## Typical Tools

- Python 3
- local validation harnesses
- shell tracing
- URL encoders and decoders
- diff tools
- structured test cases

---

## Example Labs

- compare a filter's view with a parser's view
- observe decoding before and after validation
- test one input constraint at a time
- classify failures by processing stage
- build a mutation matrix for a local harness

---

### Session 01

Filters and Parsers Are Different Systems

---

### Session 02

Allow Lists and Deny Lists

---

### Session 03

Normalization Before Validation

---

### Session 04

Validation Before Normalization

---

### Session 05

Separator Constraints

---

### Session 06

Whitespace Constraints

---

### Session 07

Quote Constraints

---

### Session 08

Path and Character Restrictions

---

### Session 09

Encoding Layers and Decoder Order

---

### Session 10

Environment Expansion Under Constraints

---

### Session 11

Globbing as Parser Behavior

---

### Session 12

Classifying Rejection Points

---

### Session 13

Designing a Constraint Matrix

---

### Session 14

Comparing Equivalent Parser Outcomes

---

### Session 15

Building a Local Mutation Test Harness

---

### Session 16

Phase Review Lab — Explaining a Filter and Parser Mismatch

---

# Phase 03 — Blind Injection & Observable Side Effects

## Goal

Determine whether controlled input changed execution when direct output is
missing, using bounded and verifiable local observations.

---

## Outcomes

After completing this phase, you should be able to:

- distinguish execution from visible output
- identify safe local side effects
- design timing and state-change observations
- control false positives and measurement noise
- document evidence without relying on assumptions

---

## Typical Tools

- Python 3
- local HTTP server
- shell timing tools
- filesystem observation
- logs
- `curl`
- process inspection tools

---

## Example Labs

- compare exit status with displayed output
- observe a temporary local file change
- measure bounded timing differences
- correlate requests with local logs
- repeat experiments to reject false positives

---

### Session 01

Execution Without Direct Output

---

### Session 02

Observable State Changes

---

### Session 03

Exit Status as Evidence

---

### Session 04

Separating Absence of Output from Failure

---

### Session 05

Filesystem Side Effects

---

### Session 06

Process and Resource Side Effects

---

### Session 07

Log-Based Observation

---

### Session 08

HTTP Response Differences

---

### Session 09

Timing-Based Observation

---

### Session 10

Measurement Noise and Baselines

---

### Session 11

Repeated Trials and Confidence

---

### Session 12

Avoiding False Positives

---

### Session 13

Correlating Multiple Evidence Sources

---

### Session 14

Designing Safe Local Side Effects

---

### Session 15

Building an Observation Harness

---

### Session 16

Phase Review Lab — Verifying Hidden Execution

---

# Phase 04 — SQL Injection Parser Reasoning

## Goal

Understand SQL injection as a boundary failure between application data and SQL
syntax, using local databases and intentionally vulnerable queries.

---

## Outcomes

After completing this phase, you should be able to:

- explain how applications construct SQL statements
- distinguish values from SQL syntax
- reason about quoting, termination and boolean structure
- compare unsafe string construction with parameterized queries
- interpret errors, response differences and bounded timing observations

---

## Typical Tools

- SQLite
- Python 3
- local web application
- database logs
- query-plan and tracing features
- structured test data

---

## Example Labs

- print generated SQL before execution
- compare concatenated and parameterized queries
- observe string and numeric contexts
- trace boolean response differences
- model a query from input to database result

---

### Session 01

Applications and SQL Statements

---

### Session 02

Data Versus SQL Syntax

---

### Session 03

String and Numeric Contexts

---

### Session 04

Query Construction Boundaries

---

### Session 05

Quoting and String Termination

---

### Session 06

Comments and Statement Structure

---

### Session 07

Boolean Expression Reasoning

---

### Session 08

Result-Set Shape and UNION Concepts

---

### Session 09

Error-Based Observation

---

### Session 10

Response-Difference Observation

---

### Session 11

Bounded Timing Observation

---

### Session 12

Encoding and Query Normalization

---

### Session 13

Database-Specific Syntax Differences

---

### Session 14

Parameterized Queries and Bound Values

---

### Session 15

Building a Local Query Inspection Harness

---

### Session 16

Phase Review Lab — Explaining an Unsafe Query Boundary

---

# Phase 05 — File Inclusion & Path Resolution

## Goal

Understand how applications construct, normalize and resolve filesystem paths
from controlled input.

---

## Outcomes

After completing this phase, you should be able to:

- distinguish path strings from resolved filesystem objects
- explain relative paths, absolute paths and traversal
- trace normalization and canonicalization
- identify application base-directory and symlink effects
- compare unsafe path construction with constrained resolution

---

## Typical Tools

- Python 3
- `pathlib`
- local filesystem trees
- `realpath`
- `readlink`
- `strace`
- disposable containers

---

## Example Labs

- resolve paths inside a generated directory tree
- compare lexical normalization with filesystem resolution
- observe symbolic-link effects
- enforce a local base-directory boundary
- trace file opens from input to resolved path

---

### Session 01

Path Strings and Filesystem Objects

---

### Session 02

Relative and Absolute Paths

---

### Session 03

Application Base Directories

---

### Session 04

Path Joining Semantics

---

### Session 05

Traversal Components

---

### Session 06

Lexical Path Normalization

---

### Session 07

Canonicalization and `realpath`

---

### Session 08

Symbolic Links and Resolution

---

### Session 09

Encoding in Path Inputs

---

### Session 10

Validation and Normalization Order

---

### Session 11

File Disclosure and Inclusion Contexts

---

### Session 12

Stream and Wrapper Concepts

---

### Session 13

Constraining Resolution to a Base Directory

---

### Session 14

Tracing File Access at Runtime

---

### Session 15

Building a Local Path Resolution Harness

---

### Session 16

Phase Review Lab — Explaining a Path Boundary Failure

---

# Phase 06 — PHP Type Juggling & Serialization

## Goal

Understand how implicit type conversion and object reconstruction can change
application control flow.

---

## Outcomes

After completing this phase, you should be able to:

- compare strict and loose equality
- explain implicit casting and truthiness
- reason about numeric-string behavior
- inspect serialized values and object state
- identify trust boundaries around deserialization

---

## Typical Tools

- local PHP runtime
- PHP CLI
- Python 3 for comparison
- local test scripts
- serialized sample data
- explicit logging

---

## Example Labs

- compare strict and loose equality outcomes
- build a type-conversion table
- inspect serialized scalar and object values
- observe object lifecycle hooks locally
- replace implicit assumptions with explicit validation

---

### Session 01

PHP Values and Runtime Types

---

### Session 02

Strict and Loose Comparison

---

### Session 03

Implicit Type Conversion

---

### Session 04

Truthiness and Control Flow

---

### Session 05

Numeric Strings

---

### Session 06

Comparison Edge Cases

---

### Session 07

Hash-Like String Comparisons

---

### Session 08

Explicit Validation and Type Checks

---

### Session 09

Serialization Formats

---

### Session 10

Serializing Scalars and Arrays

---

### Session 11

Object Serialization

---

### Session 12

Object Lifecycle and Magic Methods

---

### Session 13

Deserialization Trust Boundaries

---

### Session 14

Reasoning About Object Graphs

---

### Session 15

Building a Local Type and Serialization Harness

---

### Session 16

Phase Review Lab — Tracing Type and Object State

---

# Phase 07 — Multi-Parser Exploitation

## Goal

Model how input changes meaning while crossing multiple decoders, parsers and
execution boundaries.

---

## Outcomes

After completing this phase, you should be able to:

- identify every parser in a data path
- record the representation at each boundary
- explain nested decoding and normalization
- detect parser disagreement
- reconstruct an end-to-end interpretation pipeline

---

## Typical Tools

- Python 3
- local HTTP applications
- shell and SQL harnesses
- structured logs
- proxy inspection tools
- diff and byte-display utilities

---

## Example Labs

- trace URL data into an application parser
- follow serialized input into a database or shell boundary
- compare representations before and after each decoder
- locate the first point of parser disagreement
- document a complete local multi-parser flow

---

### Session 01

One Input, Multiple Interpreters

---

### Session 02

Mapping Parser Boundaries

---

### Session 03

Recording Data State at Each Boundary

---

### Session 04

Trust Transitions Between Components

---

### Session 05

HTTP Decoding and Application Input

---

### Session 06

Application Parsing and Serialization

---

### Session 07

Application Data Entering SQL

---

### Session 08

Application Data Entering a Shell

---

### Session 09

Nested Encoding Layers

---

### Session 10

Repeated Normalization

---

### Session 11

Parser Disagreement

---

### Session 12

Recursive Interpretation

---

### Session 13

Locating the First Unsafe Boundary

---

### Session 14

Building an End-to-End Data-State Diagram

---

### Session 15

Building a Multi-Parser Observation Harness

---

### Session 16

Phase Review Lab — Explaining a Multi-Stage Interpretation Flow

---

# Phase 08 — Payload Automation & Tooling

## Goal

Convert verified parser reasoning into small, transparent tools for controlled
experiments.

---

## Outcomes

After completing this phase, you should be able to:

- represent test inputs and constraints explicitly
- generate bounded input variations
- normalize and compare responses
- measure timing and state changes carefully
- produce reproducible reports with clear safety limits

---

## Typical Tools

- Bash
- Python 3
- `curl`
- `requests`
- `argparse`
- diff tools
- structured output formats

---

## Example Labs

- automate a local request matrix
- normalize and diff controlled responses
- record timing with baselines and repeated trials
- generate a reproducible experiment report
- build a scope-limited parser analysis CLI

---

### Session 01

Automation as an Extension of Reasoning

---

### Session 02

Defining Inputs, Constraints and Expected Results

---

### Session 03

Building Reproducible Test Cases

---

### Session 04

Adding Scope and Safety Controls

---

### Session 05

Automating Local Requests with `curl`

---

### Session 06

Automating Requests with Python

---

### Session 07

Generating Bounded Input Variations

---

### Session 08

Recording Requests and Observations

---

### Session 09

Normalizing Response Data

---

### Session 10

Diffing Response Behavior

---

### Session 11

Measuring Timing with Baselines

---

### Session 12

Tracking Filesystem and Log Side Effects

---

### Session 13

Designing Composable Analysis Functions

---

### Session 14

Building a Scope-Limited CLI

---

### Session 15

Producing a Reproducible Experiment Report

---

### Session 16

Final Capstone Lab — Building a Local Parser Analysis Toolkit

---

# Final Outcome

Upon completing this roadmap, you should be able to:

- model how controlled input moves through parsers
- distinguish data, syntax, decoding and normalization
- reason about constraints without memorizing payload strings
- verify hidden behavior through bounded local observations
- explain SQL, path, type and serialization boundaries
- trace input through multiple interpreters
- build transparent automation for authorized experiments
- document results as reproducible evidence

---

# Core Mental Model

```text
Controlled Input
       │
       ▼
Decoding and Normalization
       │
       ▼
Validation and Filtering
       │
       ▼
Parser Interpretation
       │
       ▼
Execution or Data Access
       │
       ▼
Observable State Change
       │
       ▼
Evidence-Based Explanation
```

The objective is not to remember a payload.

The objective is to understand why an input changes system behavior.

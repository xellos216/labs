# Python Crypto Reasoning & Automation Roadmap

## Objective

Build a practical mental model for reasoning about cryptographic data as bytes,
representations and reversible or irreversible transformations.

This roadmap focuses on:

- byte-level reasoning
- encoding and decoding
- XOR and stream cipher intuition
- web token and cookie analysis
- reverse transformation analysis
- small Python automation tools
- reproducible challenge workflows

The objective is not to memorize algorithms or collect scripts.

The objective is to inspect unknown data, reconstruct how it changed and
explain every transformation.

---

# Philosophy

Cryptography should not be approached as:

- opaque mathematical magic
- a list of algorithms to memorize
- copy-paste challenge solutions
- automation without understanding

Instead, follow data through explicit states:

```text
Input Bytes
     │
     ▼
Representation
     │
     ▼
Transformation
     │
     ▼
Output Bytes
```

Core principles:

- bytes before text
- representation is not encryption
- manual reasoning before automation
- observation before assumption
- transformations should be reversible in thought
- tools should expose behavior rather than hide it

---

# Core Skills

After completing this roadmap, you should be able to:

- distinguish Python `str` from `bytes`
- convert safely between text, hex, Base64 and raw bytes
- reason about XOR manually and programmatically
- explain plaintext, keystream and ciphertext relationships
- reconstruct layered token and cookie transformations
- trace observed outputs backward toward their inputs
- identify repeated patterns and unsafe stream reuse
- build small, inspectable Python analysis tools
- apply a consistent workflow to unfamiliar crypto data

---

# Learning Method

Each phase uses a fixed 16-session curriculum so that learning can continue
consistently across separate study sessions.

## Concept Sessions

Build the vocabulary and mental models required to explain the data flow.

## Observation Sessions

Inspect byte values, representations, patterns and transformation boundaries.

## Hands-on Sessions

Perform transformations manually, reproduce them with Python and verify that
the observed output matches the prediction.

Typical workflow:

```text
Classify

↓

Represent

↓

Transform

↓

Reverse

↓

Verify

↓

Explain
```

---

# Lab Environment

Host system:

- Arch Linux

Primary workflow:

- Python 3
- zsh
- tmux
- neovim
- CLI-first tooling

Experiments should use:

- local files
- generated sample data
- isolated scripts
- authorized challenge material
- explicit intermediate output

---

# Typical Phase Structure

Every phase contains exactly 16 sessions.

```text
Session 01–04
Core Concepts

↓

Session 05–08
Direct Observation and Manual Work

↓

Session 09–12
Reverse Reasoning and Relationship Analysis

↓

Session 13–15
Integrated Practice and Automation

↓

Session 16
Phase Review Lab
```

---

# Phase 01 — Bytes & Encoding Foundations

## Goal

Understand how Python represents text and binary data, and distinguish data
representation from cryptographic transformation.

---

## Outcomes

After completing this phase, you should be able to:

- distinguish `str`, `bytes` and integer byte values
- explain ASCII, Unicode and binary-safe representations
- convert between text, raw bytes, hex and Base64
- inspect and manipulate byte sequences safely
- identify common representations without calling them encryption

---

## Typical Tools

- Python 3 REPL
- `bytes`
- `bytearray`
- `binascii`
- `base64`
- `xxd`
- `file`

---

## Example Labs

- inspect the byte values of a text string
- compare text length with encoded byte length
- perform round-trip hex and Base64 conversions
- identify representation layers in unknown data
- build a small byte-inspection script

---

### Session 01

Python Text and Binary Data

---

### Session 02

Understanding `str` and `bytes`

---

### Session 03

ASCII and Integer Byte Values

---

### Session 04

Encoding Text into Bytes

---

### Session 05

Decoding Bytes into Text

---

### Session 06

Hexadecimal Representation

---

### Session 07

Converting Hex with `bytes.fromhex()`

---

### Session 08

Base64 Encoding and Decoding

---

### Session 09

Inspecting Raw Bytes

---

### Session 10

Byte Indexing and Slicing

---

### Session 11

Mutable Bytes with `bytearray`

---

### Session 12

Binary-Safe Data Handling

---

### Session 13

Recognizing Common Data Representations

---

### Session 14

Peeling Layered Encodings

---

### Session 15

Building a Byte Inspection Utility

---

### Session 16

Phase Review Lab — Classifying Unknown Data

---

# Phase 02 — XOR & Stream Cipher Intuition

## Goal

Understand XOR as a reversible byte operation and use it to build an accurate
mental model of stream encryption.

---

## Outcomes

After completing this phase, you should be able to:

- compute XOR and explain its reversible properties
- distinguish single-byte and repeating-key XOR
- explain plaintext, keystream and ciphertext relationships
- recover keystream bytes from known plaintext
- identify the risks of nonce and keystream reuse

---

## Typical Tools

- Python 3
- `bytes`
- `bytearray`
- `zip`
- hexadecimal output
- small XOR helper functions

---

## Example Labs

- calculate XOR by hand and verify it with Python
- encrypt and decrypt with a repeating key
- compare ciphertexts for repeated patterns
- recover a partial keystream
- demonstrate the effect of keystream reuse

---

### Session 01

What XOR Actually Does

---

### Session 02

XOR Truth Tables and Bitwise Reasoning

---

### Session 03

XOR as a Reversible Operation

---

### Session 04

Single-Byte XOR by Hand

---

### Session 05

Single-Byte XOR with Python

---

### Session 06

Repeating-Key XOR

---

### Session 07

Detecting Repeating Patterns

---

### Session 08

The Keystream Mental Model

---

### Session 09

Plaintext, Keystream and Ciphertext

---

### Session 10

Known Plaintext Reasoning

---

### Session 11

Recovering Partial Keystreams

---

### Session 12

Comparing Related Ciphertexts

---

### Session 13

Why Nonces and IVs Exist

---

### Session 14

Keystream Reuse Risks

---

### Session 15

Building a Reusable XOR Utility

---

### Session 16

Phase Review Lab — Investigating Stream Reuse

---

# Phase 03 — Web Token & Cookie Analysis

## Goal

Analyze web tokens and cookies as structured transformation pipelines with
explicit trust and security properties.

---

## Outcomes

After completing this phase, you should be able to:

- identify common token and cookie representations
- reconstruct serialization and encoding flows
- distinguish integrity from confidentiality
- explain token roles and trust boundaries
- test transformations without assuming that decoding implies verification

---

## Typical Tools

- Python 3
- `base64`
- `json`
- `urllib.parse`
- `hmac`
- `hashlib`
- browser developer tools

---

## Example Labs

- decode URL-safe Base64 token segments
- reconstruct a serialized cookie
- compare signed and encrypted data
- inspect how tampering changes verification state
- document an end-to-end token pipeline

---

### Session 01

Tokens, Cookies and Application State

---

### Session 02

Recognizing Token Boundaries

---

### Session 03

URL Encoding in Web Data

---

### Session 04

URL-Safe Base64

---

### Session 05

Serialized Data Structures

---

### Session 06

Reconstructing Cookie Pipelines

---

### Session 07

Nested Encoding Layers

---

### Session 08

Token Structure Fingerprinting

---

### Session 09

JWT Header, Payload and Signature

---

### Session 10

Token Roles and Claims

---

### Session 11

Integrity and Confidentiality

---

### Session 12

Signatures, MACs and Verification

---

### Session 13

Trust Boundaries in Token Processing

---

### Session 14

Tampering and Verification State

---

### Session 15

Building a Token Inspection Utility

---

### Session 16

Phase Review Lab — Reconstructing a Web Token Flow

---

# Phase 04 — Crypto Reasoning & Reverse Flow Analysis

## Goal

Trace layered transformations backward from observed output and justify each
step with byte-level evidence.

---

## Outcomes

After completing this phase, you should be able to:

- model data as a sequence of explicit states
- identify likely transformation boundaries
- reverse layered representations in the correct order
- use partial plaintext and structural clues
- compare candidate explanations against observed bytes

---

## Typical Tools

- Python 3
- byte and hex viewers
- Base64 and URL decoders
- XOR helpers
- comparison and diff utilities

---

## Example Labs

- diagram a multi-stage transformation pipeline
- peel nested representation layers
- recover partial plaintext from known structure
- compare multiple outputs for shared transformations
- produce an evidence-backed analysis of unknown data

---

### Session 01

Data States and Transformation Boundaries

---

### Session 02

Building Transformation Pipelines

---

### Session 03

Forward and Reverse Data Flow

---

### Session 04

Choosing the Correct Reverse Order

---

### Session 05

Layer Peeling by Observation

---

### Session 06

Recognizing Transformation Fingerprints

---

### Session 07

Using Length and Alphabet Clues

---

### Session 08

Separating Representation from Transformation

---

### Session 09

Partial Plaintext Recovery

---

### Session 10

Known Structure as Evidence

---

### Session 11

Ciphertext Relationship Analysis

---

### Session 12

Comparing Multiple Transformation Hypotheses

---

### Session 13

Debugging Failed Reverse Flows

---

### Session 14

Documenting an Analysis Pipeline

---

### Session 15

Building a Layer-Peeling Harness

---

### Session 16

Phase Review Lab — Explaining an Unknown Transformation

---

# Phase 05 — Python Automation

## Goal

Turn verified manual reasoning into small, transparent and reusable Python
analysis tools.

---

## Outcomes

After completing this phase, you should be able to:

- normalize and classify unknown inputs
- automate common decoding and XOR operations
- detect printable output and repeated patterns
- build composable command-line utilities
- validate automation against known manual results

---

## Typical Tools

- Python 3
- `argparse`
- `base64`
- `binascii`
- `json`
- `string`
- unit tests or explicit test vectors

---

## Example Labs

- build a representation detector
- automate multiple decoding attempts
- score printable byte sequences
- create a token-inspection command
- combine helpers into a CLI analysis harness

---

### Session 01

From Manual Reasoning to Automation

---

### Session 02

Normalizing Text and Byte Inputs

---

### Session 03

Designing Small Decoder Functions

---

### Session 04

Handling Conversion Errors Explicitly

---

### Session 05

Detecting Hexadecimal Input

---

### Session 06

Detecting Base64 Input

---

### Session 07

Measuring Printable Byte Output

---

### Session 08

Building Decoder Pipelines

---

### Session 09

Automating Single-Byte XOR Tests

---

### Session 10

Automating Repeating-Key XOR

---

### Session 11

Detecting Repeated Byte Patterns

---

### Session 12

Comparing Candidate Outputs

---

### Session 13

Designing a Token Inspector

---

### Session 14

Building a CLI Interface

---

### Session 15

Testing and Verifying Analysis Utilities

---

### Session 16

Phase Review Lab — Building a Crypto Analysis Harness

---

# Phase 06 — Practical Crypto Challenge Workflows

## Goal

Apply byte reasoning, reverse analysis and automation through a consistent
workflow for authorized practical crypto problems.

---

## Outcomes

After completing this phase, you should be able to:

- classify unfamiliar challenge inputs
- separate representation, serialization and cryptographic operations
- select manual tests before broad automation
- investigate nonce, keystream and padding behavior
- document a complete solution as a reproducible reasoning process

---

## Typical Tools

- Python 3
- local analysis utilities
- `xxd`
- `file`
- OpenSSL inspection commands
- provided challenge interfaces

---

## Example Labs

- classify an unknown challenge artifact
- reconstruct a layered transformation flow
- test a known-plaintext hypothesis
- investigate repeated nonces or keystreams
- complete and document a capstone analysis

---

### Session 01

Reading a Crypto Challenge as a System

---

### Session 02

Classifying Inputs and Outputs

---

### Session 03

Separating Representation from Cryptography

---

### Session 04

Constructing an Initial Data-Flow Model

---

### Session 05

Manual Tests Before Automation

---

### Session 06

Building Minimal Reproduction Scripts

---

### Session 07

Testing Known-Plaintext Hypotheses

---

### Session 08

Investigating Repeating-Key Behavior

---

### Session 09

Investigating Nonce and IV Misuse

---

### Session 10

Investigating Keystream Reuse

---

### Session 11

Observing Padding and Block Boundaries

---

### Session 12

Analyzing Token Manipulation Scenarios

---

### Session 13

Failure Analysis and Hypothesis Revision

---

### Session 14

Building a Reproducible Challenge Workflow

---

### Session 15

Writing an Evidence-Based Analysis

---

### Session 16

Final Capstone Lab — Analyzing an Unknown Crypto Flow

---

# Long-Term Direction

This roadmap prepares the foundation for:

- AES mode intuition
- CBC and CTR behavior
- padding and oracle concepts
- authenticated encryption
- protocol-level crypto flows
- token and serialization security
- lightweight CLI crypto tooling
- deeper applied cryptography

These topics should extend the byte and transformation mental model rather than
replace it with algorithm memorization.

---

# Final Outcome

Upon completing this roadmap, you should be able to:

- inspect unknown data as bytes before interpreting it as text
- distinguish representation, serialization and cryptographic transformation
- reason manually about XOR and stream relationships
- analyze token and cookie transformation pipelines
- reverse layered data flows using observable evidence
- automate repetitive analysis without hiding intermediate behavior
- approach authorized crypto problems through a reproducible workflow

---

# Core Mental Model

```text
Unknown Input
      │
      ▼
Byte Classification
      │
      ▼
Representation and Structure
      │
      ▼
Transformation Pipeline
      │
      ▼
Relationships and Security Properties
      │
      ▼
Reverse Analysis
      │
      ▼
Verified Explanation
```

The objective is not to guess which tool to run.

The objective is to explain what happened to the bytes.

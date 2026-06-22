# Payload Daily Sessions

Practical payload construction and parser reasoning training.

---

# Philosophy

This repository is NOT focused on:

- payload memorization
- copy-paste exploitation
- tool dependency
- “CTF trick collection”

Instead, the goal is to build:

- parser mental models
- execution flow reasoning
- payload mutation ability
- filter adaptation skills
- exploitation intuition under constraints

Core mindset:

```text
input
→ parser
→ interpretation
→ tokenization
→ execution
→ observable behavior
````

---

# Training Structure

The training is divided into:

* fixed high-level Phases
* adaptive daily Sessions

Meaning:

* overall progression stays structured
* daily exercises mutate constraints dynamically
* emphasis stays on reasoning, not memorization

---

# Phase Roadmap

---

# Phase 1 — Shell Parsing & Command Injection Foundations

Focus:

* shell tokenization
* command separators
* quote handling
* URL decoding vs shell interpretation
* whitespace bypass
* word splitting
* shell expansion
* command substitution
* redirection
* execution flow reasoning

Goal:

Understand how shell parsers reinterpret attacker-controlled input.

---

# Phase 2 — Filter Evasion & Payload Mutation

Focus:

* blacklist bypass
* separator mutation
* encoding mutation
* quote restriction bypass
* slash/space restriction bypass
* environment variable tricks
* shell globbing
* wildcard behavior
* parser confusion

Goal:

Adapt payloads under changing constraints instead of relying on fixed payloads.

---

# Phase 3 — Blind Injection & Observable Side Effects

Focus:

* blind command injection
* timing-based reasoning
* output suppression
* side-channel observation
* HTTP response analysis
* DNS/ping/callback reasoning
* execution verification without visible output

Goal:

Reason about execution even when direct output is unavailable.

---

# Phase 4 — SQL Injection Parser Reasoning

Focus:

* SQL parser behavior
* query structure reasoning
* string termination
* UNION logic
* boolean-based reasoning
* time-based SQLi
* stacked queries
* encoding interaction
* DB-specific syntax differences

Goal:

Understand SQL injection as parser manipulation rather than payload memorization.

---

# Phase 5 — File Inclusion & Path Resolution

Focus:

* LFI/RFI fundamentals
* path traversal
* path normalization
* wrapper behavior
* stream wrappers
* file disclosure reasoning
* inclusion context analysis

Goal:

Understand how filesystem paths are interpreted and reconstructed internally.

---

# Phase 6 — PHP Type Juggling & Serialization

Focus:

* loose comparison behavior
* magic hashes
* implicit casting
* object serialization
* POP chains
* unserialize behavior
* object lifecycle reasoning

Goal:

Understand how application logic can be manipulated through type interpretation.

---

# Phase 7 — Multi-Parser Exploitation

Focus:

* chained parser behavior
* HTTP → PHP → shell transitions
* nested interpretation
* encoding layers
* recursive parsing
* injection across trust boundaries

Goal:

Mentally simulate multi-stage parser pipelines.

---

# Phase 8 — Payload Automation & Tooling

Focus:

* bash automation
* curl orchestration
* grep/sed/awk pipelines
* Python requests automation
* payload mutation scripts
* response diffing
* fuzzing primitives
* lightweight exploit tooling

Goal:

Build small, understandable automation tools based on strong parser understanding.

---

# Long-Term Goal

The final objective is NOT:

```text
"remembering payloads"
```

The final objective is:

```text
seeing a parser boundary
→ predicting reinterpretation
→ reconstructing payloads manually
under constraints
```

Eventually:

* payload mutation becomes natural
* parser behavior becomes predictable
* exploitation reasoning becomes composable
* automation becomes an extension of understanding
  rather than a replacement for it

# AGENTS.md

# Labs Workspace Agent Rules

## Purpose

This repository is a centralized personal learning workspace.

Goals:

* preserve learning history
* preserve topic-oriented organization
* keep experiments reproducible
* maintain readable notes and lab records
* prefer systems understanding over command memorization

Favor clarity, incremental progress, and maintainability over broad automation.

This repository contains:

* topic roadmaps
* phase-based learning records
* practical lab notes
* small experiments and proof-of-concept code
* repository operational documentation

---

## Agent Document Index

Additional agent-facing rules and templates live under `docs/agent/`.

Before creating, moving, or refactoring lab documents, read the relevant documents below.

* `docs/agent/DESIGN_PRINCIPLES.md`
  * General design principles for this learning repository.
* `docs/agent/LABS_SESSION_RULES.md`
  * Rules for phase/session-based lab learning documents.
* `docs/agent/QA_TEMPLATE_SPECIFICATION.md`
  * QA document format and requirements.
* `docs/agent/LAB_EXPERIMENT_TEMPLATE.md`
  * Template for experiment-style lab notes.
* `docs/agent/ARCHIVE_TEMPLATE.md`
  * Template for archived learning/session documents.
* `docs/agent/ROADMAP_FORMAT.md`
  * Format rules for roadmap documents.
* `docs/agent/ROADMAP_INDEX.md`
  * Index of roadmap documents and learning tracks.

## Required Reading Policy

For ordinary small file edits, read only this `AGENTS.md`.

For session archive generation, read:

* `docs/agent/LABS_SESSION_RULES.md`
* `docs/agent/ARCHIVE_TEMPLATE.md`
* `docs/agent/QA_TEMPLATE_SPECIFICATION.md`

For roadmap creation or roadmap modification, read:

* `docs/agent/ROADMAP_FORMAT.md`
* `docs/agent/ROADMAP_INDEX.md`

For repository structure, taxonomy, or organization changes, read:

* `docs/agent/DESIGN_PRINCIPLES.md`

---

# Workspace Map

```text
LFS/

c/
└── phase01/

crypto/
├── phase01/
└── phase02/

flask/
├── flask-lab/
└── phase01/

linux_admin/

network/
└── phase01/

payload/
├── phase01/
└── phase02/

toolsmith/
└── networking/

unix/
├── phase01/
└── phase02/
```

---

# Directory Semantics

## LFS/

Linux From Scratch or low-level Linux build notes.

Use for:

* Linux build process records
* toolchain and bootstrapping observations
* system construction notes

Do not place unrelated Linux administration exercises here.

---

## c/

C, memory, debugging, embedded systems, firmware, and low-level systems learning.

Use for:

* C language experiments
* memory layout observations
* GDB notes
* ELF and binary internals
* embedded Linux and firmware analysis material

---

## crypto/

Cryptography learning records and experiments.

Use for:

* cryptographic concepts
* classical crypto exercises
* practical analysis notes
* reusable explanations of crypto primitives

Keep challenge-specific or one-off exercise history in the relevant phase directory.

---

## flask/

Flask and web application learning.

Use for:

* Flask application experiments
* web backend notes
* route, template, session, and database exercises
* local lab application code

Keep runnable application code organized separately from conceptual notes when practical.

---

## linux_admin/

Linux server administration training.

Use for:

* user, permission, service, logging, and maintenance notes
* VM-based administration exercises
* troubleshooting records
* operational security observations

Prefer lab VM changes over host system changes for administration experiments.

---

## network/

Networking concepts, Linux networking, packet analysis, and protocol learning.

Use for:

* protocol notes
* packet capture observations
* routing, DNS, TCP, UDP, HTTP, and TLS material
* Linux networking experiments

When a note is primarily about system administration, place it under `linux_admin/`.

---

## payload/

Payload construction and security lab material.

Use for:

* controlled payload experiments
* exploit development learning records
* offensive security concepts in an educational lab context

Keep content ethical, local, and explicitly educational.

Do not add instructions intended for unauthorized use.

---

## toolsmith/

Custom tooling and utility-building experiments.

Use for:

* small tools
* scripts
* networking utilities
* reusable CLI workflows

Prefer simple, inspectable tools over hidden automation.

---

## unix/

Unix and Linux command-line training.

Use for:

* shell workflows
* text processing
* pipelines
* filesystem inspection
* process and service observation

Prefer composable commands and observable behavior.

---

# Content Placement Rules

Top-level topic directories are stable learning areas.

Use them for:

* topic roadmaps
* reusable concepts
* long-term notes
* organized lab records

Use `phaseXX/` directories for:

* chronological learning sessions
* exercise records
* incremental lab work
* rough observations that may later be distilled

Do not place:

* unrelated temporary files
* generated build artifacts
* downloaded archives without context
* broad cross-topic notes without a clear home

When content fits multiple directories, choose the directory based on the primary learning objective.

---

# Naming Rules

Prefer:

* lowercase_with_underscores.md
* stable names
* grep-friendly filenames
* explicit phase and session names when useful

Examples:

* process_memory_layout.md
* tcp_three_way_handshake.md
* file_permissions.md
* flask_routing_basics.md

Avoid:

* duplicate topic files
* vague names like `notes.md` when context is unclear
* mixed naming styles
* unnecessary mass renaming

---

# Modification Policy

Always prefer:

* small diffs
* explicit reasoning
* incremental changes
* preserving existing learning history
* reading local README files before changing a topic area

Never:

* mass-delete files
* perform large reorganizations without approval
* rewrite notes for style alone
* modify unrelated files
* collapse phase history into polished notes without review

Before significant changes:

1. inspect repository structure
2. read relevant README or roadmap files
3. summarize findings
4. explain the proposed change
5. provide dry-run output when appropriate
6. wait for approval

For filesystem operations:

* prefer dry-run first
* use git-aware workflows
* preserve directory semantics
* avoid broad wildcard modifications

---

# Refactor Policy

Refactoring should prioritize:

1. semantic clarity
2. searchability
3. stable topic boundaries
4. maintainability
5. low cognitive overhead

Avoid refactors that:

* increase nesting without clear benefit
* rename files without strong justification
* mix roadmaps, notes, and runnable code in confusing ways
* destroy historical learning context
* obscure the reason a lab was created

When extracting reusable knowledge from phase notes, preserve the original phase record unless the user explicitly approves consolidation.

---

# Lab Safety

Prefer experiments that are:

* local
* reproducible
* observable
* reversible
* ethically scoped

For administration, networking, payload, and security exercises:

* prefer VMs, containers, namespaces, or isolated lab targets
* avoid unnecessary host modifications
* document what changed and how it was observed
* do not run destructive commands without explicit approval
* do not create instructions for unauthorized access or harm

Before destructive actions:

1. explain intent
2. show affected files or systems
3. propose a plan
4. wait for approval

---

# Verification Checklist

After modifications, verify as appropriate:

```bash
git status
git diff --stat
find . -maxdepth 2 -type d | sort
```

For structural refactors:

```bash
rg 'old/path'
rg '\]\(.*\.md\)'
find . -type d -empty
```

Check for:

* broken links
* duplicate files
* empty directories
* accidental mass changes
* generated artifacts committed by mistake

For runnable code or lab tools, verify with the smallest relevant command first.

---

# Ambiguity Policy

If requirements are unclear:

* ask questions
* present options
* avoid assumptions

Do not infer project requirements without evidence.

When classification is uncertain:

* mark content as ambiguous
* request human review
* avoid automatic categorization

---

# Workspace Preferences

Prefer:

* CLI-first workflows
* observable system behavior
* composable tools
* git-based safety
* incremental learning records
* first-principles explanations

Typical environment:

* Arch Linux
* zsh
* tmux
* neovim
* CLI-first workflow

When teaching or documenting:

* explain why before how
* connect commands to system behavior
* prefer mental models over memorized recipes
* preserve transferable concepts

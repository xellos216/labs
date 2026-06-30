# AGENTS.md

# Labs Workspace Agent Rules

## Purpose

This repository is a centralized personal learning workspace for long-term technical study.

The primary goals are:

* preserve learning history
* preserve topic-oriented organization
* maintain roadmap-based learning continuity
* keep experiments reproducible
* maintain readable notes and lab records
* support ChatGPT and Codex collaboration
* prefer systems understanding over command memorization

Favor clarity, incremental progress, and maintainability over broad automation.

This repository contains:

* active learning roadmaps
* phase-based learning records
* practical lab notes
* archive documents
* review questions
* experiment records
* small experiments and proof-of-concept code
* repository operational documentation

---

# Source Policy

Labs uses both a local Git repository and a GitHub remote.

For source-of-truth and ChatGPT Project Sources policy, read:

```text
docs/labs/LABS_SOURCE_SYNC.md
```

General rule:

* GitHub remote and committed repository files are authoritative.
* ChatGPT Project Sources are cached working references, not canonical originals.
* Uncommitted local changes are invisible to ChatGPT unless pasted into the conversation or pushed to a branch.
* If uploaded Project Sources and repository files conflict, repository files win.

---

# Agent Document Index

Labs governance documents live under:

```text
docs/labs/
```

Before creating, moving, or refactoring lab documents, read the relevant documents below.

* `docs/labs/LABS_SOURCE_SYNC.md`

  * Source-of-truth, Project Sources, and GitHub connector policy.
* `docs/labs/DESIGN_PRINCIPLES.md`

  * Stable design principles for the Labs project.
* `docs/labs/LABS_SESSION_RULES.md`

  * Rules for interactive learning sessions.
* `docs/labs/ARCHIVE_TEMPLATE.md`

  * Template for archived learning/session documents.
* `docs/labs/QA_TEMPLATE_SPECIFICATION.md`

  * QA document format and review-question requirements.
* `docs/labs/LAB_EXPERIMENT_TEMPLATE.md`

  * Template for experiment-style lab notes.
* `docs/labs/ROADMAP_INDEX.md`

  * Index of roadmap documents and learning tracks.
* `docs/labs/ROADMAP_FORMAT.md`

  * Format rules for roadmap documents.
* `docs/labs/ARCHIVE_MIGRATION_PLAN.md`

  * Policy for handling older archive formats and future archive refactoring.

---

# Required Reading Policy

For ordinary small file edits, read only this `AGENTS.md` unless the task touches a specific policy area.

For source policy, Project Sources, or GitHub connector behavior, read:

* `docs/labs/LABS_SOURCE_SYNC.md`

For session archive generation, read:

* `docs/labs/LABS_SESSION_RULES.md`
* `docs/labs/ARCHIVE_TEMPLATE.md`
* `docs/labs/QA_TEMPLATE_SPECIFICATION.md`

For experiment documentation, read:

* `docs/labs/LAB_EXPERIMENT_TEMPLATE.md`

For roadmap continuation, read:

* `docs/labs/ROADMAP_INDEX.md`
* the active roadmap's `<topic>/README.md`

For roadmap creation or roadmap modification, read:

* `docs/labs/ROADMAP_FORMAT.md`
* `docs/labs/ROADMAP_INDEX.md`
* the relevant `<topic>/README.md` if it already exists

For archive migration or archive format cleanup, read:

* `docs/labs/ARCHIVE_TEMPLATE.md`
* `docs/labs/QA_TEMPLATE_SPECIFICATION.md`
* `docs/labs/ARCHIVE_MIGRATION_PLAN.md`

For repository structure, taxonomy, or organization changes, read:

* `docs/labs/LABS_SOURCE_SYNC.md`
* `docs/labs/ROADMAP_INDEX.md`
* `docs/labs/DESIGN_PRINCIPLES.md`
* `docs/labs/ARCHIVE_MIGRATION_PLAN.md`

---

# Roadmap Layout Policy

Each active roadmap directory owns its roadmap document.

The canonical roadmap path is:

```text
<topic>/README.md
```

Examples:

```text
unix/README.md
c/README.md
network/README.md
server/README.md
window/README.md
crypto/README.md
payload/README.md
```

Do not move roadmap documents into a central `roadmaps/` directory unless the user explicitly requests a structural redesign.

Roadmap documents and their session archives should stay close to each other inside the topic directory.

---

# Workspace Map

Current high-level repository structure:

```text
AGENTS.md
README.md

docs/
└── labs/

archive/

c/
crypto/
devtool/
network/
numbersystem/
payload/
server/
unix/
window/
```

`docs/labs/` contains governance documents, templates, and source policy.

Top-level topic directories contain roadmap-specific material and learning records.

`archive/` contains preserved historical or inactive learning material.

---

# Directory Semantics

## docs/labs/

Labs governance and operational documentation.

Use for:

* source sync policy
* project design principles
* session rules
* archive templates
* QA templates
* experiment templates
* roadmap index and roadmap format rules
* archive migration policy

Do not place ordinary session archives here.

---

## c/

C, memory, debugging, embedded systems, firmware, and low-level systems learning.

This track may lead toward embedded Linux, firmware analysis, and IoT systems.

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
* byte-level reasoning
* encoding and decoding
* XOR and stream cipher reasoning
* practical analysis notes

---

## devtool/

Browser DevTools and web troubleshooting learning records.

Use for:

* browser inspection notes
* network panel observations
* console observations
* practical web debugging records

---

## network/

Networking concepts, Linux networking, packet analysis, and protocol learning.

Use for:

* protocol notes
* packet capture observations
* routing, DNS, TCP, UDP, HTTP, and TLS material
* Linux networking experiments
* authorized network lab observations

---

## numbersystem/

Number systems and byte-representation learning records.

Use for:

* binary
* hexadecimal
* ASCII
* byte/bit relationships
* representation-focused notes

---

## payload/

Payload construction and parser reasoning material.

Use for:

* controlled payload experiments
* parser-boundary reasoning
* input mutation observations
* local and authorized security lab material

Keep content ethical, local, and explicitly educational.

Do not add instructions intended for unauthorized use.

---

## server/

Linux server administration training.

Use for:

* users and permissions
* authentication
* services
* logging
* SSH
* firewalling
* troubleshooting
* recovery
* VM-based administration exercises

Prefer lab VM changes over host system changes for administration experiments.

---

## unix/

Unix and Linux command-line training.

Use for:

* shell workflows
* text processing
* pipelines
* filesystem inspection
* process and service observation
* composable CLI practice

Prefer learner-first task solving and observable behavior.

---

## window/

Windows fundamentals, enterprise systems, and security-oriented Windows learning.

Use for:

* Windows architecture
* processes and services
* NTFS
* users and permissions
* event logs
* PowerShell
* Active Directory fundamentals
* Windows security observations

---

## archive/

Preserved historical or inactive learning material.

Use for:

* archived roadmaps
* old project records
* historical learning notes
* material that should remain accessible but is not a current top-level active roadmap

Do not treat archived material as an active roadmap unless the user explicitly reactivates it.

---

# Content Placement Rules

Top-level topic directories are stable learning areas.

Use them for:

* topic roadmaps
* reusable concepts
* long-term notes
* organized lab records
* phase/session archives

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

# Archive Rules

Archive documents are learning records.

Do not silently rewrite old archives to match the latest template.

Existing archives may use older formats.

Future archives should follow:

```text
docs/labs/ARCHIVE_TEMPLATE.md
```

Future QA sections should follow:

```text
docs/labs/QA_TEMPLATE_SPECIFICATION.md
```

Archive migration should be handled only as an explicit refactoring task.

Before migrating existing archives, read:

```text
docs/labs/ARCHIVE_MIGRATION_PLAN.md
```

---

# Naming Rules

Prefer:

* lowercase_with_underscores.md
* stable names
* grep-friendly filenames
* explicit phase and session names when useful

Examples:

```text
process_memory_layout.md
tcp_three_way_handshake.md
file_permissions.md
flask_routing_basics.md
```

Avoid:

* duplicate topic files
* vague names when context is unclear
* mixed naming styles
* unnecessary mass renaming

Roadmap files should normally remain:

```text
README.md
```

inside their topic directory.

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
* invent missing phase or session metadata

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
* separate roadmaps from their topic directories without approval
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
git status --short
git diff --stat
git diff --check
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

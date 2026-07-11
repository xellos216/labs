# AGENTS.md

# Labs Workspace Agent Rules

## Purpose

This repository is a centralized personal learning workspace for long-term technical study.

The primary goals are:

* preserve learning continuity
* preserve topic-oriented organization
* maintain roadmap-based progress
* keep experiments reproducible
* maintain readable notes and lab records
* support ChatGPT and Codex collaboration
* prefer systems understanding over command memorization

Favor clarity, incremental progress, and maintainability over broad automation.

This repository contains:

* active learning roadmaps
* backlog roadmaps
* archived roadmaps retained for review and reference
* phase-based learning records
* practical lab notes
* session archive documents inside roadmap tracks
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
* `docs/labs/MARKDOWN_GENERATION_POLICY.md`

  * Markdown generation, formatting, markdownlint validation, and redaction policy.
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

---

# Required Reading Policy

For ordinary small file edits, read only this `AGENTS.md` unless the task touches a specific policy area.

For source policy, Project Sources, or GitHub connector behavior, read:

* `docs/labs/LABS_SOURCE_SYNC.md`

For Markdown generation, Markdown cleanup, privacy redaction, or Markdown policy changes, read:

* `docs/labs/MARKDOWN_GENERATION_POLICY.md`

For session archive generation, read:

* `docs/labs/LABS_SESSION_RULES.md`
* `docs/labs/ARCHIVE_TEMPLATE.md`
* `docs/labs/QA_TEMPLATE_SPECIFICATION.md`

For experiment documentation, read:

* `docs/labs/LAB_EXPERIMENT_TEMPLATE.md`

For roadmap continuation, read:

* `docs/labs/ROADMAP_INDEX.md`
* the roadmap's `README.md` from its current `active/`, `backlog/`, or `archive/` lifecycle directory

For roadmap creation or roadmap modification, read:

* `docs/labs/ROADMAP_FORMAT.md`
* `docs/labs/ROADMAP_INDEX.md`
* the relevant roadmap `README.md` from `active/`, `backlog/`, or `archive/` if it already exists

For repository structure, taxonomy, or organization changes, read:

* `docs/labs/LABS_SOURCE_SYNC.md`
* `docs/labs/ROADMAP_INDEX.md`
* `docs/labs/DESIGN_PRINCIPLES.md`

---

# Repository Layout Policy

Current high-level repository structure:

```text
AGENTS.md
README.md
active/
backlog/
archive/
docs/
```

## active/

`active/` contains roadmaps that are currently practiced or expanded.

Canonical active roadmap path:

```text
active/<roadmap>/README.md
```

Use active roadmap directories for:

* topic roadmaps
* reusable concepts
* long-term notes
* organized lab records
* phase/session archives
* practical observations

## backlog/

`backlog/` contains planned, paused, or future roadmaps.

Backlog roadmap path:

```text
backlog/<roadmap>/README.md
```

Backlog material is not active unless explicitly reactivated.

## archive/

`archive/` contains roadmaps whose planned learning sessions are complete and whose roadmap, session records, and review material remain available.

Canonical archived roadmap path:

```text
archive/<roadmap>/README.md
```

Review answers, factual corrections, link repairs, and clearly scoped maintenance may continue in an archived roadmap. Review-only work does not reactivate a track.

The lifecycle `archive/` directory is not a restoration area for historical, pre-redaction, or legacy material. Reintroducing such material requires an explicit audited restoration, migration, or private archival task.

## docs/labs/

`docs/labs/` contains governance and operational documentation.

Use for:

* source sync policy
* project design principles
* session rules
* Markdown generation policy
* archive templates
* QA templates
* experiment templates
* roadmap index and roadmap format rules

Do not place ordinary session archives here.

---

# Roadmap Layout Policy

Each roadmap directory owns its roadmap document inside its current lifecycle directory.

Canonical roadmap paths are:

```text
active/<roadmap>/README.md
backlog/<roadmap>/README.md
archive/<roadmap>/README.md
```

Current examples:

```text
active/unix/README.md
active/c/README.md
active/network/README.md
active/server/README.md
active/crypto/README.md
active/payload/README.md
backlog/window/README.md
archive/numbersystem/README.md
```

Do not move roadmap documents into a central `roadmaps/` directory unless the user explicitly requests a structural redesign.

Roadmap documents and their session archives should stay close to each other inside the topic directory.

---

# Content Placement Rules

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

Session archive documents are learning records and may exist inside roadmap directories under `active/`, `backlog/`, or `archive/`.

The term "session archive" describes a learning record. The top-level `archive/` directory describes a roadmap lifecycle state. Do not confuse lifecycle relocation with session archive format migration.

Future archives should follow:

```text
docs/labs/ARCHIVE_TEMPLATE.md
```

Future QA sections should follow:

```text
docs/labs/QA_TEMPLATE_SPECIFICATION.md
```

Do not silently rewrite populated learner answers.

Do not collapse phase history into polished notes without review.

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

Roadmap files should normally remain named:

```text
README.md
```

---

# Modification Policy

Always prefer:

* small diffs
* explicit reasoning
* incremental changes
* preserving learning continuity
* reading local README files before changing a topic area

Never:

* mass-delete files without explicit approval
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
* destroy learning context without explicit approval
* obscure the reason a lab was created

When extracting reusable knowledge from phase notes, preserve the original phase record unless the user explicitly approves consolidation.

---

# Privacy and Redaction

Labs may be public.

Before committing Markdown produced from real local output, follow:

```text
docs/labs/MARKDOWN_GENERATION_POLICY.md
```

Mask personal and local environment identifiers such as public IPs, MAC addresses, host-specific interface names, usernames, hostnames, local paths, tokens, or account IDs.

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

For Markdown changes, run:

```bash
npx markdownlint-cli2@latest \
  "README.md" \
  "AGENTS.md" \
  "active/**/*.md" \
  "backlog/**/*.md" \
  "archive/**/*.md" \
  "docs/labs/**/*.md"
```

For public Markdown generated from real network or host output, run the redaction checks documented in:

```text
docs/labs/MARKDOWN_GENERATION_POLICY.md
```

For structural refactors:

```bash
rg 'old/path' active backlog archive docs README.md AGENTS.md
rg '\]\(.*\.md\)' active backlog archive docs README.md AGENTS.md
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

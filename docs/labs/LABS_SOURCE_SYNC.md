# Labs Source Sync Policy

> This document defines how Labs project context is shared between the local repository, GitHub remote, ChatGPT Project Sources, and GitHub connector.
>
> Labs differs from ordinary coding or documentation projects because ChatGPT is also used as an interactive learning partner and archive generator.

---

# Purpose

The purpose of this document is to define which source should be treated as authoritative when ChatGPT works with the Labs project.

Labs uses multiple context locations:

* local working tree
* GitHub remote repository
* ChatGPT Project Sources
* current conversation

These locations do not always contain the same state.

This document defines how to handle that difference.

---

# Source-of-Truth Model

The local Git repository and its GitHub remote are the canonical source of truth for Labs.

Version-controlled project documents should be updated locally, committed, and pushed.

The GitHub remote is the preferred source for ChatGPT when current repository state matters.

ChatGPT Project Sources are not canonical.

Uploaded Project Sources may be useful as cached working references, but they may become stale and must not override the GitHub repository.

If ChatGPT Project Sources and GitHub conflict, GitHub wins.

---

# Context Locations

## Local Working Tree

The local working tree is where edits are created, reviewed, and committed.

Uncommitted local changes are not visible through the GitHub connector.

To ask ChatGPT to review uncommitted work, either:

* paste the relevant `git diff` directly into the conversation
* commit and push the work to a branch, then tell ChatGPT which branch to read

Do not assume that ChatGPT can see local uncommitted changes.

## GitHub Remote Repository

The GitHub remote contains committed and pushed Labs history.

It is authoritative for:

* roadmap documents
* archive documents
* session records
* project templates
* source policy documents
* long-term project structure

## ChatGPT Project Sources

ChatGPT Project Sources are cached working references.

They may be used for high-frequency documents that ChatGPT needs during ordinary learning and archive generation.

They are not authoritative.

## Current Conversation

The current conversation may contain temporary instructions, clarifications, or user decisions.

Conversation context can guide the current task, but it must not silently override the repository when repository state is relevant.

---

# Recommended Project Sources

Keep the following in ChatGPT Project Sources:

* `docs/labs/LABS_SOURCE_SYNC.md`
* `docs/labs/LABS_SESSION_RULES.md`
* `docs/labs/MARKDOWN_GENERATION_POLICY.md`
* `docs/labs/ARCHIVE_TEMPLATE.md`
* `docs/labs/QA_TEMPLATE_SPECIFICATION.md`
* `docs/labs/LAB_EXPERIMENT_TEMPLATE.md`
* `docs/labs/ROADMAP_INDEX.md`

Optionally keep:

* `docs/labs/DESIGN_PRINCIPLES.md`

Do not keep ordinary session archives, handoff files, temporary notes, or frequently changing progress records in ChatGPT Project Sources.

Individual roadmap documents should normally be read from the GitHub remote through the GitHub connector.

---

# Roadmap Loading Policy

Each active roadmap owns its roadmap document.

The canonical roadmap path is:

```text
active/<roadmap>/README.md
```

Examples:

```text
active/unix/README.md
active/c/README.md
active/network/README.md
active/server/README.md
active/window/README.md
active/crypto/README.md
active/payload/README.md
active/numbersystem/README.md
```

Backlog roadmaps may be referenced at `backlog/<roadmap>/README.md`, but they are not active unless explicitly reactivated.

Before continuing a learning sequence, ChatGPT should consult the relevant roadmap document from the GitHub remote.

If a roadmap file has moved or the expected path is unavailable, ChatGPT should report the missing file instead of inventing the session order.

Uploaded Project Sources may contain cached references, but they must not override the roadmap in the GitHub remote.

---

# Archive and Template Policy

For ordinary archive generation, ChatGPT may use cached Project Sources for:

* archive format
* QA format
* experiment format
* session interaction rules
* Markdown generation and redaction policy

If the user says templates were recently edited, or if there is any conflict, ChatGPT should fetch the current template from GitHub before generating final archive output.

Archive documents are generated only when explicitly requested.

Existing archives may use older formats.

Do not silently rewrite historical archives unless the user explicitly requests an archive migration or refactoring task.

---

# Preferred Workflow

For repository updates:

```text
Local repo
→ commit
→ push
→ GitHub remote
→ ChatGPT reads current files through GitHub connector
```

For frequent archive output:

```text
Project Sources cached templates
→ generate archive
→ user saves locally
→ commit
→ push
```

---

# Conflict Policy

If Project Sources and GitHub remote disagree:

1. Treat GitHub remote as authoritative.
2. Report the conflict.
3. Ask whether the stale Project Source should be updated or removed.

Do not silently merge conflicting rules.

---

# New Session Bootstrap

At the start of a Labs session, use this rule:

```text
Use Project Instructions and `docs/labs/LABS_SOURCE_SYNC.md` for source policy.
Use cached Project Sources for common templates.
Use the GitHub connector to read the active roadmap before continuing a learning sequence.
Treat GitHub remote as authoritative over uploaded Project Sources.
```

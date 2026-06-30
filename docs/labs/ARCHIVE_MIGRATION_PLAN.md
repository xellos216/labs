# Labs Archive Migration Plan

> This document records how Labs handles historical archive documents that were generated under older formats.
>
> Existing archives are learning records. They should not be silently rewritten without an explicit migration task.

---

# Purpose

Labs archives have been created over time while the project rules, archive templates, QA format, and metadata conventions were still evolving.

As a result, older archive documents may not match the current archive format.

This document defines how to classify, preserve, and later refactor those archives.

---

# Current Policy

Existing archives are historical records.

They should remain valid as records of the learning session even if their format differs from the current template.

Do not rewrite old archives automatically.

Do not silently normalize old archives during unrelated learning sessions.

Archive migration should be performed only as an explicit refactoring task.

---

# Current Archive Format

Current archive documents should follow:

```text
docs/labs/ARCHIVE_TEMPLATE.md
```

Current QA sections should follow:

```text
docs/labs/QA_TEMPLATE_SPECIFICATION.md
```

Current experiment records should follow:

```text
docs/labs/LAB_EXPERIMENT_TEMPLATE.md
```

---

# Archive Version Policy

Future archive documents should include an archive version field in metadata.

Recommended current value:

```yaml
ArchiveVersion: 2
```

Archives without `ArchiveVersion` should be treated as legacy archives unless there is clear evidence that they already follow the current format.

---

# Legacy Archive Indicators

A document may be treated as a legacy archive if it has one or more of the following:

* no `ArchiveVersion` field
* missing `Review` metadata
* old QA format
* answers filled when they were not explicitly requested
* missing collapsible answer sections
* inconsistent session metadata
* roadmap/session naming that no longer matches the current roadmap
* archive sections that do not match the current template

These indicators do not mean the archive is invalid.

They only mean the document may require migration if consistency is desired.

---

# Migration Goals

A future migration should aim to:

* preserve the original learning content
* preserve roadmap, phase, session, title, and date metadata when available
* add missing current metadata where it can be inferred safely
* mark uncertain metadata explicitly instead of guessing
* normalize QA sections to the current format
* keep answers blank unless the archive was explicitly intended as an answer key
* avoid changing the meaning of the original session record

---

# Migration Rules

During migration:

1. Do not invent missing session information.
2. Do not silently change roadmap order.
3. Do not rewrite technical explanations unless they are clearly incorrect.
4. Do not remove useful learner observations.
5. Do not convert historical uncertainty into certainty.
6. Preserve old wording when it reflects the actual learning process.
7. Add notes only when needed to clarify migration decisions.

## Unix Scope Exclusion

The `unix/` directory is excluded from general archive migration and refactoring work.

Unix uses a separate compact roadmap and archive format. Do not inspect, classify, migrate, normalize, or rewrite Unix files as part of a general archive migration task.

Do not force Unix `notes.md` files or compact session files into the full archive template.

Unix files may be modified only through an explicit Unix-specific task requested by the user.

General archive inventory reports should either omit Unix entirely or identify it only as explicitly out of scope, not as migration work.

---

# Roadmap Reconciliation Policy

The current canonical roadmap is authoritative for the active roadmap session sequence.

If an existing archive path, title, or session conflicts with the current roadmap, do not silently rename the file or rewrite its content to make it appear that the historical session followed the current sequence.

Preserve mismatched files as historical or pre-roadmap archives. When appropriate, move them into a local `legacy/` directory near their original phase or session location.

Example:

```text
server/phase00/legacy/05_virtmanager_virsh.md
```

Moving a file into `legacy/` must preserve its historical learning content. Do not delete the file or rewrite its technical content solely to match the current roadmap.

Do not invent a missing current-roadmap session archive automatically. If the user explicitly approves creation and the conditions in `Current Session Creation Limit` are satisfied, create a new Draft archive or study file using:

* the current canonical roadmap
* `docs/labs/ARCHIVE_TEMPLATE.md`
* nearby current-format session files

New study archives should use:

```yaml
Status: Draft
Review: Pending
ArchiveVersion: 2
```

QA answers should remain blank.

Prepared study archives must not fabricate completed observations, command outputs, screenshots, logs, packet captures, learner answers, or other completed learner work. Suggested observations and study targets should be labeled as such.

## Current Session Creation Limit

Do not create archives for future or not-yet-learned roadmap sessions during archive migration.

A missing session in the current roadmap is not automatically a migration candidate. If no historical local archive occupied that session number or path, report it as:

```text
not yet learned / no archive expected
```

A replacement Draft archive or study file may be created only when all of the following are true:

1. A historical local archive or session file already existed.
2. Its session number or path conflicted with the current canonical roadmap.
3. The historical file was moved into a local `legacy/` directory, creating a gap in the current roadmap-aligned sequence.
4. The user explicitly approved creating a replacement current-roadmap Draft archive or study file for that reconciliation gap.

Do not fabricate study completion, observations, command outputs, screenshots, logs, packet captures, or learner answers in a replacement file.

Do not mark a replacement archive or study file as `Completed` unless explicit evidence supports that status.

Treat future roadmap sessions as learning work, not archive migration work.

Treat this work as roadmap reconciliation, not as a simple archive format migration. Reconciliation requires checking the current roadmap sequence, historical file identity, and content placement before applying format changes.

---

# Suggested Migration Workflow

Use a dedicated branch for archive migration.

```text
main
↓
refactor/archive-format-migration
```

Recommended process:

```text
Inventory archives
↓
Classify legacy/current format
↓
Identify missing metadata
↓
Normalize one roadmap at a time
↓
Review diff carefully
↓
Commit in small batches
```

---

# Suggested Codex Task Scope

When using Codex for migration, provide a narrow task.

Example:

```text
Refactor only Networking Phase 02 archive files to the current Labs archive format.

Use:
- docs/labs/ARCHIVE_TEMPLATE.md
- docs/labs/QA_TEMPLATE_SPECIFICATION.md
- docs/labs/ARCHIVE_MIGRATION_PLAN.md

Do not invent missing metadata.
Do not change roadmap order.
Do not rewrite technical explanations unless there is an obvious factual error.
Leave QA answers blank unless they were already intentionally filled as review answers.
```

---

# Non-Goals

This migration plan is not for:

* changing the learning roadmap
* merging or deleting completed sessions
* rewriting the learner's historical answers
* making old archives look artificially uniform
* changing technical content without review
* replacing the current archive template

---

# Final Principle

Archive migration is a cleanup task, not a learning task.

The goal is consistency without losing the historical record of how understanding developed.

# Markdown Generation Policy

This document defines how Markdown should be created or modified in Labs.

The goal is to prevent recurring cleanup work by making generated Markdown match the repository lint policy before commit.

---

# Scope

This policy applies to generated or modified Markdown under:

```text
README.md
AGENTS.md
LICENSE.md
THIRD_PARTY_NOTICES.md
active/**/*.md
backlog/**/*.md
archive/**/*.md
docs/labs/**/*.md
```

Repository Markdown outside these paths should be handled only when the task explicitly includes it.

Canonical legal texts stored under `LICENSES/` are not generated repository Markdown. They are excluded from normal Markdown linting and formatting normalization.

The public repository baseline does not keep a `legacy/` tree. The top-level `archive/` directory is reserved for completed roadmap lifecycles; it is not a restoration area for historical or pre-redaction material. Do not reintroduce historical archive directories unless the user explicitly requests a dedicated restoration or migration task.

---

# Source of Truth

The repository is authoritative.

Markdown generation must follow:

```text
.markdownlint-cli2.jsonc
.github/workflows/markdown.yml
```

ChatGPT Project Sources are cached references. If Project Sources and committed repository files disagree, the committed repository files win.

---

# Required Formatting Habits

When creating or editing Markdown, follow these rules by default:

- Put blank lines before and after lists.
- Use language identifiers on fenced code blocks.
- End every Markdown file with exactly one trailing newline.
- Avoid trailing spaces.
- Avoid repeated blank lines unless a template explicitly requires them.
- Do not rewrite learner answers for style-only reasons.

Example list formatting:

```markdown
After completing this phase, you should be able to:

- explain the concept
- observe the behavior
- connect it to related systems

Next paragraph starts here.
```

Example fenced code formatting:

````markdown
```bash
git status --short
```
````

---

# Canonical Legal-Text Preservation

Official license texts must be obtained from the authoritative license publisher and stored verbatim. Do not edit, reflow, translate, trim, or normalize a canonical legal text merely to satisfy repository formatting conventions.

When practical, verify downloaded legal text byte-for-byte against a fresh copy from the same official source. Record the official source and verification method. If an exact canonical source causes an intentional whitespace warning, document the warning instead of silently correcting the legal text.

This exception applies only to verified canonical legal text. Ordinary repository documents, including `LICENSE.md` and `THIRD_PARTY_NOTICES.md`, remain subject to the normal Markdown policy.

---

# Privacy and Redaction

Labs is a public repository.

When creating or editing Markdown, do not preserve raw personal or local environment identifiers unless the user explicitly requests it for a private note.

Mask or generalize:

- public WAN IP addresses
- home or local gateway IP addresses
- private LAN IP addresses when they reveal the user's real network layout
- MAC addresses
- stable device-specific interface names from the real host, replacing them with documentation-safe names such as `eth0` or `wlan0`
- hostnames, usernames, local paths, tokens, account IDs, or other identifiers tied to the user's real environment

Prefer documentation-safe examples:

```text
Public example IPs:
203.0.113.10
198.51.100.23
192.0.2.15

Private LAN examples:
192.168.0.10
192.168.0.1

IPv6 documentation example:
2001:db8::1

MAC examples:
aa:bb:cc:dd:ee:ff
aa:bb:cc:dd:ee:11

Interface examples:
eth0
wlan0
```

For network learning archives, preserve the technical relationship while masking the real identifier.

Example:

```text
Real observation:
default via <real-public-gateway> dev <real-interface> src <real-public-ip>
<real-mac-address>

Archive-safe form:
default via 203.0.113.1 dev eth0 src 203.0.113.10
aa:bb:cc:dd:ee:ff
```

The purpose is to preserve the network model without exposing the user's actual environment.

Historical or pre-redaction material must not be reintroduced into the public repository unless the task is explicitly about audited restoration, migration, or private archival work.

## Images and Other Media

Every image or other media file intended for the public repository requires review of the rendered or visible content, its filename and surrounding Markdown context, and embedded metadata when present. For images, manual visual inspection is mandatory. Text searches cannot detect identifiers rendered inside image pixels.

Inspect visible content for:

- terminal prompts, usernames, and hostnames
- local filesystem paths
- timestamps when they are sensitive
- debugger PINs, tokens, session identifiers, QR codes, credentials, or other secrets
- public or revealing network identifiers
- window titles, tabs, notifications, and background content

List tracked media with a Git-aware command, adapting the extensions to the task:

```bash
git ls-files -- '*.png' '*.jpg' '*.jpeg' '*.gif' '*.webp' '*.svg' '*.pdf' '*.mp4' '*.webm'
```

When `exiftool` is already available, it may be used to inspect embedded metadata:

```bash
exiftool "<media-path>"
```

If `exiftool` is unavailable, use an equivalent local metadata viewer or request human metadata review. Do not require tool installation or OCR solely to satisfy this policy. Removing metadata does not replace visual inspection.

---

# Git Metadata and History Exposure

Commit author names and email addresses are public metadata when repository history is published. Before making public commits, contributors should inspect their configured identity. A GitHub-provided noreply address may be used when appropriate.

Useful inspection commands include:

```bash
git config --get user.name
git config --get user.email
git log --all --format='%h %an <%ae>' | sort -u
git log --all -- <repository-relative-path>
```

Removing or sanitizing a file in the current tree does not remove earlier versions from Git history. Renamed or deleted files may remain reachable from old commits, tags, branches, forks, and clones.

Findings from identity or history inspection require human review and must not trigger automatic history rewriting. History rewriting is destructive and must be a separate, explicitly approved task. Ordinary Markdown cleanup must not rewrite history, and rewriting the current repository cannot guarantee removal from existing forks or clones.

---

# Required Validation

Before committing Markdown changes, run:

```bash
npx markdownlint-cli2@latest \
  "README.md" \
  "AGENTS.md" \
  "LICENSE.md" \
  "THIRD_PARTY_NOTICES.md" \
  "active/**/*.md" \
  "backlog/**/*.md" \
  "archive/**/*.md" \
  "docs/labs/**/*.md"
```

Expected result:

```text
Summary: 0 error(s)
```

Also check the diff:

```bash
git diff --check
git diff
```

When staged changes are relevant, inspect them as well:

```bash
git diff --cached --check
git diff --cached
```

Before committing public Markdown that used real network or host output, search for unmasked environment identifiers.

Check MAC addresses:

```bash
rg -n --pcre2 \
  -e '\b[0-9A-Fa-f]{2}(?::[0-9A-Fa-f]{2}){5}\b' \
  -- active backlog archive docs README.md AGENTS.md LICENSE.md THIRD_PARTY_NOTICES.md
```

Check public IPv4 addresses:

```bash
rg -n --pcre2 \
  -e '\b(?!(?:10|127)\.)(?!(?:172\.(?:1[6-9]|2[0-9]|3[01]))\.)(?!(?:192\.168)\.)(?!(?:169\.254)\.)(?!(?:0|255)\.)(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}\b' \
  -- active backlog archive docs README.md AGENTS.md LICENSE.md THIRD_PARTY_NOTICES.md
```

Review matches manually because documentation ranges such as `203.0.113.0/24`, `198.51.100.0/24`, `192.0.2.0/24`, and well-known public examples such as `8.8.8.8` may be intentional.

Do not commit broad formatting changes unless the task is explicitly a formatting cleanup.

---

# Agent Instruction

When an agent generates or edits Markdown for Labs, it must:

1. Read this policy when the task involves Markdown generation, Markdown cleanup, privacy redaction, or Markdown policy changes.
2. Keep changes scoped to the requested files.
3. Preserve learner answers and historical context.
4. Avoid reintroducing historical or pre-redaction material into the public repository unless explicitly requested.
5. Mask personal or local environment identifiers before writing public Markdown.
6. Visually inspect public media and review its metadata, or request human review when the agent cannot do so; do not rely only on text searches for image privacy.
7. Preserve verified canonical legal texts exactly and exclude them from ordinary formatting normalization.
8. Run or request the repository markdownlint command before commit.
9. Run or request redaction checks when real network or host output appears in the generated Markdown.
10. Report Git identity or historical exposure findings for human review without rewriting history.
11. Keep public-documentation changes narrow, observable, and reviewable.

---

# ChatGPT Project Instruction Snippet

Use this short instruction in the ChatGPT Labs project settings:

```text
When creating or editing Markdown for Labs, follow the canonical repository policy in docs/labs/MARKDOWN_GENERATION_POLICY.md. The GitHub repository is authoritative over Project Sources; do not reintroduce historical or pre-redaction material unless explicitly requested.
```

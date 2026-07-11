# Markdown Generation Policy

This document defines how Markdown should be created or modified in Labs.

The goal is to prevent recurring cleanup work by making generated Markdown match the repository lint policy before commit.

---

# Scope

This policy applies to generated or modified Markdown under:

```text
README.md
AGENTS.md
active/**/*.md
backlog/**/*.md
archive/**/*.md
docs/labs/**/*.md
```

Repository Markdown outside these paths should be handled only when the task explicitly includes it.

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

---

# Required Validation

Before committing Markdown changes, run:

```bash
npx markdownlint-cli2@latest \
  "README.md" \
  "AGENTS.md" \
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

Before committing public Markdown that used real network or host output, search for unmasked environment identifiers.

Check MAC addresses:

```bash
rg -n --pcre2 \
  -e '\b[0-9A-Fa-f]{2}(?::[0-9A-Fa-f]{2}){5}\b' \
  -- active backlog archive docs README.md AGENTS.md
```

Check public IPv4 addresses:

```bash
rg -n --pcre2 \
  -e '\b(?!(?:10|127)\.)(?!(?:172\.(?:1[6-9]|2[0-9]|3[01]))\.)(?!(?:192\.168)\.)(?!(?:169\.254)\.)(?!(?:0|255)\.)(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}\b' \
  -- active backlog archive docs README.md AGENTS.md
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
6. Run or request the repository markdownlint command before commit.
7. Run or request redaction checks when real network or host output appears in the generated Markdown.

---

# ChatGPT Project Instruction Snippet

Use this short instruction in the ChatGPT Labs project settings:

```text
When creating or editing Markdown for Labs, follow the canonical repository policy in docs/labs/MARKDOWN_GENERATION_POLICY.md. The GitHub repository is authoritative over Project Sources; do not reintroduce historical or pre-redaction material unless explicitly requested.
```

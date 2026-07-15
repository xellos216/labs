# Getting Started with Labs

## What Labs Is

Labs is a method for organizing long-term technical learning around explicit
goals, observable evidence, and durable mental models. Its main record types
have different roles:

- A **roadmap** defines a topic's learning objective, phases, and documented
  session sequence.
- A **learning session** is an interactive unit of study and investigation
  within a roadmap.
- An **experiment record** documents a reproducible practical investigation,
  including procedure, evidence, and conclusions.
- A **session archive** preserves what happened during a learning session.
  It stays inside the roadmap that owns it.
- A **lifecycle directory** is `active/`, `backlog/`, or `archive/`. The
  directory records the roadmap's current lifecycle state, not the format of
  an individual learning record.

## Two Usage Paths

There are two distinct ways to use Labs:

1. Browse the populated `xellos216/labs` repository as a reference
   implementation, including its evolving roadmaps and historical records.
2. Create a separate personal learning workspace whose goals, environment,
   roadmap order, and progress belong to you.

Do not treat the populated reference repository as an empty template. Its
content and Git history reflect an existing learner's work.

## Manual Bootstrap Until `labs-starter` Exists

A separate `labs-starter` template repository is planned but is not yet
available. Until then, a minimal directory skeleton can be created manually:

```bash
mkdir my-labs
cd my-labs
git init
mkdir -p active backlog archive docs/labs
```

These commands create only a repository and its initial directories; they do
not create a complete Labs installation. Selectively copy and adapt only the
governance and template documents you need. Preserve required attribution
and license notices, and review the reference repository's [License and
Scope](../../LICENSE.md) before reusing material.

Useful reference documents include:

- [Design Principles](DESIGN_PRINCIPLES.md)
- [Labs Session Rules](LABS_SESSION_RULES.md)
- [Roadmap Format Specification](ROADMAP_FORMAT.md)
- [Archive Template](ARCHIVE_TEMPLATE.md)
- [QA Template Specification](QA_TEMPLATE_SPECIFICATION.md)
- [Lab Experiment Template](LAB_EXPERIMENT_TEMPLATE.md)
- [Markdown Generation Policy](MARKDOWN_GENERATION_POLICY.md)

Create a roadmap index that reflects your own repository. Do not copy the
reference repository's personal roadmap inventory unchanged.

## Create the First Roadmap

1. Define the learning objective and intended scope.
2. Create `backlog/<roadmap>/README.md` using the roadmap format as a guide.
3. Review the proposed phases and sessions before beginning.
4. Move the roadmap to `active/` only when actual learning begins.
5. Keep phase and session records inside the same roadmap directory.
6. Move the whole roadmap to `archive/` only when its planned sequence is
   complete.

There is no universal first roadmap. Choose a topic that matches your goals
and the systems you can investigate safely.

## Run a Session

Use the canonical cycle:

```text
Understand
↓
Predict
↓
Observe
↓
Explain
```

Begin with enough context to understand the problem. When practical, make a
learner prediction before receiving a complete explanation. Observe a real
system or controlled lab before drawing conclusions, and record observations
separately from interpretations, assumptions, and speculation.

Prefer local, reproducible, observable, reversible, and authorized
experiments. Generate a session archive only when you explicitly want to
preserve the session as a record.

## Git Workflow

Prefer small changes, clean working trees, narrow commits, and explicit diff
review. Inspect the affected paths before reorganizing or deleting material.
Use a separate branch for broad structural changes, and preserve historical
records unless a reviewed migration explicitly includes them.

Git is a safety boundary: it should make changes observable and reversible,
not hide large automated rewrites.

## Public Repository Safety

Before publishing learning records, remove or mask:

- usernames and hostnames
- personal filesystem paths
- public or revealing network identifiers
- MAC addresses
- tokens and credentials
- debugger output containing secrets
- private screenshots
- sensitive Git metadata where relevant

Follow the [Markdown Generation Policy](MARKDOWN_GENERATION_POLICY.md) for
formatting, privacy, and redaction checks.

## Next Step

Labs does not require an AI tool. If you want an optional AI assistant for
interactive sessions, review the [Optional ChatGPT Setup](CHATGPT_SETUP.md).

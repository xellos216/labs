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
2. Generate a separate personal learning workspace from the clean
   `xellos216/labs-starter` template, then adapt its goals, environment,
   roadmap order, and progress to your needs.

Do not treat the populated reference repository as an empty template. Its
content and Git history reflect an existing learner's work.

## Create a Workspace from Labs Starter

Use the public
[xellos216/labs-starter](https://github.com/xellos216/labs-starter) template
to create a clean personal workspace. The generated repository has Git history
independent from both the populated `xellos216/labs` reference repository and
the `xellos216/labs-starter` template repository.

After generating the repository, adapt its `README.md` to describe your own
learning workspace and choose appropriate licenses for future personal
content. Before the first personal commit, confirm the Git identity that will
be recorded publicly:

```bash
git config --get user.name
git config --get user.email
```

Create the first roadmap with the roadmap template included in the generated
repository, then register it in that repository's roadmap index. The generated
workspace is yours to adapt; it does not copy the populated reference
repository's personal roadmaps or progress. AI setup is optional.

## Create the First Roadmap

1. Define the learning objective and intended scope.
2. Create `backlog/<roadmap>/README.md` from the roadmap template included in
   the generated repository.
3. Register the roadmap in the generated repository's roadmap index.
4. Review the proposed phases and sessions before beginning.
5. Move the roadmap to `active/` only when actual learning begins.
6. Keep phase and session records inside the same roadmap directory.
7. Move the whole roadmap to `archive/` only when its planned sequence is
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

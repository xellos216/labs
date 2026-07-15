# Labs

## Purpose

Labs is a long-term technical learning workspace built around systems
understanding, observable evidence, practical investigation, and durable
mental models. It records how concepts were predicted, tested, explained,
and connected across related systems.

The repository is a noncommercial learning resource, not a finished
commercial curriculum or a substitute for direct observation and practice.

## Repository Status

This is the populated personal learning workspace of `xellos216` and a
reference implementation of the Labs method. Its roadmap order, recorded
progress, and topic selection reflect one learner's path. Historical session
archives may use older formats that remain useful as learning records.

This repository is not an empty starter repository. A separate
`labs-starter` repository is planned but is not yet available. Until it
exists, readers should adapt only the parts of this reference implementation
that fit their own goals. The repository is not distributed as a whole under
an OSI-approved software license.

## Who It Is For

Labs may be useful to learners who want durable understanding of areas such
as systems, Unix and Linux, programming, networking, administration,
embedded systems, firmware, or practical security investigation. Readers can
adapt the method to their own operating system, shell, editor, tools, and lab
environment.

## Learning Method

The canonical learning cycle is:

```text
Understand
↓
Predict
↓
Observe
↓
Explain
```

A short concept establishes the problem, a prediction creates a testable
expectation, observation supplies evidence, and explanation connects the
result to a durable mental model. See the [Design
Principles](docs/labs/DESIGN_PRINCIPLES.md) and [Labs Session
Rules](docs/labs/LABS_SESSION_RULES.md) for the canonical method.

## Explore the Repository

- `active/` contains roadmaps currently being practiced or expanded.
- `backlog/` contains planned, paused, or future roadmaps.
- `archive/` contains roadmaps whose planned learning sequence is complete.
- `docs/labs/` contains governance, templates, policies, and navigation.

A roadmap's directory determines its current roadmap lifecycle state. A
session archive is a learning record stored with its roadmap; it is not the
same thing as the top-level `archive/` lifecycle directory. See the [Roadmap
Index](docs/labs/ROADMAP_INDEX.md) for the current inventory.

## Quick Start for Reading

Clone the populated reference repository:

```bash
git clone https://github.com/xellos216/labs.git
cd labs
```

Then read this `README.md`, open the [Roadmap
Index](docs/labs/ROADMAP_INDEX.md), choose a relevant roadmap `README.md` in
its lifecycle directory, and inspect its existing phase or session records.

Cloning this repository copies the populated personal learning workspace and
its Git history. It is useful for reference, but it is not the recommended
clean bootstrap for a new personal Labs repository.

## Start Your Own Labs

- [Getting Started with Labs](docs/labs/GETTING_STARTED.md)
- [Optional ChatGPT Setup](docs/labs/CHATGPT_SETUP.md)
- [Project Instructions Template](docs/labs/PROJECT_INSTRUCTIONS.md)

ChatGPT or another LLM can be used as an optional AI assistant, but Labs can
be operated without one. The committed repository remains the source of
truth.

## Safety and Public Documentation

Experiments should be local, reproducible, observable, reversible, and
authorized. Follow the safety guidance in the [Labs Session
Rules](docs/labs/LABS_SESSION_RULES.md) and the privacy and redaction rules in
the [Markdown Generation Policy](docs/labs/MARKDOWN_GENERATION_POLICY.md)
before publishing observations.

## License

Original learning documents and embedded code examples are available under
the repository's stated noncommercial documentation license where the owner
holds the necessary rights. Standalone programs, automation, configuration,
and third-party material do not automatically inherit that license. Read
[License and Scope](LICENSE.md) and [Third-Party
Notices](THIRD_PARTY_NOTICES.md) before copying or adapting material.

## Contributions and Support

This repository is currently maintained as a personal learning workspace. It
is not yet accepting general curriculum contributions or providing
individual learning support.

# Optional ChatGPT Setup for Labs

## Role of ChatGPT

ChatGPT can be used as:

- a reasoning partner
- an interactive learning assistant
- a review and drafting tool
- an optional archive generator

ChatGPT is not:

- the canonical source of repository state
- a replacement for system observation
- proof that an experiment occurred
- mandatory for using Labs

The committed repository remains the source of truth. ChatGPT is an optional
AI assistant around that workflow.

## Recommended Workspace Setup

Use a project-scoped ChatGPT workspace, or the current equivalent available
to you, to keep related instructions and references together:

1. Create a workspace for your personal Labs repository.
2. Add the contents of [Project Instructions](PROJECT_INSTRUCTIONS.md) as the
   workspace's project instructions or equivalent persistent guidance.
3. Make the relevant repository material available to the workspace.
4. Keep the committed repository authoritative over cached or uploaded
   copies.
5. Load the relevant roadmap before continuing a learning sequence.

Interface labels and available features may differ by product surface or
change over time. The workflow matters more than a fixed menu location.

## Ways to Provide Repository Context

Choose the narrowest supported method that provides the material needed for
the current session:

- Use a supported GitHub connection when it is available for your account,
  product experience, and repository.
- Upload stable governance and template documents as reusable references.
- Paste the relevant roadmap, file excerpt, or local diff into the current
  conversation.

Do not assume that every account or platform provides every integration.
Uncommitted local changes are invisible unless you paste them or otherwise
make them available to the conversation.

## Recommended Stable Reference Documents

Follow [Labs Source Sync Policy](LABS_SOURCE_SYNC.md) when deciding what to
keep as reusable project context. Recommended stable references include:

- `LABS_SOURCE_SYNC.md`
- `LABS_SESSION_RULES.md`
- `MARKDOWN_GENERATION_POLICY.md`
- `ARCHIVE_TEMPLATE.md`
- `QA_TEMPLATE_SPECIFICATION.md`
- `LAB_EXPERIMENT_TEMPLATE.md`
- `ROADMAP_INDEX.md`

`DESIGN_PRINCIPLES.md` and `ROADMAP_FORMAT.md` can also be useful when the
session needs them. Do not keep ordinary session archives, handoffs,
temporary notes, or frequently changing progress records as persistent
reference sources.

## Source-of-Truth Order

Use this order when sources disagree:

```text
Committed repository state
↓
Relevant roadmap in its lifecycle directory
↓
Stable cached project references
↓
Current conversation clarification
```

A stale uploaded document must not override the current committed repository
or a roadmap in its authoritative lifecycle directory.

## Add Project Instructions

Copy and adapt the [Project Instructions Template](PROJECT_INSTRUCTIONS.md).
Update it for your repository, preferred conversational language,
environment, tools, learning goals, and safety boundaries. Do not inherit
another learner's private context or progress.

## Start the First Session

Example prompt:

```text
Read docs/labs/LABS_SOURCE_SYNC.md and docs/labs/ROADMAP_INDEX.md.
Then read <lifecycle>/<roadmap>/README.md from the committed repository.
Identify the next documented session without inventing missing progress.
Begin with a short concept and ask for my prediction before observation.
Do not generate a session archive unless I explicitly request one.
```

Replace the placeholders with a roadmap path that exists in your repository.

## Archive and Review Workflow

Learning happens interactively. Generate a session archive only on explicit
request, after the relevant observations and reasoning are available. Never
fabricate experiments, command output, dates, progress, or learner answers.
Review answers remain blank unless the learner explicitly asks to populate
them.

Review every repository change locally before committing it. The assistant's
draft is not evidence that a command ran or that a file matches the committed
repository.

## Maintenance Note

ChatGPT interfaces and available integrations can change. Rely on the
workflow principles in this guide and current official OpenAI documentation
rather than screenshots or fixed menu coordinates.

Official product references used for this guide:

- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt)
- [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903/)

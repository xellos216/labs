# Labs Archive Template

> This document defines the standard archive format used throughout the Labs project.
>
> Archive documents are intended for long-term storage and review.
> They are **not** the primary learning interface.

---

# Metadata

```yaml
Roadmap:
Phase:
Session:
Title:
Status:
Review:
ArchiveVersion:
Date:
```

`Status` records the archive document state.

Recommended values:

```text
Draft
In Progress
Completed
```

`Review` records whether the review answers have been completed.

Recommended values:

```text
Pending
Completed
```

`ArchiveVersion` records the archive template version used by the document.

Recommended current value:

```text
2
```

Archives without `ArchiveVersion` should be treated as legacy archives unless there is clear evidence that they already follow the current format.

---

# Roadmap-Specific Archive Formats

The full archive template is the default format for Labs session archives.

Some roadmaps may use a compact archive format when their learning mode requires it.

The `unix/` roadmap may use `notes.md` as its primary session archive when the session is conducted in task-solving mode.

In that case, the archive should still preserve:

* the core idea
* important commands
* corrected mistakes
* reusable command patterns
* observations from the task
* the final mental model

A compact `notes.md` archive does not need to include every section from this template.

When a roadmap uses a compact format, the output should match that roadmap's established archive style rather than forcing the full template.

---

# Objective

Briefly describe the purpose of this session.

Focus on:

* what was studied
* why it matters
* how it connects to the roadmap

---

# Learning Summary

Summarize the key ideas learned during the session.

The summary should emphasize:

* mental models
* relationships between concepts
* important observations

Avoid turning this section into a command reference.

---

# Key Concepts

List the most important concepts introduced.

Example:

* Concept A
* Concept B
* Concept C

Each concept should be short and easily scannable.

---

# Practical Observations

Record important observations made during experiments.

Suggested format:

```text
Prediction

↓

Observation

↓

Explanation
```

Focus on:

* observable behavior
* unexpected results
* corrected assumptions

For an experiment that requires detailed reproduction steps, environment
records, or preserved evidence, use `LAB_EXPERIMENT_TEMPLATE.md` as a
separate document and link it from this section.

---

# Commands / Code

Include only commands or code that are worth keeping as future references.

Each example should include a short explanation.

Example:

````markdown
```bash
ip addr
```

Shows the current network interfaces.
````

---

# Connections

Explain how this session connects to previous or future topics.

Examples:

```text
ARP
↓

Ethernet

↓

Packet Capture
```

or

```text
ELF

↓

Program Loader

↓

Process Memory
```

The purpose is to reinforce systems thinking.

---

# Common Misconceptions

Record mistakes that were corrected during the session.

Example:

* Incorrect assumption
* Why it was incorrect
* Correct understanding

---

# Key Takeaways

Summarize the session in a small number of concise points.

Prefer understanding over memorized facts.

Example:

* A parser interprets input according to grammar.
* Validation and parsing are separate stages.
* Observable behavior provides evidence.

---

# Review Questions

Create review questions according to `QA_TEMPLATE_SPECIFICATION.md`.

For normal session archives:

* questions remain visible
* answers remain blank unless explicitly requested
* question count and difficulty match the scope of the session

Final review documents may include answers when explicitly requested.
Existing archives do not need to be rewritten to follow this policy.

---

# Next Session

Record the intended continuation point.

Example:

```text
Next:
Phase 02
Session 05

Topic:
Normalization Before Validation
```

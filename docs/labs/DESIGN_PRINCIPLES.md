# Design Principles

> This document defines the guiding principles of the Labs project.
>
> These principles are intended to remain stable over time and apply across every roadmap, experiment, and archive.
>
> Operational procedures for individual learning sessions are defined in
> `LABS_SESSION_RULES.md`.

---

# Purpose

Labs exists to build durable systems understanding through observation, reasoning, and practical investigation.

The project is not organized around:

* certifications
* interview preparation
* memorizing commands
* collecting tools

Instead, it develops the ability to understand unfamiliar systems by reasoning from observable evidence.

---

# Core Principles

## Understanding Before Memorization

Memorized facts are useful only when they support understanding.

Prefer asking:

* Why does this exist?
* What problem does it solve?
* How does it work?

rather than:

* Which command should I remember?

---

## Observation Before Explanation

Whenever practical:

```text
Observe

↓

Explain
```

Real system behavior provides stronger understanding than abstract descriptions.

Preferred observations include:

* logs
* packet captures
* debugger output
* process state
* filesystem changes
* browser developer tools

---

## Prediction Before Verification

Encourage forming a hypothesis before running an experiment.

Typical workflow:

```text
Predict

↓

Observe

↓

Compare

↓

Revise Mental Model
```

Incorrect predictions are valuable because they expose incorrect assumptions.

---

## Evidence-Based Reasoning

Conclusions should be supported by observable evidence.

Distinguish clearly between:

* observations
* verified conclusions
* assumptions
* speculation

Avoid presenting assumptions as facts.

---

## Systems Thinking

Every concept should be understood as part of a larger system.

Examples:

```text
HTTP

↓

TCP

↓

IP

↓

Ethernet
```

```text
Application

↓

Operating System

↓

Kernel

↓

Hardware
```

Understanding relationships is more valuable than remembering isolated components.

---

## Practical Investigation

Learning should include experiments whenever practical.

Experiments should be:

* local
* reproducible
* observable
* reversible
* ethically scoped

The objective is to understand system behavior, not simply complete tasks.

---

## Mental Models Over Procedures

Commands and APIs change.

Fundamental concepts usually do not.

The project prioritizes understanding:

* architectures
* execution flow
* data flow
* state transitions
* component interactions

over procedural knowledge.

---

## Simplicity

Prefer explanations that are:

* technically correct
* minimal
* structurally clear

Avoid unnecessary complexity when a simpler explanation accurately represents the system.

---

## Incremental Learning

Build understanding in layers.

Typical progression:

```text
Concept

↓

Observation

↓

Experiment

↓

Integration
```

Advanced topics should extend earlier mental models rather than replace them.

---

## Reproducibility

Experiments should be repeatable by another learner.

Good experiments include:

* environment information
* clear procedure
* observable results
* evidence-backed conclusions

---

## Failure as Evidence

Unexpected results are valuable observations.

Preferred workflow:

```text
Prediction

↓

Unexpected Result

↓

Investigation

↓

Explanation

↓

Improved Mental Model
```

Failures should refine understanding rather than discourage experimentation.

---

## Ethical Scope

All practical work should remain within explicitly authorized environments.

Preferred environments include:

* local systems
* virtual machines
* containers
* intentionally vulnerable applications
* authorized training platforms

The objective is understanding systems, not unauthorized access.

---

## Long-Term Perspective

Knowledge should remain useful beyond a specific technology version.

Prefer learning:

* principles
* architectures
* reasoning techniques

over:

* version-specific features
* temporary workflows
* tool-specific shortcuts

---

# Decision Framework

When choosing between two approaches, prefer the one that better satisfies the following priorities:

1. Technical correctness
2. Evidence-based reasoning
3. Transferable understanding
4. Reproducibility
5. Simplicity
6. Maintainability

---

# Project Vision

Labs aims to produce an engineer who can explain, investigate, and reason about complete computing systems.

Success is measured not by the number of commands remembered, but by the ability to answer questions such as:

* Why did this happen?
* Which component is responsible?
* What evidence supports this conclusion?
* How does this connect to the rest of the system?
* What would happen if this component changed?

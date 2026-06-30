# Roadmap Format Specification

> This document defines the standard structure for all roadmap documents used in the Labs project.
>
> Every roadmap should follow this specification unless there is a clear project-specific reason to deviate.

---

# Design Goals

A roadmap should:

* define a long-term learning path
* remain understandable months later
* allow learning to continue across chat sessions
* build transferable mental models
* emphasize systems understanding over memorization

A roadmap is a curriculum specification, not a collection of notes.

---

# Standard Structure

New roadmaps should use the following top-level sections.

```text
Title

Objective

Philosophy

Learning Method

Lab Environment

Typical Phase Structure

Phase 01
Phase 02
...

Final Outcome

Core Mental Model
```

---

# Required and Optional Sections

Required sections:

* Title
* Objective
* Learning Method
* Typical Phase Structure
* Phase definitions
* Final Outcome

Optional sections:

* Philosophy
* Lab Environment
* Core Mental Model

Optional sections should be included when they improve clarity. They should
not be added only to satisfy a template.

Existing roadmaps are historical learning records. Do not rewrite them solely
to match this specification. Apply the current format when creating a roadmap
or when making a substantive revision that already affects its structure.

---

# Title

The title should clearly identify the subject.

Examples:

```text
Networking Roadmap

Linux Server Administration

Embedded Linux & Firmware Analysis

Security Toolsmith
```

---

# Objective

Describe:

* the long-term purpose
* the expected capabilities
* the intended scope

Avoid describing individual sessions.

---

# Philosophy

Describe the learning philosophy.

Typical themes include:

* understanding before memorization
* observation before modification
* systems thinking
* evidence-based reasoning
* practical experimentation
* ethical learning

---

# Learning Method

Describe how learning progresses.

Typical workflow:

```text
Concept

↓

Observation

↓

Experiment

↓

Explanation
```

or

```text
Understand

↓

Predict

↓

Observe

↓

Explain
```

The workflow should remain consistent throughout the roadmap.

---

# Lab Environment

Specify the recommended environment.

Typical items include:

* operating system
* virtual machines
* containers
* development tools
* debugging tools
* packet analyzers
* browsers
* local services

Experiments should generally be:

* local
* reproducible
* observable
* reversible
* ethically scoped

---

# Typical Phase Structure

Describe the overall organization of a phase.

Example:

```text
Core Concepts

↓

Observation

↓

Hands-on

↓

Integrated Lab

↓

Review
```

The roadmap may define a fixed or variable number of sessions per phase.

---

# Phase Structure

Each phase should follow a consistent format.

```text
Phase Title

Goal

Outcomes

Typical Tools

Example Labs

Sessions
```

---

## Goal

Describe what the learner should understand after completing the phase.

Focus on concepts rather than commands.

---

## Outcomes

List measurable abilities.

Use statements beginning with:

* explain
* identify
* distinguish
* inspect
* observe
* analyze
* reason about
* troubleshoot
* compare

Avoid vague outcomes such as:

* "know"
* "learn"

---

## Typical Tools

List the primary tools introduced in the phase.

Examples:

* ip
* tcpdump
* GDB
* Wireshark
* curl
* systemctl

Do not include every command used during labs.

---

## Example Labs

Provide representative experiments.

Experiments should be:

* practical
* observable
* reproducible

Focus on investigation rather than completing tasks.

---

## Sessions

Each session should contain:

```text
Session Number

Title
```

Descriptions are optional unless needed for clarity.

Session names should remain stable over time.

---

# Final Outcome

Describe the capabilities expected after completing the entire roadmap.

Focus on:

* reasoning ability
* systems understanding
* practical competence

Avoid listing every individual topic again.

---

# Core Mental Model

End every roadmap with a concise systems diagram.

Example:

```text
Application

↓

Operating System

↓

Kernel

↓

Hardware
```

or

```text
Source Code

↓

Compiler

↓

Executable

↓

Operating System

↓

Hardware
```

The diagram should express the central mental model of the roadmap.

---

# Naming Conventions

Use:

* clear technical names
* consistent capitalization
* stable terminology

Prefer:

```text
Processes

Windows Services

Packet Capture

Authentication
```

Avoid ambiguous or informal titles.

---

# Exceptions

A roadmap may deviate from this specification when its subject requires a
different structure.

Any deviation should:

* have a clear learning or technical reason
* preserve stable phase and session identifiers
* remain understandable without hidden context
* avoid forcing unrelated material into the standard structure

Document significant exceptions in the roadmap itself.

---

# Roadmap Principles

Every roadmap should satisfy the following principles.

* Begin with concepts before implementation.
* Progress from observation to experimentation.
* Build durable mental models.
* Connect topics to the larger system.
* Favor reproducible local experiments.
* Separate roadmap structure from archive templates.
* Preserve phase and session numbering once published whenever practical.

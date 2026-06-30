# Lab Experiment Template

> This document defines the standard format for documenting practical experiments performed throughout the Labs project.
>
> The purpose is to capture reasoning, observations, and conclusions—not simply the commands that were executed.

---

# Relationship to Session Archives

`ARCHIVE_TEMPLATE.md` records what was learned across an entire session.
This template records how one specific experiment was predicted, performed,
observed, and explained.

Use a separate experiment document when the work requires one or more of:

* detailed reproduction steps
* environment-specific setup
* preserved evidence files
* investigation of unexpected or inconclusive results
* reuse outside the original session

Small experiments may remain in the archive's Practical Observations section.

---

# Experiment Metadata

```yaml
Roadmap:
Phase:
Session:
Experiment:
Environment:
Date:
Status:
```

Use one of the following status values:

```text
planned
completed
inconclusive
failed
```

`failed` means the procedure could not be completed. An unexpected result
from a completed procedure should be recorded under Unexpected Results rather
than marked as failed.

---

# Objective

Describe the purpose of the experiment.

Answer questions such as:

* What is being investigated?
* Why is this experiment being performed?
* Which concept does it support?

---

# Background

Provide only the minimum theory necessary to understand the experiment.

Avoid turning this section into a lecture.

---

# Prediction

Record the expected behavior before performing the experiment.

Questions that may help:

* What do I think will happen?
* Which component will be responsible?
* Why do I expect this behavior?

Predictions are valuable even when they are incorrect.

---

# Environment

Record only information relevant to reproducing the experiment.

Example:

```text
Host:
Arch Linux

Guest:
Ubuntu Server 24.04

Tools:
ss
tcpdump
curl
```

---

# Procedure

Describe the experiment as a sequence of reproducible steps.

Prefer explaining intent rather than only listing commands.

Example:

````markdown
1. Start the local web server.

```bash
python3 -m http.server
```

2. Send an HTTP request.

```bash
curl http://127.0.0.1:8000
```

3. Observe the server output.
````

---

# Observations

Record only facts that were actually observed.

Examples:

* terminal output
* packet captures
* process state
* logs
* browser behavior
* debugger output

Do not include explanations here.

---

# Explanation

Explain why the observed behavior occurred.

Connect the observation to the underlying mechanism.

Preferred flow:

```text
Observation

↓

Mechanism

↓

Mental Model
```

---

# Evidence

Include evidence that supports the explanation.

Possible evidence:

* command output
* screenshots
* packet captures
* log excerpts
* memory maps
* debugger state

Evidence should support conclusions rather than replace them.

When evidence is stored separately, record its repository-relative path and
briefly explain what it demonstrates.

---

# Unexpected Results

Document anything that differed from the original prediction.

Example:

```text
Prediction

↓

Observed Difference

↓

Reason

↓

Updated Mental Model
```

Unexpected behavior often produces the most valuable learning.

---

# Related Concepts

List concepts reinforced by this experiment.

Example:

* Virtual Memory
* ARP
* TCP Handshake
* Process Lifecycle
* Routing

---

# Key Takeaways

Summarize the experiment in a few concise points.

Focus on transferable understanding rather than procedural steps.

Example:

* The kernel resolved the routing decision before packet transmission.
* ARP resolved the destination MAC only when necessary.
* The observation matched the predicted packet flow.

---

# Reproduction Checklist

Verify that another learner could repeat the experiment.

Checklist:

* [ ] Environment recorded
* [ ] Procedure documented
* [ ] Observations recorded
* [ ] Explanation included
* [ ] Evidence preserved
* [ ] Conclusions supported by evidence

---

# Follow-up Questions

Record questions for future investigation.

Examples:

* Why did this behavior differ from the prediction?
* What would happen under different conditions?
* Which component should be investigated next?

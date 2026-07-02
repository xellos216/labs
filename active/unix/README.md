# Unix Daily Sessions

CLI-first Unix/Linux training roadmap focused on practical stream processing, observability, and composable system workflows.

Environment:
- Arch Linux
- zsh
- tmux
- neovim
- CLI-first workflow

Philosophy:
- understanding over memorization
- composability over monolithic tools
- stream-based thinking
- practical one-liners
- observability first

---

# Goal

Reach a level where Unix command-line tools become a natural problem-solving language.

Target outcome:

- read and transform structured text quickly
- compose pipelines naturally
- inspect systems from the shell
- analyze logs and services efficiently
- automate repetitive inspection workflows
- think in streams, filters, and transformations

---

# Phase 1 — Text Processing Fundamentals

Core focus:
- grep
- cut
- awk
- sed
- sort
- uniq
- tr
- pipes

Skills:
- filtering
- field extraction
- transformation
- counting
- deduplication
- one-liner composition

Typical patterns:

```bash
filter → extract → count
````

```bash
find → xargs → awk
```

```bash
sort → uniq -c
```

---

# Phase 2 — Filesystem & Multi-File Processing

Core focus:

* find
* xargs
* globbing
* recursive processing

Skills:

* directory-wide analysis
* safe filename handling
* recursive filtering
* batch processing

Topics:

* file discovery
* recursive log analysis
* file metadata extraction
* mass transformations

---

# Phase 3 — Log Analysis & Observability

Core focus:

* auth logs
* access logs
* service logs
* structured parsing

Skills:

* anomaly detection
* status filtering
* aggregation
* incident-oriented analysis

Topics:

* login failures
* HTTP status analysis
* metrics parsing
* timeline extraction

Typical workflows:

```bash
journalctl | grep | awk
```

```bash
tail -f | grep
```

---

# Phase 4 — Process & Service Inspection

Core focus:

* ps
* top/htop
* pgrep
* systemctl
* journalctl

Skills:

* process observation
* service debugging
* runtime inspection
* dependency awareness

Topics:

* service states
* failed services
* process trees
* resource usage
* boot logs

---

# Phase 5 — Permissions & Ownership

Core focus:

* chmod
* chown
* umask
* groups
* sudo

Skills:

* permission reasoning
* access control understanding
* ownership debugging

Topics:

* rwx model
* octal permissions
* sticky bit
* setuid/setgid
* privilege boundaries

---

# Phase 6 — Networking & Socket Observation

Core focus:

* ss
* ip
* ping
* traceroute
* dig
* curl

Skills:

* socket inspection
* service exposure analysis
* connection tracing
* protocol observation

Topics:

* listening ports
* TCP/UDP inspection
* routing
* DNS queries
* HTTP requests

Typical workflows:

```bash
ss -tulpn
```

```bash
curl | jq
```

---

# Phase 7 — Data Streams & Automation

Core focus:

* tee
* wc
* env
* loops
* shell composition

Skills:

* reusable pipelines
* lightweight automation
* report generation
* shell-driven workflows

Topics:

* stream duplication
* batch automation
* CLI reporting
* chained analysis

---

# Phase 8 — Real System Workflows

Core focus:

* practical troubleshooting
* system inspection
* combined workflows

Skills:

* diagnosing issues from CLI
* building reusable workflows
* integrating multiple Unix tools naturally

Example workflows:

* service debugging
* suspicious login analysis
* web log inspection
* resource bottleneck analysis
* automated reporting

---

# Long-Term Direction

This roadmap is intended to become the foundation for:

* Linux internals
* observability engineering
* embedded Linux
* infrastructure debugging
* networking
* practical security analysis
* CLI-first automation
* hacker-level system reasoning

---

# Core Principle

Unix tools are not isolated commands.

They are composable operators for transforming streams of information.

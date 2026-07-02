# Online Opinion Pattern Analyzer

A defensive, educational data-analysis project for detecting unusual coordination-like patterns in public online comment datasets.

This project does **not** identify real individuals, doxx users, harass accounts, or claim that specific users are bots.

The tool focuses only on observable dataset-level signals such as:

- Posting time patterns
- Repeated or near-duplicate comments
- Account activity patterns
- Synchronized engagement
- Burst activity after content publication
- Basic text similarity
- Simple network graph structure

---

## Core Principle

This project can detect patterns that may deserve further review.

It cannot prove intent, identity, automation, political manipulation, or whether a specific account is a bot.

Use careful language:

- suspicious pattern
- coordination-like behavior
- high similarity cluster
- unusual timing pattern
- requires further verification

Avoid final claims such as:

- this user is a bot
- this group is fake
- this is confirmed manipulation
- this person is responsible

---

## Project Goals

The goal is to build a reproducible, portfolio-quality Python project that analyzes neutral sample comment datasets.

The project starts with synthetic or manually prepared data before touching any real public dataset.

Primary goals:

1. Understand how online comment datasets can be structured.
2. Analyze time-based activity patterns.
3. Detect repeated and near-duplicate text.
4. Detect burst-like and synchronized behavior.
5. Model simple account-post relationships as graphs.
6. Generate a readable Markdown or HTML report.
7. Document ethical limitations clearly.

---

## Non-Goals

This project is not for:

- harassment
- doxxing
- political targeting
- deanonymizing users
- bypassing platform protections
- scraping private or restricted data
- violating website terms of service
- claiming that specific accounts are bots

---

## Project Structure

```text
online-opinion-pattern-analyzer/
├── README.md
├── data/
│   ├── sample_comments.csv
│   └── synthetic_comments.csv
├── src/
│   ├── load_data.py
│   ├── time_analysis.py
│   ├── text_similarity.py
│   ├── burst_detection.py
│   ├── network_analysis.py
│   └── report.py
├── outputs/
│   ├── charts/
│   └── report.md
├── notebooks/
│   └── exploration.ipynb
└── requirements.txt
````

---

# Roadmap

## Phase 01 — Dataset Design

### Objective

Define a simple, neutral dataset format for public comment analysis.

### Key Concepts

* Dataset schema
* CSV and JSON structure
* Anonymous account identifiers
* Synthetic data
* Reproducibility
* Ethical data handling

### Dataset Fields

```text
comment_id
author_id_hash
created_at
content
post_id
like_count
reply_count
```

### Implementation Goals

* Create `data/synthetic_comments.csv`
* Create `src/load_data.py`
* Load the dataset with pandas
* Validate required columns
* Print basic dataset information

### Expected Output

* Total number of comments
* Number of unique authors
* Number of unique posts
* Time range of comments
* Missing field warnings, if any

### Limitations

At this phase, the project does not detect suspicious behavior.
It only prepares a clean and analyzable dataset.

---

## Phase 02 — Time Pattern Analysis

### Objective

Analyze when comments are posted and detect basic timing patterns.

### Key Concepts

* Posting frequency
* Hourly activity
* Daily activity
* Repeated intervals
* 24-hour activity pattern
* Human-like vs unusual timing behavior

### Implementation Goals

* Create `src/time_analysis.py`
* Parse `created_at` timestamps
* Count comments by hour
* Count comments by author
* Calculate time gaps between comments
* Generate a basic activity chart

### Expected Output

* Hourly comment count chart
* Most active time windows
* Authors with unusually consistent intervals
* Basic time gap summary

### Limitations

Unusual timing does not prove automation.
Shift workers, global users, scheduled posts, or platform-specific behavior can create false positives.

---

## Phase 03 — Text Similarity Analysis

### Objective

Detect repeated and near-duplicate comments.

### Key Concepts

* Text normalization
* Exact duplicate detection
* Token overlap
* Cosine similarity
* TF-IDF
* High similarity clusters

### Implementation Goals

* Create `src/text_similarity.py`
* Normalize comment text
* Detect exact duplicate comments
* Detect near-duplicate comments using simple similarity metrics
* Group similar comments into clusters

### Expected Output

* Exact duplicate groups
* Near-duplicate comment pairs
* Similarity score table
* High similarity cluster summary

### Limitations

Similar text does not prove coordination.
Common slogans, templates, quotes, memes, or repeated public phrases can naturally create high similarity.

---

## Phase 04 — Burst and Synchronization Analysis

### Objective

Detect sudden spikes and short-window synchronized behavior.

### Key Concepts

* Burst activity
* Publication-relative timing
* Short time windows
* Coordinated-looking activity
* Threshold-based detection

### Implementation Goals

* Create `src/burst_detection.py`
* Count comments within fixed time windows
* Detect spikes after post publication
* Detect multiple accounts commenting in short intervals
* Label suspicious windows without making final claims

### Expected Output

* Burst windows
* Comment count per time bucket
* Groups of accounts active in the same short window
* Markdown-ready summary of suspicious timing patterns

### Limitations

Burst activity can happen naturally after viral posts, breaking news, livestreams, or platform recommendations.

---

## Phase 05 — Network Graph Analysis

### Objective

Model relationships between authors and posts using a simple graph.

### Key Concepts

* Nodes
* Edges
* Bipartite graph
* Account-post relationship
* Shared target posts
* Dense clusters
* Degree centrality

### Implementation Goals

* Create `src/network_analysis.py`
* Use `networkx`
* Create account nodes and post nodes
* Add edges when an account comments on a post
* Calculate simple graph metrics
* Identify dense account-post clusters

### Expected Output

* Number of nodes
* Number of edges
* Most connected posts
* Most active anonymous accounts
* Dense cluster candidates

### Limitations

Graph density does not prove manipulation.
Popular posts naturally attract many users, and active users may comment frequently without coordination.

---

## Phase 06 — Report Generator

### Objective

Generate a readable analysis report.

### Key Concepts

* Reproducible reporting
* Markdown report generation
* Chart embedding
* Summary tables
* Evidence vs interpretation
* Limitations-first reporting

### Implementation Goals

* Create `src/report.py`
* Generate `outputs/report.md`
* Include charts from `outputs/charts/`
* Summarize time, text, burst, and graph findings
* Add an explicit limitations section

### Report Sections

```text
1. Dataset Summary
2. Time Pattern Summary
3. Text Similarity Summary
4. Burst and Synchronization Summary
5. Network Graph Summary
6. Suspicious Pattern Candidates
7. Limitations
8. What This Tool Can and Cannot Prove
```

### Limitations

The report should never present suspicious patterns as confirmed manipulation.

---

## Phase 07 — Portfolio Polish

### Objective

Turn the project into a clean GitHub portfolio project.

### Key Concepts

* README quality
* Reproducible commands
* Sample dataset
* Screenshots
* Ethical documentation
* Clear project scope

### Implementation Goals

* Clean project structure
* Add installation instructions
* Add usage examples
* Add sample output screenshots
* Add ethical limitations section
* Add “What this tool can and cannot prove” section
* Add future improvement ideas

### Final Portfolio Features

* CLI-friendly Python scripts
* Synthetic dataset included
* Charts generated automatically
* Markdown report generated automatically
* Clear ethical boundaries
* No real-user targeting
* No bot-certainty claims

---

# Planned Session Flow

## Session 01 — Dataset Schema and Synthetic Data

Build the dataset foundation.

Output:

* `data/synthetic_comments.csv`
* `src/load_data.py`
* Basic dataset validation
* `QA.md`
* `notes.md`

---

## Session 02 — Basic Time Analysis

Analyze posting times.

Output:

* Hourly activity summary
* Basic time gap calculation
* First chart in `outputs/charts/`
* `QA.md`
* `notes.md`

---

## Session 03 — Text Normalization and Exact Duplicates

Start text similarity with simple methods.

Output:

* Normalized text column
* Exact duplicate detection
* Duplicate group summary
* `QA.md`
* `notes.md`

---

## Session 04 — Near-Duplicate Detection

Add simple similarity methods.

Output:

* Token overlap
* TF-IDF cosine similarity
* Near-duplicate pairs
* `QA.md`
* `notes.md`

---

## Session 05 — Burst Detection

Detect short-term activity spikes.

Output:

* Time bucket analysis
* Burst candidate windows
* Spike chart
* `QA.md`
* `notes.md`

---

## Session 06 — Synchronization Analysis

Detect accounts acting within short time windows.

Output:

* Short-window account grouping
* Coordination-like candidate table
* False positive discussion
* `QA.md`
* `notes.md`

---

## Session 07 — Network Graph Basics

Build account-post graph structure.

Output:

* Graph nodes
* Graph edges
* Basic graph metrics
* `QA.md`
* `notes.md`

---

## Session 08 — Cluster Interpretation

Interpret dense clusters carefully.

Output:

* Dense cluster candidates
* Graph summary
* Limitation notes
* `QA.md`
* `notes.md`

---

## Session 09 — Report Generator

Generate the first Markdown report.

Output:

* `outputs/report.md`
* Chart links
* Summary tables
* Limitations section
* `QA.md`
* `notes.md`

---

## Session 10 — README and Portfolio Polish

Prepare the final GitHub-ready project.

Output:

* Final `README.md`
* Usage instructions
* Example output
* Ethical limitations
* Future improvements
* `QA.md`
* `notes.md`

---

# What This Tool Can Detect

This tool can help identify:

* unusual posting frequency
* repeated time intervals
* high-volume activity windows
* exact duplicate comments
* near-duplicate comments
* accounts targeting the same posts
* dense account-post clusters
* coordination-like patterns that deserve further review

---

# What This Tool Cannot Prove

This tool cannot prove:

* that an account is a bot
* that a person is acting maliciously
* that a group is politically coordinated
* that comments were paid for
* that automation was used
* who controls an account
* intent behind the activity

The correct conclusion should be:

> This dataset contains patterns that may require further verification.

Not:

> These users are bots.

---

# Ethical Data Rules

Use only:

* synthetic datasets
* manually prepared datasets
* public data where collection is allowed
* small samples for educational analysis

Do not:

* scrape private data
* bypass login
* bypass rate limits
* bypass anti-bot systems
* collect personal information
* publish real usernames as accusations
* target individuals or groups

---

# Recommended Dependencies

```text
pandas
matplotlib
scikit-learn
networkx
```

Use only when needed.

Start simple first:

1. CSV loading
2. timestamp parsing
3. counting
4. grouping
5. simple charts
6. text normalization
7. similarity metrics
8. graph metrics

---

# Example CLI Workflow

```bash
python src/load_data.py data/synthetic_comments.csv

python src/time_analysis.py data/synthetic_comments.csv

python src/text_similarity.py data/synthetic_comments.csv

python src/burst_detection.py data/synthetic_comments.csv

python src/network_analysis.py data/synthetic_comments.csv

python src/report.py data/synthetic_comments.csv
```

---

# Final Learning Outcome

By the end of this project, I should understand:

* how comment datasets are structured
* how time-based analysis works
* how duplicate and near-duplicate text detection works
* how burst detection works
* how simple synchronization signals can be measured
* how account-post graphs can reveal structural patterns
* why suspicious patterns require careful interpretation
* why data analysis cannot automatically prove intent or identity

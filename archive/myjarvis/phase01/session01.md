# Phase01 - Session01 Notes

## Session Goal

Understand the minimum architecture required to communicate with a local LLM through a Linux environment.

The objective was not learning AI concepts themselves, but understanding how an LLM behaves as a network-accessible service inside a Linux system.

---

## Core Mental Model

An LLM should not be viewed as a chat application.

Instead, it should be viewed as:

```text
Client
↓
HTTP Request
↓
LLM Server
↓
Model
↓
Response Stream
````

For MyJarvis, the future architecture will be:

```text
User
↓
MyJarvis
↓
Ollama API
↓
Model
↓
Response Stream
↓
MyJarvis
↓
User
```

---

## Components Observed

### Client

Current client:

```bash
curl
```

Role:

* Creates HTTP requests
* Sends requests to the Ollama API
* Receives HTTP responses

Example:

```bash
curl http://127.0.0.1:11434/api/generate
```

---

### Server

Current server:

```text
Ollama
```

Observed process:

```bash
/usr/bin/ollama serve
```

Role:

* Listens on TCP port 11434
* Accepts HTTP requests
* Loads and executes models
* Returns generated output

---

### Model

Current model:

```text
qwen2.5:1.5b
```

Important distinction:

```text
Ollama ≠ Model

Ollama = Runtime / Server
qwen2.5:1.5b = LLM
```

---

## Local API Architecture

Observed endpoint:

```text
http://127.0.0.1:11434
```

Verified using:

```bash
ss -ltnp | grep 11434
```

API query:

```bash
curl http://127.0.0.1:11434/api/tags
```

Returned installed models.

---

## JSON Streaming

Observed output:

```json
{"response":"TCP"}
{"response":" stands"}
{"response":" for"}
...
```

Key observation:

LLM output is not transmitted as a completed paragraph.

It is transmitted as a stream of generated tokens.

Concept:

```text
LLM
↓
Token Stream
↓
JSON Stream
↓
Client
```

This enables real-time interfaces.

---

## UNIX Pipeline Analysis

Command:

```bash
curl -s ... | jq -r '.response' | tr -d '\n'
```

Pipeline:

```text
curl
↓
JSON Stream

jq
↓
Plain Text

tr
↓
Formatted Text
```

---

### curl

Role:

```text
HTTP Client
```

Responsibilities:

* Send HTTP requests
* Receive HTTP responses

---

### jq

Role:

```text
JSON Parser
```

Responsibilities:

* Parse JSON
* Extract selected fields

Example:

```bash
jq -r '.response'
```

---

### tr

Role:

```text
Character Transformer
```

Responsibilities:

* Replace characters
* Delete characters
* Reformat text streams

Example:

```bash
tr -d '\n'
```

Removes newline characters.

---

## Shell vs Python Mapping

Shell:

```text
curl
↓
jq
↓
tr
```

Python:

```text
requests
↓
json parsing
↓
string processing
```

Approximate mapping:

```python
requests.post(...)
response.json()
string.replace(...)
string.strip(...)
```

---

## Key Lessons

### Lesson 1

LLMs are network services.

```text
LLM != Magic

LLM = Process + API + Model
```

---

### Lesson 2

Models and runtimes are different things.

```text
Ollama = Runtime

qwen2.5:1.5b = Model
```

---

### Lesson 3

UNIX pipelines compose small tools together.

```text
Tool A Output
↓
Tool B Input

Tool B Output
↓
Tool C Input
```

This same concept will later be used in MyJarvis.

---

### Lesson 4

Future MyJarvis Architecture

Current:

```text
User
↓
curl
↓
Ollama
↓
qwen
```

Future:

```text
User
↓
MyJarvis
↓
Ollama
↓
qwen
```

MyJarvis will act as the client.

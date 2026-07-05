# Phase 01 — Session 02
## User Mode vs Kernel Mode

## Metadata

```yaml
Roadmap: Windows Fundamentals
Phase: 01
Session: 02
Title: User Mode vs Kernel Mode
Status:
Review:
ArchiveVersion: 2
Date:
```

### Notes

Modern operating systems do not allow ordinary applications to directly control hardware.

Instead, they separate execution into two protection levels:

- User Mode
- Kernel Mode

The purpose of this separation is to improve system stability, reliability, and security.

---

## Why Separation Exists

If every application could directly access hardware, any program could:

- overwrite another program's memory
- delete arbitrary files
- monopolize hardware resources
- crash the entire operating system
- damage overall system stability

Instead, applications must request services from the operating system.

---

## Windows Execution Model

```text
Application
↓
Windows API
↓
NT Kernel
↓
Hardware
```

Applications do not directly interact with:

- CPU
- Memory
- Disk
- Network devices

The NT Kernel decides whether and how those resources are used.

---

## Linux Comparison

Linux follows the same overall philosophy.

```text
Application
↓
System Call
↓
Linux Kernel
↓
Hardware
```

Windows:

```text
Application
↓
Windows API / System Call
↓
NT Kernel
↓
Hardware
```

Although the implementation differs, both operating systems isolate user applications from privileged system components.

---

## User Mode

Characteristics:

- Runs ordinary applications
- Limited privileges
- Cannot directly control hardware
- Requests operating system services through system calls
- Failure is generally isolated to the affected process

Examples:

- Chrome
- Notepad
- Explorer.exe
- PowerShell

---

## Kernel Mode

Characteristics:

- Runs the operating system kernel
- Runs hardware drivers
- Full access to system resources
- Manages processes, memory, filesystems, devices, and scheduling
- Errors can affect the entire operating system

Examples:

- NT Kernel
- Device Drivers

---

## Isolation

Example:

```text
Chrome crashes
        │
        ▼
Chrome terminates

NT Kernel
Windows Services
Other Processes

Continue running
```

This isolation prevents most application failures from bringing down the entire operating system.

---

## Security Perspective

Most software—including malware—starts in User Mode.

```text
User Mode
        │
        │ Exploit
        ▼
Kernel Mode
```

Direct execution in Kernel Mode is not normally allowed.

To gain kernel-level privileges, an attacker typically needs:

- a kernel vulnerability
- a vulnerable driver
- another privilege escalation path

---

## Linux Comparison

| Linux | Windows |
| --- | --- |
| User Space | User Mode |
| Kernel Space | Kernel Mode |
| System Call | Windows API / System Call |
| Linux Kernel | NT Kernel |

The terminology differs, but the security model is fundamentally similar.

---

## Key Mental Model

Operating systems separate trusted and untrusted execution.

```text
User Mode

↓

Requests

↓

Kernel Mode

↓

Hardware
```

Applications request.

The kernel decides.

---

# Review Questions

### Q1. Why do modern operating systems separate User Mode and Kernel Mode?

<details>
<summary>A</summary>

</details>

---

### Q2. Can an ordinary application directly control hardware?

Why or why not?

<details>
<summary>A</summary>

</details>

---

### Q3. Describe the simplified execution path of a Windows application.

<details>
<summary>A</summary>

</details>

---

### Q4. What responsibilities belong to the NT Kernel?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does an application crash usually not crash the entire operating system?

<details>
<summary>A</summary>

</details>

---

### Q6. Which components typically run in User Mode?

Give three examples.

<details>
<summary>A</summary>

</details>

---

### Q7. Which components typically run in Kernel Mode?

Give two examples.

<details>
<summary>A</summary>

</details>

---

### Q8. Where does malware usually begin executing?

Why?

<details>
<summary>A</summary>

</details>

---

### Q9. Compare the following concepts:

- User Space vs User Mode
- Kernel Space vs Kernel Mode

<details>
<summary>A</summary>

</details>

---

### Q10. Explain in your own words:

```text
Applications request.
The kernel decides.
```

<details>
<summary>A</summary>

</details>

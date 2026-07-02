# Phase 01 — Session 01
## What Is Windows?

## Metadata

```yaml
Roadmap: Windows Fundamentals
Phase: 01
Session: 01
Title: What Is Windows?
Status:
Review:
ArchiveVersion: 2
Date:
```

### Notes

Windows is not a graphical interface.

Windows is an operating system that manages:

- CPU
- Memory
- Storage
- Networking
- Processes
- Users

The graphical desktop is only one component running on top of the operating system.

---

A common misconception:

```text
Linux = Operating System
Windows = GUI
```

A more accurate model:

```text
Linux
├─ Kernel
├─ Services
├─ Users
├─ Filesystem
├─ Networking
└─ Optional GUI

Windows
├─ NT Kernel
├─ Services
├─ Users
├─ Filesystem
├─ Networking
└─ Explorer.exe (GUI)
```

---

Explorer.exe is not Windows itself.

Explorer.exe provides:

- Desktop
- Taskbar
- Start Menu
- File Explorer

If Explorer.exe stops:

```text
Desktop disappears
Taskbar disappears
File Explorer disappears
```

The operating system can still continue running.

---

The NT Kernel is closer to the operating system itself.

The kernel manages:

- Process creation
- Memory allocation
- File access
- Device access
- Scheduling
- Networking resources

Applications do not directly control hardware.

---

Example execution flow:

```text
notepad.exe
↓
Windows API
↓
NT Kernel
↓
CPU / RAM / Storage
```

Similar Linux model:

```text
Application
↓
System Call
↓
Linux Kernel
↓
Hardware
```

Windows model:

```text
Application
↓
Windows API
↓
NT Kernel
↓
Hardware
```

---

Many core operating system concepts exist in both Linux and Windows.

Examples:

| Linux | Windows |
|---------|---------|
| Process | Process |
| User | User |
| Group | Group |
| systemd Service | Windows Service |
| syslog / journalctl | Event Log |
| ext4 | NTFS |
| Shell | PowerShell |

The concepts are often similar.

The implementation and management methods differ.

---

### Key Mental Model

Windows and Linux solve many of the same problems:

- Running programs
- Managing memory
- Managing users
- Controlling permissions
- Managing files
- Managing networks

The major differences are:

- architecture
- implementation
- management interfaces

not the fundamental purpose of the operating system.

---

# Review Questions

### Q1. What is the primary role of an operating system?

<details>
<summary>A</summary>

</details>

---

### Q2. Why is Explorer.exe not considered the operating system itself?

<details>
<summary>A</summary>

</details>

---

### Q3. Which component is closer to the operating system core?

- Explorer.exe
- NT Kernel

Why?

<details>
<summary>A</summary>

</details>

---

### Q4. When an application wants to use CPU or memory, does it directly control the hardware?

<details>
<summary>A</summary>

</details>

---

### Q5. Describe the simplified execution path of a Windows application.

<details>
<summary>A</summary>

</details>

---

### Q6. What is the relationship between Windows API and the NT Kernel?

<details>
<summary>A</summary>

</details>

---

### Q7. Name three concepts that exist in both Linux and Windows.

<details>
<summary>A</summary>

</details>

---

### Q8. What is a more accurate statement?

- Windows is a GUI.
- Windows is an operating system that includes a GUI.

Why?

<details>
<summary>A</summary>

</details>

---

### Q9. What happens if Explorer.exe crashes?

<details>
<summary>A</summary>

</details>

---

### Q10. Explain in your own words:

```text
Windows and Linux differ more in implementation
than in fundamental purpose.
```

<details>
<summary>A</summary>

</details>

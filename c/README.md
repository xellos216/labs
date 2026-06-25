# Embedded Linux, Firmware Analysis & IoT Systems Roadmap

## Objective

Build a deep understanding of how embedded systems work from power-on to user-space operation.

This roadmap focuses on:

- C programming in real systems
- Linux internals
- Embedded Linux
- Firmware analysis
- ARM architecture
- Device boot processes
- Hardware interfaces
- Embedded security fundamentals

The goal is not certification preparation, interview preparation, or challenge-based hacking.

The goal is systems understanding.

---

# Philosophy

- understanding before memorization
- observation before modification
- build mental models first
- prefer practical experiments
- focus on transferable knowledge
- ethical and educational use only
- learn how systems work before learning how to break them

---

# Learning Method

This roadmap develops systems understanding through three complementary
session types.

## Concept Sessions

Build the mental models needed to explain why a component exists and how it
fits into the larger system.

## Observation Sessions

Inspect running programs, binaries, firmware images, boot logs and hardware
interfaces before changing them.

## Hands-on Sessions

Apply each concept through small, reproducible experiments and conclude each
phase with an investigation, review or case study.

Typical workflow:

```text
Understand

↓

Predict

↓

Observe

↓

Experiment

↓

Explain
```

---

# Lab Environment

Host system:

- Arch Linux

Primary workflow:

- zsh
- tmux
- neovim
- CLI-first tooling

Experiments should remain:

- local
- observable
- reproducible
- reversible
- ethically scoped

Use isolated targets, virtual machines or emulation when an experiment could
affect the host or external systems.

---

# Typical Phase Structure

Phases retain their original 12-session or 16-session scope.

```text
Foundational Concepts
        │
        ▼
Component Observation
        │
        ▼
Guided Experiments
        │
        ▼
Integrated Mini Lab, Case Study or Workflow
```

The exact distribution varies by subject. Session count is determined by the
existing curriculum rather than forced into a uniform phase length.

---

# Phase 01 — Memory & Debugging Fundamentals

## Goal

Understand how a C program exists in memory while running.

---

## Outcomes

After completing this phase, you should be able to:

- explain the major regions of a process address space
- distinguish the code, data, BSS, stack and heap regions
- trace function calls, arguments and pointers in memory
- observe stack growth and dynamic allocation
- inspect a running process with GDB

---

## Typical Tools

- C compiler
- GDB
- procfs

---

## Example Labs

- compare initialized and uninitialized global variables
- observe stack growth across nested function calls
- trace pointer values through a running program
- compare stack and heap allocation
- map the memory regions of an entire process

---

## Topics

- Process memory layout
- Stack
- Heap
- Data segment
- BSS
- Code segment
- Function call frames
- Stack frames
- Pointer tracing
- Introduction to GDB

---

### Session 01

Process Memory Layout Overview

---

### Session 02

Code Segment Observation

---

### Session 03

Data Segment Observation

---

### Session 04

BSS Segment Observation

---

### Session 05

Stack Fundamentals

---

### Session 06

Stack Growth Observation

---

### Session 07

Function Call Frames

---

### Session 08

Function Arguments In Memory

---

### Session 09

Pointer Tracing Fundamentals

---

### Session 10

Heap Fundamentals

---

### Session 11

malloc() Observation

---

### Session 12

Heap vs Stack Comparison

---

### Session 13

Introduction to GDB

---

### Session 14

Breakpoints & Stepping

---

### Session 15

Memory Inspection with GDB

---

### Session 16

Mini Lab — Mapping an Entire Process

---

# Phase 02 — Linux Executable Internals

## Goal

Understand how Linux binaries are structured and executed.

---

## Outcomes

After completing this phase, you should be able to:

- identify the major structures of an ELF binary
- distinguish sections from program headers
- explain how shared libraries and dynamic linking work
- describe the purpose of symbols, the GOT and the PLT
- follow a Linux program from its file representation to startup

---

## Typical Tools

- file
- readelf
- objdump
- strings
- nm
- ldd

---

## Example Labs

- inspect an ELF header and its sections
- compare section headers with program headers
- identify shared-library dependencies
- inspect symbols and disassembly
- trace the structures involved in program startup

---

## Topics

- ELF
- Sections
- Program headers
- Dynamic linking
- Shared libraries
- GOT
- PLT

---

### Session 01

What Is An Executable?

---

### Session 02

Introduction to ELF

---

### Session 03

ELF Header Exploration

---

### Session 04

Sections Overview

---

### Session 05

.text Section

---

### Session 06

.data Section

---

### Session 07

.bss Section

---

### Session 08

Program Headers

---

### Session 09

Dynamic Linking Concepts

---

### Session 10

Shared Libraries

---

### Session 11

ldd Analysis

---

### Session 12

Symbols & nm

---

### Session 13

objdump Fundamentals

---

### Session 14

GOT Introduction

---

### Session 15

PLT Introduction

---

### Session 16

Following Program Startup

---

# Phase 03 — Assembly Foundations

## Goal

Read simple x86-64 assembly generated from C.

---

## Outcomes

After completing this phase, you should be able to:

- explain the basic CPU execution model
- identify the roles of common x86-64 registers
- follow stack changes across function calls
- recognize common data movement, comparison and control-flow instructions
- map simple C functions to compiler-generated assembly

---

## Typical Tools

- C compiler
- objdump
- GDB

---

## Example Labs

- compare a C function with its generated assembly
- trace register changes instruction by instruction
- observe a function prologue and epilogue
- follow conditional control flow
- map a complete C call sequence to assembly

---

## Topics

- Registers
- Stack pointer
- Base pointer
- mov
- push
- pop
- call
- ret
- cmp
- jmp
- Function prologue
- Function epilogue

---

### Session 01

CPU Execution Model

---

### Session 02

Registers Overview

---

### Session 03

General Purpose Registers

---

### Session 04

Stack Pointer

---

### Session 05

Base Pointer

---

### Session 06

mov Instruction

---

### Session 07

push & pop

---

### Session 08

call Instruction

---

### Session 09

ret Instruction

---

### Session 10

Function Prologue

---

### Session 11

Function Epilogue

---

### Session 12

cmp Instruction

---

### Session 13

Conditional Jumps

---

### Session 14

Reading Compiler Output

---

### Session 15

Tracing C Functions In Assembly

---

### Session 16

Mini Lab — C ↔ Assembly Mapping

---

# Phase 04 — Memory Corruption Foundations

## Goal

Understand why memory vulnerabilities exist.

---

## Outcomes

After completing this phase, you should be able to:

- explain why fixed-size memory operations can become unsafe
- distinguish stack, heap and adjacent-memory corruption concepts
- identify off-by-one and unsafe-copy conditions
- observe controlled corruption in a local program
- explain the purpose of common defensive mechanisms

---

## Typical Tools

- C compiler
- GDB

---

## Example Labs

- observe writes beyond a fixed-size buffer
- compare expected and corrupted adjacent memory
- reproduce an off-by-one error
- inspect a controlled stack overflow
- document the effect of defensive mechanisms

---

## Topics

- Buffer overflows
- Stack overflows
- Off-by-one errors
- Unsafe functions
- Memory corruption concepts

---

### Session 01

Memory Safety Concepts

---

### Session 02

Fixed-Size Buffers

---

### Session 03

Unsafe Copy Operations

---

### Session 04

Stack Buffer Overflow

---

### Session 05

Off-by-One Errors

---

### Session 06

Adjacent Memory Corruption

---

### Session 07

Heap Corruption Concepts

---

### Session 08

Memory Corruption Observation

---

### Session 09

Function Return Corruption Concept

---

### Session 10

Defensive Mechanisms Overview

---

### Session 11

Why Embedded Devices Are Different

---

### Session 12

Mini Lab — Controlled Overflow Observation

---

# Phase 05 — Linux Internals Foundations

## Goal

Understand how Linux operates beneath user-space applications.

---

## Outcomes

After completing this phase, you should be able to:

- explain how Linux creates and manages processes and threads
- trace the relationship between `fork()`, `exec()` and `wait()`
- explain file descriptors, standard streams and signals
- inspect virtual memory, mappings and process state through procfs
- observe library calls, system calls and open files

---

## Typical Tools

- strace
- ltrace
- ps
- procfs
- lsof

---

## Example Labs

- trace process creation and replacement
- inspect a process through procfs
- observe file descriptors and standard streams
- compare library-call and system-call traces
- investigate the resources used by a running process

---

## Topics

- Processes
- Threads
- Virtual memory
- Syscalls
- fork
- exec
- wait
- mmap
- Signals
- procfs
- File descriptors

---

### Session 01

Process Fundamentals

---

### Session 02

Process Creation

---

### Session 03

fork()

---

### Session 04

exec()

---

### Session 05

wait()

---

### Session 06

File Descriptors

---

### Session 07

Standard Streams

---

### Session 08

Signals

---

### Session 09

Virtual Memory

---

### Session 10

mmap()

---

### Session 11

procfs Exploration

---

### Session 12

Threads Overview

---

### Session 13

strace Fundamentals

---

### Session 14

ltrace Fundamentals

---

### Session 15

lsof Exploration

---

### Session 16

Mini Lab — Observe A Running Process

---

# Phase 06 — Embedded Linux Foundations

## Goal

Understand how Linux is adapted for embedded devices.

---

## Outcomes

After completing this phase, you should be able to:

- explain the architecture of an embedded Linux system
- describe the role of a root filesystem, BusyBox and init
- explain cross compilation and toolchain selection
- identify the roles of Device Tree and kernel modules
- navigate a minimal root filesystem

---

## Typical Tools

- BusyBox
- cross-compilation toolchain
- Buildroot

---

## Example Labs

- inspect a minimal embedded root filesystem
- identify BusyBox-provided commands
- compare embedded and general-purpose Linux layouts
- inspect Device Tree and module artifacts
- review a Buildroot-generated system

---

## Topics

- Embedded Linux architecture
- Cross compilation
- Root filesystem
- BusyBox
- Init systems
- Device Tree
- Kernel modules
- Buildroot

---

### Session 01

What Makes Linux Embedded?

---

### Session 02

Embedded Linux Architecture

---

### Session 03

Root Filesystem

---

### Session 04

BusyBox Fundamentals

---

### Session 05

Embedded Init Systems

---

### Session 06

Cross Compilation Concepts

---

### Session 07

Toolchains Overview

---

### Session 08

Device Tree Fundamentals

---

### Session 09

Kernel Modules

---

### Session 10

Buildroot Overview

---

### Session 11

Embedded Storage Layout

---

### Session 12

Mini Lab — Explore A Minimal RootFS

---

# Phase 07 — Boot Process Foundations

## Goal

Understand how an embedded device starts from power-on to user-space.

---

## Outcomes

After completing this phase, you should be able to:

- describe the complete embedded boot sequence
- distinguish Boot ROM and bootloader stages
- explain how U-Boot loads the kernel and Device Tree
- explain kernel decompression, init and root filesystem mounting
- reconstruct a boot timeline from observable logs

---

## Typical Tools

- U-Boot console
- kernel boot logs
- dmesg

---

## Example Labs

- annotate an embedded boot log
- identify transitions between boot stages
- trace kernel and Device Tree loading
- observe root filesystem mounting
- reconstruct a complete power-on-to-user-space timeline

---

## Topics

- Power-on sequence
- Boot ROM
- Bootloader
- U-Boot
- Kernel loading
- Init process
- Root filesystem mounting

---

### Session 01

Power-On Overview

---

### Session 02

Boot ROM

---

### Session 03

First Stage Bootloader

---

### Session 04

Second Stage Bootloader

---

### Session 05

U-Boot Fundamentals

---

### Session 06

Kernel Loading

---

### Session 07

Kernel Decompression

---

### Session 08

Device Tree Loading

---

### Session 09

init Process

---

### Session 10

Root Filesystem Mounting

---

### Session 11

Complete Boot Timeline

---

### Session 12

Mini Lab — Trace Linux Boot Logs

---

# Phase 08 — Firmware Analysis Foundations

## Goal

Analyze and navigate firmware images.

---

## Outcomes

After completing this phase, you should be able to:

- identify common firmware containers and filesystems
- extract and navigate firmware contents
- distinguish SquashFS, CramFS, JFFS2 and UBI artifacts
- locate configuration, metadata and exposed services
- explain a cautious firmware-analysis and modification workflow

---

## Typical Tools

- binwalk
- strings
- hexdump
- xxd
- file
- dd

---

## Example Labs

- identify embedded filesystems in a firmware image
- extract and navigate a firmware root filesystem
- discover metadata and configuration files
- identify services from firmware contents
- document a complete firmware-analysis workflow

---

## Topics

- Firmware structure
- Firmware extraction
- Filesystem identification
- SquashFS
- CramFS
- JFFS2
- UBI
- Firmware modification concepts

---

### Session 01

What Is Firmware?

---

### Session 02

Firmware Containers

---

### Session 03

binwalk Introduction

---

### Session 04

Filesystem Identification

---

### Session 05

SquashFS

---

### Session 06

CramFS

---

### Session 07

JFFS2

---

### Session 08

UBI

---

### Session 09

Firmware Extraction Workflow

---

### Session 10

strings & Metadata Discovery

---

### Session 11

Hex Inspection Basics

---

### Session 12

Firmware Navigation Practice

---

### Session 13

Configuration Discovery

---

### Session 14

Service Discovery

---

### Session 15

Firmware Modification Concepts

---

### Session 16

Mini Lab — Analyze Real Firmware

---

# Phase 09 — ARM Foundations

## Goal

Understand the architecture used by most embedded and IoT devices.

---

## Outcomes

After completing this phase, you should be able to:

- compare ARM and x86 execution models
- identify common ARM registers and calling-convention roles
- explain ARM stack behavior and the load/store model
- follow basic branch and function-call instructions
- inspect simple ARM ELF binaries

---

## Typical Tools

- cross compiler
- objdump
- readelf
- GDB

---

## Example Labs

- compare equivalent ARM and x86 compiler output
- trace an ARM function call
- inspect ARM registers and stack behavior
- identify load, store and branch instructions
- read a simple ARM ELF binary

---

## Topics

- ARM architecture overview
- ARM registers
- ARM calling conventions
- ARM assembly basics
- ARM ELF binaries

---

### Session 01

ARM Ecosystem Overview

---

### Session 02

ARM vs x86

---

### Session 03

ARM Registers

---

### Session 04

ARM Memory Model

---

### Session 05

ARM Calling Convention

---

### Session 06

ARM Stack Behavior

---

### Session 07

ARM Assembly Basics

---

### Session 08

Load & Store Instructions

---

### Session 09

Branch Instructions

---

### Session 10

ARM Function Calls

---

### Session 11

ARM ELF Files

---

### Session 12

Mini Lab — Read ARM Binaries

---

# Phase 10 — Hardware Interface Foundations

## Goal

Understand how software interacts with hardware.

---

## Outcomes

After completing this phase, you should be able to:

- explain the roles of UART, GPIO, SPI and I2C
- distinguish NOR flash, NAND flash and eMMC
- describe how JTAG supports hardware debugging
- identify likely hardware interfaces on an embedded device
- reason about the path between software and physical hardware

---

## Typical Tools

- serial console
- logic analyzer
- multimeter
- interface documentation and pinouts

---

## Example Labs

- identify UART pins and observe serial output
- compare SPI and I2C communication roles
- inspect flash-storage characteristics
- identify possible JTAG signals
- document the interfaces visible on a device

---

## Topics

- UART
- SPI
- I2C
- GPIO
- JTAG
- eMMC
- Flash memory

---

### Session 01

Embedded Hardware Overview

---

### Session 02

UART Fundamentals

---

### Session 03

UART Observation Lab

---

### Session 04

GPIO Fundamentals

---

### Session 05

SPI Fundamentals

---

### Session 06

I2C Fundamentals

---

### Session 07

Flash Memory Overview

---

### Session 08

NOR vs NAND Flash

---

### Session 09

eMMC Fundamentals

---

### Session 10

JTAG Fundamentals

---

### Session 11

Hardware Debug Interfaces

---

### Session 12

Mini Lab — Interface Identification

---

# Phase 11 — Embedded Exploitation Foundations

## Goal

Understand common vulnerability classes in embedded systems.

---

## Outcomes

After completing this phase, you should be able to:

- identify common embedded-system attack surfaces
- explain memory corruption and command injection in embedded contexts
- assess credential storage, service configuration and privilege boundaries
- explain filesystem and firmware patching concepts
- reason about defensive architecture and persistence risks

---

## Typical Tools

- firmware-analysis tools
- C compiler
- GDB
- local or emulated lab targets

---

## Example Labs

- map the attack surface of an emulated device
- inspect stored credentials and service configuration
- observe a controlled command-injection condition
- review a root filesystem modification
- analyze a local embedded-security case study

---

## Topics

- Stack overflow review
- Command injection
- Firmware patching concepts
- Root filesystem modification
- Basic privilege escalation concepts

---

### Session 01

Embedded Attack Surface

---

### Session 02

Embedded Memory Corruption Review

---

### Session 03

Web Interfaces In Devices

---

### Session 04

Command Injection Concepts

---

### Session 05

Credential Storage Concepts

---

### Session 06

Service Misconfiguration

---

### Session 07

Privilege Boundaries

---

### Session 08

Filesystem Modification Concepts

---

### Session 09

Firmware Patching Concepts

---

### Session 10

Persistence Concepts

---

### Session 11

Embedded Security Architecture

---

### Session 12

Mini Case Study

---

# Phase 12 — Real Device Analysis

## Goal

Apply accumulated knowledge to real-world embedded systems.

---

## Outcomes

After completing this phase, you should be able to:

- compare the architectures of routers, NAS devices, cameras and smart TVs
- collect and analyze device firmware
- inspect boot behavior, filesystems, services and configuration
- evaluate update mechanisms and exposed hardware interfaces
- document a complete device-analysis workflow

---

## Target Devices

- Routers
- Smart TVs
- NAS Devices
- IP Cameras
- Consumer IoT Devices

---

## Typical Tools

- firmware-analysis tools
- serial console
- network observation tools
- device documentation
- isolated physical or emulated targets

---

## Example Labs

- compare representative device architectures
- collect and inspect a firmware image
- trace a device boot process
- enumerate local services and configuration
- complete a capstone analysis of one device

---

### Session 01

Router Architecture

---

### Session 02

Consumer NAS Architecture

---

### Session 03

IP Camera Architecture

---

### Session 04

Smart TV Architecture

---

### Session 05

Firmware Collection Workflow

---

### Session 06

Filesystem Analysis Workflow

---

### Session 07

Boot Process Observation

---

### Session 08

Service Enumeration

---

### Session 09

Configuration Analysis

---

### Session 10

Update Mechanism Analysis

---

### Session 11

Hardware Interface Discovery

---

### Session 12

Full Device Walkthrough

---

### Session 13

Router Case Study

---

### Session 14

Camera Case Study

---

### Session 15

Smart TV Case Study

---

### Session 16

Capstone Analysis Project

---

# Final Outcome

Upon completion, the learner should be able to:

- explain how Linux binaries execute
- reason about process memory
- read basic assembly
- understand Linux internals
- understand embedded Linux architecture
- follow the complete boot process
- analyze firmware images
- navigate ARM-based systems
- identify common hardware interfaces
- understand embedded security concepts
- analyze real-world embedded devices

---

# Core Mental Model

```text
Source Code
        │
        ▼
Compiler and ELF Binary
        │
        ▼
CPU, Memory and Linux Kernel
        │
        ▼
Bootloader and Embedded Linux
        │
        ▼
Firmware, Services and Configuration
        │
        ▼
Hardware Interfaces and Physical Device
```

From power-on to user-space.
From firmware image to running service.
From source code to hardware.

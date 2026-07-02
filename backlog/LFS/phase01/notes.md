# Session 01 Notes

## Linux Is Not the Entire Operating System

Linux technically refers to the kernel.

A usable system also requires:

- libraries
- shells
- userland utilities
- configuration files
- bootloader
- init system

---

## Kernel

Responsibilities:

- process management
- memory management
- device drivers
- filesystem interfaces
- networking stack

The kernel directly interacts with hardware.

---

## Userland

Userland contains programs running outside the kernel.

Examples:

- bash
- zsh
- ls
- cp
- grep
- python

Most commands users interact with are userland programs.

---

## Libraries

Programs often depend on shared libraries.

Common example:

- glibc

Libraries provide reusable functionality that many programs use.

---

## Shell

The shell is a command interpreter.

Examples:

- bash
- zsh

The shell reads user input and launches programs.

---

## High-Level Linux Structure

Hardware
→ Firmware
→ Bootloader
→ Kernel
→ Libraries
→ Userland Programs
→ Shell
→ User

---

## Key Observation

Most of what users call "Linux" is actually userland software running on top of the Linux kernel.

# Path Resolution

## PATH

`PATH` is an ordered list of directories used to locate commands without a
slash:

```sh
printf '%s\n' "$PATH"
```

When the shell sees:

```sh
ls
```

it searches PATH entries from left to right and uses the first suitable
executable.

## Explicit Paths

Commands containing `/` bypass PATH lookup:

```sh
/bin/ls
./tool
```

## Search Order Risk

```sh
PATH=/tmp/bin:/usr/bin:/bin
```

If `/tmp/bin/ls` exists, it may shadow `/usr/bin/ls`.

Never place attacker-writable directories before trusted system directories
in privileged execution contexts.

## Empty PATH Entries

Depending on the shell and context, an empty PATH entry can represent the
current directory:

```text
:/usr/bin
/usr/bin:
/usr/bin::/bin
```

This can create unexpected command resolution.

## Inspection Commands

```sh
type -a command
command -v command
which command
```

`type` and `command -v` understand shell builtins and functions better than
many external `which` implementations.

## Review

1. PATH lookup is ordered.
2. The first matching command wins.
3. A slash disables PATH search.
4. Writable PATH entries create command-hijacking risk.
5. Resolve commands explicitly in security-sensitive code.

# QA

**Q1.**
How does the shell resolve `ls` when no slash is present?

<details>
<summary><strong>A1.</strong></summary>

It searches the directories in `PATH` from left to right and uses the first
suitable executable it finds.

</details>

---

**Q2.**
Why does `/bin/ls` bypass PATH lookup?

<details>
<summary><strong>A2.</strong></summary>

A command name containing `/` is treated as a path. The shell executes that
path directly instead of searching `PATH`.

</details>

---

**Q3.**
Why is `PATH=/tmp/bin:/usr/bin:/bin` risky in privileged contexts?

<details>
<summary><strong>A3.</strong></summary>

If `/tmp/bin` is writable by an attacker, a malicious executable there can
shadow a trusted system command with the same name.

</details>

---

**Q4.**
Why can empty PATH entries be dangerous?

<details>
<summary><strong>A4.</strong></summary>

Depending on shell and context, an empty PATH entry can mean the current
directory. That can make local files unexpectedly participate in command
resolution.

</details>

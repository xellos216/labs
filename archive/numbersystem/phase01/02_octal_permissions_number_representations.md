---
Roadmap: Number Systems for Systems Programming
Phase: Phase 01 — Practical Number Representations
Session: Session 02
Title: Octal, Permissions, ASCII, and Text as Bytes
Status: Completed
Review: Pending
ArchiveVersion: 2
Date:
---

# Phase 01 — Session 02: Octal, Permissions, ASCII, and Text as Bytes

## Objective

Understand why Unix/Linux permissions are commonly represented with octal numbers and how permission bits map to observable filesystem behavior.

The goal of this session was not to memorize `chmod` values. The goal was to connect numeric permission notation to actual kernel-enforced access decisions.

This session focused on:

- octal digits as 3-bit permission groups
- symbolic permissions such as `rwx`, `rw-`, and `r--`
- file permissions versus directory permissions
- the difference between reading, writing, executing, entering, and traversing
- observable permission errors and exit statuses

---

## Learning Summary

Unix permissions are naturally represented with octal because each permission group contains three bits.

```text
r w x
````

Each permission bit has a numeric value.

```text
r = 4 = 100
w = 2 = 010
x = 1 = 001
```

One octal digit represents exactly three bits.

```text
1 octal digit = 3 bits
```

Therefore each permission group maps cleanly to one octal digit.

```text
7 = 111 = rwx
6 = 110 = rw-
5 = 101 = r-x
4 = 100 = r--
3 = 011 = -wx
0 = 000 = ---
```

A permission such as `0755` is read as:

```text
0  7   5   5
   │   │   │
   │   │   └─ other = r-x
   │   └───── group = r-x
   └───────── owner = rwx
```

The leading `0` traditionally indicates octal notation. In common `chmod` usage, `chmod 755 file` is also accepted.

The session also established a key distinction:

```text
file x
= file can be used as an execution target

directory x
= directory can be entered or traversed as part of a path
```

This distinction is critical for understanding filesystem access control.

---

## Key Concepts

* octal notation
* permission bits
* owner / group / other
* symbolic permissions
* numeric permissions
* `chmod`
* `ls -l`
* `stat`
* regular file permissions
* directory permissions
* execute bit
* read bit
* write bit
* search / traverse permission
* exit status
* permission denied
* shebang
* interpreter execution

---

## Practical Observations

### Observation 01 — Reading Common Permission Values

Predicted mappings:

```text
0755 = owner rwx, group r-x, other r-x
0644 = owner rw-, group r--, other r--
0600 = owner rw-, group ---, other ---
0700 = owner rwx, group ---, other ---
```

Explanation:

Each permission digit maps to one permission group.

```text
7 = rwx
6 = rw-
5 = r-x
4 = r--
0 = ---
```

So:

```text
755
↓
7   5   5
rwx r-x r-x
```

and:

```text
644
↓
6   4   4
rw- r-- r--
```

---

### Observation 02 — `chmod 755` on a File

Commands:

```bash
mkdir -p /tmp/numsys-perm-lab
cd /tmp/numsys-perm-lab

printf 'hello\n' > file.txt
chmod 755 file.txt
ls -l file.txt
stat -c '%a %A %n' file.txt
```

Expected permission:

```text
-rwxr-xr-x
```

Expected `stat` output:

```text
755 -rwxr-xr-x file.txt
```

Observed result matched the prediction.

Explanation:

`ls -l` shows a 10-character mode field.

```text
-rwxr-xr-x
```

The first character is the file type.

```text
- = regular file
d = directory
```

The remaining nine characters are permission bits.

```text
-   rwx   r-x   r-x
│   │     │     │
│   │     │     └─ other
│   │     └─────── group
│   └───────────── owner
└───────────────── file type
```

`stat -c '%a %A %n'` displays both the octal permission and symbolic permission.

```text
755 -rwxr-xr-x file.txt
```

---

### Observation 03 — `chmod 644` on a File

Command:

```bash
chmod 644 file.txt
ls -l file.txt
stat -c '%a %A %n' file.txt
```

Observed permission:

```text
-rw-r--r--
```

Observed `stat` result:

```text
644 -rw-r--r-- file.txt
```

Explanation:

```text
644
↓
6   4   4
rw- r-- r--
```

For a regular file:

```text
-   rw-   r--   r--
│   │     │     │
│   │     │     └─ other: read only
│   │     └─────── group: read only
│   └───────────── owner: read, write
└───────────────── regular file
```

The numeric value `644` does not appear in the `ls -l` permission field. It appears when requested through `stat`.

---

### Observation 04 — Execute Permission Missing

Current permission:

```text
-rw-r--r--
```

Command:

```bash
./file.txt
echo $?
```

Observed result:

```text
zsh: permission denied: ./file.txt
126
```

Explanation:

The file existed, but the owner permission was:

```text
rw-
```

There was no execute bit.

Execution flow:

```text
./file.txt
↓
kernel checks execute permission
↓
x bit missing
↓
execution attempt denied
↓
exit status 126
```

`126` commonly means that the command was found but could not be executed.

The file could still be read with `cat` because reading and executing are separate permissions.

Command:

```bash
cat file.txt
echo $?
```

Observed result:

```text
hello
0
```

Explanation:

```text
cat file.txt
↓
cat program executes
↓
cat opens file.txt for reading
↓
owner has r permission
↓
read succeeds
```

`cat file.txt` does not execute `file.txt`. It executes `cat` and reads `file.txt`.

---

### Observation 05 — Execute Bit Does Not Guarantee Successful Program Execution

Command:

```bash
chmod 755 file.txt
./file.txt
echo $?
```

Observed result:

```text
./file.txt: line 1: hello: command not found
127
```

Explanation:

After `chmod 755`, the permission became:

```text
-rwxr-xr-x
```

The execute bit was present, so execution was allowed.

However, the file content was only:

```text
hello
```

The file was not a valid binary and did not contain a shebang line.

The shell tried to interpret `hello` as a command, but no such command existed.

```text
x bit present
↓
execution attempt allowed
↓
file content interpreted
↓
hello command not found
↓
exit status 127
```

`127` commonly means command not found.

Important distinction:

```text
execute bit
= permission to attempt execution

valid executable content
= kernel or interpreter knows how to run the file
```

---

### Observation 06 — Shell Script with Shebang

Command:

```bash
printf '#!/bin/sh\necho hello\n' >! file.txt
chmod 755 file.txt
./file.txt
echo $?
```

Observed result:

```text
hello
0
```

Explanation:

The file now had both:

```text
execute permission
```

and:

```text
a valid interpreter line
```

The execution flow was:

```text
./file.txt
↓
execute permission checked
↓
x bit present
↓
kernel reads file header
↓
#!/bin/sh found
↓
/bin/sh interprets file.txt
↓
echo hello runs
↓
exit status 0
```

This showed that `chmod 755` does not turn arbitrary text into a program. It only changes permission bits. The file content must still be executable in a format the system understands.

---

### Observation 07 — zsh `noclobber` and `>!`

While rewriting `file.txt`, zsh produced:

```text
zsh: file exists: file.txt
```

Explanation:

This happened because zsh had `noclobber` enabled.

With `noclobber`, the shell prevents accidental overwriting of an existing file with `>`.

```text
file.txt already exists
↓
> attempts overwrite
↓
zsh noclobber blocks it
↓
file exists error
```

In zsh, forced overwrite can be written as:

```bash
printf '#!/bin/sh\necho hello\n' >! file.txt
```

Relevant redirection meanings:

```text
>   = redirect output, but may be blocked by noclobber
>!  = force overwrite in zsh
>>  = append to existing file
```

This was a shell behavior observation, not an Alacritty behavior.

---

### Observation 08 — Directory Permission `600`

Command:

```bash
cd /tmp/numsys-perm-lab
mkdir -p dir
chmod 600 dir
ls -ld dir
cd dir
echo $?
```

Predicted permission:

```text
drw-------
```

Observed result:

```text
drw-------
cd: permission denied: dir
1
```

Explanation:

For directories, `x` does not mean “execute this directory.” It means search or traverse permission.

```text
directory x
= ability to enter the directory or follow paths through it
```

`600` means:

```text
6   0   0
rw- --- ---
```

For a directory:

```text
d   rw-   ---   ---
│   │     │     │
│   │     │     └─ other
│   │     └─────── group
│   └───────────── owner
└───────────────── directory
```

Owner had `r` and `w`, but not `x`.

Therefore:

```text
cd dir
↓
directory traverse permission required
↓
x bit missing
↓
permission denied
```

---

### Observation 09 — Directory Permission `700`

Command:

```bash
chmod 700 dir
ls -ld dir
cd dir
pwd
echo $?
```

Observed result:

```text
drwx------
/tmp/numsys-perm-lab/dir
0
```

Explanation:

```text
700
↓
7   0   0
rwx --- ---
```

For a directory:

```text
r = list entries
w = create/delete entries
x = enter/search/traverse
```

Since owner had `x`, `cd dir` succeeded.

```text
directory x present
↓
cd dir succeeds
↓
pwd shows /tmp/numsys-perm-lab/dir
↓
exit status 0
```

The correct reasoning order is:

```text
cd succeeds
↓
exit status 0
```

The exit status is an observation of the result, not the cause.

---

### Observation 10 — Directory `r` and `x` Are Separate

Commands:

```bash
cd /tmp/numsys-perm-lab
printf 'secret\n' >! dir/inside.txt
chmod 300 dir
ls -ld dir
ls dir
cat dir/inside.txt
```

Predicted permission:

```text
d-wx------
```

Observed result:

```text
d-wx------
Permission denied: dir - code: 13
secret
```

Explanation:

`300` means:

```text
3   0   0
-wx --- ---
```

For a directory:

```text
r = read/list directory entries
w = create/delete entries
x = search/traverse known paths
```

Because `r` was missing:

```text
ls dir
↓
directory listing required
↓
r missing
↓
permission denied
```

Because `x` was present:

```text
cat dir/inside.txt
↓
dir path traversal required
↓
x present
↓
inside.txt name already known
↓
inside.txt read permission checked
↓
file readable
↓
secret printed
```

This demonstrated the important rule:

```text
Without directory r:
you cannot list what is inside.

With directory x:
you can still access a known name inside,
if the target file permissions also allow it.
```

---

### Observation 11 — Directory `--x`

Given:

```text
d--x------
```

Assume the directory contains a known file:

```text
known.txt
```

and `known.txt` itself is readable.

Predicted behavior:

```text
ls dir
→ fails

cat dir/known.txt
→ succeeds

cd dir
→ succeeds
```

Explanation:

```text
directory r missing
↓
cannot list names
↓
ls fails
```

```text
directory x present
↓
can traverse known path
↓
cat dir/known.txt can reach the file
↓
file read permission decides final read
```

```text
directory x present
↓
cd dir succeeds
```

This established the distinction:

```text
directory r
= see names inside

directory x
= pass through or enter using a known name
```

---

## Commands / Code

```bash
stat -c '%a %A %n' file.txt
```

Shows octal permission, symbolic permission, and filename.

---

```bash
chmod 755 file.txt
```

Sets:

```text
owner = rwx
group = r-x
other = r-x
```

---

```bash
chmod 644 file.txt
```

Sets:

```text
owner = rw-
group = r--
other = r--
```

---

```bash
./file.txt
echo $?
```

Attempts to execute a file and then displays the exit status.

---

```bash
cat file.txt
echo $?
```

Reads a file using `cat` and then displays the exit status.

---

```bash
printf '#!/bin/sh\necho hello\n' >! file.txt
```

Writes a shell script to `file.txt`, forcing overwrite in zsh.

---

```bash
chmod 600 dir
ls -ld dir
cd dir
```

Shows that a directory without `x` cannot be entered.

---

```bash
chmod 700 dir
ls -ld dir
cd dir
pwd
```

Shows that a directory with `x` can be entered.

---

```bash
chmod 300 dir
ls dir
cat dir/inside.txt
```

Shows that directory listing requires `r`, while accessing a known path requires `x`.

---

## Connections

```text
octal digit
↓
3 permission bits
↓
owner / group / other
↓
kernel access checks
↓
observable command behavior
```

This session connects to Unix/Linux systems through filesystem access control.

It also connects to C and systems programming:

```text
raw bits
↓
numeric representation
↓
permission flags
↓
kernel decision
```

It connects to server administration:

```text
SSH keys
↓
home directory permissions
↓
authorized_keys readability
↓
login success or failure
```

It connects to web server behavior:

```text
web root directory
↓
directory x needed for traversal
↓
file r needed for reading
↓
HTTP 403 if access denied
```

It connects to payload and parser reasoning:

```text
same bytes or symbols
↓
different interpretation context
↓
different meaning
```

The same `x` symbol means different things depending on whether the target is a file or a directory.

---

## Common Misconceptions

### Misconception 01 — `chmod 755` Makes a File a Program

Incorrect:

```text
chmod 755 file.txt turns file.txt into a valid program.
```

Correct:

```text
chmod 755 gives execute permission.
The file content still needs to be executable by the kernel or an interpreter.
```

---

### Misconception 02 — `cat file.txt` Executes `file.txt`

Incorrect:

```text
cat file.txt runs file.txt.
```

Correct:

```text
cat executes the cat program.
file.txt is only opened as input for reading.
```

---

### Misconception 03 — File `x` and Directory `x` Mean the Same Thing

Incorrect:

```text
x always means execute.
```

Correct:

```text
file x      = file can be executed
directory x = directory can be entered or traversed
```

---

### Misconception 04 — Directory `r` Is Enough to Enter a Directory

Incorrect:

```text
If a directory has r, cd should work.
```

Correct:

```text
cd requires directory x.
Directory r allows listing names, not entering.
```

---

### Misconception 05 — Without Directory `r`, Files Inside Are Completely Inaccessible

Incorrect:

```text
If ls dir fails, nothing inside can be accessed.
```

Correct:

```text
Without directory r, names cannot be listed.
With directory x, a known path can still be accessed if the target file permission allows it.
```

---

### Misconception 06 — `ls -l` Shows the Numeric Permission

Incorrect:

```text
ls -l directly shows 644 or 755.
```

Correct:

```text
ls -l shows symbolic permissions such as -rw-r--r--.
stat can show numeric permissions with %a.
```

---

## Key Takeaways

* One octal digit maps to three permission bits.
* Unix permission groups are owner, group, and other.
* `7 = rwx`, `6 = rw-`, `5 = r-x`, `4 = r--`, `3 = -wx`, `0 = ---`.
* `ls -l` shows file type plus symbolic permissions.
* `stat -c '%a %A %n'` can show both numeric and symbolic permissions.
* File `x` means the file may be used as an execution target.
* Directory `x` means search, traverse, or enter.
* Directory `r` means list directory entries.
* Directory `r` and `x` are separate.
* A directory can block listing while still allowing access to known filenames.
* Exit status is an observation of the result, not the cause.
* `126` commonly means found but not executable.
* `127` commonly means command not found.

---

## Review Questions

### Q1. Why does Unix permission notation fit naturally with octal?

<details>
<summary>A</summary>

</details>

---

### Q2. What permissions do `755`, `644`, `600`, and `700` represent?

<details>
<summary>A</summary>

</details>

---

### Q3. In `ls -l`, what does the first character of `-rwxr-xr-x` represent?

<details>
<summary>A</summary>

</details>

---

### Q4. What is the difference between `file x` and `directory x`?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does `cat file.txt` work on a readable file even when `./file.txt` fails with permission denied?

<details>
<summary>A</summary>

</details>

---

### Q6. Why can `chmod 755 file.txt` remove a permission error but still fail to execute successfully?

<details>
<summary>A</summary>

</details>

---

### Q7. Why did `ls dir` fail when the directory permission was `d-wx------`?

<details>
<summary>A</summary>

</details>

---

### Q8. Why did `cat dir/inside.txt` succeed even though `ls dir` failed?

<details>
<summary>A</summary>

</details>

---

### Q9. Given a directory permission of `d--x------`, what operations are possible if the filename inside is already known?

<details>
<summary>A</summary>

</details>

---

### Q10. Why is exit status evidence of a result rather than the cause of that result?

<details>
<summary>A</summary>

</details>

---

## Next Session

Next:

```text
Phase 01
Session 03
```

Topic:

```text
Signed, Unsigned, Two's Complement, and Integer Limits
```

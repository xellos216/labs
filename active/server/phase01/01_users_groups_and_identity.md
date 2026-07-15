# Linux Server Administration
## Phase 01 — Session 01
# Users, Groups, and Identity

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 01
Session: 01
Title: Users, Groups, and Identity
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-14
```

---

# Objective

Understand how Linux represents users and groups as numeric identities, how account records differ from runtime process credentials, and how those credentials participate in access-control decisions.

The session established the foundation for later work with `/etc/passwd`, `/etc/shadow`, ownership, permissions, account lifecycle management, and privilege boundaries.

---

# Learning Summary

Linux exposes human-readable user and group names, but the kernel and filesystem primarily operate on numeric identifiers.

```text
user name
↕ identity lookup
UID
```

A user account is persistent identity data. It can include a user name, UID, primary GID, home directory, login shell, and supplementary group membership.

A process identity is runtime credential state attached to a running process. It includes UID and GID values together with supplementary groups.

```text
account records
↓ login and credential setup
process credentials
↓
kernel access checks
```

The current login user and the effective identity of a process are often the same, but they are not the same concept. `sudo` demonstrated this by starting a new process with root credentials while leaving the original user shell unchanged.

```text
login shell: UID 1000
└─ sudo
   └─ command: UID 0
```

Primary and supplementary groups also come from different identity relationships:

```text
primary group
→ stored as the account's primary GID

supplementary groups
→ additional group memberships
```

---

# Key Concepts

- user name
- UID
- group name
- GID
- primary group
- supplementary groups
- account identity
- process credentials
- real UID and GID
- effective UID and GID
- saved IDs
- filesystem IDs
- login identity
- effective identity
- NSS lookup
- numeric file ownership
- privilege-separated child processes

---

# Practical Observations

## Observation 1 — Inspecting the Current Identity

```text
Prediction
↓

The identity command should show the user name, primary group,
supplementary groups, home directory, and login shell.

↓

Observation
↓

uid=1000(labuser) gid=1000(labuser)
groups=1000(labuser),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),101(lxd)

↓

Explanation
↓

The command showed the current process credential and group membership state.
It did not show the home directory or login shell because those are account
record attributes rather than fields in this credential summary.
```

The observation also exposed the numeric UID and GID values that had not been included in the initial prediction.

---

## Observation 2 — Names Versus Numeric File Ownership

A temporary file was created and inspected twice.

```text
Prediction
↓

The filesystem should record numeric UID and GID values, while user-space
tools may translate those values into names.

↓

Observation
↓

ls -l  → owner and group displayed as labuser labuser
ls -ln → owner and group displayed as 1000 1000

↓

Explanation
↓

The file did not contain two separate ownership representations. Its metadata
contained numeric ownership values. Normal ls output resolved those values to
names, while -n suppressed name resolution.
```

This explains why a file may display a numeric owner after the corresponding account record has been removed.

---

## Observation 3 — Login Identity Versus Effective Identity

```text
Prediction
↓

whoami should report the current effective identity, while logname should
report the original login identity. A command run through sudo should report
root without changing the login session identity.

↓

Observation
↓

whoami       → labuser
logname      → labuser
sudo whoami  → root
logname      → labuser

↓

Explanation
↓

whoami resolved the effective UID of the running process. logname reported the
user associated with the login session. sudo started a new command with root
credentials but did not rewrite the original login session.
```

The equal results from `whoami` and `logname` before `sudo` did not mean that the commands measured the same property.

---

## Observation 4 — Reading Credential State from `/proc`

The current shell exposed four UID and GID fields plus a supplementary group list.

```text
Uid:    1000    1000    1000    1000
Gid:    1000    1000    1000    1000
Groups: 4 24 27 30 46 100 101 1000
```

The UID fields represent:

```text
real UID
effective UID
saved set-user-ID
filesystem UID
```

The GID fields follow the corresponding group-ID structure.

The same observation inside a process started through `sudo` produced:

```text
Uid:    0    0    0    0
Gid:    0    0    0    0
Groups: 0
```

This was direct evidence that `sudo` created a root-credential process rather than converting the existing shell into a root shell.

---

## Observation 5 — Querying Account Records with `getent`

```text
Prediction
↓

An account lookup should include the home directory and login shell that were
not present in id output.

↓

Observation
↓

labuser:x:1000:1000:labuser:/home/labuser:/bin/bash

↓

Explanation
↓

The passwd database record contained the user name, password placeholder, UID,
primary GID, comment field, home directory, and login shell. Supplementary
groups were not stored in this record.
```

`getent` performs the lookup through the system's configured name-service path rather than requiring the caller to read one particular file directly.

---

## Observation 6 — Primary and Supplementary Group Records

The `sudo` group record appeared as:

```text
sudo:x:27:labuser
```

The user's primary group record appeared as:

```text
labuser:x:1000:
```

The empty final field in the primary group record did not mean that the group had no effective members. The account's primary GID established that relationship.

```text
primary group membership
→ passwd-style account record primary GID

supplementary group membership
→ explicit group member list
```

---

## Observation 7 — Current Process Groups Versus Registered Account Groups

```text
groups
→ labuser adm cdrom sudo dip plugdev users lxd

groups labuser
→ labuser : labuser adm cdrom sudo dip plugdev users lxd
```

The contents matched because the current shell credentials reflected the account's registered group state at login time. The commands still used different reference points:

- `groups` inspected the current process context.
- `groups labuser` queried registered account membership.

An already-running shell may retain old group credentials after account group records are changed. A new login or another credential-establishing process is normally required to receive the new group set.

---

# Commands / Code

```bash
id
```

Shows the current process identity and group memberships.

---

```bash
id -u
id -g
id -G
id -Gn
```

Shows the current UID, primary GID, all numeric group IDs, and all group names.

---

```bash
id root
id 0
id 1000
```

Queries registered account identity by user name or numeric UID without changing the current process identity.

---

```bash
whoami
logname
sudo whoami
```

Contrasts effective process identity with the original login identity.

---

```bash
grep -E '^(Uid|Gid|Groups):' /proc/$$/status
```

Reads the current shell's credential fields from `/proc`.

---

```bash
sudo sh -c "grep -E '^(Uid|Gid|Groups):' /proc/\$\$/status"
```

Reads credential fields from a shell started with root privileges.

---

```bash
touch /tmp/identity-test
ls -l /tmp/identity-test
ls -ln /tmp/identity-test
```

Compares name-resolved ownership with numeric ownership output.

---

```bash
getent passwd labuser
getent group sudo
getent group labuser
```

Queries user and group records through the configured name-service mechanism.

---

```bash
groups
groups labuser
```

Compares the current process group context with the registered group memberships of an account.

---

# Connections

```text
account database
↓
login and authentication
↓
process credentials
↓
UID / GID / supplementary groups
↓
kernel access-control decision
↓
file and resource access
```

---

```text
filesystem ownership metadata
↓
numeric UID and GID
↓
name-service lookup
↓
human-readable user and group names
```

---

```text
primary GID
↓
default group identity for file creation
↓
ownership and permission checks
```

---

```text
sudo policy and authentication
↓
new privileged process
↓
effective UID 0
↓
privileged kernel access checks
```

This session prepares the identity model needed for later study of `/etc/passwd`, `/etc/shadow`, ownership, permissions, account lifecycle operations, and privilege delegation.

---

# Common Misconceptions

## Incorrect

```text
A file stores its owner's user name.
```

Correct:

```text
File ownership is represented by numeric UID and GID values. Tools may resolve
those values into names for display.
```

---

## Incorrect

```text
whoami reports the name typed at login.
```

Correct:

```text
whoami resolves the effective UID of the current process. logname refers to the
login-session identity.
```

---

## Incorrect

```text
An account identity exists only after that account logs in.
```

Correct:

```text
Account identity is persistent registered data. Login uses that data to create
runtime process credentials.
```

---

## Incorrect

```text
The final member field in a group record lists every user whose primary group
is that group.
```

Correct:

```text
Primary group membership is established through each account's primary GID.
The group member field primarily records explicit supplementary members.
```

---

## Incorrect

```text
sudo permanently changes the current shell into root.
```

Correct:

```text
sudo normally starts a new process with the target credentials. The original
shell retains its existing identity.
```

---

## Incorrect

```text
id root and sudo id perform the same operation because their output is equal.
```

Correct:

```text
id root queries root's registered account information. sudo id runs id with
root process credentials.
```

---

# Key Takeaways

- Linux access control is based primarily on numeric UID and GID values rather than display names.
- Account records and process credentials are related but distinct system states.
- A process carries UID, GID, and supplementary group credentials used by the kernel.
- The primary group is recorded through the account's primary GID; supplementary membership is represented separately.
- `whoami` reports effective process identity, while `logname` reports login-session identity.
- `sudo` creates a process with different credentials without modifying the parent shell's identity.
- File ownership survives loss of a user-name mapping because numeric ownership remains in metadata.
- `getent` provides identity lookups through the configured name-service mechanism.

---

# Review Questions

### Q1. Why does `ls -l` normally display a user name even though the filesystem records a numeric UID?

<details>
<summary>A</summary>

</details>

---

### Q2. Which account properties appeared in `getent passwd labuser` but not in the initial `id` output?

<details>
<summary>A</summary>

</details>

---

### Q3. How do primary group membership and supplementary group membership appear in the identity databases?

<details>
<summary>A</summary>

</details>

---

### Q4. Why did `whoami` and `logname` initially print the same name even though they refer to different identities?

<details>
<summary>A</summary>

</details>

---

### Q5. What `/proc` evidence showed that `sudo` created a root-credential process without changing the original shell?

<details>
<summary>A</summary>

</details>

---

### Q6. Why can `id root` and `sudo id` produce the same text while performing different operations?

<details>
<summary>A</summary>

</details>

---

### Q7. A file is owned by UID 1000, but no account currently maps to UID 1000. What should `ls -l` and `ls -ln` display, and why?

<details>
<summary>A</summary>

</details>

---

### Q8. An administrator adds a logged-in user to a new supplementary group. Why might the user's existing shell not immediately receive that group credential?

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 01
Session 02

Topic:
/etc/passwd Observation

Inspect the local passwd database structure and connect each field to the
account identity model established in this session.
```

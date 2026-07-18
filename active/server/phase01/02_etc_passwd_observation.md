# Linux Server Administration
## Phase 01 — Session 02
# /etc/passwd Observation

## Metadata

```yaml
Roadmap: Linux Server Administration
Phase: 01
Session: 02
Title: /etc/passwd Observation
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-19
```

---

# Objective

Inspect the local passwd database as structured identity data and connect each field to user lookup, login behavior, group resolution, and runtime credential setup.

The session also distinguished direct file inspection from NSS-based lookup and tested the internal consistency of the current account records without modifying the system.

---

# Learning Summary

`/etc/passwd` is a local account database whose records are readable by ordinary users because they contain generally non-secret identity attributes needed throughout the system.

Each record has seven colon-separated fields:

```text
username:x:UID:primary-GID:GECOS:home:login-program
```

The observed regular account record, redacted for public documentation, was:

```text
labuser:x:1000:1000:labuser:/home/labuser:/bin/bash
```

The second field did not contain a plaintext password. The `x` value acted as a placeholder indicating that authentication data is maintained separately, conventionally through the shadow-password database.

The file and the NSS interface served different roles:

```text
direct /etc/passwd read
→ one local file

getent passwd
→ configured NSS sources
→ files systemd
```

On this VM, both paths produced the same 34 complete records during enumeration. Equal results did not make the lookup mechanisms identical.

The session also showed that account fields describe configured attributes rather than guarantees about current filesystem state:

```text
home field
→ configured path string
≠
directory existence guarantee
```

The login-program field identified the program to start for a login session. `/usr/sbin/nologin` was not merely a marker: it was an executable ELF program that printed a refusal message and returned a failure status.

System accounts dominated the server's local account database. Most had non-interactive login programs, demonstrating that a Linux account often exists to separate service privileges rather than to represent a human login.

---

# Key Concepts

- passwd database
- colon-separated account record
- user name
- UID
- primary GID
- GECOS field
- home-directory field
- login-program field
- password placeholder
- shadow-password separation
- system account
- regular login account
- service privilege separation
- `/usr/sbin/nologin`
- NSS
- `nsswitch.conf`
- `files` source
- `systemd` source
- structural validation
- referential consistency
- duplicate identity detection
- locale-stable comparison

---

# Practical Observations

## Observation 1 — Direct File Lookup Versus NSS Lookup

```text
Prediction
↓

The direct /etc/passwd record and getent result might differ because they use
different lookup paths.

↓

Observation
↓

grep '^labuser:' /etc/passwd
→ labuser:x:1000:1000:labuser:/home/labuser:/bin/bash

getent passwd labuser
→ labuser:x:1000:1000:labuser:/home/labuser:/bin/bash

↓

Explanation
↓

The results were equal on this VM, but grep read one local file while getent
followed the configured NSS lookup policy.
```

Equal output did not prove equal mechanisms.

---

## Observation 2 — Public Read Access and Protected Writes

The local passwd file had the following ownership and mode:

```text
-rw-r--r-- root root /etc/passwd
```

This meant:

```text
root owner
→ read and write

root group
→ read

other users
→ read
```

The regular account could inspect identity records but could not modify the database directly.

The broad read permission supports system-wide name and identity lookup. Sensitive authentication material is separated into a more restricted database.

---

## Observation 3 — Human Accounts and System Accounts

The beginning of `/etc/passwd` contained `root` followed by multiple low-numbered service and system identities.

Representative observed records included:

```text
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
```

This demonstrated that the final field is the login program, not merely a preferred interactive shell.

```text
/bin/bash
→ interactive shell capability

/usr/sbin/nologin
→ explicit login refusal program

/bin/sync
→ restricted command instead of an interactive shell
```

A Linux account can exist to give a service or resource a distinct UID and GID without permitting normal user login.

---

## Observation 4 — Seven Account Fields

Splitting the regular account record by `:` produced:

```text
1 labuser
2 x
3 1000
4 1000
5 labuser
6 /home/labuser
7 /bin/bash
```

The fields represented:

```text
1 username
2 password placeholder
3 UID
4 primary GID
5 GECOS / comment
6 home-directory path
7 login program
```

The session corrected two initial uncertainties:

- fields 3 and 4 were the UID and primary GID
- the observed login program was `/bin/bash`, not `/usr/bin/bash`

---

## Observation 5 — `/etc/passwd` and `/etc/shadow` Permission Separation

The two files had different access modes:

```text
/etc/passwd
-rw-r--r-- root root

/etc/shadow
-rw-r----- root shadow
```

A normal read attempt against `/etc/shadow` failed:

```text
head: cannot open '/etc/shadow' for reading: Permission denied
```

The failure path was:

```text
path exists
↓
path resolution succeeds
↓
read open is requested
↓
current process credentials are checked
↓
permission denied
```

The regular user was neither the `root` owner nor a member of the `shadow` group, and the `other` permission bits granted no access.

---

## Observation 6 — Login-Program Distribution

Counting exact login-program values produced:

```text
nologin: 29
bash: 2
```

The server contained far more non-interactive accounts than Bash login accounts.

```text
many accounts
→ service or system identity
→ privilege separation
→ no interactive login
```

This corrected the assumption that every account primarily represents a person.

---

## Observation 7 — UID Range as a Hint, Not Proof

The local account records were grouped by UID range:

```text
uid 0: 1
uid 1-999: 31
uid >=1000: 2
```

The two UID values at or above 1000 were:

```text
nobody 65534 /nonexistent /usr/sbin/nologin
labuser 1000 /home/labuser /bin/bash
```

`nobody` was a direct counterexample to the rule that every UID at or above 1000 is a regular human account.

```text
UID range
→ useful classification hint

home + login program + account purpose
→ stronger evidence about account role
```

---

## Observation 8 — Home Paths Are Not Existence Guarantees

Several configured home paths did not exist as directories.

Observed examples included:

```text
lp -> /var/spool/lpd
news -> /var/spool/news
www-data -> /var/www
_apt -> /nonexistent
nobody -> /nonexistent
messagebus -> /nonexistent
syslog -> /nonexistent
tcpdump -> /nonexistent
```

The passwd record remained valid as account data even when the configured path was absent.

A service account may not need an interactive environment or per-user configuration directory. Some home fields instead represent historical defaults, package conventions, service data locations, or intentionally unusable paths.

---

## Observation 9 — `nologin` Is an Executable Program

The configured refusal program existed and was executable:

```text
-rwxr-xr-x root root /usr/sbin/nologin
```

File inspection identified it as an ELF executable.

Running it directly produced:

```text
This account is currently not available.
exit status: 1
```

The behavior served both human and programmatic consumers:

```text
message
→ explains the refusal to a person

nonzero exit status
→ signals failure to the caller
```

A scan of all configured login-program paths produced no missing or non-executable paths on the current VM.

---

## Observation 10 — NSS Lookup Policy

The passwd entry in `/etc/nsswitch.conf` was:

```text
passwd:         files systemd
```

The sources meant:

```text
files
→ local file-backed account data
→ primarily /etc/passwd

systemd
→ identities exposed through systemd's NSS integration
```

The complete enumeration counts were:

```text
/etc/passwd lines: 34
getent passwd lines: 34
```

A user-name set comparison produced no differences. A later full-record set comparison also produced no differences.

The verified conclusion was limited to the current enumeration:

```text
current /etc/passwd record set
=
current getent passwd enumeration
```

This did not prove that `systemd` was unused or that another system would produce the same result.

---

## Observation 11 — Locale-Stable Set Comparison

An initial `comm` comparison reported that both inputs were not in sorted order even though each stream had passed through `sort`.

The exact cause was not isolated during the session. The reliable correction was to pin the collation environment for both sorting and comparison:

```bash
LC_ALL=C comm -3 \
  <(LC_ALL=C sort /etc/passwd) \
  <(getent passwd | LC_ALL=C sort)
```

With `LC_ALL=C`, the comparison produced no output.

```text
no comm output
→ no records existed exclusively in either sorted input
```

The experiment reinforced that comparison tools may depend on locale-sensitive ordering and that reproducible text comparisons should use one explicit collation rule.

---

## Observation 12 — An `awk` Built-In Name Collision

The first UID-range counter used `system` as a variable name and failed:

```text
awk: cmd. line:5:     system++
awk: cmd. line:5:           ^ syntax error
```

`system()` is an `awk` built-in function. Renaming the counter to `system_count` removed the collision and allowed the intended logic to run.

```text
correct classification logic
+
invalid variable name
→ syntax failure
```

The failure was evidence about the command language rather than the account data.

---

## Observation 13 — Duplicate Identity Check

A scan for repeated user names and repeated UID values produced no output.

```text
duplicate username
→ none observed

duplicate UID
→ none observed
```

The absence of duplicates showed that the current local records were consistent. It did not mean duplicates are structurally impossible.

Two different names can technically map to the same UID. In that situation, the kernel's ownership and access checks treat them as the same numeric identity even though user-space names differ.

---

## Observation 14 — Primary GID Resolution

Every primary GID recorded in `/etc/passwd` resolved successfully through:

```bash
getent group "$gid"
```

No account reported a missing primary GID.

Using `getent` made the validation follow the configured NSS group lookup policy rather than restricting the check to `/etc/group`.

A missing group-name mapping would not erase the numeric GID. The kernel could still carry and compare the number, but user-space name resolution and administrative consistency would be degraded.

---

## Observation 15 — Seven-Field Structural Validation

The final structural check searched for records whose field count was not seven:

```bash
awk -F: 'NF != 7 {
  print "invalid field count:", NR, NF, $0
}' /etc/passwd
```

It produced no output.

```text
all records
→ seven colon-separated fields
```

This established format consistency only. Semantic validity still required separate checks for duplicates, group references, paths, login programs, and identity purpose.

---

# Commands / Code

```bash
grep '^labuser:' /etc/passwd
getent passwd labuser
```

Compares a direct local-file record with an NSS-based account lookup.

---

```bash
ls -l /etc/passwd
ls -l /etc/shadow
```

Compares public account-record permissions with protected authentication-record permissions.

---

```bash
head -n 10 /etc/passwd
```

Inspects representative root, system, service, and restricted-command accounts.

---

```bash
grep '^labuser:' /etc/passwd | \
awk -F: '{ for (i = 1; i <= NF; i++) print i, $i }'
```

Numbers and displays all seven fields in one passwd record.

---

```bash
awk -F: '$7 == "/usr/sbin/nologin" { nologin++ }
         $7 == "/bin/bash" { bash++ }
         END {
           print "nologin:", nologin
           print "bash:", bash
         }' /etc/passwd
```

Counts two observed login-program categories.

---

```bash
awk -F: '{
  if ($3 == 0)
    root_count++
  else if ($3 < 1000)
    system_count++
  else
    regular_count++
}
END {
  print "uid 0:", root_count
  print "uid 1-999:", system_count
  print "uid >=1000:", regular_count
}' /etc/passwd
```

Groups account records into broad UID ranges while avoiding the `awk` built-in name `system`.

---

```bash
awk -F: '$3 >= 1000 { print $1, $3, $6, $7 }' /etc/passwd
```

Shows why UID range alone cannot identify account purpose.

---

```bash
while IFS=: read -r account_name _ uid gid gecos home_path login_program; do
  if [ ! -d "$home_path" ]; then
    printf '%s -> %s\n' "$account_name" "$home_path"
  fi
done < /etc/passwd
```

Finds configured home paths that are not existing directories.

---

```bash
while IFS=: read -r account_name _ uid gid gecos home_path login_program; do
  if [ ! -x "$login_program" ]; then
    printf '%s -> %s\n' "$account_name" "$login_program"
  fi
done < /etc/passwd
```

Finds configured login programs that are absent or not executable.

---

```bash
/usr/sbin/nologin
printf 'exit status: %s\n' "$?"
```

Observes the refusal message and failure status of the non-login program.

---

```bash
grep '^passwd:' /etc/nsswitch.conf
```

Shows the configured NSS sources for passwd lookups.

---

```bash
printf '/etc/passwd lines: '
wc -l < /etc/passwd

printf 'getent passwd lines: '
getent passwd | wc -l
```

Compares enumeration counts without assuming that equal counts imply equal records.

---

```bash
LC_ALL=C comm -3 \
  <(cut -d: -f1 /etc/passwd | LC_ALL=C sort) \
  <(getent passwd | cut -d: -f1 | LC_ALL=C sort)
```

Compares the user-name sets with an explicit byte-order collation rule.

---

```bash
LC_ALL=C comm -3 \
  <(LC_ALL=C sort /etc/passwd) \
  <(getent passwd | LC_ALL=C sort)
```

Compares the complete enumerated record sets.

---

```bash
awk -F: '
{
  name_count[$1]++
  uid_count[$3]++
}
END {
  for (name in name_count)
    if (name_count[name] > 1)
      print "duplicate username:", name

  for (uid in uid_count)
    if (uid_count[uid] > 1)
      print "duplicate UID:", uid
}' /etc/passwd
```

Checks for duplicate account names and duplicate numeric identities.

---

```bash
while IFS=: read -r account_name _ uid gid gecos home_path login_program; do
  if ! getent group "$gid" >/dev/null; then
    printf '%s -> missing primary GID %s\n' "$account_name" "$gid"
  fi
done < /etc/passwd
```

Checks that each primary GID resolves through the configured group lookup policy.

---

```bash
awk -F: 'NF != 7 {
  print "invalid field count:", NR, NF, $0
}' /etc/passwd
```

Checks the seven-field structure of every local passwd record.

---

# Connections

```text
/etc/passwd account record
↓
username / UID / primary GID / home / login program
↓
login and session setup
↓
process credentials
↓
kernel access checks
```

---

```text
/etc/passwd
↓ public identity attributes

/etc/shadow
↓ protected authentication and aging attributes

authentication stack
↓
session creation
```

---

```text
passwd field 4
↓ primary GID
↓
NSS group lookup
↓
group name and policy context
```

---

```text
passwd login-program field
├─ /bin/bash
│  ↓
│  interactive session
│
└─ /usr/sbin/nologin
   ↓
   refusal message + failure status
```

---

```text
application identity lookup
↓
NSS policy in /etc/nsswitch.conf
├─ files
└─ systemd
↓
normalized passwd-style result
```

---

```text
service
↓
dedicated system account
↓
restricted login program
↓
separate UID / GID boundary
↓
reduced privilege sharing
```

This session prepared the local account-record model required for the next study of the protected shadow database.

---

# Common Misconceptions

## Incorrect

```text
The x field means that the account can execute programs.
```

Correct:

```text
The x field is a password placeholder indicating that authentication data is
stored separately from the public passwd record.
```

---

## Incorrect

```text
Every account in /etc/passwd represents a human who can log in.
```

Correct:

```text
Many accounts exist to isolate services, files, and processes under distinct
numeric identities without permitting interactive login.
```

---

## Incorrect

```text
The final passwd field is only the user's preferred shell name.
```

Correct:

```text
The field identifies the program to execute for the login session. It may be
an interactive shell, a restricted command, or a refusal program.
```

---

## Incorrect

```text
/usr/sbin/nologin is only a symbolic string checked elsewhere.
```

Correct:

```text
On the observed system it was an executable ELF program that printed a refusal
message and exited with status 1.
```

---

## Incorrect

```text
A configured home-directory path proves that the directory exists.
```

Correct:

```text
The field is account data. Directory existence is separate filesystem state.
```

---

## Incorrect

```text
UID values at or above 1000 always identify normal human users.
```

Correct:

```text
UID ranges are policy-based hints. The nobody account with UID 65534 was a
non-login counterexample.
```

---

## Incorrect

```text
Because getent passwd matched /etc/passwd, both commands use the same lookup
mechanism.
```

Correct:

```text
Direct file inspection reads one local file. getent follows NSS policy and may
consult multiple configured identity sources.
```

---

## Incorrect

```text
If a primary GID has no group-name record, the kernel cannot use the numeric
GID at all.
```

Correct:

```text
The numeric GID can still exist in credentials and ownership metadata, while
name resolution and administrative consistency fail.
```

---

## Incorrect

```text
Seven fields guarantee that a passwd record is fully valid.
```

Correct:

```text
Seven fields establish structural shape only. Semantic checks must validate
identifiers, references, paths, login programs, and policy intent separately.
```

---

# Key Takeaways

- `/etc/passwd` is a public local identity database, not a plaintext password file.
- Every passwd record contains seven colon-separated account fields.
- The `x` field is a placeholder for separately maintained authentication data.
- The home field records a configured path but does not guarantee directory existence.
- The final field identifies the login-session program, not necessarily an interactive shell.
- `/usr/sbin/nologin` is an executable refusal program that returns failure.
- Most observed accounts were system or service identities rather than human login accounts.
- UID ranges support classification but do not prove account purpose.
- `getent` follows NSS policy, while direct file tools inspect `/etc/passwd` alone.
- Equal lookup results do not imply identical lookup mechanisms.
- Locale-stable sorting matters when comparing identity datasets with `comm`.
- Structural validation and semantic validation are different operations.
- The current database had no duplicate names or UIDs, no unresolved primary GIDs, and no malformed field counts.

---

# Review Questions

### Q1. What are the seven fields in a passwd record, and which fields represent numeric identity?

<details>
<summary>A</summary>

</details>

---

### Q2. Why can ordinary users read `/etc/passwd` while `/etc/shadow` is more restricted?

<details>
<summary>A</summary>

</details>

---

### Q3. What does the `x` field mean, and why is interpreting it as a password or execution flag incorrect?

<details>
<summary>A</summary>

</details>

---

### Q4. What evidence showed that `/usr/sbin/nologin` is a real program rather than only a marker?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does a home-directory field not prove that the corresponding directory exists?

<details>
<summary>A</summary>

</details>

---

### Q6. How did the `nobody` account demonstrate that UID range alone cannot classify an account as a normal user?

<details>
<summary>A</summary>

</details>

---

### Q7. Why did equal results from `/etc/passwd` and `getent passwd` not prove that the lookup mechanisms were identical?

<details>
<summary>A</summary>

</details>

---

### Q8. What did pinning `LC_ALL=C` contribute to the `sort` and `comm` comparison?

<details>
<summary>A</summary>

</details>

---

### Q9. If two different user names map to the same UID, how will the kernel treat their file ownership and access checks?

<details>
<summary>A</summary>

</details>

---

### Q10. Why is a seven-field record structurally valid but not necessarily semantically valid?

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Phase 01
Session 03

Topic:
/etc/shadow Overview

Inspect the protected shadow database at a conceptual level and connect its
authentication and aging fields to the public identity records in /etc/passwd.
```

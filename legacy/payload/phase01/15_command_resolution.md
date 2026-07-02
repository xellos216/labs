# Command Resolution

## Resolution Sources

A command name may resolve to:

- alias
- reserved word
- shell function
- builtin
- hashed executable path
- executable found through PATH

Use:

```sh
type -a name
command -V name
```

to inspect resolution.

## Aliases

```sh
alias ls='ls --color=auto'
```

Alias expansion is shell parsing behavior and is commonly enabled in
interactive shells.

Bypass an alias with:

```sh
command ls
\ls
/bin/ls
```

## Functions

```sh
ls() {
    printf 'custom function\n'
}
```

A shell function can shadow a builtin or PATH executable.

```sh
command ls
```

skips functions and aliases, while an explicit path selects a specific file.

## Hashing

Shells may cache executable locations. After PATH changes, refresh the cache
when necessary:

```sh
hash -r
rehash
```

## Security Relevance

Scripts that assume a command name always means one executable may be wrong.
Control aliases, functions, PATH, and shell mode in sensitive automation.

## Review

1. Command text is resolved through several namespaces.
2. Aliases and functions are shell-internal objects.
3. An explicit path avoids alias, function, and PATH ambiguity.
4. Cached locations may outlive PATH changes.
5. Resolution context is part of program behavior.

# QA

**Q1.**
Why can the same command name resolve differently in different shells?

<details>
<summary><strong>A1.</strong></summary>

Aliases, reserved words, functions, builtins, hash tables, and PATH entries
can differ between shell sessions and modes.

</details>

---

**Q2.**
How can an alias be bypassed?

<details>
<summary><strong>A2.</strong></summary>

Use a form such as `command ls`, `\ls`, or an explicit path like `/bin/ls`,
depending on which resolution layers should be skipped.

</details>

---

**Q3.**
Why can a shell function shadow an executable?

<details>
<summary><strong>A3.</strong></summary>

The shell checks function definitions before PATH executables in normal
command resolution. A function with the same name can therefore run instead.

</details>

---

**Q4.**
Why might `hash -r` or `rehash` matter after PATH changes?

<details>
<summary><strong>A4.</strong></summary>

Some shells cache executable locations. Clearing or refreshing the cache
prevents an old resolved path from surviving after PATH has changed.

</details>

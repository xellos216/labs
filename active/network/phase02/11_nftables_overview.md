# Phase 02 - Session 11

## Metadata

```yaml
Roadmap: Networking
Phase: 02
Session: 11
Title: nftables Overview
Status: Completed
Review: Pending
ArchiveVersion: 3
Date: 2026-07-19
```

---

# Objective

Understand how nftables represents Linux packet-filtering rules, how it relates
to iptables and netfilter, and how to read an existing ruleset without changing
rules managed by higher-level tools.

---

# Learning Summary

nftables is the modern Linux framework for expressing packet-filtering, NAT,
and related netfilter rules. It organizes rules using a hierarchy:

```text
family
  ↓
table
  ↓
chain
  ↓
rule
  ↓
verdict
```

The observed host used the `iptables-nft` compatibility backend. This means
commands such as `iptables -L` and `nft list ruleset` exposed different views of
the same underlying nftables-backed kernel ruleset.

```text
UFW / Tailscale
        ↓
iptables-compatible management
        ↓
iptables-nft
        ↓
nftables ruleset
        ↓
netfilter
```

The ruleset contained a warning that `table ip filter` was managed by
`iptables-nft`. This established an important ownership rule: observe the table
with `nft`, but modify it through the tool that owns and regenerates it.

The session also distinguished base chains from regular chains. A base chain is
attached directly to a netfilter hook. A regular chain receives packets only
when another rule transfers control to it with `jump` or `goto`.

Finally, the observed rule handles demonstrated that a handle is an identifier,
not a priority value. Rules execute according to their position in the chain,
not according to numerical handle order.

---

# Key Concepts

- nftables
- netfilter
- iptables-nft
- compatibility layer
- ruleset
- family
- table
- base chain
- regular chain
- hook
- priority
- policy
- rule
- counter
- verdict
- jump
- goto
- handle
- rule ownership
- IPv4 and IPv6 families
- `inet` family
- sets and maps

---

# Practical Observations

## Observation 1 - iptables Uses the nftables Backend

Prediction:

```text
The iptables command will likely report the nf_tables backend.
```

Observation:

```text
iptables-nft / nf_tables backend
```

Explanation:

The iptables command-line interface was not managing an independent legacy
ruleset. It was operating through the nftables compatibility backend.

```text
iptables command
        ↓
iptables-nft compatibility layer
        ↓
nftables ruleset
```

This explains why UFW and Tailscale chains appeared in both the iptables and
nftables views.

---

## Observation 2 - Existing nftables Tables

Observation:

```text
table ip filter
table ip6 filter
table ip nat
table ip6 nat
table ip libvirt_network
table ip6 libvirt_network
table ip mangle
table ip6 mangle
```

Explanation:

The first word after `table` identifies the family.

```text
ip
= IPv4

ip6
= IPv6

inet
= IPv4 and IPv6 together
```

The family is not a packet direction. Direction is represented by hooks such as
`input`, `output`, or `forward` inside base chains.

The table name describes an administrative grouping. Names such as `filter`,
`nat`, and `mangle` reflect the compatibility layout created by iptables-nft and
its management tools.

---

## Observation 3 - Managed Table Warning

Observation:

```text
Warning: table ip filter is managed by iptables-nft, do not touch!
```

Explanation:

The warning identifies rule ownership. The table is generated and maintained
through iptables-compatible tooling.

Directly adding or deleting rules with `nft` could create several problems:

- the higher-level tool may not know about the manual rule
- a reload may overwrite the manual change
- rule order may diverge from the manager's expected state
- troubleshooting becomes harder because ownership is unclear

The correct operational model is:

```text
Observe with nft
        ↓
Identify the owning manager
        ↓
Modify through UFW, Tailscale, or the corresponding configuration
```

---

## Observation 4 - Base Chain Structure

Observation:

```nft
chain INPUT {
    type filter hook input priority filter; policy drop;
    ...
}
```

Explanation:

This is a base chain because it is attached directly to the `input` hook.

```text
type filter
= chain is used for packet filtering

hook input
= receives packets whose local destination is this host

priority filter
= ordering among base chains attached to the same hook

policy drop
= unmatched packets are dropped after rule evaluation completes
```

The chain name `INPUT` is conventional in this compatibility ruleset, but the
name itself does not create the behavior. The hook does.

A differently named chain could perform the same role:

```nft
chain inbound_packets {
    type filter hook input priority filter;
    policy drop;
}
```

---

## Observation 5 - Regular Chains Require Transfer

Observation:

```nft
chain ufw-before-input {
    ...
}
```

The chain had no hook declaration.

Explanation:

A regular chain does not receive packets directly from the network path. A rule
in another chain must transfer control to it.

```text
hook input
        ↓
base chain INPUT
        ↓
jump ufw-before-input
        ↓
regular chain ufw-before-input
```

If the regular chain finishes without a terminating verdict, execution returns
to the rule after the original `jump`.

---

## Observation 6 - Rule Counters and Verdicts

Observed rule form:

```nft
counter packets 100 bytes 5000 jump ufw-before-input
```

Explanation:

```text
counter packets 100 bytes 5000
= accumulated traffic statistics

jump ufw-before-input
= rule action
```

The packet and byte counts are not the verdict. They show how much traffic
matched and passed through the counter expression.

Possible terminating verdicts include:

```text
accept
drop
reject
```

Control-flow verdicts include:

```text
jump
goto
return
```

---

## Observation 7 - Rule Handles Do Not Define Priority

Observation:

```nft
jump ts-input                 # handle 162
jump ufw-before-logging-input # handle 20
jump ufw-before-input         # handle 21
```

Explanation:

The rule with handle `162` appeared before handles `20` and `21`, and therefore
executed first.

```text
handle
= stable identifier used to refer to a rule

rule position
= actual execution order inside a chain
```

Handles may appear out of numerical order when rules are created, deleted, and
inserted later.

```text
Creation history
        ≠
Execution priority
```

The chain is evaluated in displayed order from top to bottom.

---

## Observation 8 - Chain Priority and Rule Handle Are Different

Observed base-chain declaration:

```nft
type filter hook input priority filter; policy drop;
```

Explanation:

`priority filter` applies to the base chain relative to other base chains on the
same hook. It is not related to individual rule handles.

```text
base-chain priority
= ordering between chains attached to one hook

rule order
= top-to-bottom order inside one chain

handle
= identifier for one rule
```

---

## Observation 9 - jump and goto Behave Differently

`jump` behaves like a call:

```nft
chain input_chain {
    jump chain_A
    accept
}

chain chain_A {
    counter
}
```

Flow:

```text
input_chain
        ↓
jump chain_A
        ↓
chain_A ends without final verdict
        ↓
return to the next rule in input_chain
        ↓
accept
```

`goto` does not return to the next rule in the originating chain:

```nft
chain input_chain {
    goto chain_A
    accept
}
```

The `accept` after `goto` is not resumed when `chain_A` ends.

The essential distinction is:

```text
jump
= transfer control and return afterward

goto
= transfer control without returning to the next originating rule
```

---

## Observation 10 - Compatibility Expressions Remain Visible

Observation:

```text
xt match "conntrack" ... accept
```

Explanation:

The `xt` expression reflects compatibility with the older xtables and iptables
extension model. It is evidence that the ruleset was produced through an
iptables-compatible layer rather than written entirely in native nftables
syntax.

A comparable native nftables expression would often look like:

```nft
ct state established,related accept
```

This reinforced that nftables structure and iptables compatibility expressions
can coexist in the same visible ruleset.

---

# Commands / Code

```bash
iptables --version
```

Shows whether the iptables command uses the `nf_tables` or `legacy` backend.

---

```bash
sudo nft list ruleset
```

Displays the complete active nftables ruleset.

---

```bash
sudo nft list ruleset | sed -n '1,160p'
```

Displays only the beginning of a large ruleset for focused inspection.

---

```bash
sudo nft list tables
```

Lists all nftables tables and their families.

---

```bash
sudo nft -a list chain ip filter INPUT
```

Displays the selected chain and includes rule handles with `-a`.

---

# nftables Mental Model

```text
netfilter
        ↓
packet hooks
        ↓
nftables base chains
        ↓
ordered rules
        ↓
regular chains through jump or goto
        ↓
verdict
```

Ruleset hierarchy:

```text
family
  ↓
table
  ↓
chain
  ↓
rule
  ↓
match expressions + actions
  ↓
verdict
```

Management hierarchy on the observed host:

```text
UFW / Tailscale
        ↓
iptables-compatible commands or APIs
        ↓
iptables-nft
        ↓
nftables ruleset
        ↓
netfilter
```

---

# Connections

```text
Session 09 - Linux Packet Flow
        ↓
Packets pass kernel hooks along their path

Session 10 - iptables Fundamentals
        ↓
iptables presents tables, chains, rules, targets, and policies

Session 11 - nftables Overview
        ↓
The same filtering foundation is represented as families, tables, hooks,
chains, rules, and verdicts

Session 12 - Connection Tracking
        ↓
Rules can classify packets using tracked connection state
```

---

# Common Misconceptions

- Incorrect: `ip` family means INPUT traffic.
- Correct: `ip` means IPv4. Packet direction is determined by hooks.

---

- Incorrect: A chain named `ufw-before-input` automatically receives input
  packets.
- Correct: A chain without a hook is entered only through `jump`, `goto`, or
  another transfer.

---

- Incorrect: `policy drop` drops a packet as soon as it enters the chain.
- Correct: The policy applies only if rule evaluation produces no earlier final
  verdict.

---

- Incorrect: A larger handle means a higher-priority rule.
- Correct: Handles identify rules. Their displayed positions determine
  evaluation order.

---

- Incorrect: `counter packets ... bytes ...` is a verdict.
- Correct: It records matched traffic. The following expression supplies the
  action.

---

- Incorrect: `jump` and `goto` are interchangeable.
- Correct: `jump` returns to the next originating rule; `goto` does not.

---

- Incorrect: iptables and nftables were separate kernel firewalls on the
  observed host.
- Correct: iptables-nft provided an iptables-compatible view of the same
  nftables-backed netfilter ruleset.

---

- Incorrect: Direct nft modification is safe because the rules are visible in
  `nft list ruleset`.
- Correct: Visibility does not imply ownership. Managed tables should be
  changed through their owning tools.

---

# Key Takeaways

- nftables organizes rules as family, table, chain, rule, and verdict.
- Base chains attach directly to netfilter hooks; regular chains require a
  control transfer.
- The `ip` family handles IPv4, `ip6` handles IPv6, and `inet` can handle both.
- Chain names are labels; hook declarations determine packet-path roles.
- Rules execute in chain order, not numerical handle order.
- Handles identify rules for later reference or modification.
- `jump` returns to the calling chain; `goto` does not resume at the next rule.
- The observed iptables command used the nftables compatibility backend.
- UFW and Tailscale managed the active rules through iptables-nft.
- Managed rulesets should be modified through their owning tools.
- nftables provides unified syntax, flexible chains, sets, maps, and atomic
  ruleset updates.

---

# Review Questions

### Q1. What hierarchy does nftables use to organize packet-filtering rules?

<details>
<summary>A</summary>

</details>

---

### Q2. What is the difference between the `ip`, `ip6`, and `inet` families?

<details>
<summary>A</summary>

</details>

---

### Q3. What makes a chain a base chain?

<details>
<summary>A</summary>

</details>

---

### Q4. How does a regular chain receive packets if it has no hook?

<details>
<summary>A</summary>

</details>

---

### Q5. Why does `policy drop` not mean that every packet is immediately dropped
when it enters the chain?

<details>
<summary>A</summary>

</details>

---

### Q6. What is the difference between a rule handle and rule priority?

<details>
<summary>A</summary>

</details>

---

### Q7. What evidence showed that handles do not determine execution order?

<details>
<summary>A</summary>

</details>

---

### Q8. Compare `jump` and `goto` control flow.

<details>
<summary>A</summary>

</details>

---

### Q9. Why did UFW and Tailscale rules appear in both iptables and nftables
output?

<details>
<summary>A</summary>

</details>

---

### Q10. Why should a table marked as managed by iptables-nft not be modified
directly with native nft commands?

<details>
<summary>A</summary>

</details>

---

# Next Session

```text
Next:
Phase 02
Session 12

Topic:
Connection Tracking
```

# Third-Party Notices

## General Notice

Third-party project names, product names, service names, and trademarks
referenced by this repository belong to their respective owners. References
are made for identification and educational context and do not imply
affiliation, sponsorship, approval, or endorsement.

Third-party material remains subject to its original license, permission, or
other applicable rights. The repository-specific license grant does not
claim ownership of, or grant rights in, third-party material.

This notice is intentionally conservative and is not a representation that
every third-party reference or item has been fully inventoried.

## References and Dependency Invocation

A textual reference to a third-party project, or a workflow instruction that
invokes a dependency by identifier, is distinct from vendoring or
redistributing that dependency's source code. If third-party source or other
material is added to this repository in the future, its applicable notice
and terms should be recorded separately.

## Externally Invoked GitHub Actions

The repository workflow invokes the following external GitHub Actions by
reference:

- [`actions/checkout@v4`](https://github.com/actions/checkout)
- [`DavidAnson/markdownlint-cli2-action@v23`](https://github.com/DavidAnson/markdownlint-cli2-action)

These entries identify dependencies invoked by
`.github/workflows/markdown.yml`. Their source code is not distributed in
this repository merely because the workflow contains a `uses:` reference.
Their upstream licenses and other applicable terms continue to govern them;
their license texts are not copied into this repository by this notice.

## Future Notice Format

Use the following fields when a verified third-party notice is needed:

```text
Material or component:
Source:
Author or copyright holder:
Applicable license or permission:
Repository location:
Modification status:
```

Do not add an attribution entry until its authorship, source, applicable
terms, and repository location have been verified.

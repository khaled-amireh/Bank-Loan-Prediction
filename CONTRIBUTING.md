# Contributing

Thank you for helping make this study easier to understand and reproduce. Start with the [README](README.md), [implementation evidence](docs/implementation-evidence.md), and [reliability assessment](docs/reliability.md).

## Documentation changes

Keep technical claims tied to an original code location, saved notebook output, direct dataset count, or linked primary source. Describe default status consistently: class 0 is non-default; class 1 is default. Treat approval wording in the original plot as a preserved presentation label.

For documentation-only work, limit changes to `README.md`, `CONTRIBUTING.md`, Markdown references under `docs/`, and new documentation artwork. Preserve original Python, notebook JSON and outputs, CSV bytes, evaluation plots, and `LICENSE`. The [SHA-256 baseline](docs/protection-baseline.md) supplies the original reference values.

Use repository-relative links and the actual root-level file names. A new banner must be self-contained and committed along with its references. Static SVG artwork should use a `viewBox`, accessible text descriptions, supported fonts, and high-contrast colors, without scripts or external image/font dependencies.

## Proposing an experiment

Implementation improvements should be a separate, explicitly scoped contribution. Describe the known preprocessing leak and notebook/script discrepancy before claiming new performance. Record the environment, data snapshot, split/validation protocol, explicit estimator settings, and provenance of any new outputs.

Fit learned preprocessing inside training folds, choose settings using training/validation data, and keep a final test set separate. Label new results as a new experiment. Do not silently replace the historical notebook metrics, relabel the target, or claim that a proposed change has already improved the model.

## Review checklist

- [ ] Claims match source evidence, and saved results are distinguished from new measurements.
- [ ] Precision, recall, and error rates state their class and denominator.
- [ ] Internal links, image paths, heading anchors, Markdown tables, and Mermaid rendering work.
- [ ] The banner displays on light and dark backgrounds, and its asset is tracked.
- [ ] Setup instructions use existing files and disclose unpinned versions.
- [ ] The changed-file list fits the contribution's scope; original artifacts are preserved for documentation-only changes.
- [ ] No measured savings, deployment, fairness, or compliance claim is made without supporting evidence.

Before committing, inspect the actual diff and whitespace:

```bash
git status --short
git diff --stat
git diff --check
```

Stage specific paths and write a message describing the completed change. Publishing is a separate maintainer action; a local documentation contribution does not require rewriting history or pushing.

## Reporting reproducibility issues

Include the commit you inspected, operating system, Python and relevant package versions, working directory, selected notebook kernel, exact command or cell, and error text. State whether the result was already saved in the notebook or newly executed. A report can be useful without rerunning training or saving changes to the notebook.

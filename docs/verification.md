# Documentation sprint verification

[Project overview](../README.md) · [Implementation evidence](implementation-evidence.md) · [Original SHA-256 values](protection-baseline.md)

This record describes documentation work dated **2026-10-30**, based on original HEAD `ace83acdc7723ac183649eb3e087d500fc400c85` on `main`. The starting working tree was clean. The sprint adds 15 local commits without pushing, deploying, or rewriting existing history.

## Scope and file inventory

| File | Change / purpose |
|---|---|
| [README.md](../README.md) | Rebuilt case study, navigation, verified metrics, architecture, original plot interpretation, and setup |
| [Banner SVG](../images/credit-risk-intelligence-banner.svg) | New static, self-contained navy/cyan/gold visual identity |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Documentation review and separately scoped experiment guidance |
| [Implementation evidence](implementation-evidence.md) | Claim-to-source map, notebook/script discrepancy, and corrected claims |
| [Protection baseline](protection-baseline.md) | Original hashes and byte sizes of all five protected artifacts |
| [Dataset inspection](dataset.md) | Provenance, label counts, EDA scope, duplicates, and extreme values |
| [Feature glossary](feature-glossary.md) | All CSV fields, category coverage, and unit caveats |
| [Preprocessing](preprocessing.md) | Actual imputation, encoding, scaling, and fit boundaries |
| [Model reference](model.md) | Explicit SVM settings and absent comparisons |
| [Evaluation](evaluation.md) | Saved report, exact metric arithmetic, matrix, and error denominators |
| [Reproduction](reproduction.md) | Real paths, verified imports, cross-platform examples, and troubleshooting |
| [Reliability](reliability.md) | Confirmed safeguards, limitations, uncertainties, and future work |
| [This verification record](verification.md) | Scope and validation results |

Only the original README is modified. All other listed files are additions. No Python, notebook, data, original chart, license, Git configuration, dependency manifest, workflow, or executable file was changed or added.

## Validation performed

| Check | Result and scope |
|---|---|
| Protected bytes | All five original SHA-256 values and file sizes match the pre-edit baseline |
| Protected Git content | No diff from the initial commit for the script, notebook, CSV, original PNG, or license |
| Dataset facts | CSV row count, header, class counts, missing cells, categorical counts, duplicates, and selected ranges inspected without fitting models |
| Saved metrics | Notebook report checked; matrix visually read from both original images; class metrics and accuracy recomputed using scalar arithmetic |
| Markdown | All repository Markdown parsed; table widths, code fences, local targets, image references, and heading fragments checked |
| Mermaid | Actual diagram parsed and rendered using an already-installed Mermaid library in a temporary localhost preview |
| SVG | XML parsed; viewBox, accessible title/description, and absence of scripts, animation, external images/fonts, and linked dependencies checked |
| Visual review | Banner and full README locally rendered; light/dark desktop, 390-pixel viewport, and evaluation section inspected; images loaded and no page-level horizontal overflow detected in that preview |
| Setup | Root-relative CSV, notebook, and script paths checked against files; import-to-package list reviewed; correct clone URL used |
| Whitespace and scope | `git diff --check` against the initial HEAD and documentation-only changed-file review |
| Banner tracking | New SVG explicitly included in local Git history |

The preview used temporary HTML, browser state, and screenshots outside the repository. No rendering tools or executable validation scripts were committed. Local Markdown styling approximates GitHub; remote GitHub rendering was not checked because no publication was performed. Badges use Shields.io; the hero SVG has no external dependencies.

## Deliberate limits of verification

No training, notebook execution, model import, dependency installation, or fresh environment replay was performed. Setup commands are checked examples, not a claim of a certified environment. The scores remain the original saved results with the confirmed pre-split imputation leak. No replacement score, new comparison, corrected preprocessing, or financial-impact measurement was produced.

Original dependency versions, fresh-kernel behavior, prediction-time feature availability, duplicate overlap across the split, earlier manual test reuse, and population/subgroup reliability remain unresolved. An upstream byte match to a particular Kaggle release was not established.

## Read-only completion checks

The final delivery includes the exact commit list and post-commit clean-tree result. These commands reproduce the Git portion of the review:

```bash
git log --reverse --format="%H %s" ace83acdc7723ac183649eb3e087d500fc400c85..HEAD
git diff --name-status ace83acdc7723ac183649eb3e087d500fc400c85..HEAD
git diff --check ace83acdc7723ac183649eb3e087d500fc400c85..HEAD
git ls-files --error-unmatch images/credit-risk-intelligence-banner.svg
git status --short
```

The [baseline reference](protection-baseline.md) supplies the byte-level PowerShell comparison. Git's remote-tracking ref is also checked against the original HEAD; no push command is part of this workflow.

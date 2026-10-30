# Implementation evidence

[Project overview](../README.md) · [Protected-file baseline](protection-baseline.md)

This audit describes the checkout at `ace83acdc7723ac183649eb3e087d500fc400c85` on branch `main`, inspected on 2026-10-30. The working tree was clean before documentation work. Sources were read without executing the notebook, importing the model script, or training a model.

**Historical audit:** the findings and original file references below apply to that pre-fix checkout. A subsequent minimal correction moves the split ahead of training-only imputation in both implementations and removes the notebook assignment discrepancy. See [current preprocessing](preprocessing.md) and the [verified corrected evaluation](evaluation.md#corrected-workflow-verification); the historical evidence is retained here for traceability.

## Evidence map

Notebook cell numbers below are **zero-based JSON cell indices**, including Markdown cells. Script references use the original file's line numbers.

| Question | Verified evidence | Location |
|---|---|---|
| Prediction target | `y = df['loan_status']`; removed from `X` | Script lines 13–15; notebook cell 3 |
| Target meaning | Source data card defines 0 as non-default and 1 as default; local plot labels also identify class 1 as default | [Publisher's data card](https://www.kaggle.com/laotse/credit-risk-dataset/metadata); notebook cell 23 |
| Dataset shape | 32,581 data rows, 12 columns including the target; 11 predictors | Direct CSV scan; notebook cell 5 output |
| Class counts | 25,473 class-0 rows; 7,108 class-1 rows | Direct CSV scan |
| Missing values | 3,116 in `loan_int_rate`; 895 in `person_emp_length`; zero in other columns | Direct CSV scan; notebook cell 7 output |
| Imputation order | Full-dataset mean fitting occurs **before** the split | Script lines 28–40; notebook cells 10 and 13 |
| Script/notebook discrepancy | Script assigns `fit_transform(...)` to `df`; notebook assigns `fit(...)` to `df`; both separately transform `X` | Script lines 31–32; notebook cell 10 |
| Split | `test_size=0.2`, `random_state=42`; no `stratify` argument | Script lines 38–40; notebook cell 13 |
| Encoding | Four named categorical columns, `OneHotEncoder()`, remainder passed through; fit on training, transform test | Script lines 43–54; notebook cell 15 |
| Scaling | `StandardScaler()` on the entire encoded matrix, including indicator columns; fit on training, transform test | Script lines 57–59; notebook cell 17 |
| Classifier | `SVC(kernel='rbf', class_weight='balanced', random_state=42)` | Script line 62; notebook cell 19 |
| Model comparison | One RBF classifier is present; no saved linear/RBF experiment, tuning search, or cross-validation | Both source artifacts |
| Evaluation | Saved accuracy `0.8777044652447445`; classification report supports 5,072 / 1,445 | Notebook cell 23 output |
| Confusion matrix | Rows true, columns predicted, order `[0, 1]`: `[[4633, 439], [358, 1087]]` | Visually checked both cell 23 PNG and original repository PNG |
| Sample prediction | Reuses the first transformed test row; not a new applicant supplied independently | Script lines 91–96; notebook cell 25 |
| Environment evidence | Notebook metadata records Python 3.11.9; dependency versions are absent | Notebook metadata; repository file inventory |

## Consistency and interpretation

The two implementations share the split, feature encoding, scaling, classifier settings, evaluation functions, and sample selection. Their imputation assignment differs, and the script adds `plt.tight_layout()`. Saved metrics belong to the notebook; the script has no committed execution log proving identical results.

`SimpleImputer.fit()` returns the fitted estimator, not imputed numeric data ([API reference](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.fit)). The notebook's subsequent zero-missing-value display for `df` does not establish correct numeric replacement. `X` is separately transformed, so this discrepancy alone does not prove that the saved model used estimator objects as features. A fresh run was deliberately not attempted.

The full-data imputer is a **confirmed preprocessing leak**. Training-only encoder/scaler fitting is confirmed separately. No validation or model-selection loop appears in the committed artifacts; whether earlier manual choices reused these test results is unknown. No leakage-adjusted score is available.

## Arithmetic checks without model execution

- `4633 + 439 = 5072`; `358 + 1087 = 1445`; total test support is 6,517.
- `(4633 + 1087) / 6517 = 0.8777044652447445`.
- Default precision: `1087 / (1087 + 439) = 0.7123197903`.
- Default recall: `1087 / (1087 + 358) = 0.7522491349`.
- Default F1: `2 × 1087 / (2 × 1087 + 439 + 358) = 0.7317401548`.

## Corrections to the previous README

| Previous claim | Evidence-based correction |
|---|---|
| Approval prediction; class 0 means approved | Default-status classification; class 0 means non-default |
| 12 input features | 11 predictors plus one target column |
| Split before imputation; no preprocessing leakage | Imputer fitted on all rows before splitting |
| Implied linear-versus-RBF advantage or measured benefit of class balancing | No comparison or ablation is saved |
| Prevented losses / protected capital | Error counts only; no financial outcomes measured |
| New-applicant demonstration | First held-out row reused after preprocessing |
| `data/`, `notebooks/`, `requirements.txt`, different clone URL | Data, notebook, and script are at repository root; no dependency manifest exists |
| Verified Python 3.8+ compatibility | Python 3.11.9 recorded; supported-version range untested |

All original implementation, data, output, and license bytes remain protected. The exact starting hashes are recorded separately for independent comparison.

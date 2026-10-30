# Saved evaluation and metric definitions

[Project overview](../README.md) · [Evidence locations](implementation-evidence.md)

## Corrected workflow verification

On 2026-10-30, one fresh-kernel evaluation was completed after fitting mean imputation on training rows only. One pre-fix script replay in the same installed environment matched the historical notebook metrics and matrix. No tuning or repeated search was performed.

| Metric | Historical baseline / pre-fix replay | Corrected run | Absolute change |
|---|---:|---:|---:|
| Accuracy | 87.7704% | 87.7704% | 0.0000 percentage points |
| Default precision | 71.2320% | 71.2320% | 0.0000 percentage points |
| Default recall | 75.2249% | 75.2249% | 0.0000 percentage points |
| Default F1 | 73.1740% | 73.1740% | 0.0000 percentage points |

The corrected matrix is **`[[4633, 439], [358, 1087]]`**, identical to the historical matrix: the absolute change in every count is zero. **0 of 6,517 predictions changed** between the pre-fix replay and corrected run. Train/test row indices, labels, raw and encoded feature order, input shapes, and all resolved SVC parameters were checked for equality. The historical notebook did not save per-row predictions, so the paired prediction comparison is with the replay, not a recovered historical prediction file.

The split remains `test_size=0.2, random_state=42`, without stratification; the model remains `SVC(kernel='rbf', class_weight='balanced', random_state=42)`. Encoder and scaler code is unchanged. Training-only imputation changes its means to `[11.010116175535298, 4.787233203140411]` for `[loan_int_rate, person_emp_length]`; identical classification results do not imply identical preprocessing.

The installed run environment was **Python 3.11.9, NumPy 2.4.6, pandas 3.0.3, scikit-learn 1.9.0, Matplotlib 3.11.0, and Seaborn 0.13.2**. Notebook execution used nbclient 0.11.0, nbformat 5.10.4, and ipykernel 7.3.0. No packages were installed or upgraded. These versions record this run; the historical package versions are unknown, and no dependency lockfile has been introduced.

The notebook's affected missingness, evaluation, and sample outputs were regenerated; unrelated outputs and metadata were preserved. The original repository PNG stays unchanged as a historical asset, and its counts also match this corrected run. Scalar metric definitions and the count arithmetic below apply to both evaluations because their predictions and supports match in the paired replay.

## Source and scope

The sections below retain the **historical baseline** documented before the fix at `7f74cc9`. Its notebook cell 23 output was checked against both saved confusion-matrix images and recomputed with scalar arithmetic. No historical prediction file or fitted estimator was committed. Current corrected results are independently verified above and in the regenerated notebook output.

Both versions use `train_test_split(X, y, test_size=0.2, random_state=42)` with no explicit stratification. There are 26,064 training rows and 6,517 test rows. Test support is 5,072 non-default rows and 1,445 default rows. The historical implementation fitted imputation before splitting; the corrected version fits every learned transformation on training rows only.

## Original classification report

Values below preserve the notebook's two-decimal report rounding.

| Class / average | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Non-default (`0`) | 0.93 | 0.91 | 0.92 | 5,072 |
| Default (`1`) | 0.71 | 0.75 | 0.73 | 1,445 |
| Macro average | 0.82 | 0.83 | 0.83 | 6,517 |
| Weighted average | 0.88 | 0.88 | 0.88 | 6,517 |

The separately printed accuracy is `0.8777044652447445`, or **87.77%** rounded to two decimal places. The report itself rounds accuracy to `0.88`; these are the same saved result at different display precision.

## Arithmetic from saved counts

| Metric | Calculation | Value |
|---|---|---:|
| Accuracy | `(4633 + 1087) / 6517` | 87.7704% |
| Class-0 precision | `4633 / (4633 + 358)` | 92.8271% |
| Class-0 recall | `4633 / (4633 + 439)` | 91.3446% |
| Class-0 F1 | `9266 / (9266 + 358 + 439)` | 92.0799% |
| Class-1 precision | `1087 / (1087 + 439)` | 71.2320% |
| Class-1 recall | `1087 / (1087 + 358)` | 75.2249% |
| Class-1 F1 | `2174 / (2174 + 439 + 358)` | 73.1740% |

Precision asks what fraction of predictions of a class are correct. Recall asks what fraction of actual members of that class are recovered. F1 is their harmonic mean. Support is the number of true examples of each class, not the number predicted.

Macro averages weight the two classes equally. Weighted averages weight each class by its support; with 5,072 class-0 rows, those averages give more influence to non-default performance.

## Why accuracy is insufficient

Always predicting class 0 would achieve `5072 / 6517 = 77.83%` accuracy on these saved test labels and zero default recall. This is an arithmetic reference derived from support counts, not a newly trained or saved baseline experiment.

The historical and corrected results describe classification errors under one partition and one configuration. They do not establish a calibrated default probability, robustness under a different population, financial return, fairness, or operational reliability. The corrected evaluation removes the confirmed preprocessing leak; uncertainty intervals, cross-validation, ROC-AUC, and PR-AUC remain unavailable.

## Confusion matrix and error interpretation

The historical embedded PNG and the [original repository image](../images/confusion_matrix%28SVM%29.png) were visually inspected during the original audit. Their counts agree with the regenerated corrected-run plot. With class 1 as the positive class, the matrix for both evaluations is:

| True label / prediction | Non-default (`0`) | Default (`1`) | Total |
|---|---:|---:|---:|
| Non-default (`0`) | TN = 4,633 | FP = 439 | 5,072 |
| Default (`1`) | FN = 358 | TP = 1,087 | 1,445 |
| Total | 4,991 | 1,526 | 6,517 |

| Error view | Calculation | Interpretation |
|---|---|---|
| Missed-default rate | `358 / 1445 = 24.78%` | Share of actual defaults classified as non-default |
| False-positive rate | `439 / 5072 = 8.66%` | Share of actual non-defaults classified as default |
| False share among flags | `439 / 1526 = 28.77%` | Share of default predictions that are incorrect |
| Total errors | `358 + 439 = 797` | Incorrect class predictions in this saved test evaluation |

The false-positive rate and the false share among flags use different denominators; neither should be substituted for the other. The class-1 precision of 71.23% is the complement of the false share among flags, while recall of 75.22% is the complement of the missed-default rate.

The preserved plot labels class 0 “Approved.” The data dictionary defines that class as **non-default**. A false negative is therefore a predicted non-default on a default-labeled row, not evidence that a bank approved and lost an entire loan balance. Likewise, a false positive does not establish that an actual customer was rejected.

Converting these errors to money would require exposure, recoveries, decision timing, intervention effects, and an explicit policy. No such calculation is supported. The aggregate matrix also cannot explain individual errors, subgroup disparities, or causes of default. No measured error reduction relative to another configuration is available.

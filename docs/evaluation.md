# Saved evaluation and metric definitions

[Project overview](../README.md) · [Evidence locations](implementation-evidence.md)

## Source and scope

These results come from the **saved output of notebook cell 23**. They were checked against both saved confusion-matrix images and recomputed with scalar arithmetic, without model execution. No script run log, serialized predictions, or fitted estimator is committed.

The source uses `train_test_split(X, y, test_size=0.2, random_state=42)` with no explicit stratification. There are 26,064 training rows and 6,517 test rows. Test support is 5,072 non-default rows and 1,445 default rows. Because imputation occurs before the split, the test subset is excluded from classifier fitting but not from all preprocessing fitting.

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

The RBF model's saved results describe classification errors under one partition and one configuration. They do not establish a calibrated default probability, robustness under a different population, financial return, fairness, or operational reliability. There is no leakage-free replacement score, uncertainty interval, cross-validation estimate, ROC-AUC, or PR-AUC in the saved artifacts.

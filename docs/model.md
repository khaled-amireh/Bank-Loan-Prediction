# Support Vector Machine configuration

[Project overview](../README.md) · [Preprocessing](preprocessing.md) · [Implementation evidence](implementation-evidence.md)

## Exact explicit configuration

The script and notebook both construct:

```python
SVC(kernel='rbf', class_weight='balanced', random_state=42)
```

| Setting | What the source establishes |
|---|---|
| Estimator | scikit-learn `SVC` |
| Kernel | Explicitly `rbf` |
| Class weights | Explicitly `balanced` |
| Estimator seed | Explicitly `42` |
| `C`, `gamma`, tolerance, iteration limit | Not explicitly supplied; library defaults apply |
| Probability estimation | Not enabled in the source; predictions use `predict`, not `predict_proba` |
| Threshold selection | No explicit threshold search or override |
| Persistence | No saved classifier or preprocessing objects |

The original scikit-learn version is not recorded. Current API defaults should not be presented as a recovered historical environment. The saved estimator representation only shows `SVC(class_weight='balanced', random_state=42)` because the RBF kernel is a default in the documented API; its omission from that representation does not indicate a linear model.

## RBF kernel and class imbalance

The radial-basis-function kernel represents nonlinear separation through similarities between scaled feature vectors. That is a description of the model family, not evidence that this kernel outperformed a linear alternative on this dataset.

According to the [SVC API](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html), balanced class weights scale class penalties inversely to training-label frequency. They do not resample the rows and do not encode a financial loss function. The less frequent class receives greater weight, but an improvement in default recall caused by that setting has not been isolated experimentally.

The API documents the estimator's `random_state` in relation to probability-estimation shuffling. Setting it does not replace environment pinning or validation; the separate `train_test_split(random_state=42)` is the explicit seed for the partition used here.

## Comparisons that are absent

Only the RBF model and one saved evaluation are present in the committed notebook and script. There is no saved:

- Linear-SVM comparison or measured kernel-selection experiment.
- Unweighted-SVM ablation establishing a class-weighting benefit.
- Logistic-regression, tree-ensemble, or other trained baseline.
- Hyperparameter search, cross-validation, or validation-set selection procedure.
- Timing, resource-use, calibration, or probability-quality benchmark.

Kernel and class-weight choices should therefore be described as implementation choices. Future comparisons require a separate experiment, with preprocessing fitted inside training folds and a test set reserved for final evaluation.

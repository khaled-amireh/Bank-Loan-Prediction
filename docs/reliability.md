# Reliability, leakage, and future evaluation

[Project overview](../README.md) · [Implementation evidence](implementation-evidence.md) · [Saved evaluation](evaluation.md)

## Confirmed safeguards

| Safeguard present in the source | What it establishes |
|---|---|
| Target dropped from `X` | `loan_status` is not directly supplied as a predictor |
| Train/test partition before classifier fitting | The classifier is fitted on training rows and predicts test rows |
| Training-only encoder fit | Test rows use the fitted training vocabulary |
| Training-only scaler fit | Test rows use training feature means and scales |
| Fixed split seed | The source specifies `random_state=42` for the partition |

These facts are limited to the visible implementation. A fixed seed is not an estimate of statistical uncertainty, and training-only encoding/scaling does not isolate the earlier imputer fit.

## Confirmed limitations

| Finding | Consequence for interpretation |
|---|---|
| Imputer fitted before the split | Test feature values influence preprocessing; this evaluation is not fully isolated |
| Notebook assigns the result of `fit` to `df`, script uses `fit_transform` | The artifacts are not identical preprocessing implementations; saved missingness output does not validate numeric replacement |
| One non-stratified random split | No repeated-split, fold-level, temporal, or external validation estimate is provided |
| Unpinned environment | Exact replay of the saved numerical results is not established |
| Extreme age/employment values and 165 repeated full rows | Data-quality questions remain; the workflow retains them |
| One saved RBF configuration | No measured kernel superiority or benefit from class weighting is established |
| No calibrated probabilities or financial policy | Class labels do not quantify an individual's default probability or a monetary outcome |

The size or direction of the imputation leak's numerical effect has not been measured. A leakage-free score cannot be recovered merely by adjusting the published accuracy or recall.

## Unverified risks and missing evidence

- **Historical test reuse:** no model-selection loop is visible, but the artifacts do not reveal whether earlier manual experimentation used this same test result to choose settings. Neither “confirmed test-set tuning” nor “guaranteed untouched final test” is supported.
- **Prediction-time feature availability:** grade, rate, and historical-default fields have no documented observation timestamps. Their availability before a proposed decision requires verification. This is a timing question, not confirmed target leakage.
- **Repeated-row overlap:** exact duplicate rows exist; whether identical rows crossed this particular partition was not checked. Borrower-level leakage cannot be assessed without identifiers.
- **Population transfer:** provenance lacks collection dates, geography, institution, and sampling details. The publisher describes simulated bureau-style data; transfer to a lending population is untested.
- **Subgroup behavior:** no subgroup evaluation, protected-characteristic audit, fairness assessment, or regulatory review is recorded. Aggregate accuracy cannot establish any of them.
- **Output provenance:** the notebook contains saved outputs but no independent execution trace, environment lock, prediction file, or serialized model. Readability of those outputs is not a clean-kernel reproduction test.

## Business interpretation

The matrix quantifies false default flags and missed default labels. It does not measure decisions, customer outcomes, losses avoided, recoveries, or a review team's capacity. A model flag could be considered in a hypothetical investigation workflow, but that workflow has not been built or evaluated. Automatic approval/rejection claims and measured savings are outside the evidence.

## Prioritized roadmap for a separate implementation change

1. Correct the notebook's imputation assignment and fit all learned transformations within a training-fitted pipeline; verify numeric outputs and preserve the original study as an identifiable reference.
2. Capture an explicit environment and verify a fresh-kernel run with full input, parameter, prediction, and evaluation provenance.
3. Investigate duplicate rows and extreme values with documented domain criteria. Choose stratified, group-aware, or temporal validation only when the available metadata supports it.
4. Compare a simple baseline, linear SVM, RBF SVM, and selected alternatives using training-fold validation. Tune hyperparameters there, reserving a separate final test set for one final assessment.
5. Evaluate precision–recall behavior, uncertainty, calibration if probabilities are needed, and thresholds using separate validation data. Monetary objectives require actual costs and decision effects.
6. Establish feature timing and assess external and subgroup performance before considering any operational use.

These are proposals, not completed improvements or promised performance gains. None changes the preserved implementation in this documentation sprint.

# Reliability, leakage, and future evaluation

[Project overview](../README.md) · [Implementation evidence](implementation-evidence.md) · [Saved evaluation](evaluation.md)

## Confirmed safeguards

| Safeguard present in the source | What it establishes |
|---|---|
| Target dropped from `X` | `loan_status` is not directly supplied as a predictor |
| Train/test partition before classifier fitting | The classifier is fitted on training rows and predicts test rows |
| Training-only mean imputation | Means are learned from `X_train`; `X_test` only uses `transform` |
| Training-only encoder fit | Test rows use the fitted training vocabulary |
| Training-only scaler fit | Test rows use training feature means and scales |
| Fixed split seed | The source specifies `random_state=42` for the partition |

These facts are confirmed in the corrected implementation. The imputer now follows the same training-only fit boundary as the existing encoder and scaler. A fixed seed is not an estimate of statistical uncertainty.

## Confirmed limitations

| Finding | Consequence for interpretation |
|---|---|
| No persisted fitted preprocessing or model | The experiment does not provide a reusable inference artifact |
| One non-stratified random split | No repeated-split, fold-level, temporal, or external validation estimate is provided |
| Unpinned environment | Results are verified in one recorded environment; portability is not established |
| Extreme age/employment values and 165 repeated full rows | Data-quality questions remain; the workflow retains them |
| One saved RBF configuration | No measured kernel superiority or benefit from class weighting is established |
| No calibrated probabilities or financial policy | Class labels do not quantify an individual's default probability or a monetary outcome |

The confirmed imputation leak and notebook assignment discrepancy are fixed. A [fresh-kernel evaluation](evaluation.md#corrected-workflow-verification) produced the same metrics and all 6,517 predictions as a pre-fix replay in the recorded environment. A held-out-value perturbation check confirms that training preprocessing no longer depends on test numeric values. This isolates the confirmed preprocessing issue; it does not resolve the limitations above.

## Unverified risks and missing evidence

- **Historical test reuse:** no model-selection loop is visible, but the artifacts do not reveal whether earlier manual experimentation used this same test result to choose settings. Neither “confirmed test-set tuning” nor “guaranteed untouched final test” is supported.
- **Prediction-time feature availability:** grade, rate, and historical-default fields have no documented observation timestamps. Their availability before a proposed decision requires verification. This is a timing question, not confirmed target leakage.
- **Repeated-row overlap:** exact duplicate rows exist; whether identical rows crossed this particular partition was not checked. Borrower-level leakage cannot be assessed without identifiers.
- **Population transfer:** provenance lacks collection dates, geography, institution, and sampling details. The publisher describes simulated bureau-style data; transfer to a lending population is untested.
- **Subgroup behavior:** no subgroup evaluation, protected-characteristic audit, fairness assessment, or regulatory review is recorded. Aggregate accuracy cannot establish any of them.
- **Output provenance:** a fresh-kernel run and paired replay are now verified in the recorded environment, with affected outputs regenerated. Historical package versions remain unknown, and no environment lock, prediction file, or serialized model is committed. Unrelated saved EDA outputs retain their original provenance.

## Business interpretation

The matrix quantifies false default flags and missed default labels. It does not measure decisions, customer outcomes, losses avoided, recoveries, or a review team's capacity. A model flag could be considered in a hypothetical investigation workflow, but that workflow has not been built or evaluated. Automatic approval/rejection claims and measured savings are outside the evidence.

## Prioritized roadmap for a separate implementation change

1. Completed: split before mean imputation, align notebook/script preprocessing, and verify training-only fitting without a pipeline rewrite. The pre-fix study remains identifiable in Git at `7f74cc9`.
2. Pin a reproducible environment and capture reusable input, parameter, prediction, and evaluation artifacts; one fresh-kernel run is already verified.
3. Investigate duplicate rows and extreme values with documented domain criteria. Choose stratified, group-aware, or temporal validation only when the available metadata supports it.
4. Compare a simple baseline, linear SVM, RBF SVM, and selected alternatives using training-fold validation. Tune hyperparameters there, reserving a separate final test set for one final assessment.
5. Evaluate precision–recall behavior, uncertainty, calibration if probabilities are needed, and thresholds using separate validation data. Monetary objectives require actual costs and decision effects.
6. Establish feature timing and assess external and subgroup performance before considering any operational use.

The first item is complete; the remaining items are proposals, not promised performance gains. The minimal imputation correction leaves the model settings, features, split, dataset, license, and existing image assets unchanged.

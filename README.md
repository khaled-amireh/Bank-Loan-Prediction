<p align="center">
  <img src="images/credit-risk-intelligence-banner.svg" alt="Credit Risk Intelligence — Machine Learning for Loan Default Risk Assessment" width="100%">
</p>

# Credit Risk Intelligence

**Machine Learning for Loan Default Risk Assessment**

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](loan_prediction_model.py)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-RBF%20SVM-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)](loan_prediction_model.py)
[![Jupyter](https://img.shields.io/badge/Jupyter-saved%20analysis-F37626?style=flat-square&logo=jupyter&logoColor=white)](loan_prediction_model.ipynb)
[![MIT License](https://img.shields.io/badge/License-MIT-D4AF37?style=flat-square)](LICENSE)

[Overview](#executive-overview) · [Target](#business-problem-and-target) · [Dataset](#dataset-intelligence) · [Evidence audit](docs/implementation-evidence.md) · [Author](#author-and-license)

## Executive overview

A focused machine learning case study of **binary loan-default classification** using an RBF Support Vector Machine. The repository preserves the original notebook, Python script, dataset, and confusion matrix so readers can inspect the implementation alongside its saved evaluation.

| Study at a glance | Verified scope |
|---|---|
| Data | 32,581 rows; 11 predictors and one binary target |
| Model | RBF SVM with balanced class weights |
| Evaluation | One 80/20 random split; 6,517 test rows |
| Artifacts | Notebook with saved outputs, matching core workflow in a script, original evaluation image |
| Status | Educational analysis; no deployed lending service or saved model artifact |

> [!IMPORTANT]
> The imputer learns column means from the full dataset **before** the split. Saved scores therefore have a known preprocessing-leakage limitation. The notebook and script also differ in their assignment of the imputer result. The [evidence audit](docs/implementation-evidence.md) identifies the exact locations; no corrected model was trained for this documentation update.

The engineering value of this study is its inspectable treatment of mixed feature types, class imbalance, feature scaling, and classification errors. The results describe this experiment and do not establish suitability for lending decisions.

## Business problem and target

Credit-risk analysis asks whether a loan is associated with default. This experiment learns `loan_status` from applicant, loan, and credit-history fields. The [publisher's data card](https://www.kaggle.com/laotse/credit-risk-dataset/metadata) defines the labels as follows:

| Label | Meaning | Role in evaluation |
|---|---|---|
| `0` | Non-default | Negative class |
| `1` | Default | Positive class; used for default recall |

A missed default and a false default flag have different business implications, so class-specific errors matter alongside accuracy. Their financial costs are not measured here; no loss amount, recovery rate, or lending policy is modeled.

The original plot calls class 0 “Approved,” and the sample prints “Approved” or “Default Risk / Rejected.” Those are presentation labels in the preserved implementation. The supervised target records default status, so a class-0 prediction does not establish approval eligibility or borrower safety. The sample also reuses `X_test[0]`; it is a demonstration on an existing test row.

## Dataset intelligence

The checked-in [CSV](credit_risk_dataset.csv) contains **32,581 rows and 12 columns: 11 predictors plus `loan_status`**. The attributed [Kaggle source](https://www.kaggle.com/laotse/credit-risk-dataset/metadata) describes simulated credit-bureau fields.

| Target | Records | Share |
|---|---:|---:|
| Non-default (`0`) | 25,473 | 78.18% |
| Default (`1`) | 7,108 | 21.82% |

The saved EDA consists of schema, descriptive statistics, and missing-value inspection. A read-only CSV audit also found 165 repeated full rows, maximum age 144, and maximum employment length 123 years. The original workflow retains them. These findings merit investigation before further modeling; they are not silently cleaned here.

| Feature group | Original predictors |
|---|---|
| Applicant | `person_age`, `person_income`, `person_home_ownership`, `person_emp_length` |
| Loan | `loan_intent`, `loan_grade`, `loan_amnt`, `loan_int_rate`, `loan_percent_income` |
| Credit history | `cb_person_default_on_file`, `cb_person_cred_hist_length` |

See [dataset provenance and inspection](docs/dataset.md) for source attribution and counting methods, and the [complete feature glossary](docs/feature-glossary.md) for all 12 columns, category counts, ranges, and unit caveats.

## Author and license

**Khaled Amireh** · [GitHub](https://github.com/khaled-amireh) · [Portfolio](https://portfolio-1kpn.onrender.com)

Repository code is provided under the [MIT License](LICENSE). Dataset provenance and its publisher's terms should be considered separately from the repository license.

The original ML artifacts are preserved byte for byte; see the [SHA-256 baseline](docs/protection-baseline.md).

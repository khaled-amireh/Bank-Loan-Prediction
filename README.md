<p align="center">
  <img src="images/credit-risk-intelligence-banner.svg" alt="Credit Risk Intelligence — Machine Learning for Loan Default Risk Assessment" width="100%">
</p>

# Credit Risk Intelligence

**Machine Learning for Loan Default Risk Assessment**

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](loan_prediction_model.py)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-RBF%20SVM-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)](loan_prediction_model.py)
[![Jupyter](https://img.shields.io/badge/Jupyter-saved%20analysis-F37626?style=flat-square&logo=jupyter&logoColor=white)](loan_prediction_model.ipynb)
[![MIT License](https://img.shields.io/badge/License-MIT-D4AF37?style=flat-square)](LICENSE)

[Overview](#executive-overview) · [Evidence audit](docs/implementation-evidence.md) · [Author](#author-and-license)

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

## Author and license

**Khaled Amireh** · [GitHub](https://github.com/khaled-amireh) · [Portfolio](https://portfolio-1kpn.onrender.com)

Repository code is provided under the [MIT License](LICENSE). Dataset provenance and its publisher's terms should be considered separately from the repository license.

The original ML artifacts are preserved byte for byte; see the [SHA-256 baseline](docs/protection-baseline.md).

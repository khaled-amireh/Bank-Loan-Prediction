<div align="center">

#  Bank Loan Approval Prediction

### Modeling credit risk with a Kernel SVM (RBF)

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Kernel%20SVM-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat-square&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-2ea44f?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

*An end-to-end, leakage-safe classification pipeline that flags high-risk loan applicants using a Support Vector Machine with a non-linear RBF kernel — catching **75% of defaulters** in unseen test data.*

[Overview](#-project-overview) • [Dataset](#-dataset-overview) • [Pipeline](#-technical-pipeline) • [Results](#-key-results--evaluation) • [Business Impact](#-business-key-takeaways) • [Installation](#-installation)

</div>

---

##  Project Overview

In commercial banking, approving a loan for an applicant who ultimately defaults (a **False Negative**) results in a direct loss of principal capital — a materially different cost than the inconvenience of an extra manual review on a false alarm. That asymmetry shapes every modeling decision in this project.

Traditional linear models often struggle to capture the **non-linear interactions** between financial parameters — income, loan amount, interest rate, and debt-to-income ratio rarely combine additively when it comes to real-world default risk. This project instead models the risk boundary with a **Kernel SVM using an RBF kernel**, trained on a comprehensive credit risk dataset, with class weighting applied to counter the natural imbalance between defaulters and non-defaulters.

**What this project demonstrates:**

| Capability | Implementation |
|---|---|
| Missing-value handling | Mean imputation on key numerical columns |
| Leakage-safe pipeline | Train/test split performed *before* encoding |
| Categorical encoding | `ColumnTransformer` + `OneHotEncoder` on nominal features |
| Feature scaling | `StandardScaler`, essential for distance-based SVM kernels |
| Imbalance-aware modeling | `class_weight='balanced'` to prioritize default detection |
| Business-framed evaluation | Results interpreted through cost of missed defaults, not just accuracy |

---

##  Dataset Overview

**Source:** [Credit Risk Dataset — Kaggle](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)

**Scale:** **32,581 loan records** across **12 features**, spanning applicant demographics and loan metrics.

| Category | Features |
|---|---|
| **Applicant Metrics** | Age, Income, Employment Length, Home Ownership (`RENT`, `OWN`, `MORTGAGE`, `OTHER`) |
| **Loan Metrics** | Loan Amount, Loan Intent (`EDUCATION`, `MEDICAL`, `VENTURE`, etc.), Interest Rate, Loan Grade, Percent of Income |
| **Credit History** | Default History (`Y`/`N`), Credit History Length |

### Target Variable — `loan_status`

| Value | Meaning |
|:---:|---|
| `0` | Approved / Non-Default |
| `1` | Default / High Risk |

### Feature Summary

| Feature | Description |
|---|---|
| `person_age` | Applicant age |
| `person_income` | Annual income |
| `loan_amnt` | Requested loan amount |
| `loan_int_rate` | Loan interest rate |
| `loan_percent_income` | Loan-to-income ratio |
| `cb_person_cred_hist_length` | Credit history length |

---

##  Technical Pipeline

```mermaid
flowchart LR
    A[Load & Inspect Dataset] --> B[Exploratory Data Analysis]
    B --> C[Train/Test Split — 80/20]
    C --> D[Missing Value Imputation]
    D --> E[Categorical Encoding]
    E --> F[Feature Scaling]
    F --> G[Train Kernel SVM - RBF]
    G --> H[Evaluate Performance]
    H --> I[Business Impact Analysis]
```

### 1 · Exploratory Data Analysis (EDA)
Inspected data distributions and identified null values across features to scope the preprocessing work needed.

### 2 · Data Splitting (Leakage Prevention)
Applied `train_test_split` (**80/20**, `random_state=42`) **before** any encoding or imputation was fitted. This ordering is deliberate: fitting transformers on the full dataset first would let information from the test set leak into training, inflating reported performance beyond what the model would actually achieve on truly new applicants.

### 3 · Missing Value Imputation
Applied `SimpleImputer` with a **mean strategy** on the numerical columns containing missing values — `loan_int_rate` and `person_emp_length` — preserving these rows rather than discarding them outright.

### 4 · Categorical Encoding
Used a `ColumnTransformer` with `OneHotEncoder` to encode the non-numeric columns:
- `person_home_ownership`
- `loan_intent`
- `loan_grade`
- `cb_person_default_on_file`

### 5 · Feature Scaling
Applied `StandardScaler` across all features. This step is not optional for an SVM — the RBF kernel computes distances between points in feature space, so unscaled features with different magnitudes (e.g., `person_income` vs. `person_age`) would silently dominate the decision boundary if left unscaled.

### 6 · Model Training & Optimization
Trained:

```python
SVC(kernel='rbf', class_weight='balanced')
```

`class_weight='balanced'` reweights the training loss to give the minority default class proportionally more influence — steering the model away from the trivial (and useless) strategy of simply predicting "non-default" for everyone.

---

## 📈 Key Results & Evaluation

| Metric | Performance |
|---|---:|
| **Overall Accuracy** | **87.77%** |
| **Non-Default (0) Precision / Recall** | **0.93 / 0.91** |
| **Default Risk (1) Recall** | **0.75 (75%)** |
| **Default Risk (1) F1-Score** | **0.73** |

### Why Class 1 Recall Is the Metric That Matters

Accuracy alone would be a misleading headline here: the dataset skews toward non-defaulters, so a model that leaned heavily toward predicting "non-default" could post a high accuracy while quietly missing the riskiest applicants — exactly the failure mode this project was built to avoid.

**Default Risk (Class 1) Recall of 75%** means the model correctly flags 3 out of every 4 applicants who would actually default — directly protecting the bank's capital, which is the entire point of the model.

### Confusion Matrix

<p align="center">
  <img src="images/confusion_matrix(SVM).png" alt="Confusion Matrix - Kernel SVM" width="600">
</p>

---

## 💼 Business Key Takeaways

| Insight | Detail |
|---|---|
| 🎯 **Catching Default Risks** | With `class_weight='balanced'`, the model achieves **75% Recall on Class 1**, correctly flagging **1,087 of 1,445** high-risk applicants in the test set |
| ⚖️ **Risk Mitigation vs. False Alarms** | The pipeline trades a modest amount of overall accuracy for a large reduction in missed defaults — down to just **358 False Negatives** — directly protecting the bank against capital loss |

In lending, a missed default is a direct financial write-off, while a false alarm typically just means an extra round of manual underwriting review. Given that asymmetry, trading some accuracy and precision for materially higher default recall is a rational, deliberate business trade-off — not a modeling shortcoming.

---

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| Language | Python |
| Data Handling | Pandas, NumPy |
| Machine Learning | Scikit-learn (Kernel SVM) |
| Visualization | Matplotlib, Seaborn |

---

## 📁 Project Structure

```
Bank-Loan-Approval-Prediction/
│
├── images/
│   └── confusion_matrix(SVM).png
├── data/
│   └── credit_risk_dataset.csv
├── notebooks/
│   └── bank_loan_approval_prediction.ipynb
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/khaled-amireh/Bank-Loan-Approval-Prediction.git
cd Bank-Loan-Approval-Prediction

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the notebook
jupyter notebook notebooks/bank_loan_approval_prediction.ipynb
```

---

## ⚠️ Limitations

- The model was evaluated on a single train/test split rather than cross-validated, so reported metrics may vary somewhat across different splits.
- The decision threshold used to generate the headline Precision/Recall figures was not explicitly tuned — further gains on Class 1 Recall may be available by adjusting the classification threshold for a specific cost trade-off.
- Kernel SVMs scale less efficiently to very large datasets than tree-based ensembles; at significantly greater data volumes, training time would need to be re-evaluated.

---

## 🚀 Future Improvements

- [ ] Explicit threshold tuning to optimize for a target cost function (cost of a missed default vs. cost of a false alarm)
- [ ] Cross-validation for more robust performance estimates
- [ ] Benchmark against tree-based ensembles (Random Forest, XGBoost) commonly used in credit risk modeling
- [ ] Hyperparameter tuning of `C` and `gamma` via grid/random search
- [ ] SHAP-based feature attribution for per-applicant risk explanations

---

## 👤 Author

**Khaled Amireh**
[GitHub](https://github.com/khaled-amireh)

---

<div align="center">

*If you found this project useful, consider giving it a ⭐ on GitHub.*

</div>

# Bank Loan Approval Prediction

![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)

An end-to-end Machine Learning classification pipeline built in Python to evaluate bank loan application risks. By utilizing a **Support Vector Machine (SVM)** with a non-linear **Radial Basis Function (RBF)** kernel and balanced class weighting, this model effectively identifies high-risk borrowers and mitigates default risks for financial institutions.

---

## Project Overview

In commercial banking, approving loans for applicants who ultimately default (**False Negatives**) results in significant loss of principal capital. Traditional linear models often struggle with complex interactions between financial parameters (e.g., non-linear relationships between income, loan amount, interest rate, and debt-to-income ratios).

This project models complex risk boundaries using a **Kernel SVM (RBF Kernel)** trained on a comprehensive credit risk dataset.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn

---

## Dataset Overview

* **Source:** [Credit Risk Dataset on Kaggle](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)
* **Scale:** **32,581 loan records** across **12 features** covering applicant demographics and loan metrics:

* **Applicant Metrics:** Age, Income, Employment Length, Home Ownership status (`RENT`, `OWN`, `MORTGAGE`, `OTHER`).
* **Loan Metrics:** Loan Amount, Loan Intent (`EDUCATION`, `MEDICAL`, `VENTURE`, etc.), Interest Rate, Loan Grade, Percent of Income.
* **Credit History:** Default History (`Y`/`N`), Credit History Length.
* **Target Variable (`loan_status`):** `0` = Approved / Non-Default, `1` = Default / High Risk[cite: 1, 2].

## Feature Summary

| Feature | Description |
|----------|-------------|
| person_age | Applicant age |
| person_income | Annual income |
| loan_amnt | Requested loan amount |
| loan_int_rate | Loan interest rate |
| loan_percent_income | Loan-to-income ratio |
| cb_person_cred_hist_length | Credit history length |

---

## Technical Pipeline

1. **Exploratory Data Analysis (EDA):** Inspected data distributions and identified null values across features[cite: 1, 2].
2. **Missing Value Imputation:** Applied `SimpleImputer` using mean strategy on numerical columns containing missing values (`loan_int_rate` and `person_emp_length`)[cite: 1, 2].
3. **Data Splitting:** Applied `train_test_split` (80/20 train-test ratio with `random_state=42`) **prior to encoding** to strictly prevent data leakage[cite: 1, 2].
4. **Categorical Encoding:** Used Scikit-Learn's `ColumnTransformer` with `OneHotEncoder` to encode non-numeric columns (`person_home_ownership`, `loan_intent`, `loan_grade`, `cb_person_default_on_file`)[cite: 1, 2].
5. **Feature Scaling:** Applied `StandardScaler` across all features, ensuring distance calculations in SVM remain unskewed by feature magnitudes[cite: 1, 2].
6. **Model Training & Optimization:** Trained `SVC(kernel='rbf', class_weight='balanced')` to account for class imbalance between non-defaulters and defaulters[cite: 1, 2].

---

## Project Workflow

1. Load and inspect dataset
2. Handle missing values
3. Encode categorical features
4. Scale numerical features
5. Train Kernel SVM model
6. Evaluate performance
7. Analyze business impact

---

## Key Results & Evaluation

| Metric | Performance |
| :--- | :--- |
| **Overall Accuracy** | **87.77%** |
| **Non-Default (0) Precision / Recall** | **0.93 / 0.91** |
| **Default Risk (1) Recall** | **0.75 (75%)** |
| **Default Risk (1) F1-Score** | **0.73** |

### Confusion Matrix Visual
![Confusion Matrix - Kernel SVM](images/confusion_matrix(SVM).png)

### Business Key Takeaways
* **Catching Default Risks:** By introducing `class_weight='balanced'`, the model prioritizes identifying actual defaults, achieving a **75% Recall on Class 1** (correctly flagging **1,087 high-risk applicants** out of 1,445 in the test set).
* **Risk Mitigation vs. False Alarms:** The pipeline sacrifices a minor fraction of overall accuracy to cut missed defaults down to **358 (False Negatives)**, protecting the bank against capital loss.


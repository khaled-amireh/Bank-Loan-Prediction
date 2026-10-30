# Feature glossary

[Project overview](../README.md) · [Dataset provenance](dataset.md)

Names and order below match the local CSV exactly. Numeric/text types describe the stored values and the notebook's saved schema, rather than an imposed data-validation contract. Ranges exclude missing values. Descriptions follow the field names and the [publisher's dictionary](https://www.kaggle.com/laotse/credit-risk-dataset/metadata); undocumented units are left unspecified.

| Column | Role / kind | Meaning and observed values |
|---|---|---|
| `person_age` | Predictor / integer | Age; 20–144, including extreme values |
| `person_income` | Predictor / integer | Annual income; 4,000–6,000,000; currency unspecified |
| `person_home_ownership` | Predictor / categorical | `MORTGAGE`, `OTHER`, `OWN`, `RENT` |
| `person_emp_length` | Predictor / numeric, nullable | Employment length in years; 0–123; 895 missing |
| `loan_intent` | Predictor / categorical | `DEBTCONSOLIDATION`, `EDUCATION`, `HOMEIMPROVEMENT`, `MEDICAL`, `PERSONAL`, `VENTURE` |
| `loan_grade` | Predictor / categorical | Grades `A`, `B`, `C`, `D`, `E`, `F`, `G`; encoded as categories |
| `loan_amnt` | Predictor / integer | Loan amount; 500–35,000; currency unspecified |
| `loan_int_rate` | Predictor / numeric, nullable | Recorded interest rate; 5.42–23.22; 3,116 missing; exact rate convention unspecified |
| `loan_status` | **Target** / binary integer | `0`: non-default; `1`: default; excluded from predictors |
| `loan_percent_income` | Predictor / numeric | Recorded income proportion; 0–0.83; used directly without conversion |
| `cb_person_default_on_file` | Predictor / categorical | Historical-default flag, `N` or `Y`; separate from the prediction target |
| `cb_person_cred_hist_length` | Predictor / integer | Credit-history length; 2–30; unit not formally specified in the repository |

## Category coverage in the full CSV

| Field | Counts |
|---|---|
| Home ownership | `RENT`: 16,446; `MORTGAGE`: 13,444; `OWN`: 2,584; `OTHER`: 107 |
| Loan intent | `EDUCATION`: 6,453; `MEDICAL`: 6,071; `VENTURE`: 5,719; `PERSONAL`: 5,521; `DEBTCONSOLIDATION`: 5,212; `HOMEIMPROVEMENT`: 3,605 |
| Loan grade | `A`: 10,777; `B`: 10,451; `C`: 6,458; `D`: 3,626; `E`: 964; `F`: 241; `G`: 64 |
| Historical default | `N`: 26,836; `Y`: 5,745 |

Each row of category counts sums to 32,581. Full-file category coverage is not a saved record of the fitted encoder's categories on the training subset.

## Interpretation boundaries

The dictionary is not a claim that these predictors are available before a lending decision. Timing of grade assignment, rate setting, and the historical-default observation must be verified before any application-time use. The historical flag is not substituted for `loan_status` and is not proof that the model target leaked directly into a predictor.

The publisher's dictionary misspells the credit-history field as `cb_preson_cred_hist_length`; this repository uses the actual CSV spelling, `cb_person_cred_hist_length`. Preserve it when reading the existing artifacts.

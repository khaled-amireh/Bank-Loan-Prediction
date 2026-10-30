# Dataset provenance and inspection

[Project overview](../README.md) · [Implementation evidence](implementation-evidence.md)

## Provenance

The previous README attributes the data to Lao Tse's [Credit Risk Dataset on Kaggle](https://www.kaggle.com/datasets/laotse/credit-risk-dataset). The publisher's [metadata page](https://www.kaggle.com/laotse/credit-risk-dataset/metadata), checked on 2026-10-30, describes columns that simulate credit-bureau data and defines the binary default target. Its license field is listed as **CC0: Public Domain**; the repository's separate [MIT license](../LICENSE) is unchanged.

The local filename and schema agree with that attribution. No fresh upstream download or byte-for-byte comparison with a Kaggle release was performed. The checked-in CSV is the reference for every local count below, and its exact hash appears in the [protection baseline](protection-baseline.md).

The repository does not establish a collection period, country, currency, default observation horizon, borrower identifiers, sampling methodology, or a real lending institution. Treat these as unavailable provenance details. In particular, the data card's simulation description does not support describing the rows as audited historical bank loans.

## Local snapshot

| Property | Value |
|---|---:|
| Data rows, excluding header | 32,581 |
| Columns | 12 |
| Predictors after dropping `loan_status` | 11 |
| Non-default, `loan_status=0` | 25,473 (78.18%) |
| Default, `loan_status=1` | 7,108 (21.82%) |
| Repeated complete rows beyond their first occurrences | 165 |

Counts were obtained by reading the CSV header and all rows with Python's standard-library CSV reader. Empty fields are counted as missing. Duplicate counts compare all 12 raw fields, including the label; they do not identify repeated borrowers.

## Exploratory analysis that is actually present

The notebook saves `df.info()`, `df.describe()`, and missing-value counts. It contains no saved correlation heatmap, class-distribution chart, feature-importance chart, or comparative model plot. The sole original repository image is the evaluation confusion matrix.

| Inspection finding | Evidence and implication |
|---|---|
| Income has a wide range | 4,000–6,000,000 in unspecified currency units; scale and outlier sensitivity deserve investigation |
| Age includes extreme values | Range 20–144; five rows have age above 100 |
| Employment length includes extreme values | Non-missing range 0–123 years; two rows exceed 100 |
| Missing numeric fields | Interest rate: 3,116; employment length: 895; all other columns: zero |
| Label imbalance | About one default row for every 3.58 non-default rows |
| Repeated rows | Potential partition overlap warrants checking; overlap was not established by this audit |

The code does not remove duplicates, cap outliers, or filter these extreme values. No data-quality correction has been applied. Observed associations, if explored in a future experiment, would not by themselves establish causal risk drivers.

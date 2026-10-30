# Preprocessing implementation

[Project overview](../README.md) · [Evidence locations](implementation-evidence.md)

## Missing values

| Field | Empty cells | Share of 32,581 rows | Non-missing full-file mean |
|---|---:|---:|---:|
| `loan_int_rate` | 3,116 | 9.56% | 11.0116948922 |
| `person_emp_length` | 895 | 2.75% | 4.7896862968 |
| Each of the other 10 columns | 0 | 0.00% | Not used for imputation |

Means were calculated directly from the non-empty CSV fields as an arithmetic check, without fitting an estimator. Missingness counts are per column; summing them would not establish the number of distinct affected rows.

The script performs these operations before `train_test_split`:

```python
missing_cols = ['loan_int_rate', 'person_emp_length']
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df[missing_cols] = imputer.fit_transform(df[missing_cols])
X[missing_cols] = imputer.transform(X[missing_cols])
```

This retains rows and uses the same learned column means for `df` and `X`. There is no missingness indicator, subgroup-specific imputation, or evaluation of alternative strategies.

## Confirmed leakage from the order of operations

Both original artifacts fit the imputer on the complete dataset before partitioning it. Test-set feature values therefore contribute to the means used in training. This is a preprocessing leak even though the imputer does not use `y`. Its effect on the scores cannot be quantified from saved outputs alone.

Training-only fitting of all learned transformations is the recommended evaluation practice ([scikit-learn guidance](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)). Moving imputation inside a training-fitted pipeline would be a future implementation change requiring a new evaluation; it has not been done here.

## Notebook and script differ

Notebook cell 10 contains the following assignment instead of the script's `fit_transform` assignment:

```python
df[missing_cols] = imputer.fit(df[missing_cols])
X[missing_cols] = imputer.transform(X[missing_cols])
```

The [imputer API](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.fit) returns an estimator from `fit`, whereas `fit_transform` returns transformed data. Assigning the estimator to `df` is not equivalent to assigning numeric imputed values. A later saved display of zero missing values in `df` does not validate that operation.

`X` was created earlier by dropping `loan_status`, and the notebook separately calls `imputer.transform` on its numeric columns. The discrepancy in `df` should not be presented as proof that the model itself received estimator objects. Fresh-kernel execution and numeric dtype checks would be needed to establish reproducibility; neither original file was edited or run during this documentation work.

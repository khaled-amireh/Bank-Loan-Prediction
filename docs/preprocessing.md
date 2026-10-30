# Preprocessing implementation

[Project overview](../README.md) · [Evidence locations](implementation-evidence.md)

## Missing values

| Field | Empty cells | Share of 32,581 rows | Non-missing full-file mean |
|---|---:|---:|---:|
| `loan_int_rate` | 3,116 | 9.56% | 11.0116948922 |
| `person_emp_length` | 895 | 2.75% | 4.7896862968 |
| Each of the other 10 columns | 0 | 0.00% | Not used for imputation |

Means were calculated directly from the non-empty CSV fields as an arithmetic check, without fitting an estimator. Missingness counts are per column; summing them would not establish the number of distinct affected rows.

The script and notebook now split raw features before learning the imputation means:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
missing_cols = ['loan_int_rate', 'person_emp_length']
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
X_train[missing_cols] = imputer.fit_transform(X_train[missing_cols])
X_test[missing_cols] = imputer.transform(X_test[missing_cols])
```

This retains every row and the original mean strategy. `df` and `X` remain raw EDA inputs; only the prepared partitions are imputed. Missingness verification now checks both `X_train` and `X_test`. There is no missingness indicator, subgroup-specific imputation, or evaluation of alternative strategies.

## Leakage correction

Before the fix, both artifacts fitted the imputer on the complete dataset before partitioning it. Test-set feature values therefore influenced the means used in training. The corrected training-only means are **11.0101161755** for interest rate and **4.7872332031** for employment length; the full-file means in the EDA table above are no longer used for imputation.

Training-only fitting follows [scikit-learn guidance](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage). The fix moves the existing split ahead of imputation without introducing a new pipeline. A [fresh-kernel evaluation](evaluation.md#corrected-workflow-verification) found no changed predictions versus a pre-fix replay in the same environment.

## Notebook and script consistency

Before the fix, notebook cell 10 at commit `7f74cc9` contained this assignment instead of the script's `fit_transform` assignment:

```python
df[missing_cols] = imputer.fit(df[missing_cols])
X[missing_cols] = imputer.transform(X[missing_cols])
```

The [imputer API](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.fit) returns an estimator from `fit`, whereas `fit_transform` returns transformed data. That historical assignment and the script's full-data assignment are both removed. The notebook's existing split section now precedes imputation; all headings, cell IDs, and notebook metadata are preserved.

The corrected script and notebook produce identical prepared training/test arrays with finite values, unchanged feature ordering, and shapes `(26064, 26)` / `(6517, 26)`. Changing only held-out numeric values leaves the learned training statistics and transformed training features unchanged; the same check detects the old full-data leak. Only affected verification, evaluation, and sample outputs/counts were merged from the fresh notebook run; unrelated saved outputs remain intact.

## Categorical encoding

The original `ColumnTransformer` applies `OneHotEncoder()` to these four columns:

- `person_home_ownership`
- `loan_intent`
- `loan_grade`
- `cb_person_default_on_file`

The remaining seven numeric predictors pass through using `remainder='passthrough'`. The target was already removed. The encoder fits with `ct.fit_transform(X_train)` and applies that fitted vocabulary using `ct.transform(X_test)`.

No category dropping, ordinal treatment of loan grade, unknown-category policy, or output format is explicitly configured. In particular, the implementation does not opt into ignoring unknown categories; the [encoder API](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) describes default behavior. The fitted category list and transformed matrix shape are not saved as separate artifacts. Full-CSV category counts in the glossary must not be mistaken for fitted-encoder output.

## Scaling the complete encoded matrix

Both original artifacts contain:

```python
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
```

The [scaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) learns feature means and scales from training rows. It is applied **after** one-hot encoding, so indicator columns are scaled along with income, loan amount, and the other numeric columns. There is no separate numeric-only scaling branch.

This changes the geometry used by the RBF kernel; raw income and amount magnitudes otherwise differ greatly from age and proportions. It does not establish robustness to the extreme values found in the CSV. Neither a scaled-versus-unscaled ablation nor a numeric-only-scaling comparison is saved.

Training-only fitting is now confirmed for the imputer, encoder, and scaler. Encoder/scaler code is unchanged. The workflow still uses standalone transformer objects, not a single scikit-learn `Pipeline`, and does not save the fitted transformers for future inference.

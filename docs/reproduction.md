# Installation, inspection, and reproduction

[Project overview](../README.md) · [Implementation evidence](implementation-evidence.md) · [Protected-file hashes](protection-baseline.md)

## Inspect the saved study first

Open [the notebook](../loan_prediction_model.ipynb) in GitHub's notebook viewer to read its existing tables, report, and embedded plot. This requires no local installation or execution. The [script](../loan_prediction_model.py) is a readable implementation companion; the [original plot](../images/confusion_matrix%28SVM%29.png) is also available separately.

Exact numerical replay is **not established**. Python 3.11.9 appears in notebook metadata, but there is no requirements file, lockfile, or saved list of package versions. The notebook's `fit` assignment differs from the script's `fit_transform` assignment. Read the [preprocessing explanation](preprocessing.md) before trying a fresh run.

## Dependencies supported by imports

| Installable package | Verified import / purpose |
|---|---|
| `numpy` | `numpy as np`; missing-value marker |
| `pandas` | CSV loading, dataframes, and inspection |
| `matplotlib` | `matplotlib.pyplot`; evaluation plotting |
| `seaborn` | Confusion-matrix heatmap; imported in both artifacts |
| `scikit-learn` | `sklearn`; splitting, imputation, encoding, scaling, SVC, and metrics |
| `notebook`, `ipykernel` | Suggested local notebook viewer and kernel tooling; not model imports |

No minimum Python-version range or compatible package-version combination has been tested by this documentation audit. The commands below are an **unpinned setup example**, not a recovered original environment. Installation and training were not performed during the sprint.

## Windows PowerShell

Use a separate clone for intentional experiments. The environment is placed outside the checkout so it does not add untracked dependency files to a repository that has no `.gitignore`.

```powershell
git clone https://github.com/khaled-amireh/Bank-Loan-Prediction.git
cd Bank-Loan-Prediction
python -m venv "$env:TEMP\credit-risk-intelligence-venv"
& "$env:TEMP\credit-risk-intelligence-venv\Scripts\python.exe" -m pip install numpy pandas matplotlib seaborn scikit-learn notebook ipykernel
& "$env:TEMP\credit-risk-intelligence-venv\Scripts\python.exe" -m notebook loan_prediction_model.ipynb
```

Calling the environment's interpreter directly avoids requiring a PowerShell activation script. Launch from the repository root because both ML artifacts load `credit_risk_dataset.csv` with a relative path. Opening the notebook displays saved outputs; running cells and saving it can replace them.

## macOS / Linux

```bash
git clone https://github.com/khaled-amireh/Bank-Loan-Prediction.git
cd Bank-Loan-Prediction
python3 -m venv /tmp/credit-risk-intelligence-venv
/tmp/credit-risk-intelligence-venv/bin/python -m pip install numpy pandas matplotlib seaborn scikit-learn notebook ipykernel
/tmp/credit-risk-intelligence-venv/bin/python -m notebook loan_prediction_model.ipynb
```

Temporary environments may be removed by the operating system. A user-selected environment outside the checkout is also suitable. No Kaggle download is needed for this checked-in snapshot.

## Intentional model execution in an experimental checkout

The following commands **train the model**; they were not run as part of documentation verification. They are provided only for a reader who elects to investigate execution in a separate checkout.

```powershell
& "$env:TEMP\credit-risk-intelligence-venv\Scripts\python.exe" .\loan_prediction_model.py
```

```bash
/tmp/credit-risk-intelligence-venv/bin/python loan_prediction_model.py
```

The script prints data inspection and evaluation to the console, displays a heatmap through `plt.show()`, and prints a prediction for the first transformed test row. Close the plot window if execution is waiting for it. It does not save a trained model or export a new evaluation image. New results must be labeled as a new run, rather than substituted for the saved notebook results.

## Troubleshooting grounded in this checkout

| Symptom | Check |
|---|---|
| CSV not found | Start in the directory containing `credit_risk_dataset.csv`, the script, and the notebook |
| `No module named sklearn` | Install `scikit-learn` with the same environment interpreter used to launch the notebook or script |
| Notebook uses a different environment | Inspect its selected kernel and interpreter; installing packages into another Python does not update that kernel |
| A command references `requirements.txt`, `data/`, or `notebooks/` | Those paths are absent here; use the root-level files and explicit package list above |
| Fresh results differ or notebook preprocessing behaves unexpectedly | Record actual Python/package versions and the exact error or diff; review the known `fit`/`fit_transform` discrepancy before attributing the difference to model quality |
| Script appears to pause after evaluation | Check whether the Matplotlib plot window is open |

Do not overwrite original outputs to make a new run appear identical. Environment pinning and a verified clean-kernel replay remain future work.

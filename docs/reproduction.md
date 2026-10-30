# Installation, inspection, and reproduction

[Project overview](../README.md) · [Implementation evidence](implementation-evidence.md) · [Protected-file hashes](protection-baseline.md)

## Inspect the saved study first

Open [the notebook](../loan_prediction_model.ipynb) in GitHub's notebook viewer to read its existing tables, report, and embedded plot. This requires no local installation or execution. The [script](../loan_prediction_model.py) is a readable implementation companion; the [original plot](../images/confusion_matrix%28SVM%29.png) is also available separately.

The corrected workflow has been **verified once in a fresh kernel**, with its installed versions recorded in the [evaluation comparison](evaluation.md#corrected-workflow-verification). Python 3.11.9 matches notebook metadata. There is still no requirements file or lockfile, and the original historical package versions are unknown. The notebook/script imputation discrepancy is resolved; see [preprocessing](preprocessing.md).

## Dependencies supported by imports

| Installable package | Verified import / purpose |
|---|---|
| `numpy` | `numpy as np`; missing-value marker |
| `pandas` | CSV loading, dataframes, and inspection |
| `matplotlib` | `matplotlib.pyplot`; evaluation plotting |
| `seaborn` | Confusion-matrix heatmap; imported in both artifacts |
| `scikit-learn` | `sklearn`; splitting, imputation, encoding, scaling, SVC, and metrics |
| `notebook`, `ipykernel` | Suggested local notebook viewer and kernel tooling; not model imports |

The recorded corrected-run environment is tested; no wider supported Python/package-version range is established. The commands below are an **unpinned setup example**, not a recovered historical environment or a dependency lock. No packages were installed or upgraded for the fix.

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

The following commands **train the model**. The fix was verified through one fresh-kernel notebook run and a pre-fix script replay, rather than by repeatedly running these commands. Use a separate experimental checkout for additional investigations.

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
| Fresh results differ or notebook preprocessing behaves unexpectedly | Compare versions with the verified evaluation environment and confirm the checkout contains the training-only imputation fix; record the exact error or diff |
| Script appears to pause after evaluation | Check whether the Matplotlib plot window is open |

Do not overwrite outputs to make a new run appear identical. A clean-kernel corrected run is verified; dependency pinning and portability across other environments remain future work.

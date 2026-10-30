# Protected-file baseline

[Project overview](../README.md) · [Implementation evidence](implementation-evidence.md)

- Initial commit: `ace83acdc7723ac183649eb3e087d500fc400c85`
- Initial branch: `main`
- Initial working tree: clean
- Inspection date: 2026-10-30

Every original tracked file except `README.md` is protected. SHA-256 was computed from raw file bytes before any repository edits.

| Original file | Bytes | SHA-256 |
|---|---:|---|
| `LICENSE` | 1,091 | `72a967ad8f5674562cd5bcc81b8665f2791382f23a671d5e7ce595954f636d69` |
| `credit_risk_dataset.csv` | 1,740,274 | `07a70394593c1e25c968d129b7ac7dd0e959514a15115bdc5f5cc08e0ff7064a` |
| `images/confusion_matrix(SVM).png` | 59,802 | `b83c4553b57a2b5f72ebfe8d715b112006a51f72d681998e7c5a72af6a53144d` |
| `loan_prediction_model.ipynb` | 127,790 | `175e14e4109741c9d4ba5056cbf116fa456772a68a8792d40467382ba8a9c14c` |
| `loan_prediction_model.py` | 2,911 | `aef747c0d605a558160c5c2e5f7de31dd275a87da2119c02c6e7f1e55aef828e` |

For a read-only local comparison in PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath LICENSE, credit_risk_dataset.csv, 'images/confusion_matrix(SVM).png', loan_prediction_model.ipynb, loan_prediction_model.py
git diff ace83acdc7723ac183649eb3e087d500fc400c85 -- LICENSE credit_risk_dataset.csv 'images/confusion_matrix(SVM).png' loan_prediction_model.ipynb loan_prediction_model.py
```

A Git diff checks committed content; the byte hashes also detect working-tree line-ending changes. Neither command executes the ML implementation. No Git configuration, authorship, or timestamps were changed by the documentation sprint.

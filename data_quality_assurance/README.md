# AI Dataset Quality Assurance

This independent demonstration uses **synthetic** feedback data to show a practical QA workflow. It is not client data and does not represent work completed for MECOR, Handshake, or another organization.

## Workflow
`raw data → profiling → issue detection → correction/quarantine → validation → final QA report`

1. **Raw data:** [`sample_dataset.csv`](sample_dataset.csv) intentionally includes missing values, duplicate records, inconsistent label capitalization, invalid labels and confidence values, plus inconsistent source/date formatting.
2. **Profiling and issue detection:** Run [`qa_check.py`](qa_check.py) to count and display each issue type.
3. **Correction or quarantine:** Normalize only values with an unambiguous correction. Quarantine records with missing required data, unsupported labels, invalid confidence, or duplicate invalid rows.
4. **Validation:** Confirm each retained row has required fields, a controlled label, confidence in `[0, 1]`, a normalized source, and an ISO date.
5. **Final QA report:** Review the correction rationale in [`quality_report.md`](quality_report.md) and the final [`clean_dataset.csv`](clean_dataset.csv).

## Run
```bash
python qa_check.py
python validate_clean_dataset.py
```

The first script profiles the deliberately messy raw data; the second acts as a **final acceptance gate** for the cleaned dataset. This separates issue discovery from final verification, which is useful when a dataset moves through multiple QA stages.

Requires Pandas from the repository-level [`requirements.txt`](../requirements.txt).

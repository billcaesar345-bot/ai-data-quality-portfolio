# Synthetic Data Analysis & Quality Report

## Dataset at a Glance
The example dataset contains **8 rows** of synthetic product-area feedback records. It is intended only to demonstrate a clear data-quality summary.

## Key Results
- **Record count:** 8 rows.
- **Category distribution:** `search` has 3 records, `account` has 3, and `checkout` has 2.
- **Missing values:** One `score` value is missing.
- **Duplicates:** One exact duplicate row is present (the second `r006` row).
- **Scores:** The available scores range from 2.0 to 5.0; the mean is approximately 3.8.
- **Basic quality indicators:** 75% of records have `approved` status, while 87.5% are complete across all fields.

## Interpretation
This small dataset is useful for illustrating why record count alone is not enough. A review process should resolve the missing score and determine whether the duplicate is an accidental repeat or a legitimate repeated observation before the data is used for analysis or AI dataset preparation. Category counts also help identify whether one topic is overrepresented.

## Reproduce
Run `python analysis.py` from this directory to calculate the descriptive statistics, category distribution, missing-value counts, duplicate count, and basic quality rates.

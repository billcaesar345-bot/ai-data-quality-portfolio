# Synthetic Dataset Quality Report

**Scope:** `sample_dataset.csv` contains 10 synthetic feedback records created only for this demonstration.

## Findings
| Check | Finding | Disposition |
| --- | ---: | --- |
| Required values | 2 records have a missing required value (text or ID). | Quarantined because the missing values cannot be safely inferred. |
| Duplicate records | 2 rows form one exact duplicate pair for record ID 4. | Quarantined with the invalid original rather than retained. |
| Labels | `Positive` and `NEGATIVE` need case normalization; `unknown` is outside the approved taxonomy. | Normalizable labels were standardized; the unsupported label was quarantined. |
| Confidence | Three distinct values are invalid across four rows: `1.20`, `not_available`, and `-0.10`. | Quarantined; no confidence value was guessed. |
| Formatting | Source names and review dates use inconsistent formats. | Standardized only on otherwise valid records. |

## Correction and Validation Result
The final `clean_dataset.csv` contains **3 records** that meet all acceptance rules: complete required fields, unique full records, approved lowercase labels, numeric confidence from 0 through 1, normalized source names, and ISO `YYYY-MM-DD` dates. The other records are intentionally excluded for review or correction; this prevents unsafe assumptions from entering a training-ready dataset.

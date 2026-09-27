"""Run repeatable quality checks against the synthetic raw QA dataset."""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
RAW_FILE = BASE_DIR / "sample_dataset.csv"
REQUIRED_FIELDS = ["record_id", "text", "label", "confidence", "source", "review_date"]
VALID_LABELS = {"positive", "neutral", "negative"}


def main() -> None:
    data = pd.read_csv(RAW_FILE, dtype=str)
    print(f"Rows profiled: {len(data)}")

    missing = data[REQUIRED_FIELDS].isna() | data[REQUIRED_FIELDS].eq("")
    print("\nMissing required values:")
    print(missing.sum()[missing.sum() > 0].to_string() or "None")

    duplicate_rows = data.duplicated(keep=False)
    print(f"\nDuplicate full rows: {duplicate_rows.sum()}")

    normalized_labels = data["label"].str.strip().str.lower()
    invalid_labels = ~normalized_labels.isin(VALID_LABELS)
    inconsistent_labels = data["label"].ne(normalized_labels) & ~invalid_labels
    print(f"Invalid labels: {invalid_labels.sum()}")
    print(f"Labels needing capitalization normalization: {inconsistent_labels.sum()}")

    confidence = pd.to_numeric(data["confidence"], errors="coerce")
    invalid_confidence = confidence.isna() | ~confidence.between(0, 1)
    print(f"Invalid confidence values: {invalid_confidence.sum()}")

    valid_dates = pd.to_datetime(data["review_date"], format="%Y-%m-%d", errors="coerce")
    source_normalized = data["source"].str.strip().str.lower().str.replace(r"[- ]", "_", regex=True)
    formatting_issues = valid_dates.isna() | data["source"].ne(source_normalized)
    print(f"Date/source formatting issues: {formatting_issues.sum()}")

    issue_mask = missing.any(axis=1) | duplicate_rows | invalid_labels | invalid_confidence | formatting_issues
    print("\nRecords requiring correction or quarantine:")
    print(data.loc[issue_mask, ["record_id", "label", "confidence", "source", "review_date"]].to_string(index=False))


if __name__ == "__main__":
    main()

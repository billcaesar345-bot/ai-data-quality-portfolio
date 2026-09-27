"""Validate the final synthetic QA dataset against its acceptance rules."""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
CLEAN_FILE = BASE_DIR / "clean_dataset.csv"
REQUIRED_FIELDS = ["record_id", "text", "label", "confidence", "source", "review_date"]
VALID_LABELS = {"positive", "neutral", "negative"}
VALID_SOURCES = {"web_form", "email", "app"}

def main() -> None:
    data = pd.read_csv(CLEAN_FILE, dtype=str)
    issues = []

    missing = data[REQUIRED_FIELDS].isna() | data[REQUIRED_FIELDS].eq("")
    if missing.any().any():
        issues.append("required fields contain missing values")
    if data["record_id"].duplicated().any():
        issues.append("record_id values are not unique")

    labels = data["label"].str.strip().str.lower()
    if not labels.isin(VALID_LABELS).all():
        issues.append("unsupported label found")

    confidence = pd.to_numeric(data["confidence"], errors="coerce")
    if confidence.isna().any() or not confidence.between(0, 1).all():
        issues.append("confidence contains a non-numeric or out-of-range value")

    if not data["source"].isin(VALID_SOURCES).all():
        issues.append("source values are not normalized to the approved set")

    dates = pd.to_datetime(data["review_date"], format="%Y-%m-%d", errors="coerce")
    if dates.isna().any():
        issues.append("review_date contains a non-ISO date")

    print("Final Synthetic QA Dataset Validation")
    print("=" * 39)
    print(f"Rows checked: {len(data)}")
    print(f"Validation issues: {len(issues)}")

    if issues:
        for issue in issues:
            print(f"- {issue}")
        raise SystemExit(1)

    print("Result: PASS — clean_dataset.csv satisfies the documented acceptance rules.")

if __name__ == "__main__":
    main()

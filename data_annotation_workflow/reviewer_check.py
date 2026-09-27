"""Run simple reviewer checks against the synthetic annotation example."""
from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent
INPUT = BASE_DIR / "sample_annotations.csv"
VALID_LABELS = {"positive", "neutral", "negative"}
VALID_STATUS = {"approved", "needs_review"}

def main() -> None:
    with INPUT.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    issues = []
    review_count = 0

    for row_number, row in enumerate(rows, start=2):
        if not row.get("text", "").strip():
            issues.append(f"row {row_number}: annotation text is empty")
        if row.get("sentiment") not in VALID_LABELS:
            issues.append(f"row {row_number}: invalid sentiment label")
        if row.get("review_status") not in VALID_STATUS:
            issues.append(f"row {row_number}: invalid review status")
        if row.get("review_status") == "needs_review":
            review_count += 1

    print("Synthetic Annotation Reviewer Check")
    print("=" * 36)
    print(f"Annotations checked: {len(rows)}")
    print(f"Records requiring review: {review_count}")
    print(f"Validation issues: {len(issues)}")

    if issues:
        for issue in issues:
            print(f"- {issue}")
    else:
        print("Result: PASS — taxonomy and review-status checks are valid.")
        print("Reviewer action: inspect every record marked 'needs_review' before approval.")

if __name__ == "__main__":
    main()

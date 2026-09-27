"""Validate the synthetic collection example against its documented schema."""
from pathlib import Path
from datetime import date
from urllib.parse import urlparse
import csv

BASE_DIR = Path(__file__).parent
INPUT = BASE_DIR / "sample_collected_data.csv"
REQUIRED = ["collection_id", "source_name", "source_url", "collected_date", "content", "language", "consent_status"]
ALLOWED_LANGUAGES = {"en"}
ALLOWED_CONSENT = {"documented_example"}

def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)

def main() -> None:
    with INPUT.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    issues = []
    seen_ids = set()

    for row_number, row in enumerate(rows, start=2):
        for field in REQUIRED:
            if not row.get(field, "").strip():
                issues.append(f"row {row_number}: missing required field '{field}'")

        record_id = row.get("collection_id", "").strip()
        if record_id in seen_ids:
            issues.append(f"row {row_number}: duplicate collection_id '{record_id}'")
        elif record_id:
            seen_ids.add(record_id)

        try:
            date.fromisoformat(row.get("collected_date", ""))
        except ValueError:
            issues.append(f"row {row_number}: collected_date is not ISO YYYY-MM-DD")

        if row.get("source_url") and not valid_url(row["source_url"]):
            issues.append(f"row {row_number}: source_url is not a valid HTTP(S) URL")

        if row.get("language") not in ALLOWED_LANGUAGES:
            issues.append(f"row {row_number}: unsupported language '{row.get('language')}'")

        if row.get("consent_status") not in ALLOWED_CONSENT:
            issues.append(f"row {row_number}: eligibility value '{row.get('consent_status')}' is not approved for this example")

    print("Synthetic Collection Validation")
    print("=" * 32)
    print(f"Rows checked: {len(rows)}")
    print(f"Validation issues: {len(issues)}")

    if issues:
        for issue in issues:
            print(f"- {issue}")
    else:
        print("Result: PASS — all example records satisfy the documented schema.")

if __name__ == "__main__":
    main()

"""Provide a concise, recruiter-friendly profile of synthetic quality data."""
from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent / "sample_analysis_data.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)
    print("Synthetic Dataset Analysis")
    print("=" * 26)
    print(f"Record count: {len(data)}")
    print(f"Duplicate full rows: {data.duplicated().sum()}")
    print("\nCategory distribution:")
    print(data["category"].value_counts().to_string())
    print("\nMissing values by field:")
    print(data.isna().sum().to_string())
    print("\nScore statistics:")
    print(data["score"].describe().round(2).to_string())
    approved_rate = (data["review_status"] == "approved").mean() * 100
    complete_rate = (1 - data.isna().any(axis=1).mean()) * 100
    print(f"\nApproved-status rate: {approved_rate:.1f}%")
    print(f"Complete-record rate: {complete_rate:.1f}%")


if __name__ == "__main__":
    main()

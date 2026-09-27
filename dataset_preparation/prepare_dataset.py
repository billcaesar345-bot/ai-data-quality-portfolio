"""Prepare synthetic feedback examples for a reproducible modeling workflow."""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
INPUT = BASE_DIR / "sample_input_data.csv"
OUTPUT = BASE_DIR / "prepared_dataset.csv"
VALID_LABELS = {"positive", "neutral", "negative"}


def main() -> None:
    data = pd.read_csv(INPUT, dtype=str)
    required = {"example_id", "text", "label", "confidence", "source"}
    missing_columns = required - set(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    data["label"] = data["label"].str.strip().str.lower()
    data["source"] = data["source"].str.strip().str.lower()
    data["confidence"] = pd.to_numeric(data["confidence"], errors="coerce")
    required_text = data[["example_id", "text", "label", "source"]].apply(lambda column: column.str.strip().ne(""))
    complete = data[["example_id", "text", "label", "source"]].notna().all(axis=1) & required_text.all(axis=1)
    valid = complete & data["label"].isin(VALID_LABELS) & data["confidence"].between(0, 1)
    prepared = data.loc[valid].drop_duplicates(subset=["example_id"], keep="first").copy()

    # Deterministic split labels make the preparation run reproducible.
    split_names = ["train", "validation", "test"]
    prepared = prepared.sample(frac=1, random_state=42).reset_index(drop=True)
    prepared["split"] = [split_names[index % 3] for index in range(len(prepared))]
    prepared.to_csv(OUTPUT, index=False)

    print(f"Input rows: {len(data)}")
    print(f"Accepted unique rows: {len(prepared)}")
    print("Feature: text | Target: label")
    print(f"Wrote: {OUTPUT.name}")


if __name__ == "__main__":
    main()

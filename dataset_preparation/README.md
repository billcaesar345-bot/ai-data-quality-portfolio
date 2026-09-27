# AI Training Dataset Preparation

This independent demonstration prepares synthetic feedback data for machine-learning or AI experimentation. It does **not** claim that the result trained a production AI model.

## What the Script Demonstrates
- Schema validation against [dataset schema](dataset_schema.md)
- Missing-value handling and rejection of incomplete records
- Lowercase label standardization using an approved taxonomy
- Duplicate detection by record identifier
- Invalid confidence-value handling
- Feature/target separation (`text` as feature; `label` as target)
- Reproducible processing through `random_state=42`

## Run
```bash
python prepare_dataset.py
```

The script reads [`sample_input_data.csv`](sample_input_data.csv) and writes `prepared_dataset.csv`, a local generated artifact ignored by Git.

For reviewers who do not want to run Python, [`prepared_dataset_example.csv`](prepared_dataset_example.csv) shows the expected structure of the prepared output. It is a static portfolio example, not a production training dataset.

## Splitting for Evaluation
The script assigns accepted examples to `train`, `validation`, and `test` labels deterministically to demonstrate the workflow. This is intentionally a simple portfolio demonstration, not a production splitting strategy. In a real dataset, split sizes and stratification should be chosen based on volume and label distribution; duplicate or related records must not cross splits; and leakage risks should be reviewed before evaluation. Follow the [preparation checklist](preparation_checklist.md) before using data in an experiment.

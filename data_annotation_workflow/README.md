# Data Annotation & Labeling Workflow

This independent, synthetic sentiment-classification example demonstrates how clear instructions support consistent AI training labels. It is not production or client annotation work.

## Task
Assign each feedback message one controlled sentiment label: `positive`, `neutral`, or `negative`.

## Workflow
1. Confirm that each record has usable text and a unique annotation ID.
2. Apply the definitions and rules in [annotation guidelines](annotation_guidelines.md).
3. Store the selected label and review status in [sample annotations](sample_annotations.csv).
4. Send ambiguous, mixed, sarcastic, or context-poor examples to review rather than guessing.
5. Have a reviewer check taxonomy compliance, text-label alignment, and flagged records.
6. Resolve disagreements against the written rules and document any guideline improvement.

## Reviewer Check
Run:

```bash
python reviewer_check.py
```

The check verifies that each example has usable text, an approved sentiment label, and a valid review status. Records marked `needs_review` are explicitly surfaced for human review rather than being silently treated as final annotations.

The guidelines cover task definition, label definitions, annotation rules, ambiguous cases, edge cases, examples, reviewer checks, and disagreement handling. No production annotation metrics are claimed.

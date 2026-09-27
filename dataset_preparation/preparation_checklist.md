# Dataset Preparation Checklist

- [ ] Confirm the task, permitted data use, and schema.
- [ ] Validate required columns and unique record identifiers.
- [ ] Check missing required values and route unsafe records out of the accepted set.
- [ ] Standardize labels against the controlled taxonomy.
- [ ] Detect exact duplicates before splitting data.
- [ ] Convert numeric fields and reject out-of-range values.
- [ ] Preserve source/provenance fields for auditability.
- [ ] Separate features from the target label.
- [ ] Use a reproducible random seed for train/validation/test assignment.
- [ ] Review split balance and document exclusions and limitations.

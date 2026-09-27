# Dataset Schema

| Field | Role | Validation |
| --- | --- | --- |
| `example_id` | Record identifier | Required and unique |
| `text` | Feature | Required, non-empty feedback text |
| `label` | Target | One of `positive`, `neutral`, `negative`; normalized to lowercase |
| `confidence` | Quality metadata | Numeric value from 0 through 1 |
| `source` | Provenance metadata | Required normalized source name |

The prepared modeling table uses `text` as the feature and `label` as the target. Confidence and source remain available for audit and quality review but are not treated as model targets.

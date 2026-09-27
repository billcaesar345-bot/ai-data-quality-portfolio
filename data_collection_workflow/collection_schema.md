# Collection Schema

All fields below are demonstrated with synthetic/example records only.

| Field | Type | Required | Validation rule | Purpose |
| --- | --- | --- | --- | --- |
| `collection_id` | string | Yes | Unique, non-empty identifier | Traceability and deduplication |
| `source_name` | string | Yes | Normalized source name | Source context |
| `source_url` | string | Yes | Well-formed approved source URL | Provenance reference |
| `collected_date` | date | Yes | ISO `YYYY-MM-DD` | Collection audit trail |
| `content` | string | Yes | Non-empty, appropriate text | Candidate training content |
| `language` | string | Yes | Controlled language code | Language routing |
| `consent_status` | string | Yes | Approved controlled value | Collection eligibility |

Do not collect private, confidential, restricted, or unapproved content. Document source permissions and applicable policies before collection.

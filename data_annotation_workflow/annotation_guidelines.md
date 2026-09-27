# Sentiment Annotation Guidelines

## Task Definition
Assign one label to each synthetic feedback message based on the overall sentiment expressed about the product or experience.

## Label Definitions
| Label | Use when | Example |
| --- | --- | --- |
| `positive` | The message expresses satisfaction, praise, or a favorable outcome. | “Love the new search feature.” |
| `neutral` | The message is factual, mixed without a clear overall direction, or lacks evaluative sentiment. | “It works as described.” |
| `negative` | The message expresses dissatisfaction, failure, frustration, or an unfavorable outcome. | “I cannot log in after the update.” |

## Annotation Rules
1. Label the sentiment of the whole message, not an isolated word.
2. Use the writer's stated experience; do not infer an intent or cause not in the text.
3. Choose `neutral` for a factual statement without clear approval or disapproval.
4. For mixed sentiment, select the dominant overall sentiment. If no sentiment dominates, select `neutral` and flag for review.
5. Preserve the original text exactly; labels may be normalized but the source wording should not be rewritten.

## Ambiguous and Edge Cases
- **Polite complaint:** “Please fix the slow loading.” is `negative` because the requested fix signals dissatisfaction.
- **Faint praise:** “It is okay.” is `neutral` unless context makes approval clearly stronger.
- **Sarcasm or unclear context:** Do not guess. Flag the record for reviewer review.
- **Multiple topics:** Label the overall experience; flag an evenly mixed message.
- **No usable sentiment:** Empty, unreadable, or off-topic text is not annotated and is routed for data-quality review.

## Quality-Control Process
- Annotators use this guide and the controlled three-label taxonomy.
- A reviewer checks required fields, label validity, text-label alignment, and records marked `needs_review`.
- A small overlap sample can be independently labeled to surface guideline ambiguity; this demonstration does not claim production metrics.
- Guideline updates are documented and communicated before applying them to new batches.

## Disagreement Handling
1. Compare the text and the applicable guideline rule.
2. Discuss the interpretation without changing the original record.
3. Escalate unresolved cases to a designated reviewer.
4. Record the final decision and rationale, then update the guideline if the case reveals a gap.

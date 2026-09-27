# Data Analysis & Quality Report

This independent demonstration uses a small [synthetic dataset](sample_analysis_data.csv) to turn data profiling into an understandable quality summary for a non-programming audience.

## Analysis Included
- Descriptive statistics for numeric scores
- Total record count
- Category distributions
- Missing-value analysis
- Exact duplicate analysis
- Basic completeness and review-status quality metrics

Read the recruiter-friendly [analysis report](analysis_report.md), or reproduce it with:

```bash
python analysis.py
```

The analysis intentionally surfaces a missing score and an exact duplicate so that quality findings are visible rather than hidden.

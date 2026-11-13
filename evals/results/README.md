# Evaluation result records

Place one JSON evaluation-result record per behavioural case in this directory (subdirectories are supported).

The Tier 1 result-integrity validator requires this directory to exist. An existing directory with zero JSON records is valid and means that no evaluation runs have been recorded yet; it does **not** mean that any AI-agent behaviour has been evaluated.

Run the validator with:

```bash
python evals/validate_results.py
```

See [the evaluation guide](../README.md) and [the result schema](../schemas/evaluation-result.schema.json) before adding records.

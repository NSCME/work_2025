test:
    pytest tests/ -v

validate:
    python -m "expectations.loan_app_expectations"

run_pipeline:
    python -m data_pipeline.batch.batch_etl_beam

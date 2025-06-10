from great_expectations.core import ExpectationSuite, ExpectationConfiguration

def build_suite() -> ExpectationSuite:
    suite = ExpectationSuite(name="loan_app_suite")

    # Schema validation
    suite.add_expectation(ExpectationConfiguration(
        expectation_type="expect_column_to_exist",
        kwargs={"column": "credit_score"}
    ))

    # Value bounds
    suite.add_expectation(ExpectationConfiguration(
        expectation_type="expect_column_values_to_be_between",
        kwargs={"column": "credit_score", "min_value": 300, "max_value": 850}
    ))

    # Non-null check
    suite.add_expectation(ExpectationConfiguration(
        expectation_type="expect_column_values_to_not_be_null",
        kwargs={"column": "application_id"}
    ))
    return suite

from expectations.loan_app_expectations import build_suite

def test_expectations():
    suite = build_suite()
    assert "expect_column_to_exist" in [e.expectation_type for e in suite.expectations]

def test_validation_failure():
    bad_data = {"credit_score": 200}  # Below min
    with pytest.raises(ValueError):
        validate_data(bad_data)

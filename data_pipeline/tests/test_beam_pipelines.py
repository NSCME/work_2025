import pytest
import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to

def test_high_risk_filter():
    test_data = [
        {"credit_score": 500, "application_id": "app1"},
        {"credit_score": 700, "application_id": "app2"}
    ]

    with TestPipeline() as p:
        output = (
            p
            | beam.Create(test_data)
            | beam.Filter(lambda app: app["credit_score"] < 600)
        )
        assert_that(output, equal_to([test_data[0]]))  # Only first app is high-risk

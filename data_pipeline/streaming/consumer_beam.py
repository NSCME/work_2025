import apache_beam as beam  
from apache_beam.options.pipeline_options import PipelineOptions  

def run_pipeline():  
    options = PipelineOptions(  
        streaming=True,  
        runner="DirectRunner"  # Replace with DataflowRunner for GCP  
    )  

    with beam.Pipeline(options=options) as p:  
        (  
            p  
            | "Read from Kafka" >> beam.io.ReadFromKafka(  
                consumer_config={"bootstrap.servers": "localhost:9092"},  
                topics=["loan_applications"]  
            )  
            | "Extract Values" >> beam.Map(lambda x: x[1])  # Get JSON payload  
            | "Parse JSON" >> beam.Map(json.loads)  
            | "Filter High Risk" >> beam.Filter(  
                lambda app: app["credit_score"] < 600  
            )  
            | "Write to BigQuery" >> beam.io.WriteToBigQuery(  
                table="loan_data.high_risk_applications",  
                schema="application_id:STRING, applicant_income:INTEGER, ...",  
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,  
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND  
            )  
        )  

if __name__ == "__main__":  
    run_pipeline()  

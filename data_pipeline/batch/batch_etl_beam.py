def run_batch_pipeline():  
    options = PipelineOptions(  
        runner="DirectRunner",  
        temp_location="gs://your-bucket/tmp"  # GCS path for Dataflow  
    )  

    with beam.Pipeline(options=options) as p:  
        (  
            p  
            | "Read from GCS" >> beam.io.ReadFromText("gs://loan_data_bucket/raw/*.json")  
            | "Parse JSON" >> beam.Map(json.loads)  
            | "Calculate Debt-to-Income" >> beam.Map(  
                lambda app: {  
                    **app,  
                    "dti_ratio": app["loan_amount"] / app["applicant_income"]  
                }  
            )  
            | "Write to BigQuery" >> beam.io.WriteToBigQuery(  
                table="loan_data.applications_with_dti",  
                schema="application_id:STRING, dti_ratio:FLOAT, ...",  
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE  
            )  
        )  

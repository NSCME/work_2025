from kafka import KafkaProducer  
import json  
import random  

producer = KafkaProducer(  
    bootstrap_servers="localhost:9092",  
    value_serializer=lambda v: json.dumps(v).encode("utf-8")  
)  

loan_apps = [  
    {  
        "application_id": f"app_{i}",  
        "applicant_income": random.randint(30_000, 200_000),  
        "loan_amount": random.randint(10_000, 1_000_000),  
        "credit_score": random.randint(300, 850),  
        "status": random.choice(["pending", "approved", "rejected"])  
    }  
    for i in range(100)  
]  

for app in loan_apps:  
    producer.send("loan_applications", app)  
producer.flush()  

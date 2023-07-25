from kafka import KafkaProducer
import csv
import time
import json


def writeData(file_name,kafka_topic,kafka_broker):

    producer = KafkaProducer(bootstrap_servers=kafka_broker)
    
    with open(file_name,'r',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = next(reader)  # Skip the header row if it exists
        for row in reader:
            try:
                row["UnitPrice"] = float(row["UnitPrice"])
                row["Quantity"] = int(row["Quantity"])
                data = json.dumps(row)
                producer.send(kafka_topic, data.encode('utf-8'))
                producer.flush()
                print("Message :",data[:20]+"...")
                time.sleep(1)
            except Exception as e:
                print("Error:", e)
        
    producer.close()


if __name__ == '__main__':

    kafka_topic = "orders"
    kafka_broker = "kafka-svc:9092"
    
    inputFile = "data.csv"
    writeData(inputFile,kafka_topic,kafka_broker)








# while True:
#     message = fake.text() 
#     print("Message: ", message[:20])
#     try:
#         producer.send(kafka_topic, message.encode("utf-8"))
#     except Exception as e:
#         print("Error:", e)  
#     time.sleep(1)


# # Close the producer
# producer.close()

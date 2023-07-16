from kafka import KafkaProducer
from faker import Faker
import time

# Configure Kafka producer
kafka_topic = "topic1"
kafka_broker = "kafka-svc:9092"
producer = KafkaProducer(bootstrap_servers=kafka_broker)

# Publish a message
# message = "Hello, Kafka!"
# producer.send(kafka_topic, message.encode("utf-8"))


fake = Faker()
while True:
    message = fake.name()
    producer.send(kafka_topic, message.encode("utf-8"))
    time.sleep(1)


# Close the producer
producer.close()

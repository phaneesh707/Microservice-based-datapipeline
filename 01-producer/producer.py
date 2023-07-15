from kafka import KafkaProducer

# Configure Kafka producer
kafka_topic = "topic1"
kafka_broker = "kafka-svc:9092"
producer = KafkaProducer(bootstrap_servers=kafka_broker)

# Publish a message
message = "Hello, Kafka!"
producer.send(kafka_topic, message.encode("utf-8"))

# Close the producer
producer.close()

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType

KAFKA_TOPIC = "orders"
KAFKA_BROKER = "kafka-svc:9092"

spark = SparkSession.builder.appName("test").getOrCreate()
spark.sparkContext.setLogLevel("WARN")


schema = StructType([
    StructField("OrderId", StringType()),
    StructField("CustomerId", StringType()),
    StructField("ProductId", StringType()),
    StructField("UnitPrice", DoubleType()),
    StructField("Quantity", IntegerType()),
    StructField("OrderDate", DateType()),
    StructField("Category", StringType()),
    StructField("City", StringType())
])

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BROKER) \
    .option("subscribe", KAFKA_TOPIC) \
    .option("startingOffsets", "latest") \
    .load()

row = df.selectExpr("CAST(value AS STRING)")

parsed_row = row.select(from_json(col("value"), schema).alias("data")).select("data.*")

# analysis
category_count = parsed_row.groupBy("Category").count()
total_quantity = parsed_row.groupBy("Category").sum("Quantity")
total_price = parsed_row.groupBy("Category").sum("UnitPrice")
max_order_city = parsed_row.groupBy("Category").agg({"City": "max"})




query = category_count.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()





# from kafka import KafkaConsumer

# # Configure Kafka consumer
# kafka_topic = "topic1"
# kafka_broker = "kafka-svc:9092"
# consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_broker)

# # Consume messages from Kafka
# for message in consumer:
#     print(message.value.decode("utf-8"))








# from pyspark import SparkContext
# from pyspark.streaming import StreamingContext
# from pyspark.streaming.kafka import KafkaUtils

# # Set up Spark context and streaming context
# sc = SparkContext(appName="DataPipeline")
# ssc = StreamingContext(sc, 1)

# # Define Kafka topic and broker details
# kafka_topic = "data-topic"
# kafka_broker = "10.96.74.32:9092"

# # Create a Kafka direct stream
# kafka_stream = KafkaUtils.createDirectStream(ssc, [kafka_topic], {"metadata.broker.list": kafka_broker})

# # Perform word count transformation
# word_counts = kafka_stream.flatMap(lambda x: x[1].split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# # Print the word counts
# word_counts.pprint()

# # Start the streaming context
# ssc.start()
# ssc.awaitTermination()

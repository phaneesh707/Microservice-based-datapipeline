from pyspark.sql import SparkSession

KAFKA_TOPIC = "topic1"
KAFKA_BROKER = "kafka-svc:9092"

spark = SparkSession.builder.appName("test").getOrCreate()

spark.sparkContext.setLogLevel("WARN")


df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers",KAFKA_BROKER) \
    .option("subsribe",KAFKA_TOPIC) \
    .option("startingOffsets","earliest") \
    .load()


words = df.select(
   explode(
       split(df.value, " ")
   ).alias("word")
)

# Generate running word count
wordCounts = words.groupBy("word").count()


query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
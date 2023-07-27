from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col ,split
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType
import psycopg2

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

# Assuming the value column contains the JSON data
parsed_row = df.selectExpr("CAST(value AS STRING)")
parsed_row = parsed_row.select(from_json(col("value"), schema).alias("data")).select("data.*")


def get_db_connection():
    db_host = "postgres-svc"  
    db_port = "5432"           
    db_name = "user"     
    db_user = "user"         
    db_password = "password" 

    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )
    return connection




def insert_into_orders_table(batch_df, batch_id):
    try:
        with get_db_connection() as connection, connection.cursor() as cursor:
            for row in batch_df.rdd.collect():
                order_id = row["OrderId"]
                customer_id = row["CustomerId"]
                product_id = row["ProductId"]
                unit_price = row["UnitPrice"]
                quantity = row["Quantity"]
                order_date = row["OrderDate"]
                category = row["Category"]
                city = row["City"]

                insert_query = "INSERT INTO orders (OrderId, CustomerId, ProductId, UnitPrice, Quantity, OrderDate, Category, City) " \
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(insert_query, (order_id, customer_id, product_id, unit_price, quantity, order_date, category, city))
                connection.commit()
                print(f"orderId written to DB: {order_id}")
    except Exception as e:
        print(f"Error inserting data into the database: {e}")


# Start the streaming
write_query = parsed_row.writeStream \
    .foreachBatch(insert_into_orders_table) \
    .start()


write_query.awaitTermination()

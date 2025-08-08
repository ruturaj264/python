from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window 

spark= SparkSession.builder.appName('ECOM').getOrCreate()

customers = spark.read.csv('/Volumes/mycatalog/myschema/ecom_db/customers.csv', header = True, inferSchema = True)
order_items = spark.read.csv('/Volumes/mycatalog/myschema/ecom_db/order_items.csv', header = True, inferSchema = True)
orders = spark.read.csv('/Volumes/mycatalog/myschema/ecom_db/orders.csv', header = True, inferSchema = True)
payments = spark.read.csv('/Volumes/mycatalog/myschema/ecom_db/payments.csv', header = True, inferSchema = True)
product_reviews = spark.read.csv('/Volumes/mycatalog/myschema/ecom_db/product_reviews.csv', header = True, inferSchema = True)
products = spark.read.csv('/Volumes/mycatalog/myschema/ecom_db/products.csv', header = True, inferSchema = True)
df = spark.read.csv('/Volumes/mycatalog/myschema/ecom_db/products.csv', header = True, inferSchema = True)

def display():
    pass
small_df = spark.read.csv('/Volumes/mycatalog/myschema/ecom_db/products.csv', header = True, inferSchema = True)
large_df = spark.read.csv('/Volumes/mycatalog/myschema/ecom_db/products.csv', header = True, inferSchema = True)


from pyspark.sql.functions import broadcast

# Join large_df with small_df using broadcast join
result = large_df.join(broadcast(small_df), on="id", how="inner")

spark.conf.get("spark.sql.autoBroadcastJoinThreshold")

spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 20 * 1024 * 1024)  # 20MB

spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)  # disable it

df = spark.read.csv("data.csv")

df.groupBy("country").count()

df2 = df.repartition(4)
df2 = df.repartition("country")  # rows with same country → same partition

df = df.repartition(4)

print('abcd')






































































































































































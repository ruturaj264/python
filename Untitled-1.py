# %%
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window as w
import datetime

spark = SparkSession.builder.appName("Question_bank").getOrCreate()

# Sample data
data = [
    (1, 'P100', 'Electronics', 2, 500.0, datetime.date(2023, 5, 1)),
    (2, 'P101', 'Clothing', 3, 30.0, datetime.date(2023, 5, 2)),
    (3, 'P102', 'Electronics', 1, 300.0, datetime.date(2023, 5, 3)),
    (4, 'P103', 'Home', 5, 20.0, datetime.date(2023, 5, 4)),
    (5, 'P100', 'Electronics', 4, 500.0, datetime.date(2023, 5, 5)),
    (6, 'P104', 'Clothing', 2, 50.0, datetime.date(2023, 5, 6)),
    (7, 'P105', 'Electronics', 1, 150.0, datetime.date(2023, 5, 7)),
]

# Define schema
schema = StructType([
    StructField("order_id", IntegerType(), True),
    StructField("product_id", StringType(), True),
    StructField("category", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", FloatType(), True),
    StructField("order_date", DateType(), True)
])

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show the DataFrame
df.display()

# %% [markdown]
# ## Questions

# %%
# Beginner Level Questions

# 1. How can you select specific columns from a DataFrame?

# df.select()

# 2. How can you filter rows based on a column value?

# df.where(col('col_name') condition)
# df.filter(col('col_name') condition)

# 3. How can you sort a DataFrame by a column in ascending order?

# df.orderBy(col('col_name'))

# 4. How can you filter rows where `age` is greater than 30?

# df.where('age > 30')
# df.where(col('age') > 30)
# df.where(df.age > 30)

# df.filter('age > 30')
# df.filter(col('age') > 30)
# df.filter(df.age > 30)

# 5. How can you select rows where `category` is 'Electronics'?

df.where('category == "Electronics"').display()
# df.where(col('category') == "Electronics").display()
# df.where(df.category == "Electronics").display()

# df.filter('category == "Electronics"').display()
# df.filter(col('category') == "Electronics").display()
# df.filter(df.category == "Electronics").display()

# 6. How can you rename a column in a DataFrame?

# df.withColumnRenamed('old_column', 'new_column')

# 7. How can you create a new column by performing an arithmetic operation?

# df.withColumn('new_column', col('col_1') + col('col_2'))

# 8. How can you drop a column from a DataFrame?

# df.drop('col_name')

# 9. How can you get the distinct values of a column?

df.select('col_name').distinct().display()

# 10. How can you get the first 5 rows of the DataFrame?

df.limit(5).display()

# 3. Intermediate Level Questions

# 11. How can you calculate the total sales by multiplying `quantity` and `price` for each row?

df.withColumn('total_sales', col('quantity') * col('price')).display()

# 12. How can you calculate the average price for each product category?

df.groupBy('category').agg(avg('price').alias('avg_price')).display()

# 13. How can you calculate the total sales (sum of `quantity * price`) for each category?

df.groupBy('category').agg(sum(col('quantity') * col('price')).alias('total_sales')).display()

# 14. How can you perform an inner join between two DataFrames on `product_id`?

# df1.join(df2, on = 'product_id')
# df1.join(df2, df1.product_id == df2.product_id)

# 15. How can you group by `category` and count the number of orders in each category?

df.groupBy('category').agg(count('*').alias('totaal_orders')).display()

# 16. How can you calculate the maximum price of products per category?

df.groupBy('category').agg(max('price').alias('max_price')).display()

# 17. How can you filter rows where `price` is greater than 500?

df.where('price > 500').display()
# df.where(col('price') > 500).display()
# df.where(df.price > 500).display()

# df.filter('price > 500').display()
# df.filter(col('price') > 500).display()
# df.filter(df.price > 500).display()

# 18. How can you use `select()` to select multiple columns?

# df.select('col_1', 'col_2')

# 19. How can you create a new DataFrame that contains only the rows where `price` is not null?

new_df = df.where('price is not null')
# new_df = df.where(col('price').isNotNull())
# new_df = df.where(df.price.isNotNull())

# new_df = df.filter('price is not null')
# new_df = df.filter(col('price').isNotNull())
# new_df = df.filter(df.price.isNotNull())

# 20. How can you sort the DataFrame by `total_sales` in descending order?

df.orderBy(desc(col('quantity') * col('price'))).display()

# 4. Advanced Level Questions

# 21. How can you assign a row number to each row within a partition sorted by `order_date` in descending order?

df.withColumn('row_number', row_number().over(w.partitionBy('category').orderBy(desc('order_date')))).display()

# 22. How can you calculate the rank of each row within a category based on `total_sales`?

df.withColumn('rank', rank().over(w.partitionBy('category').orderBy(col('price') * col('quantity')))).display()

# 23. How can you get the previous row's `price` value using the `lag()` window function?

df.withColumn('prev_price', lag('price').over(w.orderBy('price'))).display()

# 24. How can you get the next row's `price` value using the `lead()` window function?

df.withColumn('next_price', lead('price').over(w.orderBy('price'))).display()

# 25. How can you pivot the data to show the sum of `total_sales` for each category per month?

df.withColumn('month', month('order_date'))\
  .groupBy('category', 'month')\
  .agg(sum(col('price') * col('quantity')).alias('total_sales'))\
  .display()

# 26. How can you calculate the cumulative sum of `total_sales` ordered by `order_date`?

df.withColumn('cumulative_sum', sum(col('price') * col('quantity')).over(w.orderBy('order_date'))).display()

# 27. How can you calculate the difference between `total_sales` of the current row and the previous row?

df.withColumn('total_sales', col('price') * col('quantity'))\
  .withColumn('prev_total_sales', lag('total_sales', 1, 0).over(w.orderBy('total_sales')))\
  .withColumn('difference', col('total_sales') - col('prev_total_sales'))\
  .display()

# 28. How can you repartition the DataFrame by `category` and perform an aggregation?

df.repartition('category')\
  .groupBy('category')\
  .agg(count('*').alias('total_orders'))\
  .display()

# 29. How can you join two DataFrames (`df1` and `df2`) on `product_id` using a left join?

# df1.join(df2, on = 'product_id', how = 'left')
# df1.join(df2, df1.product_id == df2.product_id, 'left')

# 30. How can you use `withColumn()` to convert the `price` column to a different data type (e.g., integer)?

df.withColumn('price', col('price').cast(IntegerType())).display()

# 5. Window Functions & Aggregations

# 31. How can you use the `row_number()` function to assign a unique number to each row within a partition, ordered by `order_date`?

df.withColumn('row_number', row_number().over(w.partitionBy('category').orderBy('order_date'))).display()

# 32. How can you calculate the rank of `total_sales` within each `category` and handle ties with the `dense_rank()` function?

df.withColumn('rank', dense_rank().over(w.partitionBy('category').orderBy(col('price') * col('quantity')))).display()

# 33. How can you calculate the moving average of `total_sales` over the last 3 months?

df.withColumn('year_month', date_format('order_date', 'yyyy-MM'))\
  .groupBy('year_month')\
  .agg(avg(col('price') * col('quantity')).alias('avg_sales'))\
  .withColumn('moving_avg', avg('avg_sales').over(w.orderBy('year_month').rowsBetween(-3, 0)))\
  .display()

# 34. How can you get the first and last `price` for each `category` using window functions?

df.withColumn('first_price', first('price').over(w.partitionBy('category')))\
  .withColumn('last_price', last('price').over(w.partitionBy('category')))\
  .groupBy('category')\
  .agg(max('first_price').alias('first_price'), max('last_price').alias('last_price'))\
  .display()

# 35. How can you compute the percent rank of each row based on `total_sales`?

df.withColumn('precent_rank', percent_rank().over(w.orderBy(col('price') * col('quantity')))).display()

# 36. How can you compute the lead function to get the next `price` value for each `category`?

df.withColumn('next_price', lead('price').over(w.partitionBy('category').orderBy('price'))).display()

# 37. How can you partition data by `category` and get the average sales of each partition using window functions?

df.withColumn('average_cat_sales', avg(col('price') * col('quantity')).over(w.partitionBy('category'))).display()

# 38. How can you perform a self-join to match orders from the same `category`?

df.alias('a').join(df.alias('b'), col('a.category') == col('b.category'), 'inner').display()

# 39. How can you compute the first value of `total_sales` for each partition using a window function?

df.withColumn('first_cat_total_sales', first(col('price') * col('quantity')).over(w.partitionBy('category'))).display()

# 40. How can you get the last value of `total_sales` for each partition using a window function?

df.withColumn('first_cat_total_sales', last(col('price') * col('quantity')).over(w.partitionBy('category'))).display()

# 6. Joins and Transformations

# 41. How can you perform an outer join between two DataFrames (`df1` and `df2`) on the `product_id` column?

# df1.join(df2, df1.product_id == df2.product_id, "outer")

# 42. How can you filter rows in a DataFrame based on a condition from another DataFrame using join()?

# df1.join(df2, df1.product_id == df2.product_id).where(df1.product_id > 5)

# 43. How can you merge two DataFrames (`df1` and `df2`) using a full outer join?

# df1.join(df2, df1.product_id == df2.product_id, "outer")

# 44. How can you apply a cross join between two DataFrames and explain its use case?

# df_cross = df1.crossJoin(df2)

# used to join two DataFrames without any common columns, which can be useful for creating pairs/combinations of rows from both DataFrames.

# 45. How can you use union() to combine two DataFrames with the same schema?

# df1.union(df2)

# 46. How can you compute the distinct values of a column after applying a filter?

df.where('price < 500').select('price').distinct().display()

# 47. How can you use coalesce() to reduce the number of partitions before writing data?

# df.coalesce(1).format('delta').mode("overwrite").save("path")

# 48. How can you calculate the variance of `price` for each `category` using an aggregation function?

df.groupBy('category').agg(variance('price').alias('variance')).display()

# 49. How can you compute the sum and count of orders for each `category` in one step?

df.groupBy('category')\
  .agg(sum(col('price') * col('quantity')).alias('total_sales'), count('order_id').alias('total_orders'))\
  .display()

# 50. How can you calculate the percentage of `total_sales` for each category relative to the total sales across all categories?

df.withColumn('total_sales_all', sum(col('price') * col('quantity'))\
                                 .over(w.rowsBetween(w.unboundedPreceding, w.unboundedFollowing)))\
  .groupBy('category')\
  .agg(round(sum(col('price') * col('quantity')) / max('total_sales_all'), 2).alias('percent_sales'))\
  .display()







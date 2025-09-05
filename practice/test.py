
# num = 13

# for i in range(2,num):

#     if num % i == 0:
#         print('not prime')
#         break
# else:
#     print('prime')


# mylist = [2,8,3,1,9]
# n = len(mylist)


# for i in range(n-1):

#     for j in range(i+1, n):

#         if mylist[i] > mylist[j]:
#             mylist[i], mylist[j] = mylist[j], mylist[i]

# print(mylist)

# my_list = [1,2,3,4,5,6]

# l = len(my_list)
# n = l // 2

# for i in range(n):

#     index1 = i
#     index2 = l - (i+1)

#     my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# print(my_list)



def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in word if ch in vowels)

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

count_vowels_udf = udf(count_vowels, IntegerType())

spark = SparkSession.builder.appName("UDF Example").getOrCreate()

data = [("apple",), ("banana",), ("grape",)]
df = spark.createDataFrame(data, ["word"])

df.withColumn("vowel_count", count_vowels_udf(col("word"))).show()


spark.udf.register("countVowels", count_vowels, IntegerType())
df.createOrReplaceTempView("words")

df = spark.read.csv("data.csv")
result = df.groupBy("city").count()
result.show()


from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, explode
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.conf import SparkConf

conf = SparkConf()
#conf.set("spark.jars", "jar_files/redshift-jdbc42-2.1.0.3.jar")
        #.config(conf=conf) \
        #.config("spark.driver.extraClassPath", "jar_files/redshift-jdbc42-2.1.0.3.jar") \
spark = SparkSession \
        .builder \
        .appName("test") \
        .getOrCreate()

"""
df = spark.read \
        .format("jdbc") \
        .option("url","jdbc:url") \
        .option("dbtable", "users") \
        .option("driver", "com.amazon.redshift.jdbc42.Driver") \
        .option("user", "awsuser") \
        .option("password", "password") \
        .load()
df.show()
"""
rdd = spark.sparkContext.parallelize([("abc",),("def",)]*100)

df = rdd.toDF(["dummy_str"])
df.show()

spark.stop()
"""
df.write \
        .format("jdbc") \
        .option("url","jdbc:url") \
        .option("dbtable", "public.test") \
        .option("driver", "com.amazon.redshift.jdbc42.Driver") \
        .option("user", "awsuser") \
        .option("password", "password") \
        .save()
"""

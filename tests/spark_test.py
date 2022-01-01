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

rdd = spark.sparkContext.parallelize([("abc",),("def",)]*10)

df = rdd.toDF(["dummy_str"])

df = df.write \
        .format("jdbc") \
        .option("url","jdbc:redshift://redshift-cluster-free-tier.cpwksln1mngr.us-west-2.redshift.amazonaws.com:5439/dev") \
        .option("dbtable", "public.test") \
        .option("driver", "com.amazon.redshift.jdbc42.Driver") \
        .option("user", "awsuser") \
        .option("password", "Gm2f!mP7nPmA&o") \
        .save(mode="append")
df.show()
"""
rdd = spark.sparkContext.parallelize([("abc",),("def",)])

df = rdd.toDF(["dummy_str"])
df.show()
df.write \
        .format("jdbc") \
        .option("url","jdbc:redshift://redshift-cluster-free-tier.cpwksln1mngr.us-west-2.redshift.amazonaws.com:5439/dev") \
        .option("dbtable", "public.test") \
        .option("driver", "com.amazon.redshift.jdbc42.Driver") \
        .option("user", "awsuser") \
        .option("password", "Gm2f!mP7nPmA&o") \
        .save()
"""

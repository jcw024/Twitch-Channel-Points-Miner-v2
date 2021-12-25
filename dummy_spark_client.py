#from pyspark import SparkContext
#from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .master("local[2]") \
        .appName("dummy_spark_server") \
        .getOrCreate()

lines = spark \
        .readStream \
        .format("socket") \
        .option("host", "localhost") \
        .option("port", 7778) \
        .load()


query = lines \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

query.awaitTermination()

"""

#sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 10)

data = ssc.socketTextStream("127.0.0.1",7778)
#data.foreachRDD(lambda x: )
data.pprint(10)

ssc.start()
ssc.awaitTermination()
"""

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "dummy_spark_server")
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 10)

data = ssc.socketTextStream("127.0.0.1",7778)
data.pprint(10)

ssc.start()
ssc.awaitTermination()

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, explode, decode
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType, LongType, BooleanType
import json
import pprint

#upload event_created.json to s3, have spark read schema from s3
#specify target database to write to in process_df
#set master?
#specify spark.format.option

def process_prediction_df(batch_df, batch_id):
    batch_df.printSchema()
    df = batch_df.select("json.data.*")
    df = df.select("decision", "prediction.channel_id", col("timestamp").alias("datetime"), "prediction.event_id", \
            "title_A", "title_B","odds_A","odds_B","pct_users_A","pct_users_B", "prediction.result.type","color_A","color_B")
    df.show()
    df.printSchema()
    df.write \
            .format("jdbc") \
            .option("url","jdbc:redshift://redshift-cluster-free-tier.cpwksln1mngr.us-west-2.redshift.amazonaws.com:5439/dev") \
            .option("dbtable", "public.pred_results") \
            .option("user", "awsuser") \
            .option("password", "Gm2f!mP7nPmA&o") \
            .option("startingOffset", "latest") \
            .save(mode="append")

def test(batch_df, batch_id):
    print("test execute")
    df = batch_df.select("value")
    df = df.withColumn("value_decoded", decode(df.value, "utf-8")).select("value_decoded")
    df.printSchema()
    df.show()
    return

spark = SparkSession.builder \
        .appName("spark_server") \
        .getOrCreate()

spark.sparkContext.setLogLevel('error')

bootstrap_server = "b-2.twitchminer1.4lmexb.c11.kafka.us-west-2.amazonaws.com:9092,b-1.twitchminer1.4lmexb.c11.kafka.us-west-2.amazonaws.com:9092"
subscribe = "predictionTopic"

#json_schema = spark.read.json("prediction_result.json").schema
json_schema = StructType([
    StructField("data",StructType([
        StructField("color_A",StringType(),True),
        StructField("color_B",StringType(),True),
        StructField("decision",StringType(),True),
        StructField("event_A",StringType(),True),
        StructField("event_B",StringType(),True),
        StructField("odds_A",DoubleType(),True),
        StructField("odds_B",DoubleType(),True),
        StructField("pct_users_A",DoubleType(),True),
        StructField("pct_users_B",DoubleType(),True),
        StructField("prediction",StructType([
            StructField("channel_id",StringType(),True),
            StructField("event_id",StringType(),True),
            StructField("id",StringType(),True),
            StructField("outcome_id",StringType(),True),
            StructField("points",LongType(),True),
            StructField("predicted_at",StringType(),True),
            StructField("result",StructType([
                StructField("is_acknowledged",BooleanType(),True),
                StructField("points_won",StringType(),True),
                StructField("type",StringType(),True)]),True),
            StructField("updated_at",StringType(),True),
            StructField("user_display_name",StringType(),True),
            StructField("user_id",StringType(),True)]),True),
            StructField("timestamp",TimestampType(),True),
            StructField("title_A",StringType(),True),
            StructField("title_B",StringType(),True)]),True),
        StructField("type",StringType(),True)])
"""
json_schema = StructType([ \
        StructField("data", StructType([ \
            StructField("decision",StringType(),True), \
            StructField("prediction", StructType([ \
                StructField("channel_id",DoubleType(),True), \
                StructField("event_id", StringType(),True),
                StructField("result", StructType([ \
                        StructField("type", StringType(),True) \
                        ]))
                    ])
                ),
            StructField("timestamp",TimestampType(),True), \
            StructField("title_A",StringType(),True), \
            StructField("title_B",StringType(),True), \
            StructField("odds_A",DoubleType(),True), \
            StructField("odds_B",DoubleType(),True), \
            StructField("pct_users_A",DoubleType(),True), \
            StructField("pct_users_B",DoubleType(),True), \
            StructField("type",StringType(),True), \
            StructField("color_A",StringType(),True), \
            StructField("color_B",StringType(),True)
            ])
        )])
"""
input_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", bootstrap_server) \
        .option("subscribe", subscribe) \
        .option("startingOffsets", "earliest") \
        .load()

query = input_df \
        .select("value") \
        .withColumn("value", decode(input_df.value, "utf-8")) \
        .withColumn('json', from_json(col('value'), json_schema)) \
        .writeStream.foreachBatch(process_prediction_df).start()
print("query started...")
query.awaitTermination()


"""

query = input_df \
        .select("value") \
        .withColumn("value", decode(df.value, "utf-8"))
        .withColumn('json', from_json(col('value'), json_schema)) \
        .select(col('json').alias('header')) \
        .writeStream \
        .foreachBatch(test) \
        .outputMode("append") \
        .start()

print("query started...")
query.awaitTermination()

"""

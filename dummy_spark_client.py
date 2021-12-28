from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, explode
import json

#upload event_created.json to s3, have spark read schema from s3
#specify target database to write to in process_df
#set master?
#specify spark.format.option

def process_prediction_df(batch_df, batch_id):
    df = batch_df.select("header.data.*")
    df = df.select("decision", "event.channel_id", "event.created_at", "event.id", 
            "event.title", "event.outcomes")
    df = df.withColumn("outcome_A", df.outcomes.getItem(0))
    df = df.withColumn("outcome_B", df.outcomes.getItem(1))
    df = df.select("decision", "channel_id", "created_at", "id", 
            "title", col("outcome_A.id").alias("outcome_id_A"), col("outcome_A.title").alias("outcome_title_A"),
            col("outcome_A.odds").alias("odds_A"), col("outcome_A.percentage_users").alias("pct_users_A"), 
            col("outcome_B.id").alias("outcome_id_B"), col("outcome_B.title").alias("outcome_title_B"),
            col("outcome_B.odds").alias("odds_B"), col("outcome_B.percentage_users").alias("pct_users_B")
            )

    df.show()
    df.printSchema()
    return

def process_result_df(batch_df, batch_id):
    df = batch_df.select("header.data.*")
    df = df.select("timestamp","color_A", "color_B","decision","odds_A","odds_B","pct_users_A","pct_users_B","title_A","title_B",
            "prediction.channel_id","prediction.event_id","prediction.result.type")
    df.show()
    df.printSchema()
    return

spark = SparkSession.builder \
        .master("local[3]") \
        .appName("dummy_spark_server") \
        .getOrCreate()

spark.sparkContext.setLogLevel('error')

input_df = spark \
        .readStream \
        .format("socket") \
        .option("host", "localhost") \
        .option("port", 7778) \
        .load()

json_schema = spark.read.json("prediction_result.json").schema

query = input_df \
        .withColumn('json', from_json(col('value'), json_schema)) \
        .select(col('json').alias('header')) \
        .writeStream \
        .foreachBatch(process_result_df) \
        .outputMode("append") \
        .start()

print("query started...")
query.awaitTermination()


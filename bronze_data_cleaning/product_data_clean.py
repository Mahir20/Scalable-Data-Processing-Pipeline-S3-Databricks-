# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

df_product = spark.read.table('project_04.bronze_layer_load.product')
display(df_product)

# COMMAND ----------

df_product = df_product.withColumn('price', col('price').cast('double'))
df_product = df_product.withColumn('is_active', col('is_active').cast('string'))

# COMMAND ----------

df_product = df_product.drop('ingestion_timestamp')
df_product = df_product.withColumn(
    "price",
    when(col("price") < 0, -col("price"))
    .when(col('price').isNull(), 0)
    .otherwise(col("price"))
)
df_product = df_product.withColumn(
    'is_active', when(col('is_active') == 'true', 'Active').otherwise('Inactive')
)

# COMMAND ----------

df_product.display()


# COMMAND ----------

df_product.write.mode('overwrite').saveAsTable('project_04.silver_layer_store_data.products')

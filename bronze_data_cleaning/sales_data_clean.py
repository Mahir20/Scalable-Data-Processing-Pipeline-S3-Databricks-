# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

df_sales = spark.read.table('project_04.bronze_layer_load.sales')
display(df_sales)

# COMMAND ----------

df_sales.printSchema()

# COMMAND ----------

df_sales = df_sales.withColumn(
    'store_id',col('store_id').cast('int')
)

# COMMAND ----------

df_sales = df_sales.filter(col("sale_id").isNotNull())
df_sales = df_sales.filter(col("store_id").isNotNull())

# COMMAND ----------

df_sales.write.mode('ignore').saveAsTable('project_04.silver_layer_store_data.sales')

# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

df_store = spark.read.table('project_04.bronze_layer_load.storedata')
display(df_store)

# COMMAND ----------

df_store.printSchema()

# COMMAND ----------

df_store = (df_store
    .withColumn('store_id', col('store_id').cast('int'))
    .withColumn('store_size',col('store_id').cast('int'))
)

# COMMAND ----------

df_store = df_store.filter(col('store_id').isNotNull())
df_store = df_store.fillna({'store_size': 0})

# COMMAND ----------

display(df_store)

# COMMAND ----------

df_store.write.mode('ignore').saveAsTable('project_04.silver_layer_store_data.store')

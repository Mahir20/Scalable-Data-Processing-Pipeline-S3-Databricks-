# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

df_store = spark.read.table('project_04.silver_layer_store_data.store')
df_
display(df_store)

# COMMAND ----------

df_store.createOrReplaceTempView('store')

# COMMAND ----------

# MAGIC %sql
# MAGIC -- stores exist per country
# MAGIC

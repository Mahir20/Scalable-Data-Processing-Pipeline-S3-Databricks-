# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

df_customer = spark.read.table('project_04.bronze_layer_load.customer')
display(df_customer)

# COMMAND ----------

df_customer = (df_customer
            .withColumn('age', col('age').cast('int'))
            .withColumn('customer_id', col('customer_id').cast('int'))
            .withColumn('total_purchases', col('total_purchases').cast('int'))
            .withColumn('registration_date', col('registration_date').cast('date'))
)

# COMMAND ----------

df_customer = df_customer.drop('ingestion_timestamp')
df_customer = df_customer.fillna({
    'email' : 'unknown'
})
df_customer = df_customer.withColumn(
    'age', when(col('age') < 0, 18).otherwise(col('age'))

)

# COMMAND ----------

display(df_customer)

# COMMAND ----------

df_customer.write.mode('ignore').saveAsTable('project_04.silver_layer_store_data.customer')

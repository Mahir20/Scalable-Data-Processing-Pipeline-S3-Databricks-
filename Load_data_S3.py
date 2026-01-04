# Databricks notebook source
# MAGIC %fs ls s3://customersales4/

# COMMAND ----------

df_customer = spark.read.csv('s3://customersales4/customer.csv', header=True, inferSchema=True)
df_product = spark.read.csv('s3://customersales4/product.json', header=True, inferSchema=True)
df_store_data = spark.read.csv('s3://customersales4/store_data.csv', header=True, inferSchema=True)

# COMMAND ----------

df_produst = spark.read.json('s3://customersales4/product.json')

# COMMAND ----------

df_customer.write.mode('ignore').saveAsTable('project_04.bronze_layer_load.customer')
df_product.write.mode('ignore').saveAsTable('project_04.bronze_layer_load.product')
df_sales_data.write.mode('ignore').saveAsTable('project_04.bronze_layer_load.sales')
df_store_data.write.mode('ignore').saveAsTable('project_04.bronze_layer_load.storedata')

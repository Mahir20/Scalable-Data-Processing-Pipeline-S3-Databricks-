# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

df_sales = spark.read.table('project_04.silver_layer_store_data.sales')
display(df_sales)

# COMMAND ----------

df_sales.createOrReplaceTempView('sale')

# COMMAND ----------

# MAGIC %sql
# MAGIC -- total sales transactions are recorded
# MAGIC select count(sale_id) as total_transactions
# MAGIC from sale

# COMMAND ----------

# MAGIC %sql
# MAGIC -- revenue generated per day
# MAGIC select sale_date, round(sum(quantity*total_amount), 2) as total
# MAGIC from sale
# MAGIC where sale_date is not null
# MAGIC group by sale_date
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- day has txest sales
# MAGIC select sale_date, round(sum(quantity*total_amount), 2) as total
# MAGIC from sale
# MAGIC where sale_date is not null
# MAGIC group by sale_date
# MAGIC order by total desc
# MAGIC limit 5

# COMMAND ----------

# MAGIC %sql
# MAGIC -- repeat purchases exist
# MAGIC select count(*) as total_repeat_purchases
# MAGIC from sale
# MAGIC group by sale_id
# MAGIC having count(*) > 1

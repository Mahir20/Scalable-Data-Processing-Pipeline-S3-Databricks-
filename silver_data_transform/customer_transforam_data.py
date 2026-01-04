# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

df_customer = spark.read.table('project_04.silver_layer_store_data.customer')
display(df_customer)

# COMMAND ----------

df_customer.createOrReplaceTempView('customer')

# COMMAND ----------

# MAGIC %sql
# MAGIC -- unique customers
# MAGIC select count(distinct(customer_id)) as customer_count
# MAGIC from customer

# COMMAND ----------

# MAGIC %sql
# MAGIC -- average age of customers
# MAGIC select avg(age) as avg_age
# MAGIC from customer;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- customers were created most recently
# MAGIC select registration_date, customer_id
# MAGIC from customer
# MAGIC where registration_date is not null
# MAGIC order by registration_date desc

# COMMAND ----------

# MAGIC %sql
# MAGIC -- customers have never made a purchase
# MAGIC select customer_id
# MAGIC from customer
# MAGIC where total_purchases = 0

# COMMAND ----------

# MAGIC %sql
# MAGIC -- customers fall into each age group
# MAGIC select customer_id, age,
# MAGIC   CASE
# MAGIC     WHEN age < 18 THEN 'under 18'
# MAGIC     WHEN age BETWEEN 18 AND 25 THEN '18-25'
# MAGIC     WHEN age BETWEEN 26 AND 35 THEN '26-35'
# MAGIC     WHEN age BETWEEN 36 AND 50 THEN '36-50'
# MAGIC     ELSE '50+'
# MAGIC   END AS age_group
# MAGIC from customer

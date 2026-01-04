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

%sql
# total sales transactions are recorded
select count(sale_id) as total_transactions
from sale

# COMMAND ----------

%sql
# revenue generated per day
select sale_date, round(sum(quantity*total_amount), 2) as total
from sale
where sale_date is not null
group by sale_date


# COMMAND ----------

%sql
# day has txest sales
select sale_date, round(sum(quantity*total_amount), 2) as total
from sale
where sale_date is not null
group by sale_date
order by total desc
 limit 5

# COMMAND ----------
 %sql
# repeat purchases exist
select count(*) as total_repeat_purchases
from sale
group by sale_id
having count(*) > 1

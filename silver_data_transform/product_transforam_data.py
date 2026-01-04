# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

df_product = spark.read.table('project_04.silver_layer_store_data.products')
df_product.display()

# COMMAND ----------

df_product.createOrReplaceTempView('product')

# COMMAND ----------

# MAGIC %sql
# MAGIC -- total products exist
# MAGIC select count(*) as total_product
# MAGIC from product
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- active vs inactive products
# MAGIC select is_active, count(product_id) as count_active_inactive
# MAGIC from product
# MAGIC group by is_active

# COMMAND ----------

# MAGIC %sql
# MAGIC -- average price per category
# MAGIC select category, round(avg(price),2) as avg_price
# MAGIC from product
# MAGIC group by category

# COMMAND ----------

# MAGIC %sql
# MAGIC -- products are out of stock or low in stock
# MAGIC select product_id,  
# MAGIC   case 
# MAGIC     when stock_quantity <= 0 then 'out_of_stock'
# MAGIC     when stock_quantity <= 50 then 'low_stock'
# MAGIC     else 'in_stock'
# MAGIC   end as stock_status
# MAGIC from product 
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select price 
# MAGIC from product
# MAGIC where price is null

# COMMAND ----------

# MAGIC %sql
# MAGIC -- distribution of products by price range?
# MAGIC select price_range, count(*) as count_price_range
# MAGIC from
# MAGIC (
# MAGIC     select case
# MAGIC         when price <= 100 then 'low_price'
# MAGIC         when price between 101 and 500 then 'medium_price'
# MAGIC         else 'high_price'
# MAGIC         end as price_range
# MAGIC     from product
# MAGIC ) t
# MAGIC group by price_range
# MAGIC order by price_range desc;

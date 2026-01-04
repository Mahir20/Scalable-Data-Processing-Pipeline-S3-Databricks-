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

%sql
# total products exist
select count(*) as total_product
 from product


# COMMAND ----------

 %sql
# active vs inactive products
select is_active, count(product_id) as count_active_inactive
from product
 group by is_active

# COMMAND ----------

 %sql
# average price per category
select category, round(avg(price),2) as avg_price
from product
group by category

# COMMAND ----------

 %sql
#products are out of stock or low in stock
 select product_id,  
   case 
     when stock_quantity <= 0 then 'out_of_stock'
     when stock_quantity <= 50 then 'low_stock'
     else 'in_stock'
   end as stock_status
 from product 


# COMMAND ----------

 %sql
 select price 
 from product
 where price is null

# COMMAND ----------

 %sql
# distribution of products by price range?
 select price_range, count(*) as count_price_range
 from
 (
     select case
         when price <= 100 then 'low_price'
         when price between 101 and 500 then 'medium_price'
         else 'high_price'
         end as price_range
     from product
 ) t
group by price_range
order by price_range desc;

# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

df_customer = spark.read.table('project_04.silver_layer_store_data.customer')
display(df_customer)



df_customer.createOrReplaceTempView('customer')



%sql
 MAGIC -- unique customers
select count(distinct(customer_id)) as customer_count
 from customer



%sql
MAGIC -- average age of customers
 MAGIC select avg(age) as avg_age
 from customer;

# COMMAND ----------

 %sql
#customers were created most recently
 select registration_date, customer_id
 from customer
 where registration_date is not null
 order by registration_date desc

# COMMAND ----------

%sql
# customers have never made a purchase
 select customer_id
 from customer
 where total_purchases = 0



%sql
# customers fall into each age group
 select customer_id, age,
   CASE
     WHEN age < 18 THEN 'under 18'
     WHEN age BETWEEN 18 AND 25 THEN '18-25'
     WHEN age BETWEEN 26 AND 35 THEN '26-35'
     WHEN age BETWEEN 36 AND 50 THEN '36-50'
     ELSE '50+'
   END AS age_group
 from customer

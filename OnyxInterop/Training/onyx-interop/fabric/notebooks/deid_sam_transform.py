# Fabric notebook (PySpark) — same de-id SAM contract as Databricks.
# Run only against Safe Harbor / tokenized tables. No identified PHI.

from pyspark.sql import functions as F

bronze = spark.read.format("delta").load("Files/onyx/deid/bronze")
silver = (
    bronze.filter(F.col("_deid_method") == "safe_harbor")
    .filter(F.col("member_golden_id").isNotNull())
)
silver.write.format("delta").mode("overwrite").save("Tables/deid_silver_sam")

gold = silver.groupBy("workflow_family").agg(F.count("*").alias("row_count"))
gold.write.format("delta").mode("overwrite").save("Tables/deid_gold_kpis")
print("Fabric de-id SAM transform complete")

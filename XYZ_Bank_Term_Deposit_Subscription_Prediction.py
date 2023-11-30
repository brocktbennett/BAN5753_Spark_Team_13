# Import libraries necessary for Mini Project 2
# Team 13
# Team Members: Isabella Lieberman, Brock Bennett, John Ramirez, Nathan Zlomke

# Import Findspark
import findspark
findspark.init()


# Setting log level to suppress WARN messages
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('MiniProject2').setMaster('local[*]')
conf.set("spark.hadoop.validateOutputSpecs", "false")
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql.functions import countDistinct
from pyspark.sql.functions import col, asc,desc
from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.sql.functions import avg
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pyspark.sql import SQLContext
from pyspark.mllib.stat import Statistics
import pandas as pd
from pyspark.sql.functions import udf
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler,StandardScaler
from pyspark.ml import Pipeline
from sklearn.metrics import confusion_matrix

# Initiate a Spark session for Mini Project 2
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("MiniProject2") \
    .getOrCreate()

# Set display options
pd.set_option('display.width', 1000, 'display.max_colwidth', 100, 'display.max_columns', None)

# Load the dataset with semicolon (;) as the delimiter
#xyz_bank_df = spark.read.option("delimiter", ";").csv("/Users/brocktbennett/GitHub/Project Data/mini_project_2/XYZ_Bank_Deposit_Data_Classification-2.csv", header=True, inferSchema=True)
# xyz_bank_df = spark.read.option("delimiter", ",").csv("/Users/brocktbennett/GitHub/Project Data/mini_project_2/KNN_input.csv", header=True, inferSchema=True)
xyz_bank_df = spark.read.parquet("/Users/brocktbennett/GitHub/Project Data/mini_project_2/_SUCCESS")
# Renaming columns to remove dots and replace them with underscores
# xyz_bank_df = xyz_bank_df \
#     .withColumnRenamed('emp.var.rate', 'emp_var_rate') \
#     .withColumnRenamed('cons.price.idx', 'cons_price_idx') \
#     .withColumnRenamed('cons.conf.idx', 'cons_conf_idx') \
#     .withColumnRenamed('nr.employed', 'nr_employed')

# Check to see how many rows and columns we received
num_rows = xyz_bank_df.count()
num_columns = len(xyz_bank_df.columns)
print(f"CSV file loaded successfully with {num_rows} rows and {num_columns} columns.\n")

# Display data types of each column
print("Data Types of Each Column:")
xyz_bank_df.printSchema()

# Show the first 25 rows of the DataFrame to verify the data is loaded correctly
xyz_bank_df.show(25)

# Assuming 'xyz_bank_df' has all necessary columns already transformed to numeric
numeric_cols = ['age', 'duration', 'campaign', 'previous', 'emp_var_rate', 'cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed']
# Make sure all these columns exist in your DataFrame and are of numeric type

# assembler = VectorAssembler(inputCols=numeric_cols, outputCol="features")
# xyz_bank_df = assembler.transform(xyz_bank_df)
xyz_bank_df.head(1)
# Rest of your code for KMeans and plotting

from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

evaluator = ClusteringEvaluator()

silhouette_scores = []
k_range = range(2, 10)  # Example range, can be adjusted

for k in k_range:
    kmeans = KMeans(featuresCol='features', k=k).setSeed(1)
    model = kmeans.fit(xyz_bank_df)
    predictions = model.transform(xyz_bank_df)
    silhouette = evaluator.evaluate(predictions)
    silhouette_scores.append(silhouette)

plt.figure(figsize=(8, 6))
plt.plot(k_range, silhouette_scores, marker='o')
plt.xlabel('Number of clusters k')
plt.ylabel('Silhouette Score')
plt.title('Elbow Plot for Optimal k')
plt.show()




# Assume you want to create 5 clusters
kmeans = KMeans(featuresCol='features', k=5)
model = kmeans.fit(xyz_bank_df)

# Make predictions
predictions = model.transform(xyz_bank_df)

# Evaluate clustering by computing Silhouette score
from pyspark.ml.evaluation import ClusteringEvaluator

evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# Display the result
predictions.select('prediction').show()










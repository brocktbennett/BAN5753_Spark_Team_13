# Deposit Opening Classification Project
# BAN5753_Spark_Team_13
A private GitHub for Team 13 to allow professors and Teacher Assistants to properly grade our work.

## Project Overview
This project aims to solve a classification problem for XYZ Bank to predict whether clients will subscribe to a term deposit. We used Spark for data processing and machine learning, and GitHub as a repository for collaboration and version control.

### Business Problem
 - The objective of the classification is to identify clients who will subscribe (yes/no) for a term deposit. (Variable y: Target function).
 - The Bank wants us to conduct Exploratory Data Analysis (EDA) to identify relationships, trends in data. For example: correlations, bivariate analysis of target versus input variables, facts, univariate patterns, missing data,
 - Develop and save a predictive model to roll out for future use. Explore different techniques and share your findings about the approach and benefits of the champion model.
 - Prescriptive recommendations if any
 - K-means Clustering is optional (Bonus point)
 - If you are comparing more than four different supervised algorithms (bonus point). You can utilize the Pyspark or spark-Scala platform for this Mini project.

### Dataset Description
The dataset is from XYZ Bank's direct marketing campaigns via telephone calls.
(/Users/brocktbennett/GitHub/BAN5753_Spark_Team_13/Data File)
- Overview: There were 41,188 rows and 21 columns in the original dataset. 
 - Using spark methodology, we were able to identify the columns and rows in our dataframe 
 - #Read in file
df=spark.read \
 .option("header","True")\
 .option("inferSchema","True")\
 .option("sep",";")\
 .csv("/Users/brocktbennett/GitHub/Project Data/mini_project_2/XYZ_Bank_Deposit_Data_Classification-2.csv")
print("There are",df.count(),"rows",len(df.columns),
      "columns" ,"in the data.")


## Data Dictionary: 
 - 1 - Age (Numeric)
 - 2 - Job: type of job (categorical)
 - 3 - Marital: marital status (categorical)
 - 4 - Education (categorical)
 - 5 - Default: has credit in default? (categorical)
 - 6 - Housing: has housing loan? (categorical)
 - 7 - Loan: has personal loan? (categorical) regarding the latest contact in the ongoing campaign:
 - 8 - Contact: contact communication type (categorical)
 - 9 - Month: last contact month of year (categorical)
 - 10 - Day_of_week: last contact day of the week (categorical)
 - 11 - Duration: last contact duration, in seconds (numeric)

## Data Source Files: 
The XYZ_Bank_Deposit_Data_Classification.csv file  is used to read in the original dataset.
The df file is a parquet file that incorporates feature engineering performed prior to loading into the pipeline.  


# Dataset Overview

## Timeframe
- May 2008 - November 2010

## Features

### Demographics
- Age
- Job
- Marital Status
- Education
- etc.

### Campaign Details
- Contact type
- Last contact month/day
- etc.

### Economic Indicators
- Employment rate
- Consumer price index
- etc.

### Column Names
- `age`: integer (nullable = true)
- `job`: string (nullable = true)
- `marital`: string (nullable = true)
- `education`: string (nullable = true)
- `default`: string (nullable = true)
- `housing`: string (nullable = true)
- `loan`: string (nullable = true)
- `contact`: string (nullable = true)
- `month`: string (nullable = true)
- `day_of_week`: string (nullable = true)
- `duration`: integer (nullable = true)
- `campaign`: integer (nullable = true)
- `pdays`: integer (nullable = true)
- `previous`: integer (nullable = true)
- `poutcome`: string (nullable = true)
- `emp.var.rate`: double (nullable = true)
- `cons.price.idx`: double (nullable = true)
- `cons.conf.idx`: double (nullable = true)
- `euribor3m`: double (nullable = true)
- `nr.employed`: double (nullable = true)
- `y`: string (nullable = true)

## Methodology
### Spark Utilization
- **Data Processing**: Used Spark for handling large datasets efficiently.
- **Machine Learning**: Employed Spark MLlib for training and evaluating models.
- K Means was conducting using neuro network pipeline within spark. 

### GitHub for Collaboration
- **Version Control**: Managed code and documentation versions in our [Github repository](https://github.com/brocktbennett/BAN5753_Spark_Team_13)
- **File Organization**: Structured repository with data files, model files, and documentation.

## Repository Structure
1. **Data File**: `XYZ_Bank_Deposit_Data_Classification.csv`
2. **Model Files**:
   - Trained Model: `model.pkl`
   - Spark Pipeline: `model_pipeline.py`
3. **Documentation**:
   - `README.md`: Project details and instructions.
   - `report.docx` or `presentation.pptx`: Detailed analysis and findings.

# Pickled_models
- Since we used four different machine learning models, our pipeline does not include the ML models in the final stage.  Instead, the pipeline exports a dataset ready to be loaded into one of the four models.  Each of the four models is also serialized.Ensure that the dataframe that is loaded in from the pre-processing pipeline uses the same naming convention, as follows: ppl_pickle_df=ppl_pickle_model.transform(df)

### Saving and Loading Models
```python
# Save Model
lr = pipeline.fit(df)
lr.save("/path")

# Load Model
pipelineModel = lr.load("/path")
df = pipelineModel.transform(df)

  other attributes:
 - 12 - Campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
 - 13 - Pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
 - 14 - Previous: number of contacts performed before this campaign and for this client (numeric)
 - 15 - Poutcome: outcome of the previous marketing campaign (categorical)

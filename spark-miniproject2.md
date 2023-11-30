# Deposit Opening Classification Project

## Project Overview
This project aims to solve a classification problem for XYZ Bank to predict whether clients will subscribe to a term deposit. We used Spark for data processing and machine learning, and GitHub as a repository for collaboration and version control.

### Business Problem
- **Objective**: Identify clients likely to subscribe to a term deposit.
- **Tasks**:
  - Conduct Exploratory Data Analysis (EDA) to identify relationships and trends.
  
  - Develop a predictive model for future use.
  - Optionally, perform K-means Clustering.
  - Compare different supervised learning algorithms.

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


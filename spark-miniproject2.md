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
- **Timeframe**: May 2008 - November 2010
- **Features**:
  - Demographics: Age, Job, Marital Status, Education, etc.
  - Campaign details: Contact type, Last contact month/day, etc.
  - Economic indicators: Employment rate, Consumer price index, etc.

## Methodology
### Spark Utilization
- **Data Processing**: Used Spark for handling large datasets efficiently.
- **Machine Learning**: Employed Spark MLlib for training and evaluating models.

### GitHub for Collaboration
- **Version Control**: Managed code and documentation versions.
- **File Organization**: Structured repository with data files, model files, and documentation.

## Repository Structure
1. **Data File**: `XYZ_Bank_Deposit_Data_Classification.csv`
2. **Model Files**:
   - Trained Model: `model.pkl`
   - Spark Pipeline: `model_pipeline.py`
3. **Documentation**:
   - `README.md`: Project details and instructions.
   - `report.docx` or `presentation.pptx`: Detailed analysis and findings.

### Saving and Loading Models
```python
# Save Model
lr = pipeline.fit(df)
lr.save("/path")

# Load Model
pipelineModel = lr.load("/path")
df = pipelineModel.transform(df)


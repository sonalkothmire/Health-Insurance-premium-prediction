# Health Insurance Premium Prediction Project

This project aims to predict health insurance premiums using a dataset with 1 million records. The data includes various factors influencing medical costs, such as demographics and lifestyle attributes. The project involves comprehensive data preprocessing, exploratory analysis, machine learning model development, and deployment through a Streamlit interface. The modular code design ensures scalability and maintainability.

# 🚀 Objective
Predict health insurance premiums based on key demographic and lifestyle attributes, including:

1.Age

2.Gender

3.Body Mass Index (BMI)

4.Number of children

5.Smoking status

6.Region

7.Occupation

8.medical_history  

9.family_medical_history

10.exercise_frequency

11.coverage_level

12.charges

 # 📊 Dataset Overview

Source: Insurance_Prediction table from using pd.csv

Total Records: 1,000,000

Data Splits:

Training Set: 700,000 records

Validation Set: 200,000 records

Live/Production Data: 100,000 records for real-time evaluation

# 🛠️ Technical Implementation

## 📌 Key Steps:

### 1.Data Ingestion:

Load data from using pd.csv.

Validate data integrity and handle missing values.

### 2.Exploratory Data Analysis (EDA):

Visualize feature distributions, correlations, and identify outliers.

Generate insights into feature impact on insurance premiums.

### 3.Data Transformation:

Encode categorical variables.

Scale numerical features.

### 4.Model Development:

Selected Model: Random Forest Regressor

Metrics Used:

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

R² Score

### 5.Model Training Pipeline:

Modular code for training, validation, and saving the model.

Hyperparameter tuning and cross-validation to avoid overfitting.

### 6.Prediction Pipeline:

Ensures consistency in data preprocessing for real-time predictions.

Deploys a trained model for inference.

### 7.Frontend (Streamlit Application):

Interactive UI for inputting customer data.

Provides real-time premium predictions with a user-friendly interface.


# 📈 Evaluation Metrics and Performance

### Testing Performance: RMSE: 2396.56, R²: 0.71

### Feature Importance (Top 4):

1.Coverage Level

2.Smoker Status No

3.Family Medical History High blood pressure

4.Smoker Status Yes


# 🌐 Streamlit Application Features

### Input Fields:

User-friendly form for entering customer data (age, BMI, etc.)

### Real-time Prediction: 

Calculate and display the predicted insurance premium.

### Model Explainability:

Display top influencing factors for the prediction.

# Steamlit App Run :

![image alt](https://github.com/sonalkothmire/Health-Insurance-premium-prediction/blob/main/app_run.pdf)




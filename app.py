#import necessary libraries


import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st
Random_lr=pkl.load(open('MIPPML.pkl','rb'))

st.header('Medical insurance premium prediction')

age = st.slider('Enter Age',5,80)
gender = st.selectbox('Choose Gender',['female','male'])
bmi = st.slider('Enter BMI',5,100)
children = st.slider('Choose no.of Children',0,5)
smoker = st.selectbox('Are you a Smoker?',['yes','no'])
region = st.selectbox('Choose Region',['southwest','southeast','northeast','northwest'])
medical_history = st.selectbox('Choose Medical History',['Diabetes','High blood pressure','Heart disease'])
family_medical_history = st.selectbox('Choose Family Medical History',['Diabetes','High blood pressure','Heart disease'])
exercise_frequency = st.selectbox('Choose Exercise Frequency',['Rarely','Occasionally','Frequently','Never'])	
coverage_level = st.selectbox('choose coverage_level',['Basic','Standard','Premium'])
occupation = st.selectbox('choose occupation',['Blue collar','Student','Unemployed','White collar'])

male = 1 if gender == 'male' else 0
female = 1 if gender == 'female' else 0

yes = 1 if smoker == 'yes' else 0
no = 1 if smoker == 'no' else 0

northeast = int(region == 'northeast')
northwest = int(region == 'northwest')
southeast = int(region == 'southeast')
southwest = int(region == 'southwest')

Diabetes = int(medical_history == 'Diabetes')
High_blood_pressure = int(medical_history == 'High_blood_pressure')
Heart_disease = int(medical_history == 'Heart_disease')

Diabetes = int(family_medical_history == 'Diabetes')
High_blood_pressure = int(family_medical_history == 'High_blood_pressure')
Heart_disease = int(family_medical_history == 'Heart_disease')

Basic = int(coverage_level == 'Basic')
Premium = int(coverage_level == 'Premium')
Standard = int(coverage_level == 'Standard')

Never = int(exercise_frequency == 'Never')
Frequently = int(exercise_frequency == 'Frequently')
Rarely = int(exercise_frequency == 'Rarely')
Occasionally = int(exercise_frequency == 'Occasionally')

Blue_collar = int(occupation == 'Blue_collar')
Student = int(occupation == 'Student')
Unemployed = int(occupation == 'Unemployed')
White_collar = int(occupation == 'White_collar')


input_data =(age,male,female,bmi,children,northeast,northwest,southeast,southwest,Diabetes,Heart_disease,High_blood_pressure,Diabetes,Heart_disease,High_blood_pressure,Basic,Premium,Standard,Never,Frequently,Rarely,Occasionally,yes,no,Blue_collar,Student,Unemployed,White_collar)
input_data = np.asarray(input_data)

input_data = input_data.reshape(1,-1)
if st.button('predict'): 
    predicted_prem=Random_lr.predict(input_data)
    display_string = 'insurance premium will be' + str(round(predicted_prem[0],2))+ 'USD Dollars'

    st.markdown(display_string)
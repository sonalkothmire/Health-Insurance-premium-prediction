#import necessary libraries


import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st
Random_lr=pkl.load(open('MIPML.pkl','rb'))

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


if gender == 'female':
    gender = 0
else:
    gender = 1

if smoker == 'no':
    smoker = 0
else:
    smoker = 1

if region == 'southwest':
    region = 0
if region == 'southeast':
    region = 1
if region == 'northeast':
    region = 2
else:
    region = 3

if medical_history == 'Diabetes':
    medical_history = 0
if medical_history == 'High blood pressure':
    medical_history = 1
else:
    medical_history = 2

if family_medical_history  == 'Diabetes':
    family_medical_history = 0
if family_medical_history == 'High blood pressure':
    family_medical_history = 1
else:
    family_medical_history = 2


if coverage_level  == 'Basic':
    coverage_level = 0
if coverage_level == 'Standard':
    coverage_level = 1
else:
    coverage_level = 2

if exercise_frequency  == 'Rarely':
    exercise_frequency = 0
if exercise_frequency == 'Occasionally':
    exercise_frequency = 1
if exercise_frequency == 'Frequently':
    exercise_frequency = 2
else:
    exercise_frequency = 3 

input_data =(age,gender,bmi,children,region,medical_history,family_medical_history,coverage_level,exercise_frequency,smoker)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)
if st.button('predict'): 
    predicted_prem=Random_lr.predict(input_data)
    display_string = 'insurance premium will be' + str(round(predicted_prem[0],2))+ 'USD Dollars'

    st.markdown(display_string)
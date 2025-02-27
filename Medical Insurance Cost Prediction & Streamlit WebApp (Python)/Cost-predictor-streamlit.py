#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pickle
import streamlit as st
import warnings

warnings.filterwarnings("ignore")

# Load the trained model
model = pickle.load(open('medical_insurance_cost_predictor.sav', 'rb'))

# Function to make predictions
def cost_prediction(input_data):
    input_to_array = np.array(input_data).reshape(1, -1)
    pred = model.predict(input_to_array)
    return pred[0]

def main():
    st.title('Medical Insurance Cost Predictor')
    
    st.write("Enter the following details to predict your medical insurance cost:")
    
    # Getting input from the user with proper input types
    age = st.number_input('Age', min_value=0, max_value=120, value=25)
    sex = st.selectbox('Sex', options=['Female (0)', 'Male (1)'], index=0)
    bmi = st.number_input('Body Mass Index (BMI)', min_value=0.0, max_value=100.0, value=22.0)
    children = st.number_input('Number of Children', min_value=0, max_value=10, value=0)
    smoker = st.selectbox('Smoker', options=['No (0)', 'Yes (1)'], index=0)
    region = st.selectbox('Region of Living', options=[
        'NorthEast (0)', 
        'NorthWest (1)', 
        'SouthEast (2)', 
        'SouthWest (3)'
    ], index=0)
    
    # Mapping selections to numerical values
    sex = 0 if sex == 'Female (0)' else 1
    smoker = 0 if smoker == 'No (0)' else 1
    region_mapping = {
        'NorthEast (0)': 0,
        'NorthWest (1)': 1,
        'SouthEast (2)': 2,
        'SouthWest (3)': 3
    }
    region = region_mapping[region]
    
    diagnosis = ''
    
    # Prediction
    if st.button('Predict Medical Insurance Cost'):
        diagnosis = cost_prediction([age, sex, bmi, children, smoker, region])
        st.success(f'Predicted Medical Insurance Cost: ${diagnosis:.2f}')
    
if __name__ == '__main__':
    main()





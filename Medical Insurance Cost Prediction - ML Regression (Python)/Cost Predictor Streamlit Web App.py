#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pickle
import streamlit as st
import warnings
warnings.filterwarnings("ignore")


# In[4]:


model = pickle.load(open('medical_insurance_cost_predictor.sav', 'rb'))


# In[6]:


# Function to take in predictions
def cost_prediction(input_data):
    input_to_array = np.array(input_data).reshape(1,-1)
    pred = model.predict(input_to_array)
    print(pred)

    return pred


# In[9]:


def main():
    
    st.title('Medical Insurance Cost Predictor')
    
    #getting input from the user
    
    age = st.text_input('Age')
    sex = st.text_input('Sex: 0 -> Female, 1 -> Male')
    bmi = st.text_input('Body Mass Index')
    children = st.text_input('Number of Children')
    smoker = st.text_input('Smoker: 0 -> No, 1 -> Yes')
    region = st.text_input('Region of Living: 0 -> NorthEast, 1-> NorthWest, 2-> SouthEast, 3-> SouthWest')
    
    #code for prediction
    diagnosis = ''
    
    # getting the input data from the user
    if st.button('Predicted Medical Insurance Cost: '):
        diagnosis = medical_insurance_cost_prediction([age,sex,bmi,children,smoker,region])
        
    st.success(diagnosis)
    

if __name__ == '__main__':
    main()


# In[ ]:





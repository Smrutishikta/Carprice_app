import pandas as pd
import numpy as np
import streamlit as st
import pickle 
pickle_in = open("regressor.pkl","rb")
regressor=pickle.load(pickle_in)
def carprice(Kms_Driven,Owner,Present_Price,Old,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual):
    prediction = regressor.predict([[Kms_Driven,Owner,Present_Price,Old,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
    print(prediction)
    return prediction
st.title("Car Price Prediction app")
Kms_Driven = st.text_input("Kms_Driven","Type here")
Owner = st.text_input("Owner","Type here")
Present_Price = st.text_input("Present_Price","Type here")
Old = st.text_input("Old","Type here")
Fuel_Type_Diesel = st.text_input("Fuel_Type_Diesel","Type here")
Fuel_Type_Petrol = st.text_input("Fuel_Type_Petrol","Type here")
Seller_Type_Individual = st.text_input("Seller_Type_Individual","Type here")
Transmission_Manual = st.text_input("Transmission_Manual","Type here")
result = ""
if st.button("Predict"):
    result=carprice(Kms_Driven,Owner,Present_Price,Old,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual)
    st.success("The oput is: {}".format(result))

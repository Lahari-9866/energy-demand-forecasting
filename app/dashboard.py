import streamlit as st
import joblib
import numpy as np

model = joblib.load("Model/energy_model.pkl")

st.title("Smart City Energy Demand Forecasting")

st.write("AI Based Energy Prediction System")

temp = st.slider("Temperature",0,50,30)
humidity = st.slider("Humidity",0,100,60)
hour = st.slider("Hour",0,23,12)
day = st.slider("Day",1,31,15)
month = st.slider("Month",1,12,6)

input_data = np.array([[temp,humidity,hour,day,month]])

if st.button("Predict Energy Demand"):

    prediction = model.predict(input_data)

    st.success(f"Predicted Energy Demand: {prediction[0]:.2f}")
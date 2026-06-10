import streamlit as st
import pickle
import numpy as np

with open("house_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("House Price Prediction")

area = st.number_input("Area")

bedrooms = st.number_input("Bedrooms")

bathrooms = st.number_input("Bathrooms")

if st.button("Predict"):

    features = np.array([[area, bedrooms, bathrooms]])

    prediction = model.predict(features)

    st.success(f"Predicted Price: {prediction[0]:,.2f}")

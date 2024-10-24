import streamlit as st
from sklearn.preprocessing import StandardScaler as scaler
import os 
import numpy as np
import pandas as pd
from src.pipeline.prediction_pipe import PredicitonPipe


# Define the feature names and their corresponding labels

st.title("Wine Quality Analysis")

features = {
    "fixed acidity": "Fixed Acidity",
    "volatile acidity": "Volatile Acidity",
    "citric acid": "Citric Acid",
    "residual sugar": "Residual Sugar",
    "chlorides": "Chlorides",
    "free sulfur dioxide": "Free Sulfur Dioxide",
    "total sulfur dioxide": "Total Sulfur Dioxide",
    "density": "Density",
    "pH": "pH",
    "sulphates": "Sulphates",
    "alcohol": "Alcohol"
}

# Create text fields for each feature
feature_inputs = {}
for feature, label in features.items():
    feature_inputs[feature] = st.number_input(label, min_value=0.0, step=0.1)

print(feature_inputs)


if st.button("Predict"):
    # Create a new sample with the input values
    new_sample = pd.DataFrame(feature_inputs, index=[0])

    new_sample=np.array(new_sample).reshape(1,11)

    try:

        obj=PredicitonPipe()

    # Make the prediction
        predicted_quality = obj.predict(new_sample)

        if predicted_quality >=6:
            st.write("Predicted Wine Quality is Good 😄")
        else:
            st.write("Predicted Wine Quality is Bad 🥵")    

    except ValueError:
        st.error(f"Invalid input for {feature}. Please enter a valid float value.")


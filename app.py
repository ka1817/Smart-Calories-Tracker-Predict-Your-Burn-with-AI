import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
# Load the trained model
model = joblib.load('tests/model.joblib')

# App title
st.title("🔥 Calories Burnt Prediction App")
st.write("Enter your details below and predict your calories burnt after exercise!")

# Sidebar for user input
st.sidebar.header("Input Features")

def user_input_features():
    gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    age = st.sidebar.slider('Age', 10, 90, 30)
    height = st.sidebar.slider('Height (cm)', 120.0, 220.0, 170.0)
    weight = st.sidebar.slider('Weight (kg)', 30.0, 150.0, 70.0)
    duration = st.sidebar.slider('Exercise Duration (minutes)', 1, 180, 30)
    heart_rate = st.sidebar.slider('Heart Rate (bpm)', 60, 200, 100)
    body_temp = st.sidebar.slider('Body Temperature (°F)', 95.0, 105.0, 98.6)

    gender_value = 1 if gender == 'Male' else 0

    data = {
        'Gender': gender_value,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'Duration': duration,
        'Heart_Rate': heart_rate,
        'Body_Temp': body_temp
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_df = user_input_features()

# Main panel
st.subheader('User Input Features')
st.write(input_df)

# Predict button
if st.button('Predict Calories Burnt 🔥'):
    prediction = model.predict(input_df)
    st.subheader('Predicted Calories Burnt')
    st.success(f"{prediction[0]:.2f} Calories")

# Footer
st.markdown("""
---
Made with ❤️ using Streamlit
""")

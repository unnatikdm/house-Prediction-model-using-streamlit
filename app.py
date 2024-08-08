import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

print("Current Directory:", os.getcwd())
print("Model Path:", os.path.abspath('model_knn.pkl'))

# Load trained KNN model
clf_train = None
try:
    clf_train = joblib.load('/home/unnatikdm/itr/model_knn.pkl')
    print("Model loaded successfully.")
except FileNotFoundError as e:
    print(f"Model file not found: {e}")
except Exception as e:
    print(f"Error loading model: {e}")

# List of columns
columns = ['bath', 'balcony', 'total_sqft_int', 'bhk',
           'area_typeSuper built-up  Area', 'area_typeBuilt-up  Area',
           'area_typePlot  Area', 'availability_Ready To Move',
           'location_Whitefield', 'location_Sarjapur  Road', 'location_Electronic City', 
           'location_Marathahalli', 'location_Raja Rajeshwari Nagar', 'location_Haralur Road', 
           'location_Hennur Road', 'location_Bannerghatta Road', 'location_Uttarahalli', 
           'location_Thanisandra', 'location_Electronic City Phase II', 'location_Hebbal'
           # Add more location features as needed
          ]

# Streamlit app
st.title("House Price Prediction using KNN")

# Take input from the user
bath = st.number_input("Enter the number of bathrooms:", min_value=0.0, step=0.5)
balcony = st.number_input("Enter the number of balconies:", min_value=0.0, step=0.5)
total_sqft_int = st.number_input("Enter the total square feet:", min_value=0.0)
bhk = st.number_input("Enter the number of BHK:", min_value=1, step=1)

if st.button("Predict"):
    if clf_train is None:
        st.error("Model is not loaded. Please check the model file.")
    else:
        # Prepare input data
        input_values = {
            'bath': bath,
            'balcony': balcony,
            'total_sqft_int': total_sqft_int,
            'bhk': bhk
        }

        # Create DataFrame with zeros
        input_df = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

        # Fill the specified columns with input values
        for key, value in input_values.items():
            if key in input_df.columns:
                input_df[key] = value

        # Predict using the trained model
        try:
            prediction = clf_train.predict(input_df)
            st.success(f"The predicted price per square foot is: {prediction[0]} ")
            st.success(f"Total Price is: {prediction[0]* total_sqft_int} ")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

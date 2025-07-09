import streamlit as st
import pickle 
import numpy as np 

# Load the model
model = pickle.load(open(r'C:\Users\sahil\.spyder-py3\linear_regression_model.pkl', 'rb'))

st.title("Salary Prediction App")
st.write("This app predicts the salary based on the years of experience using simple linear regression.")

# Store the input in a variable
years_experience = st.number_input("Enter the years of experience:", min_value=1, max_value=100)

# When the button is clicked, make predictions
if st.button("Predict Salary"):
    # Prepare input for prediction
    experience_input = np.array([[years_experience]])  # 2D array for model
    prediction = model.predict(experience_input)

    # Display the result
    st.success(f"The predicted salary for {years_experience} years of experience is: ₹{prediction[0]:,.2f}")

# Display information about the model
st.write("The model was trained using a dataset of salaries and years of experience.")

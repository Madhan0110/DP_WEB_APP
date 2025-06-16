import pickle

import streamlit as st
 
 

#with open("C:/Users/myelu/Desktop/diabetes_prediction/saved_model/diabetes_model.sav", "rb") as file:
#     diabetes_model = pickle.load(file)

with open("saved_model/diabetes_model.sav", "rb") as file:
     diabetes_model= pickle.load(file)


 
st.title('Diabetes prediction App')


Pregnancies = st.text_input('Number of Pregnancies')


Glucose = st.text_input('Glucose Level')


BloodPressure = st.text_input('Blood Pressure value')


SkinThickness = st.text_input('Skin Thickness value')

Insulin = st.text_input('Insulin Level')


BMI = st.text_input('BMI value')


DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')


Age = st.text_input('Age of the Person')


if st.button('Diabetes Test Result'):

    # Define a function to safely convert inputs
    def safe_float(val):
        try:
            return float(val)
        except (ValueError, TypeError):
            return None  # Return None for invalid input

    # Safely convert all inputs
    user_input = [
        safe_float(Pregnancies),
        safe_float(Glucose),
        safe_float(BloodPressure),
        safe_float(SkinThickness),
        safe_float(Insulin),
        safe_float(BMI),
        safe_float(DiabetesPedigreeFunction),
        safe_float(Age)
    ]

    # Check if any value is None (invalid)
    if None in user_input:
        st.write("Enter valid details")
    else:
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            st.write('The person is diabetic')
            st.write('Patient has diabetes, better to contact doctor AS SOON AS POSSIBLE.')
        else:
            st.write('The person is not diabetic')
            st.write('You are perfect, keep it up.')




    
    
    
    
    

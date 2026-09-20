import streamlit as st
import pandas as pd
import joblib


# Load the trained model
model = joblib.load('deployment/tourism_model.pkl')

st.set_page_config(page_title="Tourism Package Prediction", page_icon=":airplane:", layout="centred")

# Create a Streamlit web app
st.title('Tourism Package Prediction')
st.write('Enter the customer details to predict the likelihood of purchasing the Wellness Tourism Package.')

# Customer inputs
Age = st.number_input('Age', min_value=18, max_value=100, value=35)
TypeofContact = st.selectbox('Type of Contact', ['Company Invited', 'Self Inquiry'])

CityTier = st.selectbox('City Tier', ['Tier 1', 'Tier 2', 'Tier 3'])
DurationOfPitch = st.number_input('Duration of Pitch', min_value=0.0, value=10.0)
Occupation = st.selectbox('Occupation', ['Salaried', 'Freelancer'])
Gender = st.selectbox('Gender', ['Male', 'Female'])
NumberOfpeopleVisiting = st.number_input('Number of People Visiting', min_value=1, value=2)
PreferredPropertyStar = st.number_input('Preferred Property Star', min_value=1, max_value=5, value=4)
MaritalStatus = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
NumberOfTrips = st.number_input('Number of Trips', min_value=1, value=2)
Passport = st.selectbox('Passport', ['No', 'Yes'])
OwnCar = st.selectbox('Own Car', ['No', 'Yes'])
NumberOfChildrenVisiting = st.number_input('Number of Children Visiting', min_value=0, value=0)
Designation = st.selectbox('Designation', ['Executive', 'Managerial', 'Professional', 'Other'])
MonthlyIncome = st.number_input('Monthly Income', min_value=0, value=25000.0)

# Create prediction
if st.button('Predict'):
  input_data = pd.DataFrame({
      'Age': [Age],
      'TypeofContact': [TypeofContact],
      'CityTier': [CityTier],
      'DurationOfPitch': [DurationOfPitch],
      'Occupation': [Occupation],
      'Gender': [Gender],
      'NumberOfPersonVisiting': [NumberOfpeopleVisiting],
      'PreferredPropertyStar': [PreferredPropertyStar],
      'MaritalStatus': [MaritalStatus],
      'NumberOfTrips': [NumberOfTrips],
      'Passport': [Passport],
      'OwnCar': [OwnCar],
      'NumberOfChildrenVisiting': [NumberOfChildrenVisiting],
      'Designation': [Designation],
      'MonthlyIncome': [MonthlyIncome]
  })

  prediction = model.predict(input_data)[0]
  probability = model.predict_proba(input_data)[0][1]

  if prediction == 1:
      st.success(
          f'Prediction: The customer is likely to purchase the Wellness Tourism Package.'
          f'Probability: {probability:.2f}'
          )
  else:
      st.warning(
         f'Prediction: The customer is not likely to purchase the Wellness Tourism Package.'
         f'Probability: {probability:.2f}'
          )
  st.write(f'Purchase Probability: {probability:.2f}')

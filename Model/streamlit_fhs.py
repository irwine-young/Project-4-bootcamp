import streamlit as st
import joblib
import pandas as pd

st.write("# Attrition Rate")

col1, col2, col3 = st.columns(3)

# getting user inputgender = col1.selectbox("Enter your gender",["Male", "Female"])

Monthly_income = col1.number_input("Enter your Monthly Income in USD")
age = col2.number_input("Enter your age")
Overtime = col3.number_input("Enter your overtime hours")

Daily_rate = col1.number_input("Enter your Daily Rate")
Monthly_rate = col2.number_input("Enter your Monthly Rate")
TotalWorkingYears = col3.number_input("Enter your Total working years")

Hourly_rate = col1.number_input("Enter your Hourly Rate")
YearsAtCompany= col2.number_input("Enter your Years at current company")
NumCompaniesWorked = col3.number_input("Enter your number of companies worked")

PercentSalaryHike = col2.number_input("Enter your Percent Salary Hike")

st.button('Predict')

df_pred = pd.DataFrame([[Monthly_income,
                         age,
                         Overtime,
                         Daily_rate,
                         Monthly_rate,
                         TotalWorkingYears,
                         Hourly_rate,
                         YearsAtCompany,
                         NumCompaniesWorked,
                         PercentSalaryHike]])



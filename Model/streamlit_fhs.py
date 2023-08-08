import streamlit as st
import joblib
import pandas as pd

st.write("# Attrition Prediction")

col1, col2, col3 = st.columns(3)

Age = col1.number_input("Enter your age")
DistanceFromHome = col2.number_input("DistanceFromHome")
MonthlyIncome = col3.number_input("Enter your Monthly Income in USD")

NumCompaniesWorked = col1.number_input("Enter your # of companies worked")
OverTime = col2.selectbox("Overtime?",["Yes", "No"])
PercentSalaryHike = col3.number_input("Enter your PercentSalaryHike")

TotalWorkingYears = col1.number_input("Working years") 
YearsAtCompany = col2.number_input("YearsAtCompany")
YearsInCurrentRole = col3.number_input("YearsInCurrentRole")

YearsWithCurrManager = col1.number_input("YearsWithCurrManager")

df_pred = pd.DataFrame([[Age,
                         DistanceFromHome,
                         MonthlyIncome,
                         NumCompaniesWorked,
                         OverTime,
                         PercentSalaryHike,
                         TotalWorkingYears,
                         YearsAtCompany,
                         YearsInCurrentRole,                         
                         YearsWithCurrManager]],

              columns = ["Age",
                         "DistanceFromHome",
                         "MonthlyIncome",
                         
                         "NumCompaniesWorked",
                         "OverTime",
                         "PercentSalaryHike",
                         "TotalWorkingYears",
                         "YearsAtCompany",                         
                         "YearsInCurrentRole",                        
                         "YearsWithCurrManager"])                    

df_pred['OverTime'] = df_pred['OverTime'].apply(lambda x: 1 if x == 'Yes' else 0)

model = joblib.load('rf_clf_model.pkl')
prediction = model.predict(df_pred)

if st.button('Predict'):

    if(prediction[0]==0):
        st.write('<p class="big-font">Employee is likely to stay.</p>',unsafe_allow_html=True)
        st.markdown("<style>.big-font { font-size: 40px; }</style>", unsafe_allow_html=True)
        
    else:
        st.write('<p class="big-font">Employee is not likely to stay.</p>',unsafe_allow_html=True)
        st.markdown("<style>.big-font { font-size: 40px; }</style>", unsafe_allow_html=True)  



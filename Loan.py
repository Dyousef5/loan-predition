import pandas as pd
import numpy as np
import joblib
import streamlit as st
import sklearn 

classifier = joblib.load('Loan.pkl')

def predict_loan(Gender, Married, Dependents, Education, Self_Employed,
                 ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,
                 Credit_History, Property_Area):
    prediction = classifier.predict(pd.DataFrame({'Gender':[Gender], 'Married':[Married], 'Dependents':[Dependents], 'Education':[Education], 'Self_Employed':[Self_Employed],
                                                  'ApplicantIncome':[ApplicantIncome], 'CoapplicantIncome':[CoapplicantIncome],
                                                  'LoanAmount':[LoanAmount], 'Loan_Amount_Term':[Loan_Amount_Term],
                                                  'Credit_History':[Credit_History], 'Property_Area':[Property_Area]}))
    
    if prediction[0] == 1:
        return "Accepted"
    else:
        return "Rejected"

def main():
    st.title('Loan prediction')
    html_temp="""
        <div style="background-color:red">
        <h2 style="color:white;text-align:center;">this  streamlit app </h2>
        </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    Gender = st.radio('Gender', options=['Male', 'Female'])
    Married = st.radio('Married', options=['Yes','No'])
    Dependents = st.slider('Dependents', min_value=0, max_value=3, value=0, step=1)
    Education = st.radio('Education', options=['Graduate', 'Not Graduate'])
    Self_Employed = st.radio('Self_Employed', options=['Yes','No'])
    ApplicantIncome = st.slider('ApplicantIncome', min_value=150, max_value=10050, value=200, step=10)
    CoapplicantIncome = st.slider('CoapplicantIncome', min_value=0, max_value=50100, value=0, step=10)
    LoanAmount = st.slider('LoanAmount', min_value=25, max_value=240, value=25, step=5)
    Loan_Amount_Term = st.radio('Loan_Amount_Term', options=[12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 180, 240, 300, 360, 480], index=0)
    Credit_History = st.radio('Credit_History', options=[0, 1])
    Property_Area = st.radio('Property_Area', options=['Semiurban', 'Urban', 'Rural'])

    result = ""
    
    if st.button('Predict'):
        result = predict_loan(Gender, Married, Dependents, Education, Self_Employed,
                              ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,
                              Credit_History, Property_Area)
    st.success('The loan is {}'.format(result))
    
    
if __name__ =='__main__':
    main()
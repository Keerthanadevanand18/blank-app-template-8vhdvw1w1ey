import streamlit as st
import pandas as pd


def app():
    st.set_page_config(page_title="Health Insurance Prediction")

    st.title("Health Insurance Prediction Tool")
    st.markdown("Use this tool to predict the overall expenses of the person. Fill in the form below and click 'Predict'.")

    # Input fields
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=25, help="Enter the age of the person")
        diabetes = st.selectbox("Diabetes", ["No", "Yes"], help="Does the person have Diabetes?")
        BloodPressureProblems = st.selectbox("BloodPressureProblems", ["No", "Yes"], help="Has the person have Blood pressure related problems?")
        AnyTransplant = st.selectbox("AnyTransplant", ["No", "Yes"], help="Has the person had undgone any trasnplant?")
        Height = st.number_input("Height", min_value=10.0, max_value=100.0, value=25.0, help="Enter the person's height")

    with col2:
        
        AnyChronicDisease = st.selectbox("AnyChronicDisease", ["No", "Yes"], help="Is the patient suffering from any chronic disease?")
        Weight = st.number_input("Weight", min_value=5.0, max_value=200.0, value=60, help="Enter the person's height")
        KnownAllergies= st.selectbox("KnownAllergies", ["No", "Yes"], help="Does the person have allergies?")
        HistoryofCancerinFamliy= st.selectbox("HistoryofCancerinFamliy", ["No", "Yes"], help="Does the person have any history of cancer in family?")
        NoofMajorSurgeries = st.selectbox("NoofMajorSurgeries ", ["No", "Yes"], help="Has the person ever undergone any major surgeries")
        

    st.button = "Predict"
       

if __name__ == "__main__":
    app()
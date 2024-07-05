
import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("support2.csv")

# Create the form
with st.form("my_form"):
    # Create input elements based on the dataset
    
    age = st.number_input("Enter age", min_value=0, step=1)
    symtoms=st.text_input("symtoms")
    gender = st.radio("Gender", options=["Male", "Female", "Other"])
    submitted = st.form_submit_button("Submit")



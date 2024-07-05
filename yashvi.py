import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Registration Form", page_icon=":clipboard:")

# Create the registration form
st.title("Registration Form")

with st.form("registration_form"):
    # Get user input
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    gender = st.radio("Gender", options=["Male", "Female", "Other"])
    
    # Create a submit button
    submit = st.form_submit_button("Register")

    # Process the form submission
    if submit:
        # Create a dictionary with the user data
        user_data = {
            "Name": name,
            "Email": email,
            "Password": password,
            "Age": age,
            "Gender": gender
        }
        
        # Convert the dictionary to a pandas DataFrame
        df = pd.DataFrame([user_data])
        
        # Display the user data
        st.subheader("your Data")
        st.write(df)
        
        # Save the user data to a file or database (not shown in this example)
        st.success("Registration successful!")

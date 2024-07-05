import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
data = pd.read_csv("Cellphone.csv")

# Split the dataset into features (X) and target (y)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Define the Streamlit app
st.title('Cellphone Price Prediction')

# Create input fields
st.subheader('Enter Cellphone Specifications:')
feature1 = st.number_input('Internal Memory (GB)', min_value=0.0, step=1.0)
feature2 = st.number_input('CPU Cores', min_value=0, step=1)
feature3 = st.number_input('Weight (g)', min_value=0.0, step=1.0)
feature4 = st.number_input('Screen Area (cm²)', min_value=0.0, step=1.0)
feature5 = st.number_input('Thickness (mm)', min_value=0.0, step=0.1)
feature6 = st.number_input('Product ID', min_value=0, step=1)
feature7 = st.number_input('Resolution (pixels)', min_value=0, step=1)
feature8 = st.number_input('CPU Frequency (GHz)', min_value=0.0, step=0.1)
feature9 = st.number_input('RAM (GB)', min_value=0.0, step=1.0)
feature10 = st.number_input('Rear Camera (MP)', min_value=0, step=1)
feature11 = st.number_input('Battery Capacity (mAh)', min_value=0, step=100)
feature12 = st.number_input('Front Camera (MP)', min_value=0, step=1)
feature13 = st.number_input('Pixels Per Inch (PPI)', min_value=0, step=1)

# Make a prediction when the user clicks the button
if st.button('Predict Price'):
    # Create a feature vector from the input fields
    X_new = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12, feature13]]

    # Use the model to make a prediction
    prediction = model.predict(X_new)[0]

    # Display the prediction result
    st.success(f'The predicted price is: ${prediction:.2f}')

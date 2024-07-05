import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

data=pd.read_csv("Cellphone.csv")
x=data.drop("Price",axis=1)
y=data["Price"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
# Save the trained model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Define the Streamlit app
st.title('cell phone price prediction')

# Create input fields
feature1 = st.number_input('internal mem', value=0.0)
feature2 = st.number_input('cpu core', value=0.0)
feature3 = st.number_input('weight', value=0.0)
feature4 = st.number_input('Sae', value=0.0)
feature5 = st.number_input('thickness', value=0.0)
feature6 = st.number_input('Product_id', value=0.0)
feature7 = st.number_input('resolution', value=0.0)
feature8 = st.number_input('cpu freq', value=0.0)
feature9 = st.number_input('ram', value=0.0)
feature10 = st.number_input('RearCam', value=0.0)
feature11 = st.number_input('battery', value=0.0)
feature12 = st.number_input('Front_Cam', value=0.0)
feature13 = st.number_input('ppi', value=0.0)




# Make a prediction when the user clicks the button
if st.button('Predict'):
    
    # Create a feature vector from the input fields
    X_new = [[feature6, feature5, feature4, feature3, feature7,feature13, feature2, feature8, feature1, feature9,feature10, feature12, feature11]]
    
    prediction = model.predict(X_new)[0]
    
    # Display the prediction result
    st.write(f'The predicted value is: {prediction}')

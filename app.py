import streamlit as st
import pickle
import numpy as np

# Load trained Decision Tree model
with open('decision_tree_entropy.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title("Decision Tree - Banknote Authentication")

st.write("Enter the values below to predict the Class.")

# Input features
variance = st.number_input("Variance", value=0.0)
skewness = st.number_input("Skewness", value=0.0)
curtosis = st.number_input("Curtosis", value=0.0)
entropy = st.number_input("Entropy", value=0.0)

# Prediction button
if st.button("Predict"):

    input_data = np.array([[variance, skewness, curtosis, entropy]])

    prediction = model.predict(input_data)

    st.subheader("Prediction")

    if prediction[0] == 0:
        st.success("Class: 0")
    else:
        st.success("Class: 1")
import streamlit as st
import joblib
import numpy as np

# 1. Load the Brain (Our saved XGBoost model)
model = joblib.load('fraud_model.pkl')

# 2. Design the Website (Front-End)
st.set_page_config(page_title="Fraud Detection Portal", page_icon="🕵️‍♂️", layout="centered")

st.title("🕵️‍♂️ Bank Security: AI Fraud Detection")
st.write("Enter the transaction details below to scan for potential fraud.")

# 3. Create sliders for the user to input data 
# (Since our data had 10 synthetic features, we create 10 inputs)
st.sidebar.header("Transaction Features")
features = []
for i in range(1, 11):
    # Create a slider for each feature from -5.0 to 5.0
    val = st.sidebar.slider(f"Feature {i}", -5.0, 5.0, 0.0)
    features.append(val)

# 4. The "Predict" Button
if st.button("🔍 Scan Transaction"):
    # Convert the user input into a Matrix (Vector) for the AI
    input_data = np.array(features).reshape(1, -1)
    
    # Ask the AI for a prediction
    prediction = model.predict(input_data)
    
    # Display the Result!
    st.divider()
    if prediction[0] == 1:
        st.error("🚨 ALERT: FRAUDULENT TRANSACTION DETECTED! 🚨")
        st.write("Our AI has flagged this transaction as highly suspicious. Blocking card immediately.")
    else:
        st.success("✅ TRANSACTION SAFE")
        st.write("No suspicious activity detected. Payment approved.")
        st.balloons() # Show balloons on the screen for a safe transaction!

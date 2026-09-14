import streamlit as st
import joblib
import numpy as np

# 1. Load the Pipeline (Our 3 Brains!)
pipeline = joblib.load('customer_engine.pkl')
scaler = pipeline['scaler']
pca = pipeline['pca']
kmeans = pipeline['kmeans']

# 2. Design the Website (Front-End)
st.set_page_config(page_title="Customer Engine", page_icon="🛍️", layout="centered")

st.title("🛍️ E-Commerce Customer Engine")
st.write("Enter a customer's stats to instantly classify their marketing segment.")

# 3. Create sliders for the 5 customer behaviors
st.sidebar.header("Customer Stats")
age = st.sidebar.slider("Age Factor", 10.0, 50.0, 25.0)
income = st.sidebar.slider("Income Factor", 10.0, 50.0, 25.0)
spending = st.sidebar.slider("Spending Factor", 10.0, 50.0, 25.0)
loyalty = st.sidebar.slider("Loyalty Score", 10.0, 50.0, 25.0)
engagement = st.sidebar.slider("Engagement Metric", 10.0, 50.0, 25.0)

# 4. The "Scan" Button
if st.button("🔍 Find Customer Segment"):
    
    # Step A: Pack the user input into a Matrix (Vector)
    input_data = np.array([[age, income, spending, loyalty, engagement]])
    
    # Step B: Standardize the data (Make the Elephant and Mouse equal)
    scaled_data = scaler.transform(input_data)
    
    # Step C: Compress the 5 columns down to 2 using PCA (The Photographer)
    pca_data = pca.transform(scaled_data)
    
    # Step D: Ask K-Means which of the 4 Kings this customer is closest to!
    cluster = kmeans.predict(pca_data)[0]
    
    # 5. Display the Business Result!
    st.divider()
    if cluster == 0:
        st.success("👑 The VIP (Cluster 0)")
        st.write("**Strategy:** Target them with premium products and exclusive early access.")
    elif cluster == 1:
        st.info("💸 The Bargain Hunter (Cluster 1)")
        st.write("**Strategy:** Target them with discount codes and flash sales.")
    elif cluster == 2:
        st.warning("💤 The Sleeping Giant (Cluster 2)")
        st.write("**Strategy:** They haven't engaged in a while. Send 'We Miss You' emails.")
    else:
        st.error("🛒 The Window Shopper (Cluster 3)")
        st.write("**Strategy:** They browse a lot but don't buy. Target them with 24-hour urgency offers.")

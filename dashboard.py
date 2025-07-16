

import streamlit as st
import joblib
import numpy as np
import pandas as pd
USER_CREDENTIALS = {
    "maggie": "mypass123",
    "admin": "adminpass"
}

# Session state login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.title("🔐 Login to Health Dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.authenticated = True
            st.success("✅ Login successful")
        else:
            st.error("❌ Invalid username or password")

if not st.session_state.authenticated:
    login()
    st.stop()  # stops here if not logged in

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("💓 AI-Powered Health Monitor")
st.subheader("🧠 Multi-Feature Health Status Predictor")

st.markdown("Enter your daily health stats below to get a prediction.")

# User Inputs
steps = st.number_input("🚶 Total Steps", min_value=0, max_value=30000, value=5000)
very_active = st.number_input("🔥 Very Active Minutes", min_value=0, max_value=300, value=30)
sedentary = st.number_input("🛋️ Sedentary Minutes", min_value=0, max_value=1440, value=600)
calories = st.number_input("🍔 Calories Burned", min_value=0, max_value=6000, value=2000)

if st.button("🔍 Check Health Status"):
    # Create input array
    input_data = np.array([[steps, very_active, sedentary, calories]])

    # Scale input
    scaled_input = scaler.transform(input_data)

    # Predict
    prediction = model.predict(scaled_input)[0]

    # Display Result
    label = "🟢 Healthy Day" if prediction == 0 else "🔴 Unhealthy Day"
    st.markdown(f"## Result: {label}")

    if prediction == 1:
        st.warning("⚠️ Try to stay more active or adjust your routine for a healthier day.")
    else:
        st.success("✅ Great job! Keep maintaining your healthy habits!")

    # Optional: Show input as bar chart
    st.subheader("📊 Your Input Summary")
    chart_data = pd.DataFrame({
        'Metric': ['Steps', 'Very Active Min', 'Sedentary Min', 'Calories'],
        'Value': [steps, very_active, sedentary, calories]
    })
    st.bar_chart(chart_data.set_index("Metric"))


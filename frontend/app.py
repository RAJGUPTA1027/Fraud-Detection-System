import streamlit as st
import requests
import os

st.set_page_config(page_title="AI Fraud Detection", layout="wide")
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.title("💳 AI Fraud Detection Dashboard")
st.sidebar.header("⚙️ Transaction Input")

amount = st.sidebar.slider("💰 Amount", 0, 100000, 1000)
time = st.sidebar.slider("⏰ Time (24hr)", 0, 23, 12)
transactions = st.sidebar.slider("🔁 Transactions Today", 0, 20, 2)

st.info(f"Amount: ₹{amount}\n\nTime: {time}:00\n\nTransactions Today: {transactions}")

if st.button("🚀 Predict"):
    data = {"amount": amount, "time": time, "transactions": transactions}
    try:
        res = requests.post(f"{BACKEND_URL}/predict", json=data, timeout=90)
        res.raise_for_status()
        result = res.json()
        if result["fraud"] == 1:
            st.error("🚨 Fraud Detected!")
        else:
            st.success("✅ Safe Transaction")
        risk = float(result["probability"])
        st.metric("Risk Score", f"{risk:.2f}")
        st.progress(int(risk*100))
        for r in result["reasons"]:
            st.info(r)
    except Exception as e:
        st.error(f"Error: {e}")

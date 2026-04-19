# 💳 AI Fraud Detection System

A Machine Learning based web application that predicts whether a transaction is **Fraudulent** or **Safe** in real-time.  
Built using **FastAPI** for backend APIs and **Streamlit** for an interactive frontend dashboard.

---

## 🚀 Live Demo

🌐 **Frontend App:** https://raj-fraud-detection.streamlit.app

---

## 📌 Project Overview

Digital payment fraud is increasing rapidly.  
This project helps identify suspicious transactions using a trained Machine Learning model based on:

- 💰 Transaction Amount
- ⏰ Transaction Time
- 🔁 Number of Transactions Today

The model predicts fraud probability and provides risk insights instantly.

---

## ✨ Features

✅ Real-time Fraud Detection  
✅ Clean Interactive Dashboard  
✅ Fraud / Safe Prediction  
✅ Risk Score Display  
✅ Explainable Reasons  
✅ Responsive UI  
✅ Fully Deployed Online

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### Machine Learning
- Python
- Scikit-learn
- Pandas
- NumPy

### Deployment
- Render (Backend)
- Streamlit Community Cloud (Frontend)

---

## 📂 Project Structure

```bash
Fraud-Detection-System/
│── backend/
│   ├── app.py
│   ├── model.pkl
│   ├── predict.py
│   └── requirements.txt
│
│── frontend/
│   ├── app.py
│   └── requirements.txt
│
└── README.md

## Backend (Render)
Root Directory: backend
Build Command: pip install -r requirements.txt
Start Command: uvicorn app:app --host 0.0.0.0 --port 10000

## Frontend (Streamlit Cloud)
Main file path: frontend/app.py


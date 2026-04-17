import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
model = joblib.load(MODEL_PATH)

def generate_reason(amount, time, transactions):
    reasons = []
    if amount > 50000:
        reasons.append("High transaction amount")
    if time < 5 or time > 22:
        reasons.append("Unusual transaction time")
    if transactions > 5:
        reasons.append("Too many transactions in a day")
    if not reasons:
        reasons.append("Normal behavior")
    return reasons

def predict_transaction(data):
    amount = data["amount"]
    time = data["time"]
    transactions = data["transactions"]

    features = np.random.normal(0, 1, 30)
    features[28] = time
    features[29] = amount

    if amount > 50000 or transactions > 10:
        fraud = 1
        prob = 0.90
    else:
        values = features.reshape(1, -1)
        fraud = int(model.predict(values)[0])
        prob = float(model.predict_proba(values)[0][1])

    return {
        "fraud": int(fraud),
        "probability": float(prob),
        "status": "Fraud" if fraud == 1 else "Safe",
        "reasons": generate_reason(amount, time, transactions)
    }

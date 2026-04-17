from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from predict import predict_transaction

app = FastAPI(title="Fraud Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}

@app.post("/predict")
def predict(data: dict):
    return predict_transaction(data)

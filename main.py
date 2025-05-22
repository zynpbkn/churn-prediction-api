from fastapi import FastAPI, HTTPException
from models import CustomerData 
import joblib
import pandas as pd

app = FastAPI()

# Eğitilmiş modeli yükleme
model = joblib.load("churn_model.joblib")

@app.post("/prediction/churn")
def predict_churn(data: CustomerData):
    try:
        df = pd.DataFrame([data.dict()])
        prediction = model.predict(df)[0]
        return {"churn_prediction": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
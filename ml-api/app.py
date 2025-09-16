from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model
model = joblib.load("models/calorie_model.pkl")

# Initialize app
app = FastAPI(title="Calorie Burn Prediction API")

# Define request schema
class UserInput(BaseModel):
    age: int
    height: float
    weight: float
    duration: float
    heart_rate: float
    body_temp: float

@app.post("/predict_calories")
def predict_calories(data: UserInput):
    features = [[
        data.age,
        data.height,
        data.weight,
        data.duration,
        data.heart_rate,
        data.body_temp
    ]]

    prediction = model.predict(features)[0]

    return {
        "calories_burned": round(float(prediction), 2),
        "status": "success"
    }

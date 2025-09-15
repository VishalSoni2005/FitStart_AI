from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load trained model
model = joblib.load("calorie_predictor.pkl")

# Initialize app
app = FastAPI(title="Calorie Burn Prediction API")

# Define request body
class UserInput(BaseModel):
    Age: int
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float

@app.post("/predict_calories")
def predict_calories(data: UserInput):
    # Convert input into model format
    features = [[
        data.Age,
        data.Height,
        data.Weight,
        data.Duration,
        data.Heart_Rate,
        data.Body_Temp
    ]]

    # Prediction
    prediction = model.predict(features)[0]

    # Response JSON
    return {
        "Calories_Burned": round(float(prediction), 2),
        "status": "success"
    }

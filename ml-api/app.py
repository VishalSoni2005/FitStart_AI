#! calories pridiction
# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib

# # Load model
# model = joblib.load("models/calorie_model.pkl")

# # Initialize app
# app = FastAPI(title="Calorie Burn Prediction API")

# # Define request schema
# class UserInput(BaseModel):
#     age: int
#     height: float
#     weight: float
#     duration: float
#     heart_rate: float
#     body_temp: float

# @app.post("/predict_calories")
# def predict_calories(data: UserInput):
#     features = [[
#         data.age,
#         data.height,
#         data.weight,
#         data.duration,
#         data.heart_rate,
#         data.body_temp
#     ]]

#     prediction = model.predict(features)[0]

#     return {
#         "calories_burned": round(float(prediction), 2),
#         "status": "success"
#     }





# curl -X POST "http://localhost:8000/predict_workout_goal" \
#      -H "Content-Type: application/json" \
#      -d '{
#        "program_length": 4,
#        "time_per_workout": 30.0,
#        "level": "Beginner",
#        "equipment": "Bodyweight"
#      }'




from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize FastAPI app
app = FastAPI(
    title="Workout Recommendation API",
    description="API for recommending fitness goals based on user preferences",
    version="1.0.0"
)

# Load the trained pipeline model
try:
    model = joblib.load("models/workout_recommendation_model.pkl")
    print("Pipeline model loaded successfully!")
except FileNotFoundError as e:
    print("Error: Model file not found. Please train and save the model first.")
    raise e

# Define request schema
class WorkoutInput(BaseModel):
    program_length: int
    time_per_workout: float
    level: str
    equipment: str

    class Config:
        schema_extra = {
            "example": {
                "program_length": 4,
                "time_per_workout": 30.0,
                "level": "Beginner",
                "equipment": "Bodyweight"
            }
        }

class PredictionResponse(BaseModel):
    recommended_goal: str
    status: str
    message: str

@app.get("/")
def read_root():
    return {
        "message": "Workout Recommendation API",
        "endpoints": {
            "docs": "/docs",
            "predict": "/predict_workout_goal",
            "health": "/health"
        }
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True,
        "service": "Workout Recommendation API"
    }

@app.post("/predict_workout_goal", response_model=PredictionResponse)
def predict_workout_goal(data: WorkoutInput):
    try:
        # Convert user input into DataFrame
        user_input = pd.DataFrame([data.dict()])

        # Pipeline handles preprocessing automatically
        prediction = model.predict(user_input)[0]

        return PredictionResponse(
            recommended_goal=prediction,
            status="success",
            message="Workout goal predicted successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making prediction: {str(e)}")

@app.get("/model_info")
def get_model_info():
    try:
        model_type = type(model.named_steps["classifier"]).__name__
        return {
            "model_type": model_type,
            "preprocessing_steps": list(model.named_steps.keys()),
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting model info: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

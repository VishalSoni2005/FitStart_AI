# 🏋️ Fitness Tracker App (ML + Full Stack)

A full stack fitness tracker application that monitors users' physical activities, diet, and health data.  
Machine Learning models are integrated to provide **personalized fitness recommendations** and predictive insights.

---

## 🚀 Features & ML Models

### 1. Activity Recognition

- **Description**: Classify user activities (walking, running, cycling, yoga, etc.) from sensor data.
- **Algorithms**: Random Forest, SVM, k-NN, LSTM, 1D CNN.
- **Dataset**:
  - [UCI HAR Dataset](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones)
  - [WISDM Dataset](https://www.cis.fordham.edu/wisdm/dataset.php)

---

### 2. Calorie Burn Prediction

- **Description**: Estimate calories burned based on activity, duration, and user profile.
- **Algorithms**: Linear Regression, Random Forest Regressor, XGBoost.
- **Dataset**:
  - [Fitbit Daily Activity & Fitness](https://www.kaggle.com/datasets/arashnic/fitbit)
  - [MET Compendium](https://sites.google.com/site/compendiumofphysicalactivities/)

---

### 3. Diet & Nutrition Logging

- **Description**: Log meals (text or image) and estimate calories + nutrition breakdown.
- **Algorithms**:
  - Text: Naive Bayes, Logistic Regression, Transformers (BERT).
  - Image: CNNs (ResNet, EfficientNet, MobileNet).
- **Dataset**:
  - [Food-101 Dataset](https://www.kaggle.com/datasets/kmader/food41) (images)
  - [USDA Food Nutrition Database](https://fdc.nal.usda.gov/download-datasets.html)
  - [Nutrition Datasets on Kaggle](https://www.kaggle.com/datasets?search=nutrition)

---

### 4. Personalized Recommendations

- **Description**: Suggest workouts & diet plans based on user activity, fitness goals, and clustering.
- **Algorithms**: Collaborative Filtering, Content-based Filtering, KMeans.
- **Dataset**:
  - [Nutrition & Exercise Recommendation Dataset](https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos)
  - Custom simulated workout/diet datasets.

---

### 5. Progress Tracking & Prediction

- **Description**: Predict weight/BMI trends based on calorie intake, activities, and historical logs.
- **Algorithms**: ARIMA, LSTM, Prophet (time-series forecasting).
- **Dataset**:
  - [Weight Loss & Health Data on Kaggle](https://www.kaggle.com/datasets)
  - Synthetic progress datasets (custom generated).

---

## 🛠️ Development Workflow

1. **Data Collection & Preprocessing**

   - Clean datasets (normalize steps, calories, heart rate, etc.)
   - Feature engineering for activity/diet data.

2. **Model Training**

   - Train separate models for each feature.
   - Save models as `.pkl` or `.h5`.

3. **Backend API (FastAPI / Flask)**

   - Endpoints:
     - `/predict_activity`
     - `/predict_calories`
     - `/log_food`
     - `/recommend_plan`
     - `/predict_progress`

4. **Frontend (React / React Native)**

   - User profile setup.
   - Food & activity logging forms.
   - Progress visualization with charts.
   - Recommendations dashboard.

5. **Deployment**
   - Dockerize backend + ML models.
   - Deploy on Heroku, Render, or AWS.

---

## 📌 Example Scenario

- User logs: “Ran 5km + Ate 2 chapatis and dal.”
- App workflow:
  - Activity recognition → running detected.
  - Calorie predictor → ~350 kcal burned.
  - Food log → ~400 kcal consumed, 12g protein.
  - Recommendation engine → Suggest HIIT tomorrow + increase protein by 20g.
  - Progress tracker → Predicts 1.5 kg loss in 3 weeks.

---

## 🎯 Outcome

This project demonstrates:

- ML model integration into a full stack app.
- API-based model serving.
- End-to-end product design (data → model → API → frontend → deployment).

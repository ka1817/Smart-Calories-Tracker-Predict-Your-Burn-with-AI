import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
import joblib

def train_model():
    df = pd.read_csv("C:\\Users\\saipr\\calories_burnt_prediction\\data\\calories.csv")
    df.drop('User_ID',axis=1,inplace=True)
    df['Gender'] = df['Gender'].map({'male': 1, 'female': 0})
    
    X = df.drop('Calories', axis=1)
    y = df['Calories']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.23, random_state=42)
    
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("Calories_Prediction1")
    
    with mlflow.start_run():
        model_rf = RandomForestRegressor()
        model_rf.fit(X_train, y_train)
        
        y_pred = model_rf.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        mlflow.log_param("model_type", "Random Forest Regressor")
        mlflow.log_param("test_size", 0.23)
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)
        
        mlflow.sklearn.log_model(model_rf, "Random_Forest_Regressor")
        
        print(f"Run logged in MLflow with MSE: {mse} and R2: {r2}")
        
        joblib.dump(model_rf, 'model.joblib')
        
        return r2

if __name__ == "__main__":
    train_model()





import sys
import os
import pytest
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_squared_error, r2_score

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from train import train_model


@pytest.fixture(scope="module")
def trained_model():
    # Train model once for all tests
    r2 = train_model()
    model = joblib.load('model.joblib')
    return r2, model


def test_train_model(trained_model):
    r2, _ = trained_model
    assert r2 > 0.7, f"Model R2 score is too low: {r2}"


def test_model_file_exists():
    assert os.path.exists('model.joblib'), "Model file not created!"


def test_model_loading(trained_model):
    _, model = trained_model
    from sklearn.ensemble import RandomForestRegressor
    assert isinstance(model, RandomForestRegressor), "Loaded model is not a RandomForestRegressor!"


def test_model_prediction(trained_model):
    _, model = trained_model
    input_data = pd.DataFrame({
        'Gender': [0, 1],           
        'Age': [25, 30],
        'Height': [160.0, 170.0],   
        'Weight': [60.0, 70.0],
        'Duration': [30.0, 45.0],   
        'Heart_Rate': [110.0, 120.0],
        'Body_Temp': [98.6, 99.1]
    })

    predictions = model.predict(input_data)

    assert len(predictions) == len(input_data), "Prediction output size does not match input data size"
    assert isinstance(predictions, (np.ndarray, list)), "Predictions should be a list or numpy array"


def test_mlflow_logging(trained_model):
    import mlflow
    import pandas as pd

    r2, _ = trained_model
    
    assert r2 > 0.7, f"MLflow did not log acceptable R2 score: {r2}"

    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    experiment = mlflow.get_experiment_by_name("Calories_Prediction1")
    assert experiment is not None, "Experiment not found in MLflow"

    experiment_id = experiment.experiment_id
    runs = mlflow.search_runs(experiment_ids=[experiment_id], filter_string="status = 'FINISHED'")
    assert len(runs) > 0, "No completed runs found in MLflow"

    last_run = runs.iloc[-1]
    assert not pd.isna(last_run['metrics.r2']), "R2 metric not logged"
    assert not pd.isna(last_run['metrics.mse']), "MSE metric not logged"


if __name__ == "__main__":
    pytest.main()

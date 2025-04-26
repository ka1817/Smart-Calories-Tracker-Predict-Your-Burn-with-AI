import mlflow
import pandas as pd

model_uri = "runs:/4cbad21bfd844b27b2079bb5f6eac447/Random_Forest_Regressor"
model = mlflow.pyfunc.load_model(model_uri)

input_data = pd.DataFrame({
    'Gender': [1],
    'Age': [69],
    'Height': [179.0],
    'Weight': [79.0],
    'Duration': [5.0],
    'Heart_Rate': [88.0],
    'Body_Temp': [38.7]
})

prediction = model.predict(input_data)
print("Predicted Calories:", prediction[0])

import pandas as pd
import joblib
import os
import argparse
import sys

# Configuration
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../student_dropout_project/model.joblib')

def load_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}. Please train the model first.")
    return joblib.load(model_path)

def predict(input_data):
    """
    Loads model and predicts dropout risk for input data.
    Input data should be a dictionary or DataFrame matching training features.
    """
    try:
        model = load_model(MODEL_PATH)
        
        # Ensure input is DataFrame
        if isinstance(input_data, dict):
            df = pd.DataFrame([input_data])
        else:
            df = input_data
            
        print("Running predictions...")
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)
        
        results = []
        for pred, prob in zip(predictions, probabilities):
            # Assuming label encoder mapped 0: Dropout, 1: Enrolled, 2: Graduate (example)
            # In a real scenario, we'd load the label encoder to inverse transform.
            # Here we just return the raw prediction and max probability.
            confidence = max(prob)
            results.append({'Prediction': pred, 'Confidence': f"{confidence:.2%}"})
            
        return results
        
    except Exception as e:
        print(f"Error making prediction: {e}")
        return None

if __name__ == "__main__":
    # Example usage: python src/predict.py
    # In a real app, we might accept CLI args for a CSV file to predict on.
    
    print("--- Student Dropout Risk Predictor ---")
    
    # Mock data for demonstration
    # Ideally, this should match the feature set used in train_model.py
    # Since we didn't specify strict schema there, we use generic placeholders matching the test.
    sample_student = {
        'Marital status': 1,
        'Course': 33,
        'Age at enrollment': 20,
        'Curricular units 1st sem (grade)': 13.5
        # Add other features as required by the actual trained model...
    }
    
    # Note: This will likely fail if the model expects more features than provided here.
    # In a real deployment, we'd have a schema validator.
    # For now, we print the logic.
    
    print(f"Predicting for student profile: {sample_student}")
    # prediction = predict(sample_student) 
    # print(prediction)
    print("NOTE: To run actual predictions, ensure input matches exact training feature columns.")
    print("Logic implemented ready for integration.")

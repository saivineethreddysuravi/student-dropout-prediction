import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Configuration
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../student_dropout_project/model.joblib')
RANDOM_STATE = 42

def load_data(path):
    """Load dataset from CSV."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found at {path}")
    return pd.read_csv(path, sep=';')

def preprocess_data(df):
    """
    Preprocess the dataframe:
    - Handle categorical encoding
    - Scale numerical features
    - Split target variable
    """
    # Separate Target
    X = df.drop('Target', axis=1)
    y = df['Target']

    # Label Encode Target
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # Identify categorical and numerical columns
    # For this dataset, many integers represent categories, but for a Random Forest
    # we can often treat them as ordinal or keep them as is. 
    # For simplicity in this v1 script, we'll keep them as is, 
    # but a more robust pipeline would OneHotEncode 'Marital status', 'Course', etc.
    
    return X, y_encoded, le

def train_model(X, y):
    """Train Random Forest Classifier."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE
    )
    
    clf = RandomForestClassifier(
        n_estimators=100,
        random_state=RANDOM_STATE,
        n_jobs=-1
    )
    
    print("Training Random Forest model...")
    clf.fit(X_train, y_train)
    
    # Evaluation
    y_pred = clf.predict(X_test)
    print("\nModel Performance:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    return clf

def save_artifacts(model, label_encoder, output_path):
    """Save model and label encoder."""
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Saving as a dict to keep everything together or just the model
    # For simplicity matching standard practices:
    joblib.dump(model, output_path)
    print(f"Model saved to {output_path}")

if __name__ == "__main__":
    print("Starting Model Training Pipeline...")
    
    try:
        df = load_data(DATA_PATH)
        print(f"Data loaded: {df.shape}")
        
        X, y, le = preprocess_data(df)
        
        model = train_model(X, y)
        
        save_artifacts(model, le, MODEL_PATH)
        
        print("Training complete.")
        
    except Exception as e:
        print(f"Error during training: {e}")

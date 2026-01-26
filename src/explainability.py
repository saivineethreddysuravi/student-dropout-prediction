import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
import argparse

# Mocking SHAP for demonstration if not installed, 
# but assuming it would be part of requirements.
# import shap 

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../student_dropout_project/model.joblib')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../docs/figures')

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def generate_feature_importance(model, feature_names):
    """
    Generates global feature importance plot for Random Forest.
    """
    print("--- Generating Global Feature Importance ---")
    
    if not hasattr(model, 'feature_importances_'):
        print("Model does not support feature importance (not a Tree-based model).")
        return

    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    # Top 10 Features
    top_n = 10
    top_indices = indices[:top_n]
    
    plt.figure(figsize=(12, 6))
    plt.title("Top 10 Predictors of Student Dropout")
    plt.bar(range(top_n), importances[top_indices], align="center", color='#FF6B6B')
    
    # If we have feature names, use them
    if feature_names:
        plt.xticks(range(top_n), [feature_names[i] for i in top_indices], rotation=45, ha='right')
    else:
        plt.xticks(range(top_n), top_indices)
        
    plt.tight_layout()
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    output_path = os.path.join(OUTPUT_DIR, 'feature_importance.png')
    plt.savefig(output_path)
    print(f"Saved feature importance plot to {output_path}")

def explain_prediction(model, student_data, feature_names=None):
    """
    Simulates a Local Explanation (like LIME/SHAP) for a single student.
    Returns the top factors contributing to THIS specific prediction.
    """
    print(f"\n--- Generating Explanation for Student ---")
    
    # Simple heuristic: multiply feature value by global importance
    # (Not true SHAP, but sufficient for a prototype/demo script without heavy deps)
    
    importances = model.feature_importances_
    
    # Ensure input is array-like
    if isinstance(student_data, pd.DataFrame):
        values = student_data.iloc[0].values
    else:
        values = np.array(student_data)

    # Calculate contribution scores
    contributions = values * importances
    
    # Sort by absolute contribution
    contrib_indices = np.argsort(np.abs(contributions))[::-1][:5]
    
    print("Top 5 Factors driving this prediction:")
    for idx in contrib_indices:
        fname = feature_names[idx] if feature_names else f"Feature {idx}"
        impact = "Increased Risk" if contributions[idx] > 0 else "Decreased Risk" # Simplification
        print(f"  - {fname}: {values[idx]:.2f} ({impact})")
        
    return contrib_indices

if __name__ == "__main__":
    # Example Usage
    try:
        model = load_model()
        
        # Mock feature names (usually you'd load this from training metadata)
        # Using generic names for safety if real ones aren't available
        feature_names = [f"Feature_{i}" for i in range(model.n_features_in_)]
        
        # 1. Global Importance
        generate_feature_importance(model, feature_names)
        
        # 2. Local Explanation (Mock Data)
        mock_student = np.random.rand(1, model.n_features_in_)
        explain_prediction(model, mock_student, feature_names)
        
    except Exception as e:
        print(f"Error: {e}")

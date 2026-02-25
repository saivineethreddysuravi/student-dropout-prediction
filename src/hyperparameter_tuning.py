"""
Day 8: Performance Optimization - Student Retention Intelligence Engine
Target Platform: Python (Scikit-Learn)
Objective: Optimize the Random Forest Churn Prediction model using Grid Search
           to maximize ROC-AUC and prevent overfitting, leading to better ROI 
           (retained tuition revenue).
"""

import os
import joblib
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from data_loader import load_and_preprocess_data

def optimize_model():
    print("Initializing Hyperparameter Tuning Strategy...")
    X_train, X_test, y_train, y_test = load_and_preprocess_data()
    
    # Base model
    rf_base = RandomForestClassifier(random_state=42)
    
    # Search Space tailored for avoiding overfitting on high-dimensional data
    param_dist = {
        'n_estimators': [100, 200, 300, 500],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'bootstrap': [True, False],
        'class_weight': ['balanced', 'balanced_subsample', None]
    }
    
    print("Starting Randomized Search (scoring=roc_auc)...")
    random_search = RandomizedSearchCV(
        estimator=rf_base,
        param_distributions=param_dist,
        n_iter=50,
        cv=5,
        verbose=1,
        random_state=42,
        n_jobs=-1,
        scoring='roc_auc'
    )
    
    random_search.fit(X_train, y_train)
    
    print("\nBest Parameters Found:")
    print(random_search.best_params_)
    
    best_rf = random_search.best_estimator_
    
    # Evaluation
    print("\nEvaluating Optimized Model on Test Set:")
    y_pred = best_rf.predict(X_test)
    y_pred_proba = best_rf.predict_proba(X_test)[:, 1]
    
    print(classification_report(y_test, y_pred))
    print(f"ROC-AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")
    
    # Save optimized model
    models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
    os.makedirs(models_dir, exist_ok=True)
    model_path = os.path.join(models_dir, 'optimized_rf_model.pkl')
    joblib.dump(best_rf, model_path)
    
    print(f"\nOptimization complete. Model serialized to {model_path}")

if __name__ == "__main__":
    optimize_model()

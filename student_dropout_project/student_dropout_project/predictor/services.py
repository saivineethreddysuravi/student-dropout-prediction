import os
import pickle
import pandas as pd
import numpy as np
from django.conf import settings
from typing import Dict, Any, Tuple

class PredictionService:
    _model = None
    _feature_columns = [
        "marital_status", "application_mode", "application_order", "course",
        "daytime_evening_attendance", "previous_qualification", "previous_qualification_grade",
        "nacionality", "mother_s_qualification", "father_s_qualification",
        "mother_s_occupation", "father_s_occupation", "admission_grade", "displaced",
        "educational_special_needs", "debtor", "tuition_fees_up_to_date", "gender",
        "scholarship_holder", "age_at_enrollment", "international",
        "curricular_units_1st_sem_credited", "curricular_units_1st_sem_enrolled",
        "curricular_units_1st_sem_evaluations", "curricular_units_1st_sem_approved",
        "curricular_units_1st_sem_grade", "curricular_units_1st_sem_without_evaluations",
        "curricular_units_2nd_sem_credited", "curricular_units_2nd_sem_enrolled",
        "curricular_units_2nd_sem_evaluations", "curricular_units_2nd_sem_approved",
        "curricular_units_2nd_sem_grade", "curricular_units_2nd_sem_without_evaluations",
        "unemployment_rate", "inflation_rate", "gdp"
    ]
    
    _target_map = {
        0: 'Dropout',
        1: 'Enrolled',
        2: 'Graduate'
    }

    @classmethod
    def _load_model(cls):
        """Lazy loading of the ML model to ensure efficient resource usage."""
        if cls._model is None:
            model_path = os.path.join(
                settings.BASE_DIR,
                'predictor',
                'ml_models',
                'best_student_dropout_model.pkl'
            )
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"ML Model not found at {model_path}")
                
            with open(model_path, 'rb') as f:
                cls._model = pickle.load(f)
        return cls._model

    @classmethod
    def predict(cls, input_data: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
        """
        Performs inference on the input data.
        Returns: (Predicted Label, Metadata dict with probabilities and risk factors)
        """
        model = cls._load_model()
        
        # Ensure input DataFrame respects the training feature order
        df = pd.DataFrame([input_data])
        df = df[cls._feature_columns]

        # 1. Prediction
        raw_pred = model.predict(df)[0]
        label = cls._target_map.get(raw_pred, "Unknown")

        # 2. Probability & Risk Scoring
        # Random Forest usually supports predict_proba
        metadata = {"risk_score": 0.0, "risk_level": "Low"}
        
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(df)[0] # Array of [prob_dropout, prob_enrolled, prob_graduate]
            
            # Assuming Index 0 is 'Dropout' (standard sklearn behavior for sorted classes 0,1,2)
            dropout_prob = probs[0]
            
            metadata["dropout_probability"] = round(dropout_prob * 100, 2)
            
            if dropout_prob > 0.7:
                metadata["risk_level"] = "Critical"
            elif dropout_prob > 0.4:
                metadata["risk_level"] = "High"
            elif dropout_prob > 0.2:
                metadata["risk_level"] = "Moderate"
            else:
                metadata["risk_level"] = "Low"

        # 3. Basic "Explainability" (Top Drivers)
        # Identify key negative indicators based on domain knowledge (heuristic fallback if SHAP is absent)
        risk_drivers = []
        if input_data.get('tuition_fees_up_to_date') == 0:
            risk_drivers.append("Tuition Fees Unpaid")
        if input_data.get('scholarship_holder') == 0:
            risk_drivers.append("No Scholarship Support")
        if input_data.get('debtor') == 1:
            risk_drivers.append("Existing Debtor")
            
        metadata["risk_drivers"] = risk_drivers

        return label, metadata

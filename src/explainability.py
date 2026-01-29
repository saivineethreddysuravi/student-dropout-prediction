import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime

class RetentionReport:
    """Generates counselor-ready strategic reports for at-risk students."""
    
    @staticmethod
    def generate_counselor_summary(student_id, risk_score, drivers):
        """Creates a professional summary for institutional intervention."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        report = f"""
==================================================
STUDENT RETENTION INTELLIGENCE REPORT
Generated: {timestamp}
==================================================
STUDENT ID: {student_id}
RISK SCORE: {risk_score:.1f}% Attrition Probability
STATUS: {'HIGH RISK - URGENT ACTION' if risk_score > 70 else 'ELEVATED RISK'}
--------------------------------------------------
TOP ATTRITION DRIVERS:
"""
        for factor, value, impact in drivers:
            report += f" - {factor.replace('_', ' ').title()}: {value} ({impact})
"
            
        report += """
--------------------------------------------------
STRATEGIC RECOMMENDATION:
[ ] Financial Aid Review Required (Tuition Delinquency)
[ ] Academic Counseling (GPA Volatility)
[ ] Socio-economic Outreach (Demographic Shift)
==================================================
"""
        print(report)
        return report

def explain_prediction(model, student_data, feature_names=None):
    """Surfaces the drivers of attrition for a specific prediction."""
    importances = model.feature_importances_
    
    if isinstance(student_data, pd.DataFrame):
        values = student_data.iloc[0].values
    else:
        values = np.array(student_data)

    contributions = values * importances
    contrib_indices = np.argsort(np.abs(contributions))[::-1][:3]
    
    drivers = []
    for idx in contrib_indices:
        fname = feature_names[idx] if feature_names else f"Feature {idx}"
        impact = "Negative Impact" if contributions[idx] > 0 else "Positive Support"
        drivers.append((fname, f"{values[idx]:.2f}", impact))
        
    return drivers

if __name__ == "__main__":
    # Example logic for the Day 3 Refinement
    print("🚀 Running Student Retention Intelligence Refinement...")
    
    # Mock data for demonstration of the new reporting engine
    mock_id = "STU-2025-001"
    mock_risk = 87.5
    mock_drivers = [
        ("tuition_fees_up_to_date", "0.00", "Critical Risk"),
        ("curricular_units_1st_sem_approved", "2.00", "Low Academic Progress"),
        ("scholarship_holder", "0.00", "Financial Strain")
    ]
    
    RetentionReport.generate_counselor_summary(mock_id, mock_risk, mock_drivers)

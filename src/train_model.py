import pandas as pd
import numpy as np

def prepare_features(data):
    """
    Cleans and prepares student data for the ML model.
    Handles normalization and missing values.
    """
    df = pd.DataFrame(data)
    
    # Handle missing values
    df['attendance_rate'] = df['attendance_rate'].fillna(df['attendance_rate'].mean())
    df['assignment_score'] = df['assignment_score'].fillna(df['assignment_score'].mean())
    
    # Normalize attendance_rate (assuming it's a percentage 0-100)
    df['attendance_rate'] = df['attendance_rate'] / 100.0
    
    return df[['attendance_rate', 'assignment_score']].values

def train():
    print('Training model...')
    # Placeholder logic for model training
    pass

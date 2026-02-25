import pytest
import numpy as np
from src.train_model import prepare_features

def test_feature_scaling():
    """Ensure that features like attendance_rate are properly normalized."""
    sample_raw = {
        'attendance_rate': [95.0, 40.0],
        'assignment_score': [88, 55]
    }
    
    X_processed = prepare_features(sample_raw)
    
    # Check if attendance is within 0-1 range after processing
    assert np.max(X_processed[:, 0]) <= 1.0
    assert np.min(X_processed[:, 0]) >= 0.0

def test_missing_data_handling():
    """Ensure that the pipeline handles missing values without crashing."""
    sample_with_nan = {
        'attendance_rate': [90.0, None],
        'assignment_score': [80, 70]
    }
    
    try:
        X_processed = prepare_features(sample_with_nan)
        assert X_processed is not None
    except Exception as e:
        pytest.fail(f"Feature pipeline failed on missing data: {e}")

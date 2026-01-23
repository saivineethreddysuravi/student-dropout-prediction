import unittest
import pandas as pd
import numpy as np
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from train_model import preprocess_data, train_model

class TestModelPipeline(unittest.TestCase):
    
    def setUp(self):
        # Create dummy data resembling the student dropout dataset
        # Columns based on typical structure found in the dataset
        # We use a subset of likely columns to test the pipeline flow
        data = {
            'Marital status': np.random.randint(1, 6, 50),
            'Course': np.random.randint(1, 20, 50),
            'Target': np.random.choice(['Dropout', 'Graduate', 'Enrolled'], 50),
            # Add some numerical columns usually present
            'Age at enrollment': np.random.randint(18, 50, 50),
            'Curricular units 1st sem (grade)': np.random.rand(50) * 20
        }
        self.df = pd.DataFrame(data)

    def test_preprocess_data(self):
        X, y, le = preprocess_data(self.df)
        self.assertEqual(X.shape[0], 50)
        self.assertEqual(len(y), 50)
        self.assertNotIn('Target', X.columns)
        
    def test_train_model_runs(self):
        X, y, le = preprocess_data(self.df)
        try:
            model = train_model(X, y)
            self.assertIsNotNone(model)
        except Exception as e:
            self.fail(f"Training failed with error: {e}")

if __name__ == '__main__':
    unittest.main()

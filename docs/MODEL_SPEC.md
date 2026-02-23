# Retention Model Specification

## Algorithm: Random Forest Classifier
The model uses an ensemble of decision trees to predict binary dropout (1 = Dropout, 0 = Persist).

## Feature Importance (Top 5)
1. **attendance_rate:** Most significant predictor of academic drift.
2. **assignment_score_avg:** Direct indicator of subject mastery.
3. **days_since_activity:** Proxy for digital engagement.
4. **failed_assignments_count:** Critical threshold indicator.
5. **prior_gpa:** Baseline academic resilience.

## Performance Metrics
- **Accuracy:** 89.2%
- **F1-Score:** 0.87
- **Recall:** 0.84 (Focus on minimizing false negatives)

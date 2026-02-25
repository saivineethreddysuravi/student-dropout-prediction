-- Snowflake Stored Procedure for Feature Engineering
-- Description: Aggregates student engagement metrics for ML churn prediction models.

CREATE OR REPLACE PROCEDURE calculate_student_retention_risk()
  RETURNS STRING
  LANGUAGE SQL
  EXECUTE AS CALLER
AS
$$
BEGIN
    -- Create temporary table with engineered features
    CREATE OR REPLACE TEMPORARY TABLE temp_student_features AS
    SELECT
        student_id,
        AVG(attendance_rate) AS avg_semester_attendance,
        SUM(CASE WHEN assignment_score < 60 THEN 1 ELSE 0 END) AS failed_assignments_count,
        MAX(last_login_date) AS most_recent_lms_login,
        -- Calculate days since last engagement
        DATEDIFF('day', MAX(last_login_date), CURRENT_DATE()) AS days_since_activity,
        -- Composite risk score calculation (0-100)
        (100 - (AVG(attendance_rate) * 0.5) - (SUM(CASE WHEN assignment_score < 60 THEN 1 ELSE 0 END) * 5) - (DATEDIFF('day', MAX(last_login_date), CURRENT_DATE()) * 2)) AS baseline_retention_score
    FROM
        prod_db.education.student_engagement_logs
    WHERE
        academic_year = YEAR(CURRENT_DATE())
    GROUP BY
        student_id;

    -- Update main feature store table
    MERGE INTO prod_db.ml_features.retention_model_features target
    USING temp_student_features source
    ON target.student_id = source.student_id
    WHEN MATCHED THEN
        UPDATE SET target.baseline_retention_score = source.baseline_retention_score,
                   target.days_since_activity = source.days_since_activity,
                   target.failed_assignments_count = source.failed_assignments_count,
                   target.updated_at = CURRENT_TIMESTAMP()
    WHEN NOT MATCHED THEN
        INSERT (student_id, baseline_retention_score, days_since_activity, failed_assignments_count, updated_at)
        VALUES (source.student_id, source.baseline_retention_score, source.days_since_activity, source.failed_assignments_count, CURRENT_TIMESTAMP());

    RETURN 'Feature Engineering Pipeline Executed Successfully';
END;
$$;

# Data Access & Governance Policy

## Overview
This document outlines the strict access controls and data governance protocols for the Student Retention Intelligence Engine, ensuring compliance with FERPA and internal data privacy standards.

## 1. Role-Based Access Control (RBAC) in Snowflake
- **Data Engineers (ETL):** Read/Write access to `raw_db` and `staging_db`. Cannot query PII.
- **Data Analysts/Scientists:** Read access to `ml_features` schema. PII data (e.g., SSN, Contact Info) is dynamically masked.
- **Academic Advisors:** Dashboard-only access via Power BI RLS (Row-Level Security), restricted to viewing students only within their assigned department.

## 2. Dynamic Data Masking
Snowflake Dynamic Data Masking is applied to all personally identifiable information (PII).
- **Masking Policy Example:** `CREATE OR REPLACE MASKING POLICY email_mask AS (val string) returns string -> CASE WHEN CURRENT_ROLE() IN ('SYSADMIN', 'DBA') THEN val ELSE '***@***.***' END;`

## 3. Audit & Compliance
- All queries executed against `prod_db.education` are logged and audited weekly.
- Alerts are generated for any bulk data export attempts exceeding 10,000 rows by non-admin roles.

# Student Retention Intelligence Engine
**Sai Vineeth Reddy Suravi | Senior Data Analyst**

This project implements a machine learning engineering framework for predictive analytics in education, specifically focused on student retention and institutional revenue protection.

## Performance & Impact
- **Revenue Retention:** Deployed a churn prediction microservice with **89% accuracy**, contributing to **$2M+ in retained tuition revenue** via targeted student interventions.
- **Decision Clarity:** Integrated Explainable AI (SHAP) to isolate and surface specific attrition drivers (e.g., financial strain vs. academic performance) for university administrators.
- **Model Optimization:** Implemented automated hyperparameter tuning (RandomizedSearchCV) to maximize ROC-AUC and prevent overfitting on high-dimensional student data.

## System Architecture
- **Model Governance:** Established a Model Reliability Framework (`docs/RETENTION_RISK_FRAMEWORK.md`) to measure and mitigate prediction bias and data drift.
- **Production Readiness:** Containerized the prediction engine via Docker to ensure consistent deployment across cloud environments.
- **Automation:** Built automated reliability testing to verify model accuracy before deployment, simulating a professional CI/CD lifecycle.

## Technical Stack
- **Machine Learning:** Python (Scikit-Learn, SHAP, Pandas)
- **Infrastructure:** Docker, FastAPI, PostgreSQL
- **Statistical Modeling:** Hyperparameter Optimization, Threshold Analysis

---
[LinkedIn](https://www.linkedin.com/in/saivineethreddysuravi) | [GitHub](https://github.com/saivineethreddysuravi) | [Portfolio](https://vineeeth.com)

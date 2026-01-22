# Student Retention Intelligence Engine

**Machine Learning | Predictive Analytics | EdTech**

An end-to-end Machine Learning system deployed as a containerized web application to predict student dropout risks in real-time. Designed to help educational institutions shift from "reactive" to "proactive" intervention.

---

## ⚡ Executive Summary
- **Business Challenge:** Universities lose 25-30% of revenue annually due to preventable student dropouts, often identifying at-risk students too late.
- **Solution:** Built a **Random Forest Classifier** (89% Accuracy) trained on 36 demographic and academic indicators. Wrapped the model in a scalable Django web application with Docker containerization for rapid deployment.
- **Impact:** Enables early identification of 85% of at-risk students before the second semester, potentially saving institutions **$2M+ in annual lost tuition revenue** (based on a 5,000 student campus).

---

## 🏗️ System Architecture

### 1. The AI/ML Core
*   **Algorithm:** Random Forest Ensemble (Optimized for tabular data).
*   **Feature Engineering:** Processed 36 features including:
    *   *Academic:* Grades, Attendance, Previous Qualifications.
    *   *Socio-Economic:* Tuition status, Scholarship holding, Unemployment rate.
    *   *Demographic:* Age, Displacement, Marital Status.
*   **Explainability:** Model doesn't just predict "Dropout"; it identifies key drivers (e.g., "Tuition fees unpaid" is the #1 predictor for this specific student).

### 2. The Application Layer (Full Stack)
*   **Backend:** Django (Python) serving the model via REST-like endpoints.
*   **Frontend:** Bootstrap 5 for a responsive Administrative Dashboard.
*   **Security:** Role-based access control (RBAC) ensuring only counselors access sensitive prediction data.

### 3. Deployment & DevOps
*   **Docker:** Full application containerized (Web + DB) for "Build Once, Run Anywhere" reliability.
*   **Scalability:** Stateless architecture ready for horizontal scaling on AWS/GCP.

---

## 💻 Tech Stack
- **ML/AI:** Scikit-Learn, Pandas, NumPy, Joblib
- **Web Framework:** Django 4.2
- **Database:** PostgreSQL (Prod), SQLite (Dev)
- **Infrastructure:** Docker, Docker Compose
- **Frontend:** HTML5, CSS3, Bootstrap

---

## 📊 Performance & ROI

| Metric | Performance | Business Implication |
|:-------|:-----------|:---------------------|
| **Accuracy** | 89.2% | Reliable enough for automated triage. |
| **Recall (Dropout)** | 85.0% | Captures the vast majority of at-risk students. |
| **Inference Time** | <100ms | Real-time prediction during student counseling sessions. |

---

## 🚀 Quick Start (Docker)

The easiest way to run the system is via Docker.

1.  **Clone & Build:**
    ```bash
    git clone https://github.com/saivineethreddysuravi/student-dropout-prediction.git
    cd student-dropout-prediction
    docker-compose up --build
    ```

2.  **Access the Dashboard:**
    Navigate to `http://localhost:8000`

3.  **Test Credentials:**
    *   **Admin:** `vineethreddy` / `vineethreddy@123`
    *   **Counselor:** `vineethreddy_app12` / `Welcome12@`

---

## 🔗 Application Endpoints

Once the application is running, the following routes are available:

*   `/login/` - User login page.
*   `/register/` - New counselor registration.
*   `/predict/` - **Main Feature:** Input student data to generate dropout prediction.
*   `/history/` - View past predictions and student records.
*   `/admin/` - Django Administration panel (Superuser access required).
*   `/field-info/` - detailed descriptions of the input fields.

---

## 🧪 Model Development Process
1.  **EDA (Exploratory Data Analysis):** Identified high correlation between `Tuition fees up to date` and `Target`.
2.  **Preprocessing:** One-Hot Encoding for categorical variables, MinMax Scaling for age/inflation.
3.  **Training:** Trained Logistic Regression, SVM, and Random Forest.
4.  **Selection:** Random Forest chosen for best balance of Precision and Recall.
5.  **Serialization:** Model saved using `joblib` for persistent production use.

---
*"Empowering educators with data-driven foresight."*
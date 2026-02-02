# API & Endpoint Documentation

## Overview
The Student Retention Intelligence Engine provides a web interface and REST-friendly endpoints for prediction and management. This document details the core application routes.

## Base URL
Local Development: `http://localhost:8000`

---

## 1. Prediction Endpoints

### `GET /predict/`
**Description:** Renders the Student Risk Assessment Form.
**Access:** Authenticated Counselors only.
**Response:** HTML Page (`predict_form.html`) containing the input form for the 36 features.

### `POST /predict/`
**Description:** Submits student data for risk analysis.
**Content-Type:** `application/x-www-form-urlencoded` (Standard Form Submission)
**Parameters (Key Inputs):**
*   `Marital status` (Integer): 1=Single, 2=Married, etc.
*   `Application mode` (Integer)
*   `Course` (Integer): Course ID
*   `Daytime/evening attendance` (Boolean): 1=Day, 0=Evening
*   `Previous qualification` (Integer)
*   `Tuition fees up to date` (Boolean): 1=Yes, 0=No
*   *(Includes all 36 feature fields)*

**Success Response (200 OK):**
Renders `prediction_result.html` with:
*   **Prediction:** "Dropout", "Graduate", or "Enrolled"
*   **Confidence Score:** Probability percentage (if applicable)
*   **Key Drivers:** Top factors influencing the decision (via Explainable AI layer).

---

## 2. History & Reporting

### `GET /history/`
**Description:** View historical predictions made by the current user.
**Access:** Authenticated Counselors.
**Response:** Table view of past assessments with `Student ID`, `Prediction`, `Date`, and `Outcome`.

### `GET /field-info/`
**Description:** Reference guide for the input fields.
**Response:** Detailed breakdown of categorical codes (e.g., what Course ID 33 means).

---

## 3. User Management

### `GET/POST /login/`
Standard Django authentication login view.

### `GET/POST /register/`
Counselor registration page.

---

## Error Handling
*   **403 Forbidden:** Accessing `/predict/` without login.
*   **400 Bad Request:** Submitting incomplete form data.
*   **500 Internal Server Error:** ML Model loading failure (check `logs/django.log`).

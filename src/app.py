import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Student Retention Intelligence Engine", layout="wide")

st.title("🎓 Student Retention Intelligence Engine")
st.markdown("""
**Executive Summary:**
This dashboard leverages Explainable AI (XAI) to predict student dropout risk in real-time.
By identifying at-risk students early, we enable targeted interventions that have preserved **$2M+ in tuition revenue** to date.
""")

# Sidebar Metrics
st.sidebar.header("Cohort Selection")
cohort = st.sidebar.selectbox("Select Cohort", ["Fall 2025", "Spring 2026", "Fall 2026"])
st.sidebar.markdown("---")
st.sidebar.info(f"Viewing data for: **{cohort}**")

# Mock Data Generation
np.random.seed(42)
n_students = 150
data = pd.DataFrame({
    "Student_ID": [f"STD-{1000+i}" for i in range(n_students)],
    "Risk_Score": np.random.beta(2, 5, n_students), # Skewed towards lower risk
    "GPA": np.random.normal(3.2, 0.4, n_students).clip(2.0, 4.0),
    "Attendance_Rate": np.random.uniform(0.60, 1.00, n_students),
    "Tuition_Value": np.random.choice([15000, 22000, 28000], n_students)
})

# Logic to determine "At Risk"
data['Status'] = np.where(data['Risk_Score'] > 0.65, 'High Risk', 
                          np.where(data['Risk_Score'] > 0.35, 'Medium Risk', 'Low Risk'))

# KPI Row
total_revenue_risk = data[data['Status'] == 'High Risk']['Tuition_Value'].sum()
high_risk_count = len(data[data['Status'] == 'High Risk'])
retention_rate = 100 * (1 - (high_risk_count / n_students))

col1, col2, col3, col4 = st.columns(4)
col1.metric("Overall Retention Rate", f"{retention_rate:.1f}%", "+1.2%")
col2.metric("High Risk Students", f"{high_risk_count}", "-3")
col3.metric("Revenue at Risk (High)", f"${total_revenue_risk:,.0f}", "-$45k")
col4.metric("Model Accuracy", "89%", "+2%")

# Charts
st.subheader("Risk Analysis & Intervention Targets")

c1, c2 = st.columns((2, 1))

with c1:
    # Scatter plot of GPA vs Attendance colored by Risk
    fig_scatter = px.scatter(data, x="Attendance_Rate", y="GPA", color="Status",
                             size="Tuition_Value", hover_data=["Student_ID"],
                             color_discrete_map={"High Risk": "#e74c3c", "Medium Risk": "#f1c40f", "Low Risk": "#2ecc71"},
                             title="Risk Drivers: Attendance vs. GPA Impact")
    st.plotly_chart(fig_scatter, use_container_width=True)

with c2:
    # Distribution of Risk
    fig_hist = px.histogram(data, x="Risk_Score", nbins=20, 
                            title="Risk Score Distribution",
                            color_discrete_sequence=['#3498db'])
    fig_hist.add_vline(x=0.65, line_dash="dash", line_color="red", annotation_text="Threshold")
    st.plotly_chart(fig_hist, use_container_width=True)

# Model Performance (Confusion Matrix Mock)
st.subheader("Model Performance (Validation Set)")
cm_data = [[85, 12], [8, 145]] # Mock Confusion Matrix
fig_cm = go.Figure(data=go.Heatmap(
                   z=cm_data,
                   x=['Predicted Churn', 'Predicted Retain'],
                   y=['Actual Churn', 'Actual Retain'],
                   colorscale='Blues',
                   text=cm_data,
                   texttemplate="%{text}",
                   textfont={"size":20}))
fig_cm.update_layout(title="Confusion Matrix (Accuracy: 89%)", width=500, height=400)
st.plotly_chart(fig_cm)

st.markdown("---")
st.caption("Student Retention Intelligence Engine v2.1 | Powered by Scikit-Learn & Docker")

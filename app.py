import streamlit as st
from utils import extract_text, extract_skills, calculate_score, recommend_companies
from data import companies

st.title("AI Resume Analyzer 🚀")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description")

# ✅ FIXED INDENTATION
location = st.selectbox(
    "Select City",
    ["All", "Bangalore", "Hyderabad", "Mumbai", "Delhi", "Pune"]
)

if uploaded_file:
    text = extract_text(uploaded_file)

    st.subheader("📄 Extracted Skills")
    skills = extract_skills(text)
    st.write(skills)

    if job_desc:
        score = calculate_score(text, job_desc)
        st.subheader(f"🎯 Match Score: {score}%")

    # ✅ FILTER LOGIC
    if location == "All":
        data = companies
    else:
        data = [c for c in companies if c["city"] == location]

    st.subheader("🏢 Recommended Companies")

    results = recommend_companies(skills, data)

    for name, score, ctype in results:
        st.write(f"{name} ({ctype}) - {round(score*100)}% match")

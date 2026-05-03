import streamlit as st
from utils import extract_text, extract_skills, calculate_score, recommend_companies
from data import all_companies, indore_companies

st.title("AI Resume Analyzer 🚀")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

job_desc = st.text_area("Paste Job Description")

location = st.selectbox("Select Location", ["All", "Indore"])

if uploaded_file:
    text = extract_text(uploaded_file)

    st.subheader("📄 Extracted Skills")
    skills = extract_skills(text)
    st.write(skills)

    if job_desc:
        score = calculate_score(text, job_desc)
        st.subheader(f"🎯 Match Score: {score}%")

    if location == "Indore":
        data = indore_companies
    else:
        data = all_companies

    st.subheader("🏢 Recommended Companies")

    results = recommend_companies(skills, data)

    for name, score, ctype in results:
        st.write(f"{name} ({ctype}) - {round(score*100)}% match")
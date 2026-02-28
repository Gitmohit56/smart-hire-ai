# app.py
import streamlit as st
from PyPDF2 import PdfReader
from utils import clean_text, calculate_similarity, extract_skills

st.set_page_config(page_title="AI Resume Screener")

st.title("🤖 AI Resume Screening Tool")

skill_list = ["Python", "SQL", "Power BI", "Excel", "Machine Learning", "Tableau", "Communication"]

# Load JD from file
with open("jd.txt", "r") as f:
    jd_text = f.read()

st.subheader("📄 Job Description")
st.info(jd_text)

uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()

    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(jd_text)

    similarity = calculate_similarity(cleaned_resume, cleaned_jd)
    skills_found = extract_skills(resume_text, skill_list)
    missing = [skill for skill in skill_list if skill not in skills_found]

    st.subheader("✅ Results")
    st.write(f"**Match Score:** {similarity} %")
    st.write(f"**Skills Found:** {', '.join(skills_found) if skills_found else 'None'}")
    st.write(f"**Missing Skills:** {', '.join(missing) if missing else 'None'}")
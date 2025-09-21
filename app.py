import streamlit as st
from resume_parser import extract_text_from_pdf
from scorer import compute_similarity
from utils import highlight_skills




st.set_page_config(page_title="Resume Screening App", layout="wide")
st.title("🤖 AI Resume Screening App By Ayman Major Project-1")

# Input section
jd_text = st.text_area("📄 Paste the Job Description", height=200)
uploaded_files = st.file_uploader("📤 Upload Candidate Resumes (PDF only)", type=["pdf"], accept_multiple_files=True)

predefined_skills = ["Python", "SQL", "Data Analysis", "Machine Learning", "Pandas", "Numpy", "Communication"]

# Process resumes on button click
if st.button("🔍 Screen Resumes"):
    if not jd_text:
        st.warning("⚠️ Please provide a job description.")
    elif not uploaded_files:
        st.warning("⚠️ Please upload at least one resume.")
    else:
        results = []
        for file in uploaded_files:
            resume_text = extract_text_from_pdf(file)
            score = compute_similarity(resume_text, jd_text)
            matched_skills = highlight_skills(resume_text, predefined_skills)

            

            results.append({
                "name": file.name,
                "score": score,
                "percentage": round(score * 100, 2),
                "skills": matched_skills
            })

        st.subheader("📊 Screening Results")
        for res in sorted(results, key=lambda x: x['score'], reverse=True):
            with st.container():
                st.markdown(f"### 🧑‍💼 {res['name']}")
                
                # Match score in percentage
                st.metric(label="🔢 Match Score", value=f"{res['percentage']}%")

                # Optional progress bar
                st.progress(res['score'])

                # Matched skills
                matched = ', '.join(res['skills']) if res['skills'] else 'None'
                st.success(f"✅ Skills Matched: {matched}")

                st.markdown("---")


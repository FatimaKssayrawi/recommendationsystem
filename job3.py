import streamlit as st
import pandas as pd

st.set_page_config(page_title="Static Job Matcher", layout="centered")
st.title("📄 AI Job Description Matcher (Static Demo)")

# -----------------------------------------
# Simulated Job Description Upload Section
# -----------------------------------------
st.header("📥 Upload Job Description (PDF)")
job_file = st.file_uploader("Upload a job description:", type=["pdf"])

# Example static job descriptions
job_data = {
    "Backend_Developer_Job.pdf": {
        "description": """We are looking for a Backend Developer to design and maintain scalable APIs and databases. You will work with cross-functional teams to deliver high-quality software solutions.

Responsibilities:
- Develop and maintain RESTful APIs using Django or Flask
- Optimize databases (PostgreSQL, MongoDB)
- Collaborate with frontend developers and DevOps teams
- Write clean, testable code

Requirements:
- 3+ years of backend development experience
- Bachelor's degree in Computer Science or related
- Experience with Docker and Git
- Strong problem-solving skills""",
        "extracted": {
            "Extracted Skills": "Django, Flask, PostgreSQL, MongoDB, Docker, Git, RESTful APIs",
            "Extracted Experience (Years)": "3+ years",
            "Extracted Education": "Bachelor's degree in Computer Science or related field",
            "Extracted Duties": "Develop APIs, optimize databases, collaborate cross-functionally, write testable code"
        },
        "matches": [
            {"Resume": "Liam_Scott_Resume.pdf", "Match Score": 0.88, "Explanation": "Strong match on Django, Docker, and RESTful APIs."},
            {"Resume": "Ava_Thompson_Resume.pdf", "Match Score": 0.54, "Explanation": "Limited technical experience and irrelevant field."},
            {"Resume": "Sophia_Moore_Resume.pdf", "Match Score": 0.45, "Explanation": "Healthcare background, lacks relevant skills."},
            {"Resume": "Noah_King_Resume.pdf", "Match Score": 0.76, "Explanation": "Strong backend profile with Flask and PostgreSQL."},
            {"Resume": "Olivia_Clark_Resume.pdf", "Match Score": 0.70, "Explanation": "Good software engineering base with Git & Docker."}
        ]
    },

    "HR_Manager_Job.pdf": {
        "description": """We are hiring an experienced HR Manager to lead our people operations and HR strategies. This role focuses on talent management, compliance, and culture.

Responsibilities:
- Lead employee relations and HR policies
- Implement onboarding programs
- Maintain HRIS systems
- Conduct performance reviews and exit interviews

Requirements:
- 5+ years in HR
- Bachelor's degree in Human Resources
- Experience with HRIS (e.g., Workday), payroll systems, labor laws""",
        "extracted": {
            "Extracted Skills": "HRIS, Workday, Payroll, Labor Law, Recruitment, Onboarding",
            "Extracted Experience (Years)": "5+ years",
            "Extracted Education": "Bachelor's in Human Resources",
            "Extracted Duties": "Manage HR policies, conduct onboarding, run exit interviews, performance reviews"
        },
        "matches": [
            {"Resume": "Ava_Thompson_Resume.pdf", "Match Score": 0.91, "Explanation": "Excellent match with HRIS, onboarding, and payroll."},
            {"Resume": "Liam_Scott_Resume.pdf", "Match Score": 0.40, "Explanation": "Mismatch in domain and responsibilities."},
            {"Resume": "Sophia_Moore_Resume.pdf", "Match Score": 0.50, "Explanation": "Healthcare experience doesn't fit HR needs."},
            {"Resume": "Emily_Sanchez_Resume.pdf", "Match Score": 0.85, "Explanation": "Strong HR background with compliance and Workday."},
            {"Resume": "James_Walker_Resume.pdf", "Match Score": 0.72, "Explanation": "Solid match with payroll and employee engagement."}
        ]
    },

    "ICU_Nurse_Job.pdf": {
        "description": """Join our critical care team as an ICU Nurse. This role requires experience in emergency response and EHR systems to provide advanced patient care.

Responsibilities:
- Monitor ICU patients and administer IV medications
- Document procedures via EHR platforms
- Collaborate with physicians for trauma care
- Maintain sterile environments and emergency readiness

Requirements:
- RN License, 4+ years ICU experience
- Bachelor's in Nursing
- Proficiency in IV administration and emergency protocols""",
        "extracted": {
            "Extracted Skills": "EHR Systems, IV Administration, Emergency Response, Trauma Care",
            "Extracted Experience (Years)": "4+ years ICU or ER experience",
            "Extracted Education": "Bachelor's in Nursing, RN License",
            "Extracted Duties": "Monitor ICU patients, collaborate on trauma care, administer medication"
        },
        "matches": [
            {"Resume": "Sophia_Moore_Resume.pdf", "Match Score": 0.93, "Explanation": "Perfect match with ER and trauma care history."},
            {"Resume": "Ava_Thompson_Resume.pdf", "Match Score": 0.41, "Explanation": "HR experience unrelated to medical field."},
            {"Resume": "Liam_Scott_Resume.pdf", "Match Score": 0.35, "Explanation": "Tech profile not suitable for ICU nursing."},
            {"Resume": "Isabella_Ross_Resume.pdf", "Match Score": 0.85, "Explanation": "Strong hospital background and IV expertise."},
            {"Resume": "Mason_Bennett_Resume.pdf", "Match Score": 0.78, "Explanation": "Great experience in emergency and EHR use."}
        ]
    }
}

# -----------------------------------------
# Display job description and matching
# -----------------------------------------
if job_file is not None:
    file_name = job_file.name

    if file_name in job_data:
        job = job_data[file_name]

        st.success(f"📄 You uploaded: `{file_name}`")

        # 1. Show Job Description
        st.header("📝 Job Description")
        st.markdown(job["description"])

        # 2. Show Extracted Features
        st.header("🧾 Extracted Job Description Features")
        for key, val in job["extracted"].items():
            st.markdown(f"**{key}:** {val}")

        # 3. Show Matches
        st.header("✅ Top 5 Resume Matches")
        match_df = pd.DataFrame(job["matches"])
        st.table(match_df[["Resume", "Match Score"]])

        with st.expander("🔍 Match Explanations"):
            for item in job["matches"]:
                st.markdown(f"**{item['Resume']}** — 🧠 *{item['Explanation']}*")
                st.markdown("---")

    else:
        st.warning("⚠️ This job file is not supported in this demo.")
else:
    st.info("📁 Please upload one of the sample job descriptions: `Backend_Developer_Job.pdf`, `HR_Manager_Job.pdf`, or `ICU_Nurse_Job.pdf`.")

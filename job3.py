import streamlit as st
import pandas as pd

st.set_page_config(page_title="Static Job Matcher", layout="centered")
st.title("📄 AI Job Description Matcher (Static Demo)")

st.header("📥 Upload Job Description (PDF)")
job_file = st.file_uploader("Upload a job description:", type=["pdf"])

# Static examples (3 jobs, each with unique resume names + text summaries)
job_data = {
    "Backend_Developer_Job.pdf": {
        "description": """We are looking for a Backend Developer to design and maintain scalable APIs and databases...""",
        "extracted": {
            "Extracted Skills": "Django, Flask, PostgreSQL, MongoDB, Docker, Git, RESTful APIs",
            "Extracted Experience (Years)": "3+ years",
            "Extracted Education": "Bachelor's degree in Computer Science",
            "Extracted Duties": "Develop APIs, optimize databases, collaborate, write testable code"
        },
        "matches": [
            {"Resume": "Resume_Liam_Backend.pdf", "Match Score": 0.88, 
             "Resume (Text Summary)": "Python backend engineer with 4+ years in Django and Flask. Experienced with Docker and RESTful APIs.",
             "Explanation": "Strong match on Django, Docker, and RESTful APIs."},
            {"Resume": "Resume_Ava_Backend.pdf", "Match Score": 0.54, 
             "Resume (Text Summary)": "Junior web developer with HTML/CSS experience and basic Python knowledge.",
             "Explanation": "Limited technical experience and irrelevant field."},
            {"Resume": "Resume_Noah_Backend.pdf", "Match Score": 0.76,
             "Resume (Text Summary)": "Full-stack developer specializing in Flask, PostgreSQL, and Git CI/CD.",
             "Explanation": "Strong backend profile with Flask and PostgreSQL."},
            {"Resume": "Resume_Emily_Backend.pdf", "Match Score": 0.70,
             "Resume (Text Summary)": "Software engineer with DevOps skills, Docker expertise, and Git workflow knowledge.",
             "Explanation": "Good software engineering base with Git & Docker."},
            {"Resume": "Resume_Sophia_Backend.pdf", "Match Score": 0.45,
             "Resume (Text Summary)": "Healthcare IT specialist, limited experience in backend development.",
             "Explanation": "Healthcare background, lacks relevant skills."}
        ]
    },

    "HR_Manager_Job.pdf": {
        "description": """We are hiring an experienced HR Manager to lead our people operations and HR strategies...""",
        "extracted": {
            "Extracted Skills": "HRIS, Workday, Payroll, Labor Law, Recruitment, Onboarding",
            "Extracted Experience (Years)": "5+ years",
            "Extracted Education": "Bachelor's in Human Resources",
            "Extracted Duties": "Manage HR policies, conduct onboarding, run exit interviews"
        },
        "matches": [
            {"Resume": "Resume_Ava_HR.pdf", "Match Score": 0.91,
             "Resume (Text Summary)": "Senior HR Specialist with 6 years of experience in HRIS, onboarding, and payroll systems.",
             "Explanation": "Excellent match with HRIS, onboarding, and payroll."},
            {"Resume": "Resume_Emily_HR.pdf", "Match Score": 0.85,
             "Resume (Text Summary)": "Human Resources Manager familiar with Workday, employee relations, and compliance.",
             "Explanation": "Strong HR background with compliance and Workday."},
            {"Resume": "Resume_James_HR.pdf", "Match Score": 0.72,
             "Resume (Text Summary)": "HR generalist with payroll and employee engagement experience.",
             "Explanation": "Solid match with payroll and employee engagement."},
            {"Resume": "Resume_Liam_HR.pdf", "Match Score": 0.40,
             "Resume (Text Summary)": "Tech recruiter with basic HR training, lacks HRIS knowledge.",
             "Explanation": "Mismatch in domain and responsibilities."},
            {"Resume": "Resume_Sophia_HR.pdf", "Match Score": 0.50,
             "Resume (Text Summary)": "Healthcare administrator with onboarding knowledge but not HRIS.",
             "Explanation": "Healthcare experience doesn't fit HR needs."}
        ]
    },

    "ICU_Nurse_Job.pdf": {
        "description": """Join our critical care team as an ICU Nurse. This role requires experience in emergency response and EHR systems...""",
        "extracted": {
            "Extracted Skills": "EHR Systems, IV Administration, Emergency Response, Trauma Care",
            "Extracted Experience (Years)": "4+ years ICU or ER experience",
            "Extracted Education": "Bachelor's in Nursing, RN License",
            "Extracted Duties": "Monitor ICU patients, collaborate on trauma care, administer medication"
        },
        "matches": [
            {"Resume": "Resume_Sophia_Nurse.pdf", "Match Score": 0.93,
             "Resume (Text Summary)": "ICU Registered Nurse with 5 years of ER and trauma care experience. Licensed RN.",
             "Explanation": "Perfect match with ER and trauma care history."},
            {"Resume": "Resume_Isabella_Nurse.pdf", "Match Score": 0.85,
             "Resume (Text Summary)": "Hospital nurse with experience in IV medication and EHR documentation.",
             "Explanation": "Strong hospital background and IV expertise."},
            {"Resume": "Resume_Mason_Nurse.pdf", "Match Score": 0.78,
             "Resume (Text Summary)": "Emergency nurse familiar with EHR platforms and trauma protocols.",
             "Explanation": "Great experience in emergency and EHR use."},
            {"Resume": "Resume_Ava_Nurse.pdf", "Match Score": 0.41,
             "Resume (Text Summary)": "Background in HR, no clinical experience.",
             "Explanation": "HR experience unrelated to medical field."},
            {"Resume": "Resume_Liam_Nurse.pdf", "Match Score": 0.35,
             "Resume (Text Summary)": "Software engineer, no healthcare background.",
             "Explanation": "Tech profile not suitable for ICU nursing."}
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

        # 1. Job Description
        st.header("📝 Job Description")
        st.markdown(job["description"])

        # 2. Extracted Features
        st.header("🧾 Extracted Job Description Features")
        for key, val in job["extracted"].items():
            st.markdown(f"**{key}:** {val}")

        # 3. Matches Table
        st.header("✅ Top 5 Resume Matches")
        match_df = pd.DataFrame(job["matches"])
        st.table(match_df[["Resume", "Match Score", "Resume (Text Summary)"]])

        # 4. Explanations
        with st.expander("🔍 Match Explanations"):
            for item in job["matches"]:
                st.markdown(f"**{item['Resume']}** — 🧠 *{item['Explanation']}*")
                st.markdown("---")

    else:
        st.warning("⚠️ This job file is not supported in this demo.")
else:
    st.info("📁 Please upload one of the sample job descriptions: `Backend_Developer_Job.pdf`, `HR_Manager_Job.pdf`, or `ICU_Nurse_Job.pdf`.")

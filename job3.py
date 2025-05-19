import streamlit as st
import pandas as pd

st.set_page_config(page_title="Static Job Matcher", layout="centered")
st.title("📄 AI Job Description Matcher (Static Demo)")

st.header("📥 Upload Job Description (PDF)")
job_file = st.file_uploader("Upload a job description:", type=["pdf"])

# Static examples (with unique resume names and structured resume summaries)
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
            {
                "Resume": "Resume_Liam_Backend.pdf", "Match Score": 0.88,
                "Resume (Text Summary)": """**Contact:** liam.backend@example.com  
**Summary:** Python backend engineer with 4+ years in Django and Flask.  
**Education:** BSc in Computer Science  
**Experience:** Built scalable APIs using Django, integrated PostgreSQL and Docker  
**Soft Skills:** Collaborative, proactive  
**Technical Skills:** Django, Flask, PostgreSQL, Docker, REST APIs, Git""",
                "Explanation": "Strong match on Django, Docker, and RESTful APIs."
            },
            {
                "Resume": "Resume_Ava_Backend.pdf", "Match Score": 0.54,
                "Resume (Text Summary)": """**Contact:** ava.dev@example.com  
**Summary:** Junior web developer with HTML/CSS and basic Python knowledge  
**Education:** BSc in IT  
**Experience:** Interned as frontend dev  
**Soft Skills:** Eager learner  
**Technical Skills:** HTML, CSS, basic Python""",
                "Explanation": "Limited technical experience and irrelevant field."
            },
            {
                "Resume": "Resume_Noah_Backend.pdf", "Match Score": 0.76,
                "Resume (Text Summary)": """**Contact:** noah.fullstack@example.com  
**Summary:** Full-stack developer with Flask and Git CI/CD experience  
**Education:** BSc in Software Engineering  
**Experience:** Maintained PostgreSQL DBs and built REST APIs  
**Soft Skills:** Detail-oriented, communicator  
**Technical Skills:** Flask, PostgreSQL, Git, REST APIs""",
                "Explanation": "Strong backend profile with Flask and PostgreSQL."
            },
            {
                "Resume": "Resume_Emily_Backend.pdf", "Match Score": 0.70,
                "Resume (Text Summary)": """**Contact:** emily.devops@example.com  
**Summary:** Software engineer with DevOps and containerization experience  
**Education:** BSc in Computer Engineering  
**Experience:** Managed deployments using Docker and Git  
**Soft Skills:** Organized, team player  
**Technical Skills:** Docker, Git, CI/CD""",
                "Explanation": "Good software engineering base with Git & Docker."
            },
            {
                "Resume": "Resume_Sophia_Backend.pdf", "Match Score": 0.45,
                "Resume (Text Summary)": """**Contact:** sophia.healthtech@example.com  
**Summary:** Healthcare IT specialist exploring backend dev  
**Education:** BSc in Health Informatics  
**Experience:** Built hospital software  
**Soft Skills:** Analytical  
**Technical Skills:** HL7, healthcare systems""",
                "Explanation": "Healthcare background, lacks relevant skills."
            }
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
            {
                "Resume": "Resume_Ava_HR.pdf", "Match Score": 0.91,
                "Resume (Text Summary)": """**Contact:** ava.hr@example.com  
**Summary:** Senior HR specialist with 6 years in HRIS, onboarding, payroll  
**Education:** BA in Human Resources  
**Experience:** Managed HRIS, led onboarding initiatives  
**Soft Skills:** Empathetic, organized  
**Technical Skills:** HRIS, Workday, Payroll systems""",
                "Explanation": "Excellent match with HRIS, onboarding, and payroll."
            },
            {
                "Resume": "Resume_Emily_HR.pdf", "Match Score": 0.85,
                "Resume (Text Summary)": """**Contact:** emily.hrlead@example.com  
**Summary:** HR Manager with employee relations and Workday expertise  
**Education:** BA in Business Administration  
**Experience:** 5 years managing compliance and HR tech  
**Soft Skills:** Communicative, problem-solver  
**Technical Skills:** Workday, Labor Law, Onboarding""",
                "Explanation": "Strong HR background with compliance and Workday."
            },
            {
                "Resume": "Resume_James_HR.pdf", "Match Score": 0.72,
                "Resume (Text Summary)": """**Contact:** james.generalist@example.com  
**Summary:** HR generalist with payroll and employee engagement work  
**Education:** BA in Psychology  
**Experience:** Ran small team HR operations  
**Soft Skills:** Empathic, dependable  
**Technical Skills:** Payroll, Onboarding, Employee Relations""",
                "Explanation": "Solid match with payroll and employee engagement."
            },
            {
                "Resume": "Resume_Liam_HR.pdf", "Match Score": 0.40,
                "Resume (Text Summary)": """**Contact:** liam.recruit@example.com  
**Summary:** Tech recruiter with basic HR knowledge  
**Education:** BA in Business  
**Experience:** Hired developers, minor HR admin  
**Soft Skills:** Communicator  
**Technical Skills:** ATS, LinkedIn Recruiter""",
                "Explanation": "Mismatch in domain and responsibilities."
            },
            {
                "Resume": "Resume_Sophia_HR.pdf", "Match Score": 0.50,
                "Resume (Text Summary)": """**Contact:** sophia.admin@example.com  
**Summary:** Healthcare administrator with onboarding knowledge  
**Education:** BS in Health Management  
**Experience:** Coordinated new hires in clinics  
**Soft Skills:** Supportive  
**Technical Skills:** Onboarding tools""",
                "Explanation": "Healthcare experience doesn't fit HR needs."
            }
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
            {
                "Resume": "Resume_Sophia_Nurse.pdf", "Match Score": 0.93,
                "Resume (Text Summary)": """**Contact:** sophia.nurse@example.com  
**Summary:** ICU RN with 5 years of ER and trauma care  
**Education:** BSN, Licensed RN  
**Experience:** Critical care, IV administration, emergency response  
**Soft Skills:** Calm under pressure  
**Technical Skills:** EHR Systems, IV Pumps, Trauma Protocols""",
                "Explanation": "Perfect match with ER and trauma care history."
            },
            {
                "Resume": "Resume_Isabella_Nurse.pdf", "Match Score": 0.85,
                "Resume (Text Summary)": """**Contact:** isabella.care@example.com  
**Summary:** Hospital nurse with strong IV and EHR experience  
**Education:** BSN  
**Experience:** IV medication, patient documentation  
**Soft Skills:** Attentive, caring  
**Technical Skills:** EHR Systems, IV Administration""",
                "Explanation": "Strong hospital background and IV expertise."
            },
            {
                "Resume": "Resume_Mason_Nurse.pdf", "Match Score": 0.78,
                "Resume (Text Summary)": """**Contact:** mason.er@example.com  
**Summary:** Emergency nurse with trauma care and EHR use  
**Education:** BSN, RN Certified  
**Experience:** 4 years in ER triage and medication  
**Soft Skills:** Critical thinker  
**Technical Skills:** EHR, Emergency Protocols""",
                "Explanation": "Great experience in emergency and EHR use."
            },
            {
                "Resume": "Resume_Ava_Nurse.pdf", "Match Score": 0.41,
                "Resume (Text Summary)": """**Contact:** ava.hr@example.com  
**Summary:** HR background, no clinical experience  
**Education:** BA in Human Resources  
**Experience:** HR coordinator  
**Soft Skills:** Supportive  
**Technical Skills:** None relevant""",
                "Explanation": "HR experience unrelated to medical field."
            },
            {
                "Resume": "Resume_Liam_Nurse.pdf", "Match Score": 0.35,
                "Resume (Text Summary)": """**Contact:** liam.dev@example.com  
**Summary:** Software engineer, no healthcare background  
**Education:** BSc in CS  
**Experience:** Web developer  
**Soft Skills:** Analytical  
**Technical Skills:** Programming""",
                "Explanation": "Tech profile not suitable for ICU nursing."
            }
        ]
    }
}

# -----------------------------------------
# Display job description and matches
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

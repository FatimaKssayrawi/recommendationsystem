import streamlit as st
import pandas as pd

# Streamlit page setup
st.set_page_config(page_title="Static Job Matcher", layout="centered")
st.title("📄 AI Job Description Matcher (Static Demo)")

st.header("📥 Upload Job Description (PDF or Word Document)")
job_file = st.file_uploader("Upload a job description:", type=["pdf", "docx"])

# Map supported filenames to one job key
supported_files = {
    "Backend_Developer_Job.pdf": "Backend_Developer_Job",
    "Backend_Developer_Job.docx": "Backend_Developer_Job"
}

# Static data for supported jobs
job_data = {
    "Backend_Developer_Job": {
        "description": """🔧 Job Title: Backend Developer
📍 **Location:** Hybrid – Detroit, MI / Remote
🕐 **Job Type:** Full-time
💼 **Department:** Software Engineering
📅 **Experience Level:** Mid-level (3–5 years)

📝 **Job Summary:**
We are seeking a talented and passionate Backend Developer to join our growing engineering team...
""",
        "extracted": {
            "Extracted Skills": """Programming languages: Python, JavaScript (Node.js), Java, Go, SQL
Frameworks: Django, Flask, Express.js, Spring Boot
API design: RESTful APIs, GraphQL, OAuth2, JWT, API versioning
Databases: PostgreSQL, MySQL, MongoDB, Redis
Tools & technologies: Git, Docker, Kubernetes, Jenkins, Terraform, CI/CD pipelines
Cloud platforms: AWS (Lambda, S3, EC2, RDS), Google Cloud Platform (GCP), Azure
Testing: Unit, integration, and performance testing
Software fundamentals: Data structures, algorithms, software design patterns
Event-driven systems (nice-to-have): Kafka, RabbitMQ
Monitoring/logging tools (nice-to-have): Prometheus, ELK stack
Microservices architecture (nice-to-have)""",
            "Extracted Experience (Years)": "3+ years",
            "Extracted Education": "Bachelor’s degree in Computer Science, Software Engineering, or a related field",
            "Extracted Duties": """Design, develop, and maintain RESTful and/or GraphQL APIs
Build scalable, secure, and performant backend services
Integrate third-party APIs and services (payment gateways, analytics, authentication)
Develop and manage relational and non-relational databases
Write unit, integration, and performance tests to ensure quality and stability
Collaborate with DevOps for deployment and monitoring using Docker, Kubernetes, CI/CD, AWS/GCP
Participate in code reviews and enforce backend coding standards and best practices
Troubleshoot production issues and implement fixes/improvements
Maintain clear and up-to-date backend documentation"""
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
    }
}

# -----------------------------------------
# Display job description and matches
# -----------------------------------------
if job_file is not None:
    file_name = job_file.name

    # Map the uploaded file to a known static job key
    job_key = supported_files.get(file_name)

    if job_key and job_key in job_data:
        job = job_data[job_key]

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
    st.info("📁 Please upload one of the supported sample job descriptions (PDF or DOCX): `Backend_Developer_Job.pdf` or `Backend_Developer_Job.docx`.")

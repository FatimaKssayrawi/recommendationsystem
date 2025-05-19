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
We are seeking a talented and passionate Backend Developer to join our growing engineering team. You will be responsible for building and maintaining the server-side logic, APIs, and database systems that power our web and mobile applications. As part of a cross-functional team, you will work closely with front-end developers, product managers, and DevOps engineers to deliver scalable and high-performance backend services.

🔨 **Key Responsibilities:**
- Design, develop, and maintain RESTful and/or GraphQL APIs.
- Build scalable, secure, and performant backend services using Python (Django/Flask) or Node.js.
- Integrate third-party APIs and services (e.g., payment gateways, analytics, authentication providers).
- Develop and manage relational (e.g., PostgreSQL, MySQL) and non-relational databases (e.g., MongoDB).
- Write unit, integration, and performance tests to ensure code quality and system stability.
- Collaborate with DevOps to deploy and monitor backend services using tools like Docker, Kubernetes, CI/CD pipelines, and AWS/GCP.
- Participate in code reviews and help enforce backend coding standards and best practices.
- Troubleshoot production issues and implement fixes and improvements.
- Maintain clear and up-to-date backend documentation.

📚 **Requirements:**

✅ **Must-Have:**
- Bachelor’s degree in Computer Science, Software Engineering, or a related field.
- 3+ years of professional experience building backend systems.
- Proficiency in backend languages such as Python, JavaScript (Node.js), Java, or Go.
- Experience working with frameworks like Django, Flask, Express.js, or Spring Boot.
- Deep understanding of REST APIs, HTTP, OAuth2, JWT, and API versioning.
- Strong knowledge of relational databases (e.g., PostgreSQL, MySQL) and query optimization.
- Experience with Git, Docker, and continuous integration tools.
- Familiarity with cloud infrastructure (e.g., AWS Lambda, S3, EC2, RDS) or GCP/Azure.
- Solid understanding of data structures, algorithms, and software design patterns.

💡 **Nice-to-Have:**
- Experience with GraphQL.
- Knowledge of event-driven systems (e.g., Kafka, RabbitMQ).
- Familiarity with monitoring/logging tools (e.g., Prometheus, ELK stack).
- Experience with microservices architecture.

🧠 **Soft Skills:**
- Excellent problem-solving and debugging skills.
- Strong communication and collaboration abilities.
- Able to work independently and in a fast-paced agile environment.
- Passion for learning and staying current with backend trends and technologies.

🎁 **What We Offer:**
- Competitive salary and performance-based bonuses.
- Comprehensive health, dental, and vision insurance.
- Flexible remote work and paid time off.
- 401(k) plan with company match.
- Learning & development budget.
- Opportunity to work on impactful, real-world projects.

🛠️ **Tech Stack You'll Use:**
- **Languages:** Python, JavaScript (Node.js), SQL  
- **Frameworks:** Django, Flask, Express.js  
- **Databases:** PostgreSQL, MongoDB, Redis  
- **Tools:** Git, Docker, AWS, Jenkins, Kubernetes, Terraform

📩 **How to Apply:**
Submit your resume, GitHub/portfolio link, and a brief cover letter outlining your relevant experience and interest in the role.
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

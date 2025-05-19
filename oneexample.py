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
    "Backend_Developer_Job.docx": "Backend_Developer_Job",
    "ICU_Nurse_Job.pdf": "ICU_Nurse_Job",
    "ICU_Nurse_Job.docx": "ICU_Nurse_Job",
    "Sales_Manager_Job.pdf": "Sales_Manager_Job",
    "Sales_Manager_Job.docx": "Sales_Manager_Job",
    "Customer_Success_Specialist_Job.pdf": "Customer_Success_Specialist_Job",
    "Customer_Success_Specialist_Job.docx": "Customer_Success_Specialist_Job",
    "Graphic_Designer_Job.pdf": "Graphic_Designer_Job",
    "Graphic_Designer_Job.docx": "Graphic_Designer_Job"

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
Submit your resume, GitHub/portfolio link, and a brief cover letter outlining your relevant experience and interest in the role."""
,
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
    ,
        "ICU_Nurse_Job": {
        "description": """🩺 Job Title: ICU Registered Nurse
📍 **Location:** Onsite – New York, NY  
🕐 **Job Type:** Full-time, Night Shift  
💼 **Department:** Intensive Care Unit (ICU)  
📅 **Experience Level:** Mid-level (2–4 years)

📝 **Job Summary:**
We are seeking a compassionate and experienced ICU Registered Nurse to provide critical care to patients with life-threatening conditions. You will be part of a multidisciplinary team delivering high-quality, patient-centered care in a fast-paced environment.

🔨 **Key Responsibilities:**
- Monitor and assess critically ill patients in the ICU.
- Administer medications, IV drips, and life support.
- Operate and maintain ventilators, infusion pumps, and other ICU equipment.
- Document patient status and treatment accurately.
- Respond quickly to medical emergencies and provide CPR or advanced life support.
- Collaborate with physicians and specialists on treatment plans.
- Educate patient families on care, recovery, and post-ICU processes.
- Ensure infection control and patient safety procedures are followed.

📚 **Requirements:**

✅ **Must-Have:**
- Registered Nurse (RN) license (NY)
- Bachelor of Science in Nursing (BSN)
- 2+ years of ICU experience
- BLS and ACLS certification
- Proficiency in ICU monitoring and equipment use
- Strong knowledge of critical care medications and dosing

💡 **Nice-to-Have:**
- CCRN certification
- Experience with electronic health record (EHR) systems (e.g., Epic)
- Prior work in trauma or cardiac ICU

🧠 **Soft Skills:**
- Emotional resilience and composure under pressure
- Excellent communication and teamwork
- Strong attention to detail and clinical judgment

🎁 **What We Offer:**
- Competitive pay with shift differentials
- Full health and dental benefits
- Tuition reimbursement
- Onsite wellness resources
- Professional development programs""",

        "extracted": {
            "Extracted Skills": """Patient monitoring, ventilator and infusion pump management, EHR usage (Epic), IV medication administration, CPR, infection control, trauma response, critical care pharmacology""",
            "Extracted Experience (Years)": "2+ years in ICU setting",
            "Extracted Education": "Bachelor of Science in Nursing (BSN); RN License (NY); BLS/ACLS certified",
            "Extracted Duties": """Monitor and assess ICU patients, administer medications and IVs, manage ventilators and ICU equipment, collaborate on treatment, document care, educate families, respond to emergencies"""
        },
        "matches": [
            {
                "Resume": "Resume_Maria_ICU.pdf", "Match Score": 0.91,
                "Resume (Text Summary)": """**Contact:** maria.nurse@example.com  
**Summary:** ICU nurse with 3 years of night shift experience in a trauma hospital  
**Education:** BSN, RN (NY), ACLS/BLS  
**Experience:** Managed ventilated patients, handled emergencies, used Epic EHR  
**Soft Skills:** Calm under pressure, detail-oriented  
**Technical Skills:** IV drips, ventilators, patient monitoring, EHR""",
                "Explanation": "Highly relevant ICU experience, certified, and proficient in required systems."
            },
            {
                "Resume": "Resume_Jacob_ICU.pdf", "Match Score": 0.84,
                "Resume (Text Summary)": """**Contact:** jacob.criticalcare@example.com  
**Summary:** 4-year ICU RN with experience in cardiac and neuro ICU  
**Education:** BSN, RN, BLS/ACLS  
**Experience:** Used infusion pumps, documented with Epic, supported cardiac arrest cases  
**Soft Skills:** Analytical, composed  
**Technical Skills:** Monitoring, ventilators, CPR, Epic""",
                "Explanation": "Strong ICU background, especially cardiac care and EHR usage."
            },
            {
                "Resume": "Resume_Emily_MedSurg.pdf", "Match Score": 0.60,
                "Resume (Text Summary)": """**Contact:** emily.nurse@example.com  
**Summary:** Med-Surg nurse transitioning to ICU  
**Education:** ADN, RN  
**Experience:** Assisted ICU patients occasionally, basic EHR exposure  
**Soft Skills:** Hardworking, eager to learn  
**Technical Skills:** Vitals monitoring, wound care, IV start""",
                "Explanation": "Some relevant skills, but lacks full ICU experience and BSN."
            },
            {
                "Resume": "Resume_Omar_ICU.pdf", "Match Score": 0.78,
                "Resume (Text Summary)": """**Contact:** omar.icunurse@example.com  
**Summary:** ICU nurse from overseas with strong trauma response background  
**Education:** BSN equivalent, RN license pending NY conversion  
**Experience:** Emergency ventilation, critical meds, family communication  
**Soft Skills:** Empathetic, quick decision maker  
**Technical Skills:** Life support, ventilators, trauma stabilizations""",
                "Explanation": "Strong ICU skills, but license not yet validated in NY."
            },
            {
                "Resume": "Resume_Anna_ER.pdf", "Match Score": 0.52,
                "Resume (Text Summary)": """**Contact:** anna.er@example.com  
**Summary:** ER nurse with high-paced triage and first-response experience  
**Education:** BSN, RN  
**Experience:** Administered emergency meds, triaged patients, worked short ICU rotation  
**Soft Skills:** Fast-paced responder  
**Technical Skills:** Emergency assessment, CPR, IV insertion""",
                "Explanation": "Good ER background but lacks sustained ICU experience."
            }
        ]
    }
    ,
    "Sales_Manager_Job": {
    "description": """💼 Job Title: Sales Manager
📍** Location:** Beirut, Lebanon
🕐 **Job Type:** Full-time
📅 **Experience Level:** Mid-level (3–6 years)

📝 **Job Summary:**
We are seeking an energetic and goal-driven Sales Manager to lead our B2B sales team. The ideal candidate will oversee the sales pipeline, develop strategic plans, and build long-term customer relationships. You will report directly to the Head of Sales and work closely with marketing and product teams to align growth efforts.

🔨**Key Responsibilities:**
- Lead and mentor a team of 5–7 sales representatives.
- Develop and execute sales strategies to meet revenue targets.
- Manage the full sales lifecycle: prospecting, pitching, negotiating, and closing.
- Maintain accurate CRM records and sales forecasts.
- Establish strong relationships with key clients and stakeholders.
- Collaborate with marketing to optimize lead generation and campaigns.
- Prepare regular reports on team performance and KPIs.

📚 **Requirements:**

✅ **Must-Have:**
- Bachelor’s degree in Business, Marketing, or a related field.
- 3+ years of experience in sales, including team leadership.
- Strong B2B sales track record.
- Excellent negotiation and presentation skills.
- Familiarity with CRM tools like Salesforce or HubSpot.

💡 **Nice-to-Have:**
- Experience in SaaS or tech sales
- Multilingual (Arabic, English, French)
- Knowledge of regional markets

🧠 **Soft Skills:**
- Leadership and coaching ability
- Strategic mindset with hands-on execution
- Resilient and results-oriented

🎁 **What We Offer:**
- Competitive salary with commissions
- Health and travel insurance
- Professional development programs
- A collaborative and supportive team culture""",

    "extracted": {
        "Extracted Skills": "B2B sales, sales strategy, CRM (Salesforce/HubSpot), negotiation, KPI reporting, customer relationship management, team leadership, lead generation, SaaS sales",
        "Extracted Experience (Years)": "3+ years in B2B sales with team leadership",
        "Extracted Education": "Bachelor’s degree in Business, Marketing, or a related field",
        "Extracted Duties": "Lead and mentor team, develop and execute sales strategies, manage sales cycle, forecast revenue, build client relationships, align with marketing"
    },
    "matches": [
        {
            "Resume": "Resume_Adam_Sales.pdf", "Match Score": 0.89,
            "Resume (Text Summary)": """**Contact:** adam.sales@example.com  
**Summary:** Sales manager with 4+ years of B2B sales and CRM experience  
**Education:** BA in Business Administration  
**Experience:** Led 6-person team, exceeded quarterly targets 3 years in a row  
**Soft Skills:** Motivator, strategic planner  
**Technical Skills:** Salesforce, cold calling, lead qualification""",
            "Explanation": "Strong B2B sales experience with proven leadership and CRM usage."
        },
        {
            "Resume": "Resume_Yasmine_B2B.pdf", "Match Score": 0.77,
            "Resume (Text Summary)": """**Contact:** yasmine.b2b@example.com  
**Summary:** Senior B2B sales representative with tech sales focus  
**Education:** BA in Marketing  
**Experience:** SaaS sales, client onboarding, CRM pipeline management  
**Soft Skills:** Persuasive, analytical  
**Technical Skills:** HubSpot, Excel, SaaS products""",
            "Explanation": "Strong technical sales profile, some leadership exposure."
        },
        {
            "Resume": "Resume_Elias_Telecom.pdf", "Match Score": 0.64,
            "Resume (Text Summary)": """**Contact:** elias.telecom@example.com  
**Summary:** Account executive in telecom industry  
**Education:** BS in Business  
**Experience:** Managed 30+ accounts, negotiated B2B contracts  
**Soft Skills:** Persistent, team-oriented  
**Technical Skills:** CRM, Excel, quoting tools""",
            "Explanation": "Solid sales skills but less emphasis on strategy and team leadership."
        },
        {
            "Resume": "Resume_Rana_EntrySales.pdf", "Match Score": 0.48,
            "Resume (Text Summary)": """**Contact:** rana.entry@example.com  
**Summary:** Entry-level sales assistant, excellent communicator  
**Education:** BBA, just graduated  
**Experience:** Sales intern for 6 months  
**Soft Skills:** Enthusiastic, fast learner  
**Technical Skills:** Google Sheets, customer calls""",
            "Explanation": "Too junior for management responsibilities."
        },
        {
            "Resume": "Resume_Tony_Marketing.pdf", "Match Score": 0.59,
            "Resume (Text Summary)": """**Contact:** tony.marketing@example.com  
**Summary:** Marketing coordinator pivoting to sales  
**Education:** BA in Communications  
**Experience:** Handled campaigns and lead gen for B2B SaaS  
**Soft Skills:** Creative, data-driven  
**Technical Skills:** HubSpot, campaign tools, SEO""",
            "Explanation": "Marketing background aligns with lead gen, but lacks direct sales leadership."
        }
    ]
}
 ,
"Customer_Success_Specialist_Job": {
    "description": """📌 **Position:** Customer Success Specialist  
📍 **Location:** Remote (Global)  
📅 **Employment Type:** Full-time | Flexible Hours  
💬 **Reports To:** Head of Customer Experience  

🌟 **Overview:**  
At TechNova Inc., our customers are at the heart of everything we do. We’re looking for a Customer Success Specialist who can blend empathy, technical aptitude, and communication skills to deliver world-class support and proactive client care. You will be the primary point of contact for onboarding, troubleshooting, and guiding clients through their journey with our platform.  

🌍 **Key Functions:**  
As a Customer Success Specialist, you will serve as the client’s trusted advisor. From the initial onboarding to continued engagement, you’ll ensure client satisfaction and retention through strategic check-ins and problem-solving. You’ll also act as a liaison between the product team and the user base, communicating customer feedback effectively.

💼 **What You'll Be Doing:**  
- Serve as the primary contact for 50–100 SMB clients  
- Conduct onboarding calls, product walkthroughs, and quarterly health checks  
- Handle incoming support tickets and escalate technical issues  
- Monitor usage metrics and identify at-risk clients  
- Document customer feedback and advocate for user-centered improvements  
- Create and update help center articles and tutorials  
- Maintain CRM notes and status reports  

🎓 **Qualifications:**  
- Bachelor’s degree in Communication, Business, or a related field  
- 2+ years of experience in customer-facing roles (SaaS preferred)  
- Excellent verbal and written English communication  
- Familiarity with support tools like Zendesk, Intercom, or Freshdesk  
- Comfort using CRMs (e.g., Salesforce, HubSpot)  
- Strong time management and multitasking ability  

🌱 **Why Join Us:**  
- Competitive base salary + performance bonuses  
- Fully remote culture with flexible work hours  
- Annual learning stipend and mental health days  
- Fun, mission-driven team with real impact on users' lives""",

    "extracted": {
        "Extracted Skills": "Customer onboarding, client support, CRM (Salesforce, HubSpot), support platforms (Zendesk, Intercom), communication, knowledge base writing, user feedback reporting",
        "Extracted Experience (Years)": "2+ years in customer success or related field",
        "Extracted Education": "Bachelor’s in Communication, Business, or related field",
        "Extracted Duties": "Onboard clients, manage support tickets, monitor account health, report feedback, maintain documentation, conduct strategic calls"
    },
    "matches": [
        {
            "Resume": "Resume_Lana_CustSuccess.pdf", "Match Score": 0.91,
            "Resume (Text Summary)": """**Contact:** lana.success@example.com  
**Summary:** Customer Success professional with 3 years of SaaS onboarding experience  
**Education:** BA in Business Communication  
**Experience:** Managed 100+ SMB clients at a CRM company  
**Soft Skills:** Empathetic, proactive  
**Technical Skills:** Zendesk, Intercom, Salesforce""",
            "Explanation": "Excellent experience with SaaS tools, onboarding, and CRM systems."
        },
        {
            "Resume": "Resume_Mark_TechSupport.pdf", "Match Score": 0.76,
            "Resume (Text Summary)": """**Contact:** mark.support@example.com  
**Summary:** Technical support agent transitioning to customer success  
**Education:** BS in Information Systems  
**Experience:** Handled support queues, trained new users, documented solutions  
**Soft Skills:** Patient, detail-oriented  
**Technical Skills:** Freshdesk, walkthrough creation""",
            "Explanation": "Strong support background with relevant tools, learning curve for client ownership."
        },
        {
            "Resume": "Resume_Salma_Onboard.pdf", "Match Score": 0.68,
            "Resume (Text Summary)": """**Contact:** salma.onboard@example.com  
**Summary:** Onboarding associate in EdTech startup  
**Education:** BA in Education  
**Experience:** Walkthroughs, knowledge base updates, CRM reporting  
**Soft Skills:** Friendly, organized  
**Technical Skills:** HubSpot, Notion, Trello""",
            "Explanation": "Relevant onboarding experience, slightly less technical depth."
        },
        {
            "Resume": "Resume_Tom_CustomerCare.pdf", "Match Score": 0.59,
            "Resume (Text Summary)": """**Contact:** tom.care@example.com  
**Summary:** Retail customer care specialist  
**Education:** BA in English  
**Experience:** Resolved complaints, handled billing issues, led team trainings  
**Soft Skills:** Communicative, resilient  
**Technical Skills:** Excel, internal ticketing system""",
            "Explanation": "Good interpersonal skills but less aligned with SaaS and onboarding tools."
        },
        {
            "Resume": "Resume_Sophie_Sales.pdf", "Match Score": 0.50,
            "Resume (Text Summary)": """**Contact:** sophie.sales@example.com  
**Summary:** Inside sales representative with support experience  
**Education:** BBA  
**Experience:** Upselling, CRM usage, customer check-ins  
**Soft Skills:** Persuasive, solution-oriented  
**Technical Skills:** Salesforce, Zoom, Email automation""",
            "Explanation": "Sales focus overlaps with some customer success duties."
        }
    ]
}
    ,
    "Graphic_Designer_Job": {
    "description": """🎨 **We're hiring a Graphic Designer!**  
💼 **Location:** Onsite – Dubai, UAE  
🕒 **Schedule:** Full-time, Sunday to Thursday  
🧑‍🎨 **Department:** Creative Studio  
📅 **Experience:** 2–5 years

---

**About the Role:**  
We’re not looking for someone who just “knows Photoshop.” We’re looking for a visual storyteller. Someone who can take an idea, give it personality, and bring it to life across print, digital, and motion. You’ll be part of a dynamic team where design drives the conversation, not just decorates it.

You'll collaborate with copywriters, marketers, and developers to turn creative briefs into campaigns that make people stop scrolling. You’ll craft visuals that reflect our clients’ brands, moods, and messages.

---

**Your Day Might Include:**  
- Designing Instagram carousels that feel like art.  
- Mocking up landing pages that are as functional as they are beautiful.  
- Working with illustrators and animators to develop motion graphics.  
- Brainstorming ideas in creative workshops.  
- Packaging presentations with pixel-perfect precision.  

---

**What We’re Looking For:**  
- A Bachelor’s degree in Graphic Design, Fine Arts, or a related field.  
- A strong portfolio that shows range (branding, social, layout, digital).  
- Proficiency in Adobe Creative Suite (Photoshop, Illustrator, InDesign).  
- Working knowledge of Figma or Sketch is a plus.  
- Experience with motion/After Effects is a bonus, not a requirement.  
- Someone who sweats the small stuff: typography, spacing, alignment.  
- Team player with good vibes. Ego not included.

---

**What You’ll Love:**  
- A creative-first studio culture  
- An annual design budget (use it for fonts, courses, etc.)  
- Apple gear, high-end monitors, and coffee you don’t have to pay for  
- Travel opportunities to pitch with the team  
- A boss who used to be a designer too 😉""",

    "extracted": {
        "Extracted Skills": "Adobe Creative Suite, graphic layout, branding, typography, digital content design, Figma/Sketch, basic motion design (After Effects)",
        "Extracted Experience (Years)": "2–5 years of professional design experience",
        "Extracted Education": "Bachelor’s in Graphic Design, Fine Arts, or related field",
        "Extracted Duties": "Create brand visuals, design digital and print content, collaborate on creative concepts, work with developers and writers, deliver campaign-ready assets"
    },
    "matches": [
        {
            "Resume": "Resume_Mira_Design.pdf", "Match Score": 0.92,
            "Resume (Text Summary)": """**Contact:** mira.design@example.com  
**Summary:** Multidisciplinary designer with 4 years in brand, digital, and social design  
**Education:** BA in Graphic Design  
**Experience:** Campaign visuals for startups, fluent in Adobe CC and Figma  
**Soft Skills:** Creative thinker, strong communicator  
**Technical Skills:** Photoshop, Illustrator, InDesign, Figma, After Effects""",
            "Explanation": "Strong portfolio match, well-rounded creative experience, skilled in motion and layout."
        },
        {
            "Resume": "Resume_Rami_Visuals.pdf", "Match Score": 0.75,
            "Resume (Text Summary)": """**Contact:** rami.visuals@example.com  
**Summary:** Visual designer with background in web and social media assets  
**Education:** BFA in Design  
**Experience:** Freelance projects, landing page mockups, basic animation  
**Soft Skills:** Visual storyteller  
**Technical Skills:** Sketch, Photoshop, Premiere, Illustrator""",
            "Explanation": "Good digital design experience; minor gaps in branding depth."
        },
        {
            "Resume": "Resume_Lina_Junior.pdf", "Match Score": 0.60,
            "Resume (Text Summary)": """**Contact:** lina.junior@example.com  
**Summary:** Junior designer with passion for typography and layouts  
**Education:** Bachelor in Fine Arts  
**Experience:** Internship at ad agency, university design lab  
**Soft Skills:** Detail-oriented, passionate  
**Technical Skills:** InDesign, Illustrator, Canva""",
            "Explanation": "Shows potential but lacks experience and breadth in tools."
        },
        {
            "Resume": "Resume_Ahmed_UIUX.pdf", "Match Score": 0.67,
            "Resume (Text Summary)": """**Contact:** ahmed.uiux@example.com  
**Summary:** UI/UX designer with a branding background  
**Education:** BA in Visual Communication  
**Experience:** Worked on design systems and logo revamps  
**Soft Skills:** Analytical, adaptable  
**Technical Skills:** Figma, Photoshop, InDesign""",
            "Explanation": "Good Figma/UI focus, but missing emphasis on campaign design."
        },
        {
            "Resume": "Resume_Zara_Creative.pdf", "Match Score": 0.83,
            "Resume (Text Summary)": """**Contact:** zara.creative@example.com  
**Summary:** Conceptual graphic designer with agency and studio experience  
**Education:** BA in Graphic Design  
**Experience:** Designed pitch decks, social visuals, animations  
**Soft Skills:** Expressive, collaborative  
**Technical Skills:** Adobe Suite, After Effects, Google Slides, Trello""",
            "Explanation": "Great conceptual profile, strong motion skills, well-aligned."
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

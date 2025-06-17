import streamlit as st
import pandas as pd
import joblib
import re
import spacy
import docx2txt
from sentence_transformers import SentenceTransformer
import numpy as np

# Load spaCy model
nlp = spacy.load("en_core_web_lg")

# Load models and vectorizers
category_model = joblib.load("job_classifier.pkl")
category_vectorizer = joblib.load("tfidf_vectorizer.pkl")
recommendation_model = joblib.load("xgboost_resume_match_model.pkl")
recommendation_vectorizer = joblib.load("xgboost_tfidf_vectorizer.pkl")
bert_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load job descriptions
df_resumes = pd.read_csv("resumes_with_full_extraction.csv")
df_resumes.fillna("", inplace=True)

# Skill dictionaries
CATEGORY_KEYWORDS = {
    "Information Technology (IT)": ["developer", "engineer", "software", "python", "cloud", "backend", "frontend"],
    "Human Resources (HR)": ["recruitment", "talent", "hr", "employee relations", "payroll"],
    "Designer (Graphic/UI/UX)": ["designer", "ui", "ux", "figma", "adobe", "prototype", "wireframe"],
    "Teacher": ["teaching", "curriculum", "lesson", "students", "classroom", "education"],
    "Advocate (Lawyer)": ["legal", "lawyer", "contract", "litigation", "case", "court"],
    "Business Development": ["sales", "business", "growth", "crm", "leads", "partnership"],
    "Healthcare Professional": ["clinic", "nurse", "hospital", "patient", "treatment", "diagnosis"],
    "Fitness Trainer": ["fitness", "trainer", "exercise", "workout", "hiit", "nutrition"],
    "Agriculture Professional": ["farming", "agriculture", "crop", "soil", "irrigation"],
    "Sales": ["sales", "quota", "lead", "pipeline", "crm", "closing"],
    "Consultant": ["consultant", "strategy", "analysis", "advisory", "presentation"],
    "Chef": ["chef", "cooking", "recipe", "menu", "kitchen", "culinary"]
}

# Define the PROFESSIONAL_SKILLS dictionary 
PROFESSIONAL_SKILLS = {
    "Information Technology (IT)": {
        "Technical Skills": [
            "Programming in Python, Java, JavaScript, C++, SQL, Go, Rust",
            "Building applications using frameworks like Django, React, Spring Boot, and Node.js",
            "Deploying and managing services on cloud platforms (AWS, Azure, GCP)",
            "Database management, optimization, and querying using MySQL, PostgreSQL, MongoDB, Redis",
            "Version control, containerization, orchestration, and CI/CD pipeline integration",
            "System security including encryption, penetration testing, and firewall configuration",
            "Linux system administration and load testing strategies"
        ],
        "Software Tools": [
            "Python", "Java", "JavaScript", "C++", "SQL", "Go", "Rust",
            "Django", "React", "Spring Boot", "Node.js",
            "AWS", "Azure", "Google Cloud Platform",
            "MySQL", "PostgreSQL", "MongoDB", "Redis",
            "Git", "GitHub", "Docker", "Kubernetes", "Jenkins"
        ]
    },

    "Human Resources (HR)": {
        "Technical Skills": [
            "Managing end-to-end recruitment and onboarding",
            "Building employee development plans and training modules",
            "Conducting performance reviews and workforce planning",
            "Handling compensation, benefits, and payroll structures",
            "Ensuring legal compliance (OSHA, EEOC, GDPR)",
            "Analyzing workforce metrics for strategic planning"
        ],
        "Software Tools": [
            "Workday", "BambooHR", "ADP", "SAP SuccessFactors",
            "LinkedIn Recruiter", "Greenhouse", "Lever",
            "Excel", "Power BI", "Google Sheets",
            "Gusto", "QuickBooks Payroll", "Zenefits"
        ]
    },

    "Designer (Graphic/UI/UX)": {
        "Technical Skills": [
            "Creating design systems and brand identities",
            "User research, journey mapping, and persona development",
            "Wireframing and prototyping interactive interfaces",
            "Applying accessibility, usability, and heuristic principles",
            "Animating and motion design for digital experiences",
            "Basic front-end coding (HTML5, CSS3, JavaScript)"
        ],
        "Software Tools": [
            "Adobe Illustrator", "Photoshop", "Figma", "Sketch", "Affinity Designer",
            "InVision", "Marvel", "Axure RP",
            "After Effects", "Lottie"
        ]
    },

    "Teacher": {
        "Technical Skills": [
            "Lesson planning aligned with educational standards",
            "Adapting teaching styles for various learning needs",
            "Conducting interactive online and offline learning sessions",
            "Designing and grading formative and summative assessments",
            "Utilizing LMS platforms and tracking student performance",
            "Creating engaging digital educational content"
        ],
        "Software Tools": [
            "Google Classroom", "Microsoft Teams", "Zoom", "Kahoot",
            "Quizlet", "Socrative", "ExamSoft",
            "Canva for Education", "PowerPoint", "Genially",
            "Moodle", "Blackboard", "Canvas",
            "Excel", "Google Sheets"
        ]
    },

    "Advocate (Lawyer)": {
        "Technical Skills": [
            "Legal drafting and contract analysis",
            "Case law research and statutory interpretation",
            "Client consultations and legal advising",
            "Litigation, court procedures, and courtroom strategy",
            "Mediation, arbitration, and dispute resolution",
            "Document review and legal compliance advisory"
        ],
        "Software Tools": [
            "LexisNexis", "Westlaw", "CaseMine",
            "Clio", "MyCase", "PracticePanther",
            "e-Discovery tools", "Notarization software"
        ]
    },

    "Business Development": {
        "Technical Skills": [
            "Identifying and qualifying new business opportunities",
            "Building and maintaining partnerships and client relationships",
            "Creating and presenting persuasive proposals and decks",
            "Conducting market research and strategic planning",
            "Optimizing outreach campaigns and marketing funnels",
            "Tracking KPIs and measuring conversion success"
        ],
        "Software Tools": [
            "Salesforce", "HubSpot", "Zoho",
            "LinkedIn Sales Navigator", "Apollo", "Mailchimp",
            "Google Analytics", "Tableau", "SEMrush",
            "MS Office Suite", "Canva for Business"
        ]
    },

    "Healthcare Professional": {
        "Technical Skills": [
            "Patient assessment, clinical diagnosis, and documentation",
            "Administering medical treatments (IV, injections, wound care)",
            "Reading and interpreting lab results and diagnostic imaging",
            "Following HIPAA regulations and infection control standards",
            "Managing chronic care and creating personalized treatment plans",
            "Handling emergency and trauma care protocols"
        ],
        "Software Tools": [
            "Epic", "Cerner", "Allscripts",
            "Stethoscopes", "EKG machines", "X-ray/MRI equipment"
        ]
    },

    "Fitness Trainer": {
        "Technical Skills": [
            "Developing customized fitness programs and regimens",
            "Conducting fitness assessments and mobility screenings",
            "Monitoring client progress and adjusting programs accordingly",
            "Educating clients on proper exercise techniques and recovery",
            "Offering basic nutritional advice and supplementation",
            "Handling emergency protocols (CPR, AED)"
        ],
        "Software Tools": [
            "Trainerize", "MyFitnessPal", "TrueCoach",
            "Fitbit", "WHOOP", "VO2 max analyzers",
            "NASM", "ACE", "Precision Nutrition", "CrossFit certifications"
        ]
    },

    "Agriculture Professional": {
        "Technical Skills": [
            "Managing soil quality, crop cycles, and yield optimization",
            "Controlling pests and applying fertilizers effectively",
            "Designing and maintaining irrigation systems",
            "Utilizing precision farming and agri-tech tools",
            "Applying sustainable farming and climate-smart techniques",
            "Post-harvest processing and storage planning"
        ],
        "Software Tools": [
            "FarmLogs", "AgriWebb", "Climate FieldView",
            "GPS-guided tractors", "Soil sensors", "Agricultural drones"
        ]
    },

    "Sales": {
        "Technical Skills": [
            "Prospecting and cold outreach",
            "Conducting discovery calls and qualifying leads",
            "Delivering sales pitches and handling objections",
            "Managing CRM pipelines and nurturing relationships",
            "Closing sales and post-sales customer support",
            "Tracking KPIs and optimizing sales workflows"
        ],
        "Software Tools": [
            "Salesforce", "Pipedrive", "Zoho CRM",
            "Apollo.io", "LinkedIn Ads", "Outreach.io",
            "Reply.io", "SalesLoft", "Mailshake",
            "Square", "Shopify POS", "Toast"
        ]
    },

    "Consultant": {
        "Technical Skills": [
            "Business analysis and problem structuring",
            "Data-driven strategy development and benchmarking",
            "Developing financial models and simulations",
            "Creating proposals, client reports, and workshops",
            "Conducting change management and stakeholder mapping",
            "Delivering client presentations and facilitating meetings"
        ],
        "Software Tools": [
            "Excel (advanced)", "Power BI", "Tableau",
            "PowerPoint", "Miro", "Notion", "Slack"
        ]
    },

    "Chef": {
        "Technical Skills": [
            "Executing precise cooking techniques (sautéing, baking, etc.)",
            "Creating innovative dishes and developing recipes",
            "Ensuring kitchen safety and hygiene compliance",
            "Managing food inventory and minimizing waste",
            "Plating and presentation for guest experience",
            "Addressing dietary restrictions and allergen safety"
        ],
        "Software Tools": [
            "Sous-vide equipment", "Induction cooktops", "Thermomix",
            "POS-linked inventory systems", "Kitchen Display Systems (KDS)",
            "HACCP checklists", "ServSafe management tools"
        ]
    }
}

# ------------------------------
# Utility Functions
# ------------------------------
def extract_text_from_pdf(uploaded_file):
    from PyPDF2 import PdfReader
    reader = PdfReader(uploaded_file)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def extract_text_from_docx(uploaded_file):
    return docx2txt.process(uploaded_file)

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def predict_category(text):
    text_cleaned = clean_text(text)
    vec = category_vectorizer.transform([text_cleaned])
    return category_model.predict(vec)[0]



# Education extractor
def extract_education(text):
    if not isinstance(text, str):
        return ""
    text = text.replace("is required", "").replace("Is Required", "").strip()
    match = re.search(r"(bachelor|master|phd|associate|diploma|high school).*? in ([a-zA-Z\s&]+)", text, re.IGNORECASE)
    if match:
        level = match.group(1).capitalize()
        field = match.group(2).strip().title()
        return f"{level} in {field}"
    return ""

# Experience extractor
def extract_experience_years_by_dates(text):
    if not isinstance(text, str):
        return ""
    current_year = datetime.datetime.now().year
    text = text.lower()
    patterns = re.findall(r"(20[0-1][0-9]|202[0-5])\s*(?:\-|–|to)\s*(present|20[0-1][0-9]|202[0-5])", text)
    match = re.search(r"(\d+)\s+(?:\+?\s*)?years?\s+(?:of)?\s+experience", text)
    if match:
        return int(match.group(1))
    total_years = 0
    for start, end in patterns:
        start = int(start)
        end = current_year if end in ["present", "now"] else int(end)
        if end >= start:
            total_years += end - start
    return total_years if total_years > 0 else ""

# Duties extractor
def extract_duties(text):
    if not isinstance(text, str):
        return ""
    lines = re.split(r"\.|\n|\r", text)
    duties = [line.strip() for line in lines if any(word in line.lower() for word in [
        "responsibilit", "duties", "manage", "lead", "organize", "supervise", "coordinate", "develop"
    ])]
    return ". ".join(duties[:3])

# Skill extractor
def extract_all_skills(text, category):
    if not isinstance(text, str):
        return ""
    doc = nlp(text.lower())
    found_skills = set()
    for chunk in doc.noun_chunks:
        if chunk.text.strip() in SOFT_SKILLS:
            found_skills.add(chunk.text.strip())
    for token in doc:
        if token.text.strip() in SOFT_SKILLS:
            found_skills.add(token.text.strip())
    if category in PROFESSIONAL_SKILLS:
        for token in doc:
            if not token.has_vector or token.is_stop:
                continue
            for skill in PROFESSIONAL_SKILLS[category]["Technical Skills"]:
                if nlp(skill.lower()).similarity(token) > 0.75:
                    found_skills.add(skill)
            for tool in PROFESSIONAL_SKILLS[category]["Software Tools"]:
                if nlp(tool.lower()).similarity(token) > 0.75:
                    found_skills.add(tool)
    return ", ".join(sorted(found_skills))

# ✅ Master function for single job
def extract_job_features(job_description, predicted_category):
    """
    Extracts key features from a single job description.

    Parameters:
        job_description (str): The job description text.
        category (str): The job category.

    Returns:
        dict: Dictionary with education, experience, duties, and skills.
    """
    return {
        "Extracted Education": extract_education(job_description),
        "Extracted Experience (Years)": extract_experience_years_by_dates(job_description),
        "Extracted Duties": extract_duties(job_description),
        "Extracted Skills": extract_all_skills(job_description, predicted_category)
    }


def get_top_5_recommendations(job_text, job_category):
    job_clean = clean_text(job_text)
    job_vec = recommendation_vectorizer.transform([job_clean])
    job_embed = bert_model.encode(job_clean)
    
    resume_scores = []

    for _, resume_row in df_resumes[df_resumes["Category"] == job_category].iterrows():
        resume_clean = clean_text(f"{resume_row['Education']} {resume_row['Soft Skills']} {resume_row['Technical Skills']} {resume_row['Experience']}")
        resume_vec = recommendation_vectorizer.transform([resume_clean])
        resume_embed = bert_model.encode(resume_clean)

        combined_vec = np.hstack((resume_vec.toarray()[0], job_vec.toarray()[0]))
        match_prob = recommendation_model.predict_proba([combined_vec])[0][1]

        similarity = np.dot(job_embed, resume_embed) / (np.linalg.norm(job_embed) * np.linalg.norm(resume_embed))

        resume_scores.append({
            "Resume Name": resume_row["Name"],
            "Resume Email": resume_row.get("Email", ""),
            "Phone": resume_row.get("Phone", ""),
            "Category": resume_row["Category"],
            "Match Probability": round(match_prob, 3),
            "BERT Similarity": round(similarity, 3),
            
        })

    return sorted(resume_scores, key=lambda x: x["Match Probability"], reverse=True)[:5]


# ------------------------------
# Streamlit App
# ------------------------------
st.set_page_config(page_title="Job Matcher", layout="wide")
st.title("🔍 Job Analysis & Resume Matching")

uploaded_file = st.file_uploader("Upload your Job Description (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        job_text = extract_text_from_pdf(uploaded_file)
    else:
        job_text = extract_text_from_docx(uploaded_file)

    st.subheader("📄 Uploaded Job Description")
    st.text(job_text[:1000] + "..." if len(job_text) > 1000 else job_text)

    st.subheader("📌 Predicted Job Category")
    predicted_category = predict_category(job_text)
    st.success(f"Predicted Category: {predicted_category}")

    st.subheader("🔍 Extracted Job Features")
    extracted = extract_features(job_text, predicted_category)
    st.dataframe(pd.DataFrame([extracted]))

    st.subheader("📈 Top 5 Resume Recommendations")
    recommendations = get_top_5_recommendations(job_text, predicted_category)
    st.table(pd.DataFrame(recommendations))

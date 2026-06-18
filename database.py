
import re
import streamlit as st

import firebase_admin #this is the library for firebase so we can connect to the eventual site

from firebase_admin import credentials, firestore #credentials and frestore modules

def get_db():
    """
    This will init the firebase connection and then return the firestore clinet but now works with streamlit cloud as the dlpyer

    """
    if not firebase_admin._apps:
        cred = credentials.Certificate({
            "type": st.secrets["firebase"]["type"],
            "project_id": st.secrets["firebase"]["project_id"],
            "private_key_id": st.secrets["firebase"]["private_key_id"],
            "private_key": st.secrets["firebase"]["private_key"],
            "client_email": st.secrets["firebase"]["client_email"],
            "client_id": st.secrets["firebase"]["client_id"],
            "auth_uri": st.secrets["firebase"]["auth_uri"],
            "token_uri": st.secrets["firebase"]["token_uri"],
            "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
            "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
        })
        firebase_admin.initialize_app(cred)
    return firestore.client()



def seed_data(db):
    """
    This will seed the database with initial data
    """

    skills = {
        "python": {
            "name": "Python",
            "category": "Languages",
            "icon_url": "https://firebasestorage.googleapis.com/placeholder/python.png",
            "color": "#3776AB"
        },
        "sql": {
            "name": "SQL",
            "category": "Languages",
            "icon_url": "https://firebasestorage.googleapis.com/placeholder/sql.png",
            "color": "#E48E00"
        },
        "streamlit": {
            "name": "Streamlit",
            "category": "Frameworks",
            "icon_url": "https://firebasestorage.googleapis.com/placeholder/streamlit.png",
            "color": "#FF4B4B"
        },
        "react": {
            "name": "React",
            "category": "Frameworks",
            "icon_url": "https://firebasestorage.googleapis.com/placeholder/react.png",
            "color": "#61DAFB"
        },
        "firebase": {
            "name": "Firebase",
            "category": "Tools",
            "icon_url": "https://firebasestorage.googleapis.com/placeholder/firebase.png",
            "color": "#FFCA28"
        },
        "git": {
            "name": "Git",
            "category": "Tools",
            "icon_url": "https://firebasestorage.googleapis.com/placeholder/git.png",
            "color": "#F05032"
        },
    }

    # skill references bc foreign keys aren't a thing in nosql
    skill_refs = {}
    for skill_id, skill_data in skills.items():
        ref = db.collection("skills").document(skill_id)
        ref.set(skill_data)
        skill_refs[skill_id] = ref

    #about
    db.collection("about").document("main").set({
        "name": "Your Name",
        "title": "Your Title",
        "bio": "A short bio about yourself.",
        "photo_url": "https://firebasestorage.googleapis.com/placeholder/headshot.jpg",
        "email": "you@email.com",
        "linkedin": "https://linkedin.com/in/yourhandle",
        "github": "https://github.com/yourhandle"
    })

    #projects
    db.collection("projects").add({
        "title": "Project One",
        "description": "A short description of what this project does.",
        "thumbnail_url": "https://firebasestorage.googleapis.com/placeholder/project1.jpg",
        "tech_stack": [skill_refs["python"], skill_refs["streamlit"]],
        "link": "https://github.com/yourhandle/project-one"
    })

    db.collection("projects").add({
        "title": "Project Two",
        "description": "A short description of what this project does.",
        "thumbnail_url": "https://firebasestorage.googleapis.com/placeholder/project2.jpg",
        "tech_stack": [skill_refs["python"], skill_refs["sql"], skill_refs["react"]],
        "link": "https://github.com/yourhandle/project-two"
    })

    #expereince
    db.collection("experience").add({
        "company": "Company One",
        "role": "Your Role",
        "start": "Jan 2022",
        "end": "Present",
        "bullets": [
            "Did something impactful here.",
            "Built something cool with X.",
            "Improved Y by Z%."
        ],
        "skills_used": [skill_refs["python"], skill_refs["sql"]]
    })

    db.collection("experience").add({
        "company": "Company Two",
        "role": "Previous Role",
        "start": "Jun 2019",
        "end": "Dec 2021",
        "bullets": [
            "Led a team of N people.",
            "Delivered X on time and under budget.",
            "Introduced Y process that improved Z."
        ],
        "skills_used": [skill_refs["python"], skill_refs["git"]]
    })

    #blog? easier than typing on linkedin lol
    db.collection("blog").add({
        "title": "My First Post",
        "body": "This is the body of your first blog post. Write something interesting here.",
        "date": "2024-01-01",
        "tags": ["Python", "Career"]
    })
    print('Seeded :D')

def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def skills_seed(db):
    skills = {
    #languages
    "python": {"name": "Python", "category": "Languages", "icon_url": "", "color": "#3776AB"},
    "sql": {"name": "SQL", "category": "Languages", "icon_url": "", "color": "#E48E00"},
    "r": {"name": "R", "category": "Languages", "icon_url": "", "color": "#276DC3"},
    "javascript": {"name": "JavaScript", "category": "Languages", "icon_url": "", "color": "#F7DF1E"},
    "php": {"name": "PHP", "category": "Languages", "icon_url": "", "color": "#777BB4"},
    "html_css": {"name": "HTML/CSS", "category": "Languages", "icon_url": "", "color": "#E34F26"},

    #ai and ml
    "pytorch": {"name": "PyTorch", "category": "AI & Machine Learning", "icon_url": "", "color": "#EE4C2C"},
    "sklearn": {"name": "Scikit-learn", "category": "AI & Machine Learning", "icon_url": "", "color": "#F89939"},
    "vit": {"name": "Vision Transformers", "category": "AI & Machine Learning", "icon_url": "", "color": "#6B4FBB"},
    "cnn": {"name": "CNNs", "category": "AI & Machine Learning", "icon_url": "", "color": "#A855F7"},
    "transfer_learning": {"name": "Transfer Learning", "category": "AI & Machine Learning", "icon_url": "", "color": "#8B5CF6"},
    "langgraph": {"name": "LangGraph", "category": "AI & Machine Learning", "icon_url": "", "color": "#1C7C54"},
    "multi_agent": {"name": "Multi-Agent Orchestration", "category": "AI & Machine Learning", "icon_url": "", "color": "#0EA5E9"},
    "mcp": {"name": "MCP Protocol", "category": "AI & Machine Learning", "icon_url": "", "color": "#6366F1"},

    #data
    "pyspark": {"name": "PySpark", "category": "Data & Big Data", "icon_url": "", "color": "#E25A1C"},
    "pandas": {"name": "Pandas", "category": "Data & Big Data", "icon_url": "", "color": "#150458"},
    "numpy": {"name": "NumPy", "category": "Data & Big Data", "icon_url": "", "color": "#013243"},
    "etl": {"name": "ETL Pipeline Design", "category": "Data & Big Data", "icon_url": "", "color": "#FF6B35"},
    "data_validation": {"name": "Data Validation", "category": "Data & Big Data", "icon_url": "", "color": "#2D6A4F"},
    "data_quality": {"name": "Data Quality Control", "category": "Data & Big Data", "icon_url": "", "color": "#40916C"},

    #geospatial
    "geopandas": {"name": "GeoPandas", "category": "Geospatial", "icon_url": "", "color": "#139A43"},
    "rasterio": {"name": "Rasterio", "category": "Geospatial", "icon_url": "", "color": "#4A90D9"},
    "gee": {"name": "Google Earth Engine", "category": "Geospatial", "icon_url": "", "color": "#34A853"},
    "crs": {"name": "CRS Alignment", "category": "Geospatial", "icon_url": "", "color": "#4285F4"},
    "spatial_validation": {"name": "Spatial Validation", "category": "Geospatial", "icon_url": "", "color": "#FBBC05"},

    #backend and apis
    "fastapi": {"name": "FastAPI", "category": "Backend & APIs", "icon_url": "", "color": "#009688"},
    "rest": {"name": "REST APIs", "category": "Backend & APIs", "icon_url": "", "color": "#FF5733"},
    "pydantic": {"name": "Pydantic", "category": "Backend & APIs", "icon_url": "", "color": "#E92063"},
    "async_python": {"name": "Async Python", "category": "Backend & APIs", "icon_url": "", "color": "#3776AB"},
    "firebase": {"name": "Firebase/Firestore", "category": "Backend & APIs", "icon_url": "", "color": "#FFCA28"},

    #dbs
    "mariadb": {"name": "MariaDB", "category": "Databases", "icon_url": "", "color": "#003545"},
    "mysql": {"name": "MySQL", "category": "Databases", "icon_url": "", "color": "#4479A1"},
    "nosql": {"name": "NoSQL Schema Design", "category": "Databases", "icon_url": "", "color": "#47A248"},

    # frontend and viz
    "react": {"name": "React", "category": "Frontend & Visualization", "icon_url": "", "color": "#61DAFB"},
    "d3": {"name": "D3.js", "category": "Frontend & Visualization", "icon_url": "", "color": "#F9A03C"},
    "tableau": {"name": "Tableau", "category": "Frontend & Visualization", "icon_url": "", "color": "#E97627"},
    "responsive_ui": {"name": "Responsive UI Design", "category": "Frontend & Visualization", "icon_url": "", "color": "#06B6D4"},

    # infrastructure
    "git": {"name": "Git/GitHub", "category": "Infrastructure & Tools", "icon_url": "", "color": "#F05032"},
    "render": {"name": "Render", "category": "Infrastructure & Tools", "icon_url": "", "color": "#46E3B7"},
    "streamlit": {"name": "Streamlit", "category": "Infrastructure & Tools", "icon_url": "", "color": "#FF4B4B"},

    # ai tools
    "claude_code": {"name": "Claude Code", "category": "AI Tools", "icon_url": "", "color": "#C0392B"},
    "cursor": {"name": "Cursor", "category": "AI Tools", "icon_url": "", "color": "#333333"},

    #soft
    "cross_functional": {"name": "Cross-functional Collaboration", "category": "Soft Skills", "icon_url": "", "color": "#7C3AED"},
    "tech_docs": {"name": "Technical Documentation", "category": "Soft Skills", "icon_url": "", "color": "#2563EB"},
    "client_comms": {"name": "Client-facing Communication", "category": "Soft Skills", "icon_url": "", "color": "#059669"},
    "mentorship": {"name": "Mentorship & Training", "category": "Soft Skills", "icon_url": "", "color": "#D97706"},
    "deescalation": {"name": "De-escalation", "category": "Soft Skills", "icon_url": "", "color": "#DC2626"},
    "detail_oriented": {"name": "Detail Oriented", "category": "Soft Skills", "icon_url": "", "color": "#0891B2"},
    }
    skill_refs = {}
    for skill_id, skill_data in skills.items():
        ref = db.collection("skills").document(skill_id)
        ref.set(skill_data)
        skill_refs[skill_id] = ref
    
    print("seeded :)")
    return skill_refs
    
def seed_projects(db):
    # Get skill refs we'll need
    def skill(skill_id):
        return db.collection("skills").document(skill_id)

    projects = [
        {
            "title": "Deepfake Detection Using Vision Transformers",
            "description": "Developed a single-frame deepfake detection system using Vision Transformers (ViT-Base/16) fine-tuned on Celeb-DF-v2 (250K frames). Built with human-in-the-loop deployment in mind — attention map visualizations let human reviewers evaluate model reasoning rather than blindly trust a score. Achieved AUC-ROC of 0.84 and 72% reduction in false positives across a three-model progression.",
            "tech_stack": [skill("pytorch"), skill("vit"), skill("transfer_learning"), skill("cnn"), skill("python")],
            "link": "https://github.com/w00d39/deepfake_capstone",
            "thumbnail_url": "",
            "order": 1,
            "featured": True,
            "role": "Solo — Capstone Project",
            "date": "Spring 2026"
        },
        {
            "title": "Cummins Xtern Challenge",
            "description": "Built a production-grade multi-agent AI system for a Fortune 200 manufacturer from infrastructure setup to live deployment in three weeks. Architected a LangGraph orchestration pipeline with a 4-node StateGraph, conditional routing, async Python, and Firestore persistence. Set up Firebase from scratch, designed a 4-collection database schema with security rules and audit trails, and deployed a FastAPI backend on Render.",
            "tech_stack": [skill("langgraph"), skill("multi_agent"), skill("fastapi"), skill("firebase"), skill("async_python"), skill("pydantic"), skill("python"), skill("render")],
            "link": "https://github.com/w00d39/stern_challenge_team2",
            "thumbnail_url": "",
            "order": 2,
            "featured": True,
            "role": "Agent / AI Engineer",
            "date": "February — March 2026"
        },
        {
            "title": "F1 Analytics Platform",
            "description": "Built an F1 analytics platform covering the full 2023 season using seven ML-powered analysis systems: K-Means tire degradation clustering, Linear Regression team performance tracking, Random Forest and Gradient Boosting weather impact modeling (0.82 R²), driver performance analysis, lap time clustering, pit stop efficiency, and season improvement trends. Produced 45+ visualizations covering tire strategy, race dynamics, and performance optimization.",
            "tech_stack": [skill("python"), skill("sklearn"), skill("pandas"), skill("numpy"), skill("matplotlib"), skill("seaborn")],
            "link": "https://github.com/w00d39/f1_2023",
            "thumbnail_url": "",
            "order": 3,
            "featured": True,
            "role": "Solo Project",
            "date": "Spring 2025"
        },
        {
            "title": "StudyDragonAI",
            "description": "Full-stack AI-powered study planning application featuring personalized schedule generation, adaptive learning recommendations, and an interactive dashboard with task management and reflection capabilities. Integrated AI algorithms for intelligent scheduling optimization and learning pattern analysis.",
            "tech_stack": [skill("react"), skill("html_css"), skill("php"), skill("python")],
            "link": "",
            "thumbnail_url": "",
            "order": 4,
            "featured": True,
            "role": "Solo Project",
            "date": "Fall 2025"
        },
        {
            "title": "Geospatial ML Pipeline for Coastal Erosion",
            "description": "Led data pipeline engineering for a coastal erosion classification project. Processed 5,000+ satellite images using GeoPandas, Rasterio, and Google Earth Engine, handling CRS alignment, patch extraction, and spatial validation. Project reached a 0.70 F1-score on the final classification task.",
            "tech_stack": [skill("geopandas"), skill("rasterio"), skill("gee"), skill("crs"), skill("spatial_validation"), skill("python")],
            "link": "",
            "thumbnail_url": "",
            "order": 5,
            "featured": True,
            "role": "Data Lead — Team Project",
            "date": "Fall 2025"
        },
        {
            "title": "Big Data Price Prediction with PySpark",
            "description": "Cut runtime on a used car price prediction pipeline from 6 hours to 45 minutes — 88% faster — by optimizing PySpark jobs across a 2.5M+ record dataset. Focused on partition tuning, query optimization, and reducing unnecessary shuffles.",
            "tech_stack": [skill("pyspark"), skill("python"), skill("sql")],
            "link": "",
            "thumbnail_url": "",
            "order": 6,
            "featured": True,
            "role": "Solo Project",
            "date": "Spring 2025"
        },
        {
            "title": "Coffee Shop Sales Analytics Dashboard",
            "description": "Interactive D3.js visualization dashboard analyzing 3,600+ coffee shop transactions to uncover sales trends and customer behavior patterns. Includes time-series analysis, customer segmentation, and product performance metrics.",
            "tech_stack": [skill("d3"), skill("javascript"), skill("html_css")],
            "link": "https://github.com/w00d39/d3-final-project",
            "thumbnail_url": "",
            "order": 7,
            "featured": True,
            "role": "Solo Project",
            "date": "Fall 2025"
        },
    ]

    for project in projects:
        db.collection("projects").add(project)


    print("Seeded projects :)")

def seed_skills_2(db):
    skills = {
        "seaborn": {"name": "Seaborn", "category": "Frontend & Visualization", "icon_url": "", "color": "#4C72B0"},
        "matplotlib": {"name": "Matplotlib", "category": "Frontend & Visualization", "icon_url": "", "color": "#11557C"},
    }

    skill_refs = {}
    for skill_id, skill_data in skills.items():
        ref = db.collection("skills").document(skill_id)
        ref.set(skill_data)
        skill_refs[skill_id] = ref
    
    print("seeded :)")
    return skill_refs

def seed_experience(db):
    def skill(skill_id):
        return db.collection("skills").document(skill_id)

    experience = [
        {
            "company": "Barnes & Noble",
            "role": "Senior Bookseller",
            "start": "November 2025",
            "end": "Present",
            "order": 1,
            "bullets": [
                "Promoted to senior role based on strong customer engagement, hand-selling ability, and consistent reliability.",
                "Build genuine connections with customers to understand what they're looking for and guide them to the right purchase.",
                "Lead sales campaigns through personal example, making a noticeable difference in team performance.",
                "Mentor new booksellers on customer interaction and store operations.",
                "Completed de-escalation workshop to strengthen conflict resolution and difficult conversation skills.",
                "Step in as a technical resource when the team needs it."
            ],
            "skills_used": [skill("cross_functional"), skill("mentorship"), skill("client_comms"), skill("deescalation")]
        },
        {
            "company": "Barnes & Noble",
            "role": "Bookseller + Barista",
            "start": "November 2022",
            "end": "November 2025",
            "order": 2,
            "bullets": [
                "Handled technical troubleshooting for BookMaster and store systems.",
                "Gave personalized book recommendations across all sections based on what customers were actually looking for.",
                "Kept things moving at busy registers while working in membership recommendations naturally.",
                "Supported cross-functional team through proactive assistance and consistent reliability in a fast-paced environment."
            ],
            "skills_used": [skill("cross_functional"), skill("client_comms"), skill("detail_oriented")]
        },
    ]

    for exp in experience:
        db.collection("experience").add(exp)

    print("Seeded experience :)")
import firebase_admin #this is the library for firebase so we can connect to the eventual site

from firebase_admin import credentials, firestore #credentials and frestore modules

def get_db():
    """
    This will init the firebase connection and then return the firestore clinet 
    """
    if not firebase_admin._apps: #this checks if the app is already inited
        cred = credentials.Certificate("firebase_credentials.json") #loads the json secrets to Credentils
        firebase_admin.initialize_app(cred) #loads the credentials and then inits the app
    #returns the firestore client with the initialized app either newly or existing
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
import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="SRM Trichy - Placement + Timetable", page_icon="🏫")
st.title("🏫 SRM IST - Trichy Campus")
st.subheader("💼 Placement + 📅 Sem Exam Timetable")
st.write("ALL BRANCHES | 2026 Regulation | SRM Trichy")

branch = st.selectbox("Branch Select Pannu", [
    "BME - Biomedical",
    "CSE - Computer Science",
    "CSE (AI & ML) - Artificial Intelligence",
    "CSE (Cyber Security)",
    "CSE (Data Science)",
    "IT - Information Technology",
    "ECE - Electronics & Communication",
    "ECEDS - ECE (Data Science) ⭐ NEW",
    "EEE - Electrical & Electronics",
    "Mech - Mechanical",
    "Civil - Civil",
    "Biotech - Biotechnology",
    "AIDS - AI & Data Science"
])

year = st.selectbox("Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
sem = st.selectbox("Semester", ["Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6", "Sem 7", "Sem 8"])

all_branch_subjects = {
    "BME - Biomedical": {
        "Sem 1": ["Communicative English", "Calculus and Linear Algebra", "Physics: Electromagnetic Theory, Quantum, Waves & Optics", "Chemistry", "Biomedical Sensors", "Engineering Graphics and Design", "Philosophy of Engineering", "Professional Skills"],
        "Sem 2": ["Advanced Calculus", "Human Anatomy and Physiology", "Biology for Engineers", "Programming in Python", "Electrical & Electronics Engineering", "Environmental Science"],
        "Sem 3": ["Biomedical Instrumentation", "Biomechanics", "Biomaterials", "Probability & Statistics"],
        "Sem 4": ["Medical Electronics", "Biomedical Signals & Systems", "Biocontrol Systems"],
        "Sem 5": ["Medical Imaging Systems", "Biomedical Signal Processing"],
        "Sem 6": ["Rehabilitation Engineering", "Hospital Management"],
        "Sem 7": ["Telemedicine", "Artificial Organs"],
        "Sem 8": ["Major Project", "Internship"],
    },
    "ECEDS - ECE (Data Science) ⭐ NEW": {
        "Sem 1": ["Communicative English", "Calculus and Linear Algebra", "Physics: Electromagnetic Theory, Quantum, Waves & Optics", "Chemistry", "Engineering Graphics and Design", "Philosophy of Engineering", "Professional Skills"],
        "Sem 2": ["Advanced Calculus and Complex Analysis", "Programming in Python", "Electrical & Electronics Engineering", "Biology for Engineers", "Environmental Science", "Constitution of India"],
        "Sem 3": ["Digital Logic Design", "Data Structures & Algorithms", "Signals & Systems", "Probability & Statistics for Data Science", "Electronic Devices & Circuits"],
        "Sem 4": ["Microcontroller & Embedded Systems", "Database Management Systems", "Communication Systems", "Machine Learning Basics", "Analog & Digital Circuits"],
        "Sem 5": ["VLSI Design", "Deep Learning", "Data Science & Big Data Analytics", "Digital Signal Processing", "Computer Networks"],
        "Sem 6": ["5G & Wireless Communication", "AI for Electronics", "IoT & Embedded AI", "Cloud Computing"],
        "Sem 7": ["Advanced Data Science", "Antenna & Microwave", "Elective - NLP / Computer Vision"],
        "Sem 8": ["Major Project - ECE + Data Science", "Internship"],
    },
    "ECE - Electronics & Communication": {
        "Sem 1": ["Communicative English", "Calculus and Linear Algebra", "Physics", "Chemistry", "Engineering Graphics", "Philosophy of Engineering"],
        "Sem 2": ["Advanced Calculus", "Programming in Python", "Electrical & Electronics", "Biology for Engineers"],
        "Sem 3": ["Digital Logic", "Signals & Systems", "Electronic Devices", "Network Theory"],
        "Sem 4": ["Microcontroller", "Communication Systems", "Analog Circuits"],
        "Sem 5": ["VLSI", "Digital Signal Processing", "Computer Networks"],
        "Sem 6": ["Wireless Communication", "Embedded Systems", "IoT"],
        "Sem 7": ["Antenna", "Elective"],
        "Sem 8": ["Project", "Internship"],
    },
    "CSE - Computer Science": {
        "Sem 1": ["Communicative English", "Calculus and Linear Algebra", "Physics", "Chemistry", "Programming for Problem Solving", "Engineering Graphics"],
        "Sem 2": ["Advanced Calculus", "Data Structures", "Digital Logic", "Python"],
        "Sem 3": ["DSA", "DBMS", "OS", "Computer Architecture"],
        "Sem 4": ["CN", "Java", "Theory of Computation"],
        "Sem 5": ["ML", "Web Development", "Compiler Design"],
        "Sem 6": ["Cloud", "Cyber Security", "Project"],
        "Sem 7": ["Deep Learning", "Elective"],
        "Sem 8": ["Project", "Internship"],
    },
    "CSE (AI & ML) - Artificial Intelligence": {
        "Sem 1": ["Communicative English", "Calculus and Linear Algebra", "Physics", "Chemistry", "Programming"],
        "Sem 2": ["Advanced Calculus", "Python", "Data Structures"],
        "Sem 3": ["DSA", "DBMS", "AI Basics", "Statistics"],
        "Sem 4": ["Machine Learning", "OS", "CN"],
        "Sem 5": ["Deep Learning", "NLP", "Computer Vision"],
        "Sem 6": ["Generative AI", "Robotics"],
        "Sem 7": ["Elective"],
        "Sem 8": ["Project", "Internship"],
    },
    "CSE (Cyber Security)": {
        "Sem 1": ["Communicative English", "Calculus", "Physics", "Chemistry", "Programming"],
        "Sem 2": ["Advanced Calculus", "Python", "DSA"],
        "Sem 3": ["DSA", "DBMS", "Computer Networks"],
        "Sem 4": ["Cryptography", "Ethical Hacking Basics", "OS"],
        "Sem 5": ["Cyber Security", "Web Security"],
        "Sem 6": ["Penetration Testing", "Cloud Security"],
        "Sem 7": ["Forensics"],
        "Sem 8": ["Project", "Internship"],
    },
    "CSE (Data Science)": {
        "Sem 1": ["Communicative English", "Calculus", "Physics", "Chemistry", "Programming"],
        "Sem 2": ["Advanced Calculus", "Python", "Statistics"],
        "Sem 3": ["DSA", "DBMS", "Probability"],
        "Sem 4": ["Machine Learning", "Data Visualization"],
        "Sem 5": ["Big Data", "Deep Learning"],
        "Sem 6": ["Cloud", "AI"],
        "Sem 7": ["Elective"],
        "Sem 8": ["Project", "Internship"],
    },
    "IT - Information Technology": {
        "Sem 1": ["Communicative English", "Calculus", "Physics", "Chemistry", "Programming"],
        "Sem 2": ["Advanced Calculus", "Python", "DSA"],
        "Sem 3": ["DSA", "DBMS", "OS"],
        "Sem 4": ["CN", "Web Dev", "Java"],
        "Sem 5": ["Cloud", "Cyber Security"],
        "Sem 6": ["DevOps", "Project"],
        "Sem 7": ["Elective"],
        "Sem 8": ["Project", "Internship"],
    },
    "EEE - Electrical & Electronics": {
        "Sem 1": ["Communicative English", "Calculus", "Physics", "Chemistry", "Engineering Graphics"],
        "Sem 2": ["Advanced Calculus", "Basic Electrical", "Programming"],
        "Sem 3": ["Circuit Theory", "Electrical Machines 1", "Electronic Devices"],
        "Sem 4": ["Power Systems", "Control Systems", "Electrical Machines 2"],
        "Sem 5": ["Power Electronics", "Renewable Energy"],
        "Sem 6": ["Smart Grid", "Electric Vehicles"],
        "Sem 7": ["Elective"],
        "Sem 8": ["Project", "Internship"],
    },
    "Mech - Mechanical": {
        "Sem 1": ["Communicative English", "Calculus", "Physics", "Chemistry", "Engineering Graphics"],
        "Sem 2": ["Advanced Calculus", "Engineering Mechanics", "Programming"],
        "Sem 3": ["Thermodynamics", "Fluid Mechanics", "Manufacturing"],
        "Sem 4": ["Machine Design", "Heat Transfer", "Robotics"],
        "Sem 5": ["CAD/CAM", "Automobile Engineering"],
        "Sem 6": ["Robotics", "Industrial Engineering"],
        "Sem 7": ["Elective"],
        "Sem 8": ["Project", "Internship"],
    },
    "Civil - Civil": {
        "Sem 1": ["Communicative English", "Calculus", "Physics", "Chemistry", "Engineering Graphics"],
        "Sem 2": ["Advanced Calculus", "Surveying", "Mechanics"],
        "Sem 3": ["Structural Engineering", "Geotechnical", "Concrete Technology"],
        "Sem 4": ["Transportation", "Water Resources"],
        "Sem 5": ["Design of Structures", "Estimation"],
        "Sem 6": ["Construction Management"],
        "Sem 7": ["Elective"],
        "Sem 8": ["Project", "Internship"],
    },
    "Biotech - Biotechnology": {
        "Sem 1": ["Communicative English", "Calculus", "Physics", "Chemistry", "Biology"],
        "Sem 2": ["Biochemistry", "Microbiology", "Genetics"],
        "Sem 3": ["Cell Biology", "Bioprocess Engineering"],
        "Sem 4": ["Genetic Engineering", "Bioinformatics"],
        "Sem 5": ["Industrial Biotechnology"],
        "Sem 6": ["Pharmaceutical Biotechnology"],
        "Sem 7": ["Elective"],
        "Sem 8": ["Project", "Internship"],
    },
    "AIDS - AI & Data Science": {
        "Sem 1": ["Communicative English", "Calculus", "Physics", "Chemistry", "Programming"],
        "Sem 2": ["Advanced Calculus", "Python", "Statistics"],
        "Sem 3": ["DSA", "DBMS", "AI Basics"],
        "Sem 4": ["Machine Learning", "Data Visualization"],
        "Sem 5": ["Deep Learning", "Big Data"],
        "Sem 6": ["NLP", "Cloud"],
        "Sem 7": ["Elective"],
        "Sem 8": ["Project", "Internship"],
    },
}

st.write("---")
st.subheader(f"📚 SRM Curriculum - {branch} | {year} | {sem} | 2026 Regulation")
subjects_list = all_branch_subjects.get(branch, {}).get(sem, ["Subject Update Panrom"])
for s in subjects_list:
    st.write(f"- **{s}**")

st.subheader("✏️ Subject Thappa Irundha Inga Maathu Da!")
custom = st.text_area("Un Actual Subjects-a Type Pannu (Oru Line-ku Oru Subject):", value="\n".join(subjects_list))
my_subjects = [x for x in custom.split("\n") if x.strip()!=""]

# --- ONLY 2 TABS NOW ---
tab1, tab2 = st.tabs(["💼 Placement", "📅 Sem Exam Timetable"])

with tab1:
    st.subheader(f"💼 {branch} Placement - SRM Trichy")
    placement = {
        "ECEDS - ECE (Data Science) ⭐ NEW": ("Qualcomm, Intel, TCS, Infosys, Zoho, Fractal, Mu Sigma, Bosch", "4.5 - 12 LPA", "VLSI + Embedded + Python + ML + SQL + DSA", "Embedded Engineer, Data Scientist, VLSI Engineer, ML Engineer"),
        "BME - Biomedical": ("Philips, Siemens Healthineers, GE Healthcare, Apollo Hospitals", "3.5 - 8 LPA", "Biomedical Instrumentation, Hospital Training, Python", "Biomedical Engineer, Service Engineer"),
        "CSE - Computer Science": ("TCS, Infosys, Zoho, Amazon, Cognizant", "4 - 12 LPA", "DSA, Python/Java, DBMS, OS, CN", "Software Developer, Full Stack, SDE"),
        "ECE - Electronics & Communication": ("Qualcomm, Intel, Bosch, TCS, Wipro", "4 - 10 LPA", "VLSI, Embedded C, Digital Electronics", "Embedded Engineer, VLSI Engineer"),
        "EEE - Electrical & Electronics": ("L&T, Siemens, ABB, Schneider", "3.5 - 8 LPA", "Power Systems, Machines, MATLAB", "Electrical Engineer, Power Engineer"),
        "Mech - Mechanical": ("L&T, TVS, Ashok Leyland, Hyundai, Bosch", "3.5 - 7 LPA", "CAD/SolidWorks, Thermodynamics, Manufacturing", "Design Engineer, Production Engineer"),
        "Civil - Civil": ("L&T, Shapoorji, Sobha, DLF", "3.5 - 6.5 LPA", "AutoCAD, STAAD Pro, Surveying", "Site Engineer, Design Engineer"),
        "AIDS - AI & Data Science": ("Zoho, Freshworks, Fractal, Mu Sigma", "5 - 12 LPA", "Python, ML, SQL, Power BI", "Data Scientist, ML Engineer"),
        "CSE (Data Science)": ("Zoho, Fractal, TCS, Mu Sigma", "5 - 12 LPA", "Python, ML, SQL, Power BI", "Data Scientist, Data Analyst"),
        "CSE (AI & ML) - Artificial Intelligence": ("Zoho, Freshworks, TCS, Nvidia", "5 - 12 LPA", "Python, ML, Deep Learning, NLP", "AI Engineer, ML Engineer"),
        "CSE (Cyber Security)": ("TCS, Wipro, Palo Alto, Quick Heal", "4 - 10 LPA", "Ethical Hacking, Networks, Linux", "Security Analyst, Pentester"),
    }
    comp, pack, skills, roles = placement.get(branch, ("TCS, Infosys, Wipro, Accenture", "4 - 10 LPA", "Core + Python + Communication", "Engineer, Analyst"))
    st.success(f"**Top Companies:** {comp}")
    st.info(f"**Average Package:** {pack}")
    st.warning(f"**Skills Venam:** {skills}")
    st.write(f"**Job Roles:** {roles}")

    st.write("---")
    st.subheader("📊 CGPA Calculator - Placement Eligibility")
    cgpa = st.slider("Un CGPA Enna?", 5.0, 10.0, 7.5)
    if cgpa >= 8.5:
        st.success(f"CGPA {cgpa} - SEMMA DA! 🔥 Ellam Company-ku Eligible! Top Package-kku Try Pannu!")
    elif cgpa >= 7.5:
        st.success(f"CGPA {cgpa} - Super! 👍 90% Company-ku Eligible!")
    elif cgpa >= 6.5:
        st.warning(f"CGPA {cgpa} - Okay Da. 60% Company-ku Eligible. CGPA-a 7.5-ku Kondu Po!")
    else:
        st.error(f"CGPA {cgpa} - Konjam Kastam Da. Ippo irundhu Padichu CGPA-a Yethu!")

    st.write("---")
    st.subheader("📝 Resume Tips")
    st.write("**1.** 1 Page Resume - Photo, CGPA, Skills, Project, Internship Podu\n**2.** Project: 2 Project Kandippa Irukkanum - GitHub Link Podu\n**3.** Internship: 3rd Year-la Pannu\n**4.** LinkedIn Profile Create Pannu - SRM Trichy-nu Podu")

    st.subheader("❓ Interview Questions - Top 5")
    if "ECEDS" in branch:
        st.write("1. Tell me about yourself?\n2. What is VLSI? What is Embedded?\n3. Python-la Data Analysis Epdi Panuva?\n4. Microcontroller vs Microprocessor?\n5. Un Project-a Explain Pannu?")
    elif "BME" in branch:
        st.write("1. Tell me about yourself?\n2. What is ECG? PQRST Explain Pannu?\n3. MRI vs CT Difference?\n4. Pacemaker Epdi Work Aagudhu?\n5. Hospital Internship-la Enna Panna?")
    elif "CSE" in branch or "AIDS" in branch or "IT" in branch:
        st.write("1. Tell me about yourself?\n2. What is OOPs?\n3. Reverse a String Code Ezhu\n4. SQL vs NoSQL Difference?\n5. Un Project-a Explain Pannu?")
    elif "ECE" in branch:
        st.write("1. Tell me about yourself?\n2. What is VLSI?\n3. Microcontroller vs Microprocessor?\n4. Embedded C-la Code Ezhu\n5. Un Project Explain Pannu?")
    else:
        st.write("1. Tell me about yourself?\n2. Un Branch Basics?\n3. Project Explain Pannu?\n4. Why This Company?\n5. Where Do You See in 5 Years?")

    st.subheader("📅 Placement Timeline - SRM Trichy")
    st.write("**1st Year:** Basics + Python + CGPA-a Yethu\n**2nd Year:** Core Subjects + 1 Project + LinkedIn\n**3rd Year:** Internship + DSA / Core Strong + Resume Ready\n**4th Year:** Placement Drive - Aptitude + Interview + Offer Letter! 🎉")
    if "ECEDS" in branch:
        st.success("**ECEDS Advantage 🔥:** ECE Company-kkum Apply Panna Mudiyum, IT / Data Science Company-kkum Apply Panna Mudiyum! 2X Opportunity!")

with tab2:
    st.subheader(f"📅 Sem Exam Timetable - {branch} | {year} {sem}")
    exam_date = st.date_input("Sem Exam Start Date Eppo?", date.today() + timedelta(days=20))
    days_left = (exam_date - date.today()).days
    if days_left > 0:
        st.success(f"🔥 Exam-ku Innum **{days_left} Naal** Dhaan Irukku Da! Time Waste Panna Koodadhu!")
    elif days_left == 0:
        st.error("DEI! INNIKKU EXAM-A! All The Best! 🔥")
    else:
        st.info("Exam Mudinjiducha? Next Sem-kku Prepare Pannu Da!")

    st.write("### 📚 Un Subjects (SRM 2026 Regulation)")
    for i, s in enumerate(my_subjects, 1):
        st.write(f"**{i}. {s}**")

    st.write("### ⏰ Daily Study Timetable")
    hours = st.slider("Oru Naal-ku Evlo Mani Neram Padippa?", 2, 10, 5)
    st.write(f"**Un Daily Plan - {hours} Mani Neram:**")
    if hours >= 6:
        st.table({"Time": ["6:00 - 7:30 AM", "9:00 - 11:00 AM", "11:30 - 1:00 PM", "2:00 - 4:00 PM", "6:00 - 8:00 PM", "9:00 - 10:00 PM"], "What To Do": ["Revision - Yesterday Padichadhu", f"{my_subjects[0] if len(my_subjects)>0 else ''} - Theory + Diagram", f"{my_subjects[1] if len(my_subjects)>1 else ''} - Important Questions", f"{my_subjects[2] if len(my_subjects)>2 else ''} - Problems", f"{my_subjects[3] if len(my_subjects)>3 else ''} - Previous Paper", "Full Revision + Notes"]})
    elif hours >= 4:
        st.table({"Time": ["6:30 - 8:00 AM", "10:00 - 12:00 PM", "2:00 - 4:00 PM", "7:00 - 9:00 PM"], "What To Do": [f"{my_subjects[0] if len(my_subjects)>0 else ''} - Theory", f"{my_subjects[1] if len(my_subjects)>1 else ''} - Important Qns", f"{my_subjects[2] if len(my_subjects)>2 else ''} - Problems", "Revision + Mock Test"]})
    else:
        st.table({"Time": ["7:00 - 8:30 AM", "6:00 - 8:00 PM"], "What To Do": [f"{my_subjects[0] if len(my_subjects)>0 else ''} - Most Important Topic", "Revision + Previous Paper"]})

    st.write("### 📋 Exam Week Plan - SRM Pattern")
    st.table({
        "Day": ["Exam-ku 3 Naal Munnadi", "Exam-ku 2 Naal Munnadi", "Exam-ku 1 Naal Munnadi", "Exam Day Morning"],
        "Seiya Vendum": ["Full Syllabus 1 Time Mudichidu", "Important 5 Units + Diagram Practice", "Previous Year Paper + Short Notes Mattum", "6 AM Elundhirichu Formula + Diagram Mattum Paaru"]
    })

    st.write("### 🎯 Subject-wise Study Plan")
    if days_left > 0 and len(my_subjects) > 0:
        per_sub = max(1, days_left // len(my_subjects))
        st.info(f"**Plan:** Oru Subject-kku **{per_sub} Naal** Kuduthu Mudichidu. Last 3 Naal Full Revision Mattum!")
        for i, s in enumerate(my_subjects):
            start = date.today() + timedelta(days=i*per_sub)
            st.write(f"**{s}** - {start.strftime('%d %b')} - {(start + timedelta(days=per_sub-1)).strftime('%d %b')} - {per_sub} Naal")

    st.write("### ✅ SRM Exam Tips")
    st.success("""
    **1.** SRM Paper-la 2 Mark, 10 Mark, 16 Mark Pattern - 16 Mark-ku Diagram Kandippa Podu!
    **2.** Lab Record + Assignment-a Mudichidu - Internal Marks-la Dhaan Pass Easy!
    **3.** Previous 3 Year Paper-a Kandippa Paaru - 40% Questions Adhula irundhu Varum!
    **4.** Night Full-a Muzhichitu Padikkadha - 6 Mani Thoongu!
    **5.** Phone-a 1 Mani Neram Side-la Vechidu - Focus Pannu Da!
    """)

    if st.button("Enakku Motivation Kudunga! 🔥"):
        st.balloons()
        st.write(f"**Dei Tharun! {days_left} Naal Dhaan Irukku! Nee Panna Mudiyum! SRM Trichy-la Topper Aaganum-na Ippo Dhaan Time! Padichu Mudichidu Da! 💪🔥**")

st.write("---")
st.write("Made by Tharun | SRM IST Trichy - Placement + Timetable | 2026 Regulation 🔥")

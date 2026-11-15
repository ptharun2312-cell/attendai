import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="SRM Trichy - ALL Branches + ECEDS", page_icon="🏫")
st.title("🏫 SRM IST - Trichy Campus")
st.subheader("🤖 AI Teacher + 💼 Placement + 📅 Timetable")
st.write("ALL BRANCHES | 2026 Regulation | SRM Trichy")

# --- ALL BRANCHES - SRM TRICHY ---
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

# --- 2026 REGULATION SEM 1 - COMMON FOR ALL + BRANCH SPECIAL ---
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
        "Sem 1": ["Communicative English", "Calculus and Linear Algebra", "Physics: Electromagnetic Theory, Quantum, Waves & Optics", "Chemistry", "Engineering Graphics and Design", "Philosophy of Engineering", "Professional Skills", "Biomedical Sensors / Basic Engineering"],
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

# Show Curriculum
st.write("---")
st.subheader(f"📚 SRM Curriculum - {branch} | {year} | {sem} | 2026 Regulation")
subjects_list = all_branch_subjects.get(branch, {}).get(sem, ["Subject Update Panrom"])
for s in subjects_list:
    st.write(f"- **{s}**")

st.subheader("✏️ Subject Thappa Irundha Inga Maathu Da!")
custom = st.text_area("Un Actual Subjects-a Type Pannu (Oru Line-ku Oru Subject):", value="\n".join(subjects_list))
my_subjects = [x for x in custom.split("\n") if x.strip()!=""]
subject = st.selectbox("Padikka Subject Select Pannu", my_subjects)

tab1, tab2, tab3 = st.tabs(["🤖 AI Teacher", "💼 Placement", "📅 Timetable"])

with tab1:
    st.subheader(f"👨‍🏫 {branch} AI Teacher - {subject}")
    doubt = st.text_input("Doubt Type Pannu")
    def ai_answer(q):
        q=q.lower()
        if "eceds" in q or "ece data" in q: return "**ECEDS-na Enna?**\n\nECE + Data Science! Circuit-um Theriyum, Data Science-um Theriyum. 2-in-1 Branch! ECE Job + IT Job Rendum Apply Panna Mudiyum! SRM Trichy-la Semma Demand!"
        if "vlsi" in q: return "**VLSI - ECE/ECEDS!** Periya Circuit-a Chinna Chip-la Poduradhu. Mobile Chip Ellam VLSI."
        if "embedded" in q or "microcontroller" in q: return "**Embedded - ECE!** Hardware + Software. Arduino, Washing Machine Example."
        if "data science" in q: return "**Data Science - ECEDS/CSE!** Data-va Vachu Future-a Predict Panradhu. Python + ML + SQL. Example: Amazon Unakku Pudicha Product Kaatturadhu Data Science!"
        if "machine learning" in q or " ml " in q: return "**ML!** Computer-ku Data Kuduthu Thanaave Kathukka Vekkuradhu."
        if "sensor" in q: return "**Biomedical Sensors - BME!** Body Signal-a Pidikkura Device. ECG Electrode, Pulse Oximeter."
        if "ecg" in q: return "**ECG - BME!** Heart Beat Graph. PQRST."
        if "python" in q: return "**Python!** print('Hello SRM') - ECEDS / CSE-ku Main Language!"
        if "dsa" in q: return "**DSA!** Stack=Plates (LIFO), Queue=Bus Queue (FIFO). Placement-ku Mukkiyam!"
        if "dbms" in q: return "**DBMS!** Data-va Store Panna System. SQL Use Panrom."
        if "calculus" in q: return "**Calculus!** Differentiation = Rate of Change, Integration = Area."
        if "teach" in q or "tir" in q: return "**Dei SRM Tharun! Naan Irukken! 🔥 All Branches + ECEDS-kkum Naan Dhaan Teacher!**"
        return f"**Super Doubt!** {q} - {subject} la Important. Definition + Diagram + Real Life Example-nu Padichu Paaru Da!"
    if st.button("AI Teacher Kitta Kelu 🤖"):
        if doubt: st.success("Badil:"); st.write(ai_answer(doubt))
        else: st.warning("Doubt Type Pannu Da!")
    c1,c2,c3,c4 = st.columns(4)
    if c1.button("ECEDS?"): st.write(ai_answer("eceds"))
    if c2.button("Python"): st.write(ai_answer("python"))
    if c3.button("VLSI"): st.write(ai_answer("vlsi"))
    if c4.button("Data Science"): st.write(ai_answer("data science"))

with tab2:
    st.subheader(f"💼 {branch} Placement - SRM Trichy")
    placement = {
        "ECEDS - ECE (Data Science) ⭐ NEW": ("Qualcomm, Intel, TCS, Infosys, Zoho, Fractal, Mu Sigma, Bosch", "4.5 - 12 LPA", "VLSI + Embedded + Python + ML + SQL + DSA", "Embedded Engineer, Data Scientist, VLSI Engineer, ML Engineer"),
        "BME - Biomedical": ("Philips, Siemens Healthineers, GE Healthcare, Apollo", "3.5 - 8 LPA", "Biomedical Instrumentation, Hospital Training, Python", "Biomedical Engineer, Service Engineer"),
        "CSE - Computer Science": ("TCS, Infosys, Zoho, Amazon", "4 - 12 LPA", "DSA, Python/Java, DBMS, OS, CN", "SDE, Full Stack"),
        "ECE - Electronics & Communication": ("Qualcomm, Intel, Bosch, TCS", "4 - 10 LPA", "VLSI, Embedded, Digital", "Embedded Engineer, VLSI Engineer"),
    }
    comp, pack, skills, roles = placement.get(branch, ("TCS, Infosys, Wipro, L&T, Accenture", "4 - 10 LPA", "Core + Python + Communication", "Engineer, Analyst"))
    st.success(f"**Companies:** {comp}")
    st.info(f"**Package:** {pack}")
    st.warning(f"**Skills:** {skills}")
    st.write(f"**Roles:** {roles}")
    cgpa = st.slider("Un CGPA?", 5.0, 10.0, 7.5)
    if cgpa >= 7.5: st.success(f"CGPA {cgpa} - Super! Eligible!")
    else: st.warning(f"CGPA {cgpa} - Konjam Yethu Da!")
    if "ECEDS" in branch:
        st.success("**ECEDS Advantage 🔥:** ECE Company-kkum Apply Panna Mudiyum, IT / Data Science Company-kkum Apply Panna Mudiyum! 2X Opportunity!")

with tab3:
    st.subheader(f"📅 Timetable - {branch} | {sem}")
    exam_date = st.date_input("Sem Exam Start Date?", date.today() + timedelta(days=20))
    days_left = (exam_date - date.today()).days
    st.success(f"Exam-ku Innum {days_left} Naal Irukku Da! 🔥")
    st.write("**Un Subjects:**")
    for s in my_subjects: st.write(f"- {s}")
    hours = st.slider("Oru Naal Evlo Mani Padippa?", 2, 10, 5)
    st.write(f"**Daily Plan - {hours} Mani:** Core Subject 2 Hr + Problem Practice 1 Hr + Revision 1 Hr + Previous Paper 1 Hr")
    if st.button("Motivation Kudunga! 🔥"):
        st.balloons()
        st.write(f"**Dei Tharun! {days_left} Naal Dhaan! {branch}-la Topper Nee Dhaan! 💪**")

st.write("---")
st.write("Made by Tharun | SRM IST Trichy - ALL BRANCHES + ECEDS | 2026 Regulation 🔥")

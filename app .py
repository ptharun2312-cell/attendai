import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="SRM Trichy - AI Teacher + Placement + Timetable", page_icon="🏫")
st.title("🏫 SRM IST - Trichy Campus")
st.subheader("🤖 AI Teacher + 💼 Placement + 📅 Sem Exam Timetable")
st.write("SRM Institute of Science & Technology, Trichy | ALL BRANCHES")

branch = st.selectbox("Branch Select Pannu", ["BME - Biomedical", "CSE - Computer Science", "IT - Information Technology", "ECE - Electronics", "EEE - Electrical", "Mech - Mechanical", "Civil - Civil", "AIDS - AI & Data Science", "CYS - Cyber Security"])
year = st.selectbox("Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])

all_subjects = {
    "BME - Biomedical": ["Anatomy", "Physiology", "Biomedical Instrumentation", "Medical Imaging", "Biomechanics", "Biomaterials"],
    "CSE - Computer Science": ["Python", "DSA", "DBMS", "OS", "CN", "Java", "ML"],
    "IT - Information Technology": ["Python", "DSA", "DBMS", "Web Dev", "Cloud", "Cyber Security"],
    "ECE - Electronics": ["Digital Electronics", "VLSI", "Embedded Systems", "Communication", "Microcontroller"],
    "EEE - Electrical": ["Circuit Theory", "Electrical Machines", "Power Systems", "Control Systems"],
    "Mech - Mechanical": ["Thermodynamics", "Fluid Mechanics", "Machine Design", "Robotics", "CAD"],
    "Civil - Civil": ["Surveying", "Structural Engineering", "Geotechnical", "Concrete Technology"],
    "AIDS - AI & Data Science": ["Python", "Machine Learning", "Deep Learning", "Data Science", "Statistics"],
    "CYS - Cyber Security": ["Cyber Security", "Ethical Hacking", "Cryptography", "Networks", "Python"]
}
subject = st.selectbox("Subject", all_subjects[branch])

tab1, tab2, tab3 = st.tabs(["🤖 AI Teacher", "💼 Placement", "📅 Sem Exam Timetable"])

with tab1:
    st.subheader(f"👨‍🏫 {branch} AI Teacher")
    doubt = st.text_input("Doubt Type Pannu - Ex: What is ECG? What is Python?")
    def ai_answer(q):
        q=q.lower()
        if "ecg" in q: return "**ECG - BME!** Heart Beat-a Graph-a Kaattum. PQRST: P=Atria, QRS=Ventricle, T=Rest."
        if "mri" in q: return "**MRI - BME!** Magnet Use Panni Image. Radiation Illa!"
        if "python" in q: return "**Python!** Easy Language. print('Hello SRM')"
        if "dsa" in q: return "**DSA!** Stack=Plates (LIFO), Queue=Bus Queue (FIFO)."
        if "vlsi" in q: return "**VLSI - ECE!** Periya Circuit-a Chinna Chip-la Poduradhu."
        if "teach" in q or "tir" in q: return "**Dei SRM Tharun! Naan Irukken! 🔥**"
        return f"**Super Doubt!** {q} - {subject} la Important. Definition + Diagram + Example-nu Padichu Paaru!"
    if st.button("AI Teacher Kitta Kelu 🤖"):
        if doubt: st.success("AI Teacher Badil:"); st.write(ai_answer(doubt))
        else: st.warning("Doubt Type Pannu Da!")

with tab2:
    st.subheader(f"💼 {branch} Placement - SRM Trichy")
    placement_data = {
        "BME - Biomedical": {"companies": "Philips, Siemens Healthineers, GE Healthcare, Apollo", "package": "3.5 - 8 LPA", "skills": "Biomedical Instrumentation, Hospital Training, Python"},
        "CSE - Computer Science": {"companies": "TCS, Infosys, Wipro, Zoho, Amazon", "package": "4 - 12 LPA", "skills": "DSA, Python/Java, DBMS, OS, CN"},
        "IT - Information Technology": {"companies": "TCS, Infosys, HCL, Capgemini", "package": "4 - 10 LPA", "skills": "Web Dev, Cloud, DBMS, Python"},
        "ECE - Electronics": {"companies": "TCS, Qualcomm, Intel, Bosch", "package": "4 - 10 LPA", "skills": "VLSI, Embedded C, Digital Electronics"},
        "EEE - Electrical": {"companies": "L&T, Siemens, ABB", "package": "3.5 - 8 LPA", "skills": "Power Systems, Machines, MATLAB"},
        "Mech - Mechanical": {"companies": "L&T, TVS, Ashok Leyland, Hyundai", "package": "3.5 - 7 LPA", "skills": "CAD, Thermodynamics, Manufacturing"},
        "Civil - Civil": {"companies": "L&T, Shapoorji, Sobha", "package": "3.5 - 6.5 LPA", "skills": "AutoCAD, STAAD Pro, Surveying"},
        "AIDS - AI & Data Science": {"companies": "Zoho, Freshworks, Fractal", "package": "5 - 12 LPA", "skills": "Python, ML, SQL, Power BI"},
        "CYS - Cyber Security": {"companies": "TCS, Wipro, Palo Alto", "package": "4 - 10 LPA", "skills": "Ethical Hacking, Networks, Linux"}
    }
    d = placement_data[branch]
    st.success(f"**Companies:** {d['companies']}")
    st.info(f"**Package:** {d['package']}")
    st.warning(f"**Skills:** {d['skills']}")
    cgpa = st.slider("Un CGPA?", 5.0, 10.0, 7.5)
    if cgpa >= 7.5: st.success(f"CGPA {cgpa} - Super! 90% Company-ku Eligible!")
    else: st.warning(f"CGPA {cgpa} - Konjam Yethu Da!")

with tab3:
    st.subheader("📅 Sem Exam Timetable - SRM Trichy")
    st.write(f"Branch: **{branch}** | Year: **{year}**")

    st.write("### 🗓️ 1. Exam Date Select Pannu")
    exam_date = st.date_input("Sem Exam Start Date Eppo?", date.today() + timedelta(days=20))
    today = date.today()
    days_left = (exam_date - today).days
    if days_left > 0:
        st.success(f"🔥 Exam-ku Innum **{days_left} Naal** Dhaan Irukku Da! Time Waste Panna Koodadhu!")
    elif days_left == 0:
        st.error("DEI! INNIKKU EXAM-A! All The Best! 🔥")
    else:
        st.info("Exam Mudinjiducha? Next Sem-kku Prepare Pannu Da!")

    st.write("### 📚 2. Un Subjects (SRM Sem Exam)")
    subs = all_subjects[branch]
    st.write("Un Sem Subjects:")
    for i, s in enumerate(subs, 1):
        st.write(f"**{i}. {s}**")

    st.write("### ⏰ 3. Daily Study Timetable - Auto Generate!")
    hours = st.slider("Oru Naal-ku Evlo Mani Neram Padippa?", 2, 10, 5)
    st.write(f"**Un Daily Plan - {hours} Mani Neram:**")

    if hours >= 6:
        st.table({"Time": ["6:00 - 7:30 AM", "9:00 - 11:00 AM", "11:30 - 1:00 PM", "2:00 - 4:00 PM", "6:00 - 8:00 PM", "9:00 - 10:00 PM"], "What To Do": ["Revision - Yesterday Padichadhu", f"{subs[0]} - Theory + Diagram", f"{subs[1]} - Important Questions", f"{subs[2]} - Problems / Numericals", f"{subs[3] if len(subs)>3 else subs[0]} - Previous Year Paper", "Full Revision + Notes Ezhu"]})
    elif hours >= 4:
        st.table({"Time": ["6:30 - 8:00 AM", "10:00 - 12:00 PM", "2:00 - 4:00 PM", "7:00 - 9:00 PM"], "What To Do": [f"{subs[0]} - Theory", f"{subs[1]} - Important Qns", f"{subs[2]} - Problems", "Revision + Mock Test"]})
    else:
        st.table({"Time": ["7:00 - 8:30 AM", "6:00 - 8:00 PM"], "What To Do": [f"{subs[0]} - Most Important Topic", "Revision + Previous Paper"]})

    st.write("### 📋 4. Exam Week Timetable - SRM Pattern")
    st.write("SRM-la Exam-ku Naduvula 1-2 Days Gap Varum. Adha Epdi Use Pannanum:")
    st.table({
        "Day": ["Exam-ku 3 Naal Munnadi", "Exam-ku 2 Naal Munnadi", "Exam-ku 1 Naal Munnadi", "Exam Day Morning"],
        "Seiya Vendum": ["Full Syllabus 1 Time Mudichidu", "Important 5 Units + Diagram Practice", "Previous Year Paper + Short Notes Mattum", "6 AM Elundhirichu Formula + Diagram Mattum Paaru"]
    })

    st.write("### 🎯 5. Subject-wise Study Plan")
    if days_left > 0:
        per_sub = max(1, days_left // len(subs))
        st.info(f"**Plan:** Oru Subject-kku **{per_sub} Naal** Kuduthu Mudichidu. Last 3 Naal Full Revision Mattum!")
        for i, s in enumerate(subs):
            start = today + timedelta(days=i*per_sub)
            st.write(f"**{s}** - {start.strftime('%d %b')} - { (start + timedelta(days=per_sub-1)).strftime('%d %b')} - {per_sub} Naal")

    st.write("### ✅ 6. SRM Exam Tips - Topper Tips!")
    st.success("""
    **1.** SRM Question Paper-la 2 Mark, 10 Mark, 16 Mark Pattern - 16 Mark-ku Diagram Kandippa Podu!
    **2.** Lab Record + Assignment-a Mudichidu - Internal Marks-la Dhaan Pass Easy!
    **3.** Previous 3 Year Paper-a Kandippa Paaru - 40% Questions Adhula irundhu Varum!
    **4.** Night Full-a Muzhichitu Padikkadha - 6 Mani Thoongu, Brain Fresh-a Irukkum!
    **5.** Phone-a 1 Mani Neram Side-la Vechidu - Focus Pannu Da!
    """)

    st.write("### ⏳ 7. Exam Countdown - Daily Motivation")
    if st.button("Enakku Motivation Kudunga! 🔥"):
        st.balloons()
        st.write(f"**Dei Tharun! {days_left} Naal Dhaan Irukku! Nee Panna Mudiyum! SRM Trichy-la Topper Aaganum-na Ippo Dhaan Time! Padichu Mudichidu Da! 💪🔥**")

st.write("---")
st.write("Made by Tharun | SRM IST Trichy - ALL BRANCHES + PLACEMENT + TIMETABLE 🔥")

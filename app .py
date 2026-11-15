import streamlit as st
import streamlit as st
from datetime import date, timedelta
import math

# --- TOPPER MAKER - LOGIN 🔐 ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🏆 TOPPER MAKER")
    st.subheader("SRM IST | Trichy + KTR Payalugs 🔥")
    st.write("---")
    st.write("### 🔐 Sign In Pannu Da!")
    st.write("SRM Students Mattum Ulla Poga Mudiyum!")

    name = st.text_input("👤 NAME ?")
    roll = st.text_input("🆔 Roll No / Register No - Ex: RA2611000000000")
    st.success(f"👋 Hello {st.session_state.user_name}! | {st.session_state.user_roll} | {st.session_state.user_mail} | {st.session_state.user_campus}")
    campus_login = st.selectbox("🏫 Campus", ["Trichy Campus", "KTR Campus - Chennai 🔥", "Ramapuram", "Vadapalani", "Delhi NCR", "Amaravati"])
    password = st.text_input("🔑 Password - Edhuvum Vechuko (Ex: topper123)", type="password")

    if st.button("🚀 LOGIN - TOPPER MAKER Ulla Po!"):
        if name and roll and password:
            st.session_state.logged_in = True
            st.session_state.user_name = name
            st.session_state.user_roll = roll
            st.session_state.user_campus = campus_login
            st.success(f"HELLO {name}! 🔥 Login Success!")
            st.rerun()
        else:
            st.error("Dei! Peru, Roll No, Password Ellam Fill Pannu Da!")

    st.write("---")
    st.write("🏆 TOPPER MAKER | Made by Tharun | SRM Trichy + KTR")
    st.stop()

# LOGIN AANA APRAM MATTUM KEELA IRUKKURA APP THERIYUM
st.success(f"👋 Vanakkam {st.session_state.user_name}! | {st.session_state.user_roll} | {st.session_state.user_campus}")
if st.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.write("---")
# --- APP STARTS HERE ---
from datetime import date, timedelta
import math

st.set_page_config(page_title="SRM Trichy - Materials Upload", page_icon="🏫")
st.title("🏫 TOPPER MAKER SRM APP")
st.subheader("💼 Placement + 📅 Timetable + ✅ Attendance + 🎓 CGPA + 🚨 Detention + 📚 Materials")
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
        "Sem 1": ["Professional english for engineers", "Calculus and Linear Algebra", "Physics: Electromagnetic Theory, Quantum, Waves & Optics", "Chemistry", "Electrical and electronics engineering", "Engineering Graphics ", "data science and artificial intelligence of Engineering", "Professional Skills"],
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
for s in subjects_list: st.write(f"- **{s}**")
st.subheader("✏️ Subject Thappa Irundha Inga Maathu Da!")
custom = st.text_area("Un Actual Subjects-a Type Pannu (Oru Line-ku Oru Subject):", value="\n".join(subjects_list))
my_subjects = [x for x in custom.split("\n") if x.strip()!=""]

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["💼 Placement", "📅 Timetable", "✅ Attendance", "🎓 CGPA / GPA", "🚨 Detention", "📚 Materials Upload"])

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
    st.success(f"**Top Companies:** {comp}"); st.info(f"**Average Package:** {pack}"); st.warning(f"**Skills Venam:** {skills}"); st.write(f"**Job Roles:** {roles}")
    cg = st.slider("Un CGPA Enna?", 5.0, 10.0, 7.5)
    if cg >= 8.5: st.success(f"CGPA {cg} - SEMMA DA! 🔥")
    elif cg >= 7.5: st.success(f"CGPA {cg} - Super! 👍")
    else: st.warning(f"CGPA {cg} - Yethu Da!")

with tab2:
    st.subheader(f"📅 Sem Exam Timetable - {branch} | {year} {sem}")
    exam_date = st.date_input("Sem Exam Start Date Eppo?", date.today() + timedelta(days=20))
    days_left = (exam_date - date.today()).days
    if days_left > 0: st.success(f"🔥 Exam-ku Innum **{days_left} Naal** Dhaan Irukku Da!")
    elif days_left == 0: st.error("DEI! INNIKKU EXAM-A! All The Best! 🔥")
    else: st.info("Exam Mudinjiducha? Next Sem-kku Prepare Pannu Da!")
    st.write("### 📚 Un Subjects")
    for i, s in enumerate(my_subjects, 1): st.write(f"**{i}. {s}**")
    hours = st.slider("Oru Naal-ku Evlo Mani Neram Padippa?", 2, 10, 5)
    st.write(f"**Daily Plan - {hours} Mani:** Core 2 Hr + Problems 1 Hr + Revision 1 Hr + Previous Paper 1 Hr")

with tab3:
    st.subheader(f"✅ Attendance Calculator - {branch} | {sem}")
    st.write("SRM-la **75% Attendance Kandippa Venam!**")
    total = st.number_input("Total Classes Nadandhadhu Evlo?", min_value=1, value=40, key="att_total")
    attended = st.number_input("Nee Pona Classes Evlo?", min_value=0, max_value=int(total), value=30, key="att_attended")
    target = st.slider("Target Attendance %", 60, 100, 75, key="att_target")
    if total > 0:
        perc = (attended / total) * 100
        st.metric("Un Attendance %", f"{perc:.1f}%"); st.progress(min(1.0, perc/100))
        if perc >= target:
            st.success(f"✅ SAFE DA! {perc:.1f}% Irukku!")
            can_bunk = int(attended*100/target - total)
            if can_bunk > 0: st.info(f"😎 Innum **{can_bunk} Class Bunk** Adikalam!")
        else:
            st.error(f"⚠️ DANGER! {perc:.1f}% Dhaan Irukku!")
            if target < 100:
                need = math.ceil((target*total - 100*attended) / (100 - target))
                st.warning(f"🔥 Inime **{need} Class Thodarnthu** Poganaum!")

with tab4:
    st.subheader("🎓 CGPA / GPA Calculator - SRM Trichy")
    st.write("SRM Grade: **O=10, A+=9, A=8, B+=7, B=6, C=5, U=0**")
    grade_map = {"O (90-100) - 10": 10, "A+ (80-89) - 9": 9, "A (70-79) - 8": 8, "B+ (60-69) - 7": 7, "B (50-59) - 6": 6, "C (45-49) - 5": 5, "U (Fail <45) - 0": 0}
    st.subheader("📊 GPA Calculator - Indha Sem")
    total_points = 0; total_credits = 0
    default_credits = [3, 4, 5, 5, 3, 2, 2, 1]
    for i, subj in enumerate(my_subjects):
        c1, c2 = st.columns([3, 1])
        with c1: g = st.selectbox(f"{i+1}. {subj} - Grade?", list(grade_map.keys()), index=2, key=f"grade_{i}")
        with c2: cr = st.number_input("Credit", min_value=1, max_value=6, value=default_credits[i] if i < len(default_credits) else 3, key=f"credit_{i}")
        total_points += grade_map[g] * cr; total_credits += cr
    if total_credits > 0:
        gpa = total_points / total_credits
        st.metric(f"{sem} GPA", f"{gpa:.2f} / 10"); st.progress(min(1.0, gpa/10))
        if gpa >= 9: st.success(f"🎉 GPA {gpa:.2f} - OUTSTANDING DA! 🔥")
        elif gpa >= 7.5: st.success(f"👍 GPA {gpa:.2f} - VERY GOOD!")
        elif gpa >= 6: st.warning(f"⚠️ GPA {gpa:.2f} - AVERAGE!")
        else: st.error(f"🚨 GPA {gpa:.2f} - DANGER!")
    st.write("---")
    st.subheader("🎓 CGPA Calculator - Overall")
    c1,c2,c3,c4 = st.columns(4)
    with c1: s1 = st.number_input("Sem 1 GPA", 0.0, 10.0, 8.0, step=0.1)
    with c2: s2 = st.number_input("Sem 2 GPA", 0.0, 10.0, 7.5, step=0.1)
    with c3: s3 = st.number_input("Sem 3 GPA", 0.0, 10.0, 0.0, step=0.1)
    with c4: s4 = st.number_input("Sem 4 GPA", 0.0, 10.0, 0.0, step=0.1)
    c5,c6,c7,c8 = st.columns(4)
    with c5: s5 = st.number_input("Sem 5 GPA", 0.0, 10.0, 0.0, step=0.1)
    with c6: s6 = st.number_input("Sem 6 GPA", 0.0, 10.0, 0.0, step=0.1)
    with c7: s7 = st.number_input("Sem 7 GPA", 0.0, 10.0, 0.0, step=0.1)
    with c8: s8 = st.number_input("Sem 8 GPA", 0.0, 10.0, 0.0, step=0.1)
    valid = [x for x in [s1,s2,s3,s4,s5,s6,s7,s8] if x>0]
    if len(valid)>0:
        cgpa_val = sum(valid)/len(valid)
        st.metric(f"Un CGPA ({len(valid)} Sem)", f"{cgpa_val:.2f} / 10")

with tab5:
    st.subheader("🚨 Detention Calculator - SRM Trichy")
    st.info("**SRM Rule:** 75%+ = Safe | 65-75% = Condonation | <65% = Detention!")
    d_total = st.number_input("Total Classes - Sem Full-a Evlo?", min_value=1, value=80, key="det_total")
    d_att = st.number_input("Nee Pona Classes Evlo?", min_value=0, max_value=int(d_total), value=55, key="det_att")
    d_left = st.number_input("Inime Varapora Classes Evlo?", min_value=0, value=20, key="det_left")
    if d_total>0:
        d_perc = (d_att/d_total)*100
        st.metric("Ippo Un Attendance %", f"{d_perc:.1f}%")
        final_total = d_total + d_left
        final_perc = ((d_att+d_left)/final_total)*100 if final_total>0 else 0
        st.metric("Inime Full-a Pona Final %", f"{final_perc:.1f}%")
        if d_perc >= 75: st.success(f"✅ SAFE DA! {d_perc:.1f}% - Detention Illa!")
        elif d_perc >= 65: st.warning(f"⚠️ CONDONATION ZONE! {d_perc:.1f}% - Medical + Fee Venam!")
        else: st.error(f"🚨 DETENTION RISK! {d_perc:.1f}% - 65%-kku Keela!")

with tab6:
    st.subheader(f"📚 Materials Upload - {branch} | {year} | {sem}")
    st.write("Notes, PDF, Previous Paper, Lab Record Ellam Inga Upload Pannu! Friends-um Paakalaam!")
    st.write("---")

    # --- 1. UPLOAD SECTION ---
    st.subheader("📤 1. Material Upload Pannu")
    mat_subject = st.selectbox("Edha Subject-ku Material?", my_subjects, key="mat_subj")
    mat_type = st.selectbox("Material Type Enna?", ["📝 Notes", "📄 Previous Year Paper", "📕 Question Bank", "🔬 Lab Record / Manual", "📊 Presentation (PPT)", "📖 Textbook / PDF", "📝 Assignment", "🎥 Video Link / YouTube"])
    mat_title = st.text_input("Material Name Enna? Ex: Calculus Unit 1 Notes - Tharun", placeholder="Calculus Unit 1 Full Notes")
    mat_uploader = st.text_input("Un Name? (Yaar Upload Panra?)", placeholder="Ex: Tharun - BME 1st Year")

    uploaded_files = st.file_uploader(
        "File-a Inga Podu Da! (PDF, Image, PPT, Word, Excel Ellam Upload Panna Mudiyum)",
        type=["pdf", "docx", "pptx", "xlsx", "jpg", "jpeg", "png", "txt", "zip"],
        accept_multiple_files=True,
        key="mat_upload"
    )

    # Google Drive / YouTube Link Option
    drive_link = st.text_input("Google Drive / YouTube Link Irundha Inga Podu (Optional)", placeholder="https://drive.google.com/... / https://youtube.com/...")

    if st.button("📚 Material-a Upload Pannu! ✅"):
        if mat_title or uploaded_files or drive_link:
            st.success(f"✅ **{mat_title if mat_title else 'Material'}** Upload Aayiduchu Da! 🔥")
            st.balloons()
            st.write(f"**Subject:** {mat_subject}")
            st.write(f"**Type:** {mat_type}")
            st.write(f"**Uploaded By:** {mat_uploader if mat_uploader else 'SRM Student'}")
            if drive_link: st.write(f"**Link:** {drive_link}")
            if uploaded_files:
                for f in uploaded_files: st.write(f"📄 File: {f.name} - {round(f.size/1024, 1)} KB")
        else:
            st.warning("Dei! Material Name-a Illa File-a Podu Da! Onnume Illama Upload Panna Mudiyadhu!")

    if uploaded_files:
        st.write("---")
        st.subheader("👀 2. Nee Upload Panna Files - Ippo Paaru / Download Pannu")
        for f in uploaded_files:
            c1, c2 = st.columns([3, 1])
            with c1:
                st.write(f"📄 **{f.name}** - {mat_subject} - {mat_type}")
                # Image-na Kaatu, PDF-na Download Button
                if f.type in ["image/jpeg", "image/png", "image/jpg"]:
                    st.image(f, width=300)
                elif f.type == "application/pdf":
                    st.write("📕 PDF File - Keela Download Button-la Download Pannu!")
                elif f.type == "text/plain":
                    st.text(f.read().decode("utf-8", errors="ignore")[:2000])
                else:
                    st.write(f"File Type: {f.type}")
            with c2:
                st.download_button(f"⬇️ Download {f.name}", data=f.getvalue(), file_name=f.name, mime=f.type, key=f"dl_{f.name}")

    st.write("---")

    # --- 2. SUBJECT WISE MATERIALS LIST (READY-MADE) ---
    st.subheader("📂 3. Subject-wise Materials - Ready List")
    st.write("SRM Trichy Students-ku Thevaiyana Materials - Click Panni Download Pannu / Link-a Open Pannu!")
    # Filter by selected subject
    show_subj = st.selectbox("Paakka Subject Select Pannu", ["All Subjects"] + my_subjects, key="show_mat_subj")

    # Ready materials dict - SRM Common
    ready_mats = [
        ("Calculus and Linear Algebra", "📝", "Unit 1-5 Full Notes + Important Questions", "SRM Notes - Calculus PDF", "Calculus-la Matrices + ODE Mukkiyam!"),
        ("Calculus and Linear Algebra", "📄", "Previous Year Papers - 2023, 2024, 2025", "SRM Previous Papers", "40% Questions Repeat Aagum!"),
        ("Physics: Electromagnetic Theory, Quantum, Waves & Optics", "📝", "Laser + Fiber Optics Notes + Diagrams", "Physics Notes", "Diagram Podu - 10 Marks Confirm!"),
        ("Chemistry", "📝", "Chemistry Full Notes + Lab Manual", "Chemistry Lab Manual", "Titration Experiment Steps Irukku!"),
        ("Biomedical Sensors", "📝", "Sensors Notes - ECG, Pulse Oximeter", "BME Sensors Notes", "BME-kku Mattum Special!"),
        ("Communicative English", "📝", "English - Presentation + GD Tips", "English Notes", "Placement-ku English Mukkiyam!"),
        ("Programming in Python", "📝", "Python Notes + 50 Programs + Lab Record", "Python Programs", "Lab-la Code Run Panni Paaru!"),
        ("Engineering Graphics and Design", "📝", "Drawing Sheets + CAD Basics", "Graphics Notes", "Scale Olunga Vechuko!"),
    ]

    for subj, emoji, title, fname, tip in ready_mats:
        # Filter
        if show_subj != "All Subjects" and subj not in show_subj and show_subj not in subj:
            # Loose match: if show subject contains part of ready subj
            if not any(w.lower() in subj.lower() for w in show_subj.split() if len(w)>3):
                continue
        with st.expander(f"{emoji} {subj} - {title}"):
            st.write(f"**Material:** {title}")
            st.write(f"**Tip:** {tip}")
            st.write(f"**File:** {fname}")
            # Dummy download - User can replace with real Drive link
            st.write("**Link:** Google Drive-la Upload Panni Inga Link Podu Da! (Keela Text Box-la)")
            if st.button(f"📥 Download - {title[:30]}", key=f"ready_{title[:20]}_{subj[:10]}"):
                st.info("Dei! Ippo Dummy Link Dhaan! Un Real Notes-a Mela Upload Pannina, Adhu Inga Varum! Drive Link-a Inga Podu Da!")

    st.write("---")

    # --- 3. ADD DRIVE LINK - PERMANENT MATERIALS ---
    st.subheader("🔗 4. Permanent Materials - Google Drive Link Add Pannu")
    st.warning("⚠️ **Mukkiyam:** Mela Upload Panna File - App-a Close Panna Poidum! Permanent-a Irukkanumna Google Drive Link Dhaan Best!")
    st.write("**Epdi Panna?**")
    st.write("1. Notes-a Google Drive-la Upload Pannu\n2. Share -> Anyone with Link -> Copy Link\n3. Keela Paste Pannu - Ellarum Paakalaam!")
    g_subject = st.selectbox("Drive Link Edha Subject-ku?", my_subjects, key="drive_subj")
    g_title = st.text_input("Drive Material Name?", placeholder="Ex: BME Sem 1 Full Notes - All Subjects", key="drive_title")
    g_link = st.text_input("Google Drive Link-a Inga Paste Pannu", placeholder="https://drive.google.com/file/d/...", key="drive_link_input")
    g_name = st.text_input("Un Name?", placeholder="Ex: Tharun", key="drive_name")
    if st.button("🔗 Drive Link-a Save Pannu!"):
        if g_link and g_title:
            st.success(f"✅ **{g_title}** Save Aayiduchu! Friends Ellam Paakalaam!")
            st.write(f"**Subject:** {g_subject} | **By:** {g_name if g_name else 'SRM Student'}")
            st.link_button(f"📂 Open Drive Material - {g_title}", g_link)
        else:
            st.warning("Title + Link Rendum Podu Da!")

    st.write("---")
    st.subheader("💡 Materials Tips - SRM Trichy")
    st.info("""
    **1. Notes:** Class Notes + Sir Kodutha PPT - Rendum Serthu Padichu Paaru!
    **2. Previous Paper:** Last 3 Year Paper - 40% Questions Repeat Aagum!
    **3. Lab Record:** Lab Record-a Exam-kku Munnadi Mudichidu - Internal Marks!
    **4. Share Pannu:** Nee Notes Upload Panna, Friends-um Upload Pannuvanga - Ellarum Pass Aagalam!
    **5. Drive Link:** Permanent-a Irukkanumna Drive Link Dhaan Best! File Upload Temporary Dhaan!
    """)

    if st.button("Materials Upload Aayiduchu! 🔥"):
        st.balloons()
        st.write("**Dei Tharun! Notes Share Panna Dhaan Topper Aava Mudiyum! Nee Semma Da! 📚🔥**")

st.write("---")
st.write("Made by Tharun | SRM IST Trichy - Placement + Timetable + Attendance + CGPA + Detention + Materials | 2026 Regulation 🔥")

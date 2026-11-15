import streamlit as st

# --- PAGE SETTING ---
st.set_page_config(page_title="TOPPER MAKER", page_icon="🏆")

# --- LOGIN 🔐 ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🏆 TOPPER MAKER")
    st.subheader("SRM IST | Trichy + KTR Payalugs 🔥")
    st.write("---")
    st.write("### 🔐 Sign In Pannu Da!")
    st.write("SRM Students Mattum Ulla Poga Mudiyum!")

    name = st.text_input("👤 Un Peru Enna?")
    roll = st.text_input("🆔 Roll No - Ex: RA2611013050015")
    srm_mail = st.text_input("📧 SRM Mail ID - Ex: tharun@srmist.edu.in")
    campus_login = st.selectbox("🏫 Campus", ["Trichy Campus", "KTR Campus - Chennai 🔥", "Ramapuram", "Vadapalani", "Delhi NCR", "Amaravati"])
    password = st.text_input("🔑 Password", type="password")

    if st.button("🚀 LOGIN - TOPPER MAKER Ulla Po!"):
        if name and roll and srm_mail and password:
            if "@srmist.edu.in" not in srm_mail and "@srmtrichy.edu.in" not in srm_mail:
                st.error("Dei! SRM Mail ID Mattum Dhaan Da! Ex: name@srmist.edu.in")
            else:
                st.session_state.logged_in = True
                st.session_state.user_name = name
                st.session_state.user_roll = roll
                st.session_state.user_mail = srm_mail
                st.session_state.user_campus = campus_login
                st.success(f"Hello {name}! 🔥 Login Success!")
                st.rerun()
        else:
            st.error("Dei! Ellam Fill Pannu Da!")
    st.write("---")
    st.write("🏆 TOPPER MAKER | Made by Tharun | SRM Trichy + KTR")
    st.stop()

# --- LOGIN AANA APRAM ---
st.success(f"👋 Hello {st.session_state.user_name}! | {st.session_state.user_roll} | {st.session_state.user_mail} | {st.session_state.user_campus}")
# --- BIG RED LOGOUT BUTTON 🔴 ---
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #FF0000 !important;
    color: white !important;
    font-size: 22px !important;
    font-weight: bold !important;
    height: 60px !important;
    width: 100% !important;
    border-radius: 15px !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

if st.button("🚪 LOGOUT - VELIYA PO! 🔴"):
    st.session_state.logged_in = False
    st.rerun()

st.write("---")
st.title("🏆 TOPPER MAKER SRM APP")
st.write("ALL BRANCHES | 2026 Regulation | SRM Trichy + KTR Payalugs 🔥")

# --- MENU ---
menu = st.selectbox("👇 Enna Pakanum?", ["🏠 Home", "💼 Placement", "📅 Timetable", "✅ Attendance", "🎓 CGPA Calculator", "🚨 Detention Check", "📚 Materials"])

if menu == "🏠 Home":
    st.write("### 👋 Hello Topper!")
    st.write("Nee Dhaan Next Topper Da! 🔥")
    st.write("**Un Details:**")
    st.write(f"- **Peru:** {st.session_state.user_name}")
    st.write(f"- **Roll No:** {st.session_state.user_roll}")
    st.write(f"- **SRM Mail:** {st.session_state.user_mail}")
    st.write(f"- **Campus:** {st.session_state.user_campus}")

elif menu == "💼 Placement":
    st.write("### 💼 Placement - Top Companies")
    st.write("- TCS | Infosys | Wipro | Zoho | Accenture")
    st.write("- Highest Package: 50 LPA 🔥")
    st.write("- Average Package: 7 LPA")

elif menu == "📅 Timetable":
    st.write("### 📅 Timetable")
    st.write("Monday: Maths | Physics | BME Basics")
    st.write("Tuesday: Chemistry | English | Lab")
    st.write("Wednesday: Maths | Workshop | Sports")

elif menu == "✅ Attendance":
    st.write("### ✅ Attendance Calculator")
    total = st.number_input("Total Classes", value=40)
    attended = st.number_input("Attended Classes", value=30)
    if total > 0:
        perc = (attended/total)*100
        st.write(f"**Attendance: {perc:.1f}%**")
        if perc >= 75:
            st.success("Safe Da! 🔥")
        else:
            st.error("Danger! Class-ku Po Da!")

elif menu == "🎓 CGPA Calculator":
    st.write("### 🎓 CGPA Calculator")
    m1 = st.number_input("Subject 1 Marks", value=90)
    m2 = st.number_input("Subject 2 Marks", value=85)
    cgpa = ((m1+m2)/2)/10
    st.write(f"**Your CGPA: {cgpa:.2f}**")

elif menu == "🚨 Detention Check":
    st.write("### 🚨 Detention Check")
    st.write("Attendance < 75% na Detention! Careful Da!")

elif menu == "📚 Materials":
    st.write("### 📚 Materials")
    st.write("- BME Notes | Maths Notes | Physics Notes")
    st.write("- Previous Year Question Papers")

st.write("---")
st.write("🏆 Made by THARUN KUMAAR S P | SRM Trichy + KTR Payalugs 🔥")

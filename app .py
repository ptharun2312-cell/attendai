import streamlit as st

st.set_page_config(page_title="B.Tech Doubt App", page_icon="🎓")
st.title("🎓 B.Tech Doubt & Study App")
st.write("1st - 4th Year | All Branches")

year = st.selectbox("Year Select Pannu", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
branch = st.selectbox("Branch Select Pannu", ["CSE", "IT", "ECE", "EEE", "Mech", "Civil", "Other"])

subjects = {
    "1st Year": ["Maths-1", "Physics", "Chemistry", "C Programming", "English"],
    "2nd Year": ["Maths-2", "DSA", "Python", "Digital Logic", "OOPS"],
    "3rd Year": ["DBMS", "OS", "CN", "Java", "Machine Learning"],
    "4th Year": ["AI", "Project", "Cloud Computing", "Cyber Security", "Placement"]
}
subject = st.selectbox("Subject Select Pannu", subjects[year])

tab1, tab2, tab3 = st.tabs(["Doubt Kekkanum", "Notes", "CGPA Calculator"])

with tab1:
    st.subheader(f"{year} - {subject} Doubt")
    doubt = st.text_area("Un Doubt-a Inga Type Pannu")
    if st.button("Doubt Save Pannu"):
        if doubt:
            st.success("Doubt Save Aayiduchu!")
            st.write("Un Doubt:", doubt)
        else:
            st.warning("Doubt Type Pannu Da!")

with tab2:
    st.subheader("Important Topics")
    st.info(f"{subject} - Important: Unit 1, Unit 2, Previous Year Questions, Lab Manual")

with tab3:
    st.subheader("CGPA Calculator")
    s1 = st.number_input("Sem 1 GPA", 0.0, 10.0, 8.0)
    s2 = st.number_input("Sem 2 GPA", 0.0, 10.0, 8.0)
    if st.button("CGPA Calculate"):
        cgpa = (s1+s2)/2
        st.success(f"Un CGPA: {cgpa:.2f}")
        st.write("Percentage:", round(cgpa*9.5, 2), "%")

st.write("Made by Tharun | B.Tech App")

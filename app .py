import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="AttendAI", page_icon="🤖")
st.markdown("<h1 style='text-align:center; color:#2563EB;'>🤖 AttendAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>AI Attendance Predictor | 75% Safe-a Irukkiya?</p>", unsafe_allow_html=True)

if 'data' not in st.session_state:
    st.session_state.data = []

st.write("---")
st.subheader("➕ Student Details Podu")
name = st.text_input("Student Name")
total = st.number_input("Total Class Attended - Total Class Evlo?", min_value=0, step=1)
present = st.number_input("Total Present - Evlo Naal Present?", min_value=0, step=1)

if st.button("Calculate ✅"):
    if name == "":
        st.warning("Name Podu!")
    elif present > total:
        st.error("Present, Total-a Vida Perusa Irukka Mudiyadhu!")
    elif total == 0:
        st.warning("Total Class 0-va Irukka Mudiyadhu!")
    else:
        absent = total - present
        perc = round(present / total * 100, 1)
        st.session_state.data.append({"Name": name, "Total": total, "Present": present, "Absent": absent, "Percentage %": perc})
        st.success(f"{name} Added! Percentage: {perc}%")

st.write("---")
st.subheader("📊 Report + 🤖 AI Predictor")
if len(st.session_state.data) > 0:
    df = pd.DataFrame(st.session_state.data)
    st.table(df)
    for d in st.session_state.data:
        n = d["Name"]
        total = d["Total"]
        present = d["Present"]
        perc = d["Percentage %"]
        st.markdown(f"**{n} - {perc}%**")
        if perc >= 75:
            can_bunk = math.floor(present / 0.75 - total)
            if can_bunk > 0:
                st.success(f"✅ Safe! Innum {can_bunk} Naal Leave Edukkalam!")
            else:
                st.success(f"✅ Safe! Aana Leave Edukka Mudiyadhu!")
        else:
            need = math.ceil((0.75 * total - present) / 0.25)
            st.error(f"⚠️ Danger! Safe Aaga Innum Thodarnthu {need} Naal Present Irukanum!")
            future = round((present + 10) / (total + 10) * 100, 1)
            st.info(f"💡 AI Tip: Adutha 10 Naal Present Irundha {future}% Aayidum!")
        st.write("---")
    if st.button("Clear All 🗑️"):
        st.session_state.data = []
        st.rerun()
else:
    st.info("Innum Yaarum Illa, Mela Details Podu!")
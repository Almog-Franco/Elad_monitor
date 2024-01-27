import streamlit as st

medical_exams = []

st.markdown("<h1 style='text-align: center; color: black;'>מעקב לפיצקן שלנו</h1>", unsafe_allow_html=True)
option = st.sidebar.radio("נסיון בעברית לראות אם יש אפשרות בחירה בעברית", ["תורים לקבוע", "החלפת חיתול", "אוכל"])

if option == "תורים לקבוע":
    st.markdown("<h3 style='text-align: center; color: black;'>להכניס פה את הפרטים של התור שצריך לקבוע</h3>", unsafe_allow_html=True)
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.text_input("שם המרפאה")
    with col_2:
        st.text_input("מטרת הטור")
    with col_3:
        st.button("הוסף")
if option == "החלפת חיתול":
    st.text("פה יהיה הטקסט שצריך לקבוע 2")
if option == "אוכל":
    st.text("פה יהיה הטקסט שצריך לקבוע 3")
# main.py
import streamlit as st
from app.ui import run_ui
from app.simulator import run_simulation

# Sol menü
menu = st.sidebar.radio("📋 Menü", ["Danışman", "Simülasyon"])

if menu == "Danışman":
    run_ui()
elif menu == "Simülasyon":
    run_simulation()


# import streamlit as st
# from app.ui import run_ui
# from app.simulator import run_simulation  # <-- Simülasyon ekranı için

# # Menü Seçimi
# menu = st.sidebar.radio("📋 Menü", ["Danışman", "Simülasyon"])

# if menu == "Danışman":
#     run_ui()
# elif menu == "Simülasyon":
#     run_simulation()


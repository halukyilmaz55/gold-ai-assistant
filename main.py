import streamlit as st
from app.ui import run_ui
from app.simulator import run_simulation
from app.trading import run_trading_interface

# Sol menü
menu = st.sidebar.radio("📋 Menü", ["Danışman", "Simülasyon", "Portföy"])

if menu == "Danışman":
    run_ui()
elif menu == "Simülasyon":
    run_simulation()
elif menu == "Portföy":
    run_trading_interface()


# import streamlit as st
# from app.ui import run_ui
# from app.simulator import run_simulation

# # Sol menü
# menu = st.sidebar.radio("📋 Menü", ["Danışman", "Simülasyon"])

# if menu == "Danışman":
#     run_ui()
# elif menu == "Simülasyon":
#     run_simulation()

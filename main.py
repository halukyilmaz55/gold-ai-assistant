# main.py

import streamlit as st
from app.simulator import run_simulation
from app.trading import run_trading_interface
from app.portfolio import display_portfolio
from app.advisor import advise_user  # 📌 Danışmanlık fonksiyonu import

# Menü seçimi
menu = st.sidebar.radio("📋 Menü", ["Danışman", "Simülasyon", "Portföy", "Durum"])

if menu == "Danışman":
    st.title("🪙 Altın Alım/Satım Danışmanı")
    st.subheader("🔍 Bilgilerinizi Girin")

    monthly_rent = st.number_input("Aylık kira geliri (TL)", min_value=0)
    investment_duration = st.number_input("Yatırım süresi (ay)", min_value=1, step=1)

    if st.button("🧠 Tavsiye Al"):
        advice = advise_user(investment_duration, monthly_rent)
        st.success(advice)

elif menu == "Simülasyon":
    run_simulation()

elif menu == "Portföy":
    run_trading_interface()

elif menu == "Durum":
    display_portfolio()


# # main.py
# import streamlit as st
# from app.ui import run_ui
# from app.simulator import run_simulation
# from app.trading import run_trading_interface
# from app.portfolio import display_portfolio  # ✅ Portföy özeti ekranı

# # Sol menü
# menu = st.sidebar.radio("📋 Menü", ["Danışman", "Simülasyon", "Portföy", "Durum"])

# if menu == "Danışman":
#     run_ui()
# elif menu == "Simülasyon":
#     run_simulation()
# elif menu == "Portföy":
#     run_trading_interface()
# elif menu == "Durum":
#     display_portfolio()  # ✅ Kâr/Zarar ve Mevcut Bakiye ekranı





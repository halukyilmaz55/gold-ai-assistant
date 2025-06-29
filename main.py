# main.py

import streamlit as st
from app.simulator import run_simulation
from app.trading import run_trading_interface
from app.portfolio import display_portfolio
from app.advisor import advise_user                   # 📌 Kural tabanlı öneri
from app.advisor_llm import generate_ai_comment       # 🤖 AI destekli yorum
from app.nosyapi_client import get_gold_price         # 🥇 Güncel altın fiyatı

# Menü seçimi
menu = st.sidebar.radio("📋 Menü", ["Danışman", "Simülasyon", "Portföy", "Durum"])

if menu == "Danışman":
    st.title("🪙 Altın Alım/Satım Danışmanı")
    st.subheader("🔍 Bilgilerinizi Girin")

    monthly_rent = st.number_input("Aylık kira geliri (TL)", min_value=0)
    investment_duration = st.number_input("Yatırım süresi (ay)", min_value=1, step=1)

    if st.button("🧠 Tavsiye Al"):
        # 🎯 Kural tabanlı öneri
        rule_based_advice = advise_user(investment_duration, monthly_rent)
        st.success(rule_based_advice)

        # 🤖 GPT destekli ek yorum
        current_price = get_gold_price()
        ai_comment = generate_ai_comment(investment_duration, monthly_rent, current_price)
        st.info(f"🤖 AI Yorumu: {ai_comment}")

elif menu == "Simülasyon":
    run_simulation()

elif menu == "Portföy":
    run_trading_interface()

elif menu == "Durum":
    display_portfolio()


# # main.py

# import streamlit as st
# from app.simulator import run_simulation
# from app.trading import run_trading_interface
# from app.portfolio import display_portfolio
# from app.advisor import advise_user  # 📌 Danışmanlık fonksiyonu import

# # Menü seçimi
# menu = st.sidebar.radio("📋 Menü", ["Danışman", "Simülasyon", "Portföy", "Durum"])

# if menu == "Danışman":
#     st.title("🪙 Altın Alım/Satım Danışmanı")
#     st.subheader("🔍 Bilgilerinizi Girin")

#     monthly_rent = st.number_input("Aylık kira geliri (TL)", min_value=0)
#     investment_duration = st.number_input("Yatırım süresi (ay)", min_value=1, step=1)

#     if st.button("🧠 Tavsiye Al"):
#         advice = advise_user(investment_duration, monthly_rent)
#         st.success(advice)

# elif menu == "Simülasyon":
#     run_simulation()

# elif menu == "Portföy":
#     run_trading_interface()

# elif menu == "Durum":
#     display_portfolio()







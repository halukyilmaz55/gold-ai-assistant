# main.py

import streamlit as st
from app.ui import run_ui              # Danışman ekranı (yatırım önerisi)
from app.simulator import run_simulation  # Simülasyon ekranı
from app.trading import run_trading_interface  # Portföy yönetimi (işlem girişi)
from app.portfolio import display_portfolio    # Durum özeti (bakiye, kar/zarar)

# 📋 Menü başlığıyla sol tarafta seçim yapılır
menu = st.sidebar.radio("📋 Menü", ["Danışman", "Simülasyon", "Portföy", "Durum"])

# 👇 Menü seçimlerine göre sayfa yönlendirmesi
if menu == "Danışman":
    run_ui()
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





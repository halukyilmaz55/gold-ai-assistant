# app/ui.py
import os
import streamlit as st
from app.nosyapi_client import get_current_gold_price  # ✅ sadece bu yeterli
from app.logic import generate_recommendation
from app.data import record_transaction, get_transaction_history

def run_ui():
    st.title("💰 Altın Alım/Satım Danışmanı")

    # Kullanıcı verisi al
    st.header("🔍 Bilgilerinizi Girin")
    kira = st.number_input("Aylık kira geliri (TL)", min_value=0)
    sure = st.number_input("Yatırım süresi (ay)", min_value=1)

    # Altın fiyatı
    price = get_current_gold_price()
    if price > 0:
        st.markdown(f"📈 Güncel gram altın fiyatı: **{price:.2f} TL**")
    else:
        st.warning("Gram altın fiyatı alınamadı. Lütfen API anahtarınızı kontrol edin.")

    # API Key kontrol
    st.write("🔑 API Key okundu mu?:", os.environ.get("OPENAI_API_KEY", "")[:5])

    # AI Tavsiye
    if st.button("🧠 Tavsiye Al"):
        if price > 0:
            tavsiye = generate_recommendation(price, kira, sure)
            st.success(tavsiye)
        else:
            st.error("Altın fiyatı alınamadığı için tavsiye verilemiyor.")

    # Simülasyon al/sat
    st.header("📊 Portföy İşlemi (Simülasyon)")
    islem = st.selectbox("İşlem türü", ["Al", "Sat"])
    miktar = st.number_input("Miktar (gram)", min_value=0.0)
    if st.button("İşlemi Kaydet"):
        if price > 0:
            record_transaction(islem, miktar, price)
            st.info(f"{islem} işlemi kaydedildi.")
        else:
            st.error("Altın fiyatı alınamadığı için işlem kaydedilemedi.")

    # Geçmiş işlemler
    st.header("📋 Geçmiş İşlemler")
    df = get_transaction_history()
    st.dataframe(df)



# # app/ui.py
# import os
# import streamlit as st
# import app.api as api
# from app.nosyapi_client import get_current_gold_price
# from app.logic import generate_recommendation
# from app.data import record_transaction, get_transaction_history

# def run_ui():
#     st.title("💰 Altın Alım/Satım Danışmanı")

#     # Kullanıcı verisi al
#     st.header("🔍 Bilgilerinizi Girin")
#     kira = st.number_input("Aylık kira geliri (TL)", min_value=0)
#     sure = st.number_input("Yatırım süresi (ay)", min_value=1)

#     # Altın fiyatı
#     price = get_current_gold_price()
#     st.markdown(f"📈 Güncel gram altın fiyatı: **{price} TL**")

#     # API Key kontrol
#     st.write("🔑 API Key okundu mu?:", os.environ.get("OPENAI_API_KEY")[:5])

#     # AI Tavsiye
#     if st.button("🧠 Tavsiye Al"):
#         tavsiye = generate_recommendation(price, kira, sure)
#         st.success(tavsiye)

#     # Simülasyon al/sat
#     st.header("📊 Portföy İşlemi (Simülasyon)")
#     islem = st.selectbox("İşlem türü", ["Al", "Sat"])
#     miktar = st.number_input("Miktar (gram)", min_value=0.0)
#     if st.button("İşlemi Kaydet"):
#         record_transaction(islem, miktar, price)
#         st.info(f"{islem} işlemi kaydedildi.")

#     # Geçmiş işlemler
#     st.header("📋 Geçmiş İşlemler")
#     df = get_transaction_history()
#     st.dataframe(df)

#     st.write("🔍 Altın fiyatı test:", get_current_gold_price())
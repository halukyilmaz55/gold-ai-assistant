# app/advisor.py

import streamlit as st
from app.nosyapi_client import get_gold_price

def advise_user(months: int, monthly_income: float) -> str:
    """
    Yatırım süresi ve aylık gelir girdisine göre yatırım tavsiyesi üretir.
    """
    current_price = get_gold_price()
    if current_price == 0:
        return "❌ Gram altın fiyatı alınamadı. Lütfen API anahtarınızı kontrol edin."

    total_budget = months * monthly_income
    grams = total_budget / current_price

    # Görsel özet
    st.subheader("📊 Tavsiye Özeti")
    st.markdown(f"- 🕐 **Yatırım süresi:** {months} ay")
    st.markdown(f"- 💸 **Toplam bütçe:** {total_budget:.2f} TL")
    st.markdown(f"- 🥇 **Güncel gram altın fiyatı:** {current_price:.2f} TL")
    st.markdown(f"- 📦 **Toplam alınabilecek altın:** {grams:.2f} gram")

    # Tavsiye üretimi
    if months >= 12 and monthly_income >= 7000:
        return f"✅ Uzun vadeli güçlü bir yatırım planlıyorsunuz. Her ay yaklaşık **{grams / months:.2f} gram altın** alarak portföyünüzü istikrarlı şekilde büyütebilirsiniz."
    elif months >= 6:
        return f"📘 Orta vadeli bir planınız var. Her ay ortalama **{grams / months:.2f} gram altın** almanız makul görünüyor."
    elif months < 6 and grams < 15:
        return f"⚠️ Yatırım süresi kısa ve miktar düşük. Altın yerine kısa vadeli likit enstrümanlar da değerlendirilebilir."
    else:
        return f"💡 Her ay **{grams / months:.2f} gram** alarak dalgalanmalardan etkilenmeden birikim yapabilirsiniz."

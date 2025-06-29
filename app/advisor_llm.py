# app/advisor_llm.py

import openai
import streamlit as st

def generate_ai_comment(months: int, monthly_income: float, current_price: float) -> str:
    """
    OpenAI GPT kullanarak yatırım bilgilerine göre yorum üretir.
    """
    try:
        openai.api_key = st.secrets["OPENAI_API_KEY"]

        total_budget = months * monthly_income

        prompt = (
            f"Bir kullanıcı altın yatırımı yapmak istiyor. Aylık kira geliri {monthly_income} TL, "
            f"yatırım süresi {months} ay. Bu sürede toplam {total_budget} TL biriktirecek. "
            f"Şu an gram altın fiyatı {current_price:.2f} TL. "
            "Yatırım stratejisini değerlendiren kısa bir öneri veya yorum yap."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "Yatırım danışmanı gibi davran."},
                {"role": "user", "content": prompt}
            ]
        )

        return response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"AI yorumu alınamadı: {str(e)}"

# app/logic.py
import os
import openai
from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])  # ✅ düzeltildi

def generate_recommendation(price, kira, sure):
    prompt = f"""
Kullanıcının aylık kira geliri: {kira} TL
Yatırım süresi: {sure} ay
Gram altın fiyatı: {price} TL

Buna göre kısa vadeli mi, uzun vadeli mi yatırım daha mantıklı?
Şu an altın alınabilir mi, satılabilir mi?
Kısa net yorum yap.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Yapay zeka yorumuna ulaşılamadı.\nHata: {e}"

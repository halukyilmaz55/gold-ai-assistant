# app/logic.py
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_recommendation(price, kira, sure):
    base = f"""
Kullanıcının aylık kira geliri: {kira} TL
Yatırım süresi: {sure} ay
Gram altın fiyatı: {price} TL

Buna göre kısa vadeli mi, uzun vadeli mi yatırım daha mantıklı?
Şu an altın alınabilir mi, satılabilir mi?
Kısa net yorum yap.
"""
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": base}],
        )
        return completion.choices[0].message["content"]
    except Exception:
        return "Yapay zeka yorumuna ulaşılamadı."

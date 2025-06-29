# app/advisor_llm.py

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_comment(months: int, monthly_income: float, current_price: float) -> str:
    try:
        total_budget = months * monthly_income
        prompt = f"""
        Kullanıcı {months} ay boyunca her ay {monthly_income} TL altın yatırımı yapmak istiyor.
        Güncel gram altın fiyatı {current_price} TL.
        Toplam bütçesi {total_budget} TL.
        Bu bilgilerle kullanıcıya stratejik yatırım tavsiyesi ver.
        """

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen deneyimli bir finans danışmanısın."},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"AI yorumu alınamadı: {str(e)}"

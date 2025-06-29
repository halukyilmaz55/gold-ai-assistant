# app/api.py
import requests
import os

def get_current_gold_price():
    api_key = os.environ.get("NOSYAPI_KEY")
    url = "https://www.nosyapi.com/apiv2/service/economy/currency/exchange-rate"
    params = {
        "apikey": api_key,
        "currency": "gram-altin"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["selling"])
    except Exception as e:
        print("Hata:", e)
        return 0.0

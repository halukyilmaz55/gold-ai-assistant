# app/api.py
import requests

def get_current_gold_price():
    try:
        response = requests.get("https://api.genelpara.com/embed/altin.json")
        data = response.json()
        return float(data["GA"]["satis"].replace(",", "."))
    except Exception:
        return 0.0

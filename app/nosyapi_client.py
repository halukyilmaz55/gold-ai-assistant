# app/nosyapi_client.py
import requests
import streamlit as st

def get_current_gold_price():
    url = "https://www.nosyapi.com/apiv2/service/economy/currency/exchange-rate"
    params = {
        "apiKey": st.secrets["NOSYAPI_KEY"],  # ✅ DİKKAT: apiKey (küçük değil)
        "code": "gram-altin",                 # ✅ 'currency' değil, 'code'
        "type": "gold"                        # ✅ Altın için gerekli parametre
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        price_info = data.get("data")
        if isinstance(price_info, list) and price_info:
            return float(price_info[0].get("selling", 0.0))
        elif isinstance(price_info, dict):
            return float(price_info.get("selling", 0.0))
        else:
            st.warning("Veri formatı beklenmedik şekilde geldi.")
            return 0.0
    except Exception as e:
        st.warning(f"Altın fiyatı alınamadı: {e}")
        return 0.0



# import requests
# import streamlit as st

# def get_current_gold_price():
#     url = "https://www.nosyapi.com/apiv2/service/economy/currency/exchange-rate"
#     params = {
#         "apikey": st.secrets["NOSYAPI_KEY"],
#         "currency": "gram-altin"
#     }
#     try:
#         response = requests.get(url, params=params, timeout=10)
#         response.raise_for_status()
#         data = response.json()
#         return float(data["data"]["selling"])
#     except Exception as e:
#         st.warning(f"Altın fiyatı alınamadı: {e}")
#         return 0.0

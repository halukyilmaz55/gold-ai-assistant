# app/nosyapi_client.py
import requests
import streamlit as st

def get_current_gold_price():
    url = "https://www.nosyapi.com/apiv2/service/economy/currency/exchange-rate"
    params = {
        "apikey": st.secrets["NOSYAPI_KEY"],
        "code": "gram-altin",  # doğru parametre "code"
        "type": "gold"         # gold verisi olduğu belirtilmeli
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Beklenen format: data -> list -> [0] -> selling
        if "data" in data and isinstance(data["data"], list) and data["data"]:
            selling_price = data["data"][0].get("selling")
            if selling_price:
                return float(selling_price)
            else:
                st.warning("💡 Altın fiyatı verisi boş döndü.")
        else:
            st.warning("🚨 Beklenen formatta veri alınamadı.")
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

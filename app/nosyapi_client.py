import requests
import streamlit as st

def get_current_gold_price():
    """NosyAPI'den gram altın fiyatını çek"""
    url = "https://api.nosyapi.com/v1/economy/gold"
    headers = {
        "Authorization": f"Bearer {st.secrets['NOSYAPI_KEY']}"
    }
    params = {
        "code": "gram-altin"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return float(data['result']['buying'])
    except Exception as e:
        st.warning(f"Hata: {e}")
        return 2450.0



# # app/nosyapi_client.py
# import requests
# import streamlit as st

# def get_current_gold_price():
#     url = "https://www.nosyapi.com/apiv2/service/economy/currency/exchange-rate"
#     params = {
#         "apiKey": st.secrets["NOSYAPI_KEY"],
#         "code": "gram-altin",
#         "type": "gold"
#     }
#     try:
#         response = requests.get(url, params=params, timeout=10)
#         response.raise_for_status()
#         data = response.json()

#         # API cevabı hem list hem dict olabiliyor
#         price_info = data.get("data")
#         if isinstance(price_info, list) and price_info:
#             return float(price_info[0].get("selling", 0.0))
#         elif isinstance(price_info, dict):
#             return float(price_info.get("selling", 0.0))
#         else:
#             st.warning("Veri formatı beklenmedik.")
#             return 0.0
#     except Exception as e:
#         st.warning(f"Altın fiyatı alınamadı: {e}")
#         return 0.0
# app/nosyapi_client.py
import requests
import streamlit as st

def get_gold_price(api_key: str = None) -> float:
    """
    NosyAPI'den 'gramaltin' koduna sahip altının satış fiyatını döndürür.
    """
    try:
        if not api_key:
            api_key = st.secrets["NOSYAPI_KEY"]

        url = "https://www.nosyapi.com/apiv2/service/economy/live-exchange-rates"
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        params = {
            "code": "gramaltin"
        }

        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("status") != "success":
            raise ValueError("API başarısız yanıt verdi.")

        item = data.get("data", [])[0]  # gramaltin tek sonuç dönüyor
        return float(item["sell"])

    except Exception as e:
        print(f"[Altın Fiyatı Hatası] {e}")
        return 0.0


# import requests
# import streamlit as st

# def get_gold_price(api_key: str = None) -> float:
#     """
#     NosyAPI'den 'gramaltin' koduna sahip altının satış fiyatını döndürür.
#     """
#     try:
#         if not api_key:
#             api_key = st.secrets["NOSYAPI_KEY"]

#         url = "https://www.nosyapi.com/apiv2/service/economy/live-exchange-rates/list"
#         headers = {
#             "Authorization": f"Bearer {api_key}"
#         }

#         response = requests.get(url, headers=headers, timeout=10)
#         response.raise_for_status()

#         data = response.json()

#         if data.get("status") != "success":
#             raise ValueError("API başarısız yanıt verdi.")

#         for item in data.get("data", []):
#             if item.get("code", "").lower() == "gramaltin":  # Dikkat: "-" değil
#                 return float(item["selling"])

#         raise KeyError("'gramaltin' kodlu veri bulunamadı.")

#     except Exception as e:
#         print(f"[Altın Fiyatı Hatası] {e}")
#         return 0.0


# # app/nosyapi_client.py

# import requests
# import streamlit as st

# def get_gold_price():
#     """NosyAPI'den gram altın fiyatını çeker."""
#     url = "https://www.nosyapi.com/apiv2/service/economy/currency/list"
#     headers = {
#         "Authorization": f"Bearer {st.secrets['NOSYAPI_KEY']}"
#     }
#     params = {
#         "code": "gram-altin"
#     }

#     try:
#         response = requests.get(url, headers=headers, params=params, timeout=10)
#         response.raise_for_status()
#         data = response.json()
#         return float(data['result']['buying'])
#     except Exception as e:
#         st.warning(f"Altın fiyatı alınamadı: {e}")
#         return 2450.0  # fallback fiyat




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
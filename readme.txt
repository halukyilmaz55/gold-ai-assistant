
streamlit cloud da host edilecek (Mac localde yazıldı)

-------------

echo "# gold-ai-assistant" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/halukyilmaz55/gold-ai-assistant.git
git push -u origin main


git remote add origin https://github.com/halukyilmaz55/gold-ai-assistant.git
git branch -M main
git push -u origin main

---------

gold-ai-assistant/
├── app/
│   ├── __init__.py
│   ├── ui.py              # Streamlit arayüzü
│   ├── logic.py           # Ana iş mantığı (kural + AI öneri)
│   ├── data.py            # DB işlemleri (SQLite)
│   ├── api.py             # Altın fiyatı veri sağlayıcıları
│   └── config.py          # Ayarlar (modüler yapı)
├── data/
│   └── history.db         # SQLite veritabanı
├── main.py                # Streamlit giriş noktası
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml        # UI ayarları

-----------

📦 Modül Detayları
✅ api.py
get_gold_price_from_nosyapi()

İleride get_gold_price_from_vakifbank(), get_price_from_foreks() gibi fonksiyonlar kolayca eklenebilir.

✅ logic.py
Kurallı sistem ve LLM analizi ayrı fonksiyonlarda

Sonradan “risk profili”, “grafik analizi” gibi modüller kolayca eklenebilir

✅ ui.py
Streamlit bileşenleri burada.

Genişletildiğinde sayfa sayfa ayrılabilir (örneğin portfolio_ui.py)

🧠 Esneklik Sağlayan Özellikler
Özellik	Açıklama
🔌 Plug-in mimarisi	Yeni analiz / API / işlem modülleri eklenebilir
🔄 Ayarlanabilir veri sağlayıcı	Tek yerden config.py ile API seçimi yapılabilir
🔐 Secret yönetimi	OpenAI key vs. için Streamlit secrets.toml desteği
🧪 Teste uygun yapı	Modüller bağımsız yazıldığından kolay test edilebilir

🚀 İlk Sürümde Ne Olacak?
🎯 Hedef Fonksiyonlar
 Güncel altın verisi (NosyAPI ile)

 Kullanıcıdan kira ve hedef süresi alma

 AI destekli analiz + açıklama üretme

 Simülasyon işlemi: al/sat → portföyde kaydetme

 SQLite ile geçmiş işlemleri görüntüleme

 ---------------


 🎯 Proje Amacı:
Yapay zekâ destekli, altın alım-satım danışmanı uygulaması — Streamlit Cloud üzerinde çalışacak, modüler yapıda geliştirilecek.

🔨 Özellikler:
 Güncel altın verisi çekme (API üzerinden)

 Kullanıcıdan kira ve yatırım süresi alma

 GPT destekli analiz ve öneri

 Alım/satım simülasyonu (gerçek işlem henüz yok)

 SQLite ile geçmiş işlem kaydı

 Modüler yapı (ileride kolayca genişletilebilir)

🌐 Yayınlama:
GitHub’a yüklenecek

Streamlit Cloud'da host edilecek

OpenAI key, Streamlit Cloud "Secrets" bölümünde tanımlanacak


-----------


# Kişisel Portfolyo

Yağız Enes Doğan'ın kişisel portfolyo websitesi. FastAPI backend ve Jinja2 template'leri ile geliştirilmiştir.

## Proje Yapısı

```
├── backend/
│   ├── app/
│   │   ├── main.py         # FastAPI uygulaması
│   │   └── database.py     # Database bağlantısı
│   ├── models/             # SQLAlchemy modelleri
│   ├── routers/            # API route'ları
│   └── schemas/            # Pydantic şemaları
├── frontend/
│   ├── base.html           # Ana sayfa
│   ├── projects.html       # Proje detay sayfası
│   ├── css/                # Stil dosyaları
│   ├── js/                 # JavaScript dosyaları
│   └── assets/             # Görseller
├── requirements.txt        # Python bağımlılıkları
├── Dockerfile             # Docker yapılandırması
├── docker-compose.yml     # Docker Compose
└── .env.example           # Örnek environment değişkenleri
```

## Lisans

MIT License

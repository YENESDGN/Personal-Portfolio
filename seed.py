import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.app import database
from backend.models.project import Project
from sqlalchemy.orm import Session

# Tabloları oluştur
database.Base.metadata.create_all(bind=database.engine)

db = Session(bind=database.engine)

print("Veriler Ekleniyor...")

p1 = Project(
        title = "CineFlow",
        title_en = "CineFlow",
        description = "CineFlow, film ve dizi severlerin içerikleri keşfedebileceği, değerlendirebileceği ve kişisel listeler oluşturabileceği modern bir web uygulamasıdır. TMDB API entegrasyonu ile güncel içerik verileri sunan platform, kullanıcı dostu arayüzü ve zengin özellikleriyle öne çıkar. Gerek film tutkunları gerekse dizi meraklıları için ideal bir deneyim sunar.",
        description_en = "CineFlow is a modern web application where movie and series enthusiasts can discover content, rate it, and create personalized lists. The platform stands out with its user-friendly interface and rich features powered by TMDB API integration providing up-to-date content data. It offers an ideal experience for both movie lovers and series enthusiasts.",
        description2 = "Özellikler ; Geniş Katalog : Film ve dizileri keşfetmek için kapsamlı bir veritabanı. \n" \
        "Kullanıcı Profilleri : Kişiselleştirilmiş deneyim. Kullanıcılar favori içeriklerini listeleyip, değerlendirebilir. \n" \
        "Teknik Özellikler : Frontend : React.js, Tailwind CSS. Backend : Flask, SQLAlchemy. API Entegrasyonu : TMDB API ve GEMINI ya da ChatGPT.",
        description2_en = "Features: Extensive Catalog: A comprehensive database for discovering movies and series. \n" \
        "User Profiles: Personalized experience. Users can list and rate their favorite content. \n" \
        "Technical Features: Frontend: React.js, Tailwind CSS. Backend: Flask, SQLAlchemy. API Integration: TMDB API and GEMINI or ChatGPT.",
        image_url = "/static/assets/project_images/CineFlow-Kapak.png",
        image_url2 = "/static/assets/project_images/CineFlow-2.png",
        github_url = "https://github.com/YENESDGN/CineFlow"
)

p2 = Project(
        title = "StockMaster",
        title_en = "StockMaster",
        description = "StockMaster, modern ve güvenilir bir stok yönetim sistemidir. FastAPI ve React teknolojileri ile geliştirilmiş bu web uygulaması, işletmelerin ürün yönetimi, stok takibi, kategori organizasyonu ve tedarikçi bilgilerini tek bir platform üzerinden yönetmesini sağlar. JWT tabanlı kimlik doğrulama ile güvenli erişim sunan sistem, PostgreSQL veritabanı kullanarak verileri güvenle depolar. Swagger UI aracılığıyla API dokümantasyonu da sunmaktadır.",
        description_en = "StockMaster is a modern and reliable inventory management system. This web application, developed with FastAPI and React technologies, enables businesses to manage product management, inventory tracking, category organization, and supplier information from a single platform. The system provides secure access with JWT-based authentication and safely stores data using PostgreSQL database. It also provides API documentation through Swagger UI.",
        description2 = "Python 3.11 ve FastAPI framework ile geliştirilmiş asenkron bir backend'e sahiptir. SQLModel ORM kullanılarak PostgreSQL veritabanına bağlanır ve Pydantic v2 ile veri doğrulama yapılır. Frontend, React 18 ve TypeScript ile inşa edilmiş olup Tailwind CSS 4 ile stillendirilmiştir. JWT tabanlı kimlik doğrulama, bcrypt şifreleme ve CORS güvenlik önlemleri uygulanmıştır. AWS Lambda/Azure Functions uyumlu serverless fonksiyonlar da içerir.",
        description2_en = "It features an asynchronous backend developed with Python 3.11 and FastAPI framework. It connects to PostgreSQL database using SQLModel ORM and performs data validation with Pydantic v2. The frontend is built with React 18 and TypeScript, styled with Tailwind CSS 4. JWT-based authentication, bcrypt encryption, and CORS security measures are implemented. It also includes serverless functions compatible with AWS Lambda/Azure Functions.",
        image_url = "/static/assets/project_images/StockMaster-1.png",
        image_url2 = "/static/assets/project_images/StockMaster-2.png",
        github_url = "https://github.com/YENESDGN/StockMaster"
)

p3 = Project(
    title = "VisData",
    title_en = "VisData",
    description = "VisData, kullanıcıların CSV ve Excel dosyalarını kolayca yükleyip analiz etmelerini sağlayan yapay zeka destekli modern bir veri görselleştirme platformudur. FastAPI ve React teknolojileriyle geliştirilen bu uygulama, OpenAI entegrasyonu sayesinde verileriniz için en uygun grafik türlerini otomatik olarak önerir. İnteraktif tablolar, akıllı sohbet asistanı ve güvenli kullanıcı yönetimiyle karmaşık veri setlerini hızlıca anlamlı görsel içgörülere dönüştürerek profesyonel analiz süreçlerini kolaylaştırmayı hedefler.",
    description_en = "VisData is an AI-powered modern data visualization platform that enables users to easily upload and analyze CSV and Excel files. Developed with FastAPI and React technologies, this application automatically suggests the most suitable chart types for your data thanks to OpenAI integration. With interactive tables, smart chat assistant, and secure user management, it aims to simplify professional analysis processes by quickly transforming complex datasets into meaningful visual insights.",
    description2 = "VisData, modern bir teknoloji yığını üzerine inşa edilmiştir. Frontend tarafında React 18, TypeScript ve Vite kullanılarak yüksek performanslı ve tip güvenli bir kullanıcı deneyimi sunulur. Tailwind CSS ile şık bir glassmorphism arayüzü tasarlanmıştır. Backend'de FastAPI'nin asenkron gücü, Pandas'ın veri işleme yetenekleri ve OpenAI API'nin yapay zeka analizi birleşir. Veri güvenliği JWT ve Argon2 ile sağlanırken, SQLAlchemy veritabanı yönetimini optimize eder.",
    description2_en = "VisData is built on a modern technology stack. On the frontend, React 18, TypeScript, and Vite are used to deliver high-performance and type-safe user experience. An elegant glassmorphism interface is designed with Tailwind CSS. On the backend, FastAPI's asynchronous power, Pandas' data processing capabilities, and OpenAI API's AI analysis are combined. Data security is ensured with JWT and Argon2, while SQLAlchemy optimizes database management.",
    image_url = "/static/assets/project_images/VisData-1.png",
    image_url2 = "/static/assets/project_images/VisData-2.png",
    github_url = "https://github.com/YENESDGN/VisData"
)


p4 = Project(
    title = "CoLearn",
    title_en = "CoLearn",
    description = "CoLearn, üniversite öğrencileri için geliştirilmiş kapsamlı bir öğrenme yönetim sistemidir. Yapay zeka destekli sohbet robotu, kişiselleştirilmiş quiz sistemi, çalışma takvimi, Pomodoro zamanlayıcı ve not paylaşım özellikleri sunar. Rozet kazanma ve sıralama sistemiyle öğrenmeyi eğlenceli hale getirir. Öğrencilerin derslerini takip etmelerine, verimli çalışmalarına ve birbirleriyle etkileşim kurmalarına yardımcı olur.",
    description_en = "CoLearn is a comprehensive learning management system developed for university students. It offers AI-powered chat bot, personalized quiz system, study calendar, Pomodoro timer, and note-sharing features. It makes learning fun with badge earning and ranking systems. It helps students track their courses, study efficiently, and interact with each other.",
    description2 = "Django 5.2.6 tabanlı full-stack web uygulaması. Django Channels ile WebSocket desteği, gerçek zamanlı bildirimler ve AI chatbot entegrasyonu sağlar. MySQL veritabanı, gamification sistemi (XP, rozet, leaderboard), PDF'den AI tabanlı quiz üretimi, RESTful API endpoints, kullanıcı profil metrikleri, çoklu dosya yönetimi ve AJAX tabanlı dinamik içerik güncelleme özellikleri içerir. Bootstrap ve FullCalendar kütüphaneleriyle responsive arayüz.",
    description2_en = "Full-stack web application based on Django 5.2.6. It provides WebSocket support with Django Channels, real-time notifications, and AI chatbot integration. It includes MySQL database, gamification system (XP, badges, leaderboard), AI-based quiz generation from PDF, RESTful API endpoints, user profile metrics, multi-file management, and AJAX-based dynamic content updates. Responsive interface with Bootstrap and FullCalendar libraries.",
    image_url = "static/assets/project_images/CoLearn-1.png",
    image_url2 = "static/assets/project_images/CoLearn-2.png",
    github_url = "https://github.com/YENESDGN"
)

db.add(p1)
db.add(p2)
db.add(p3)
db.add(p4)
db.commit()
db.close()

print("Veriler Başarıyla Eklendi.")

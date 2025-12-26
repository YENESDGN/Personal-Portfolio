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
        description = "CineFlow, film ve dizi severlerin içerikleri keşfedebileceği, değerlendirebileceği ve kişisel listeler oluşturabileceği modern bir web uygulamasıdır. TMDB API entegrasyonu ile güncel içerik verileri sunan platform, kullanıcı dostu arayüzü ve zengin özellikleriyle öne çıkar. Gerek film tutkunları gerekse dizi meraklıları için ideal bir deneyim sunar.",
        description2 = "Özellikler ; Geniş Katalog : Film ve dizileri keşfetmek için kapsamlı bir veritabanı. \n" \
        "Kullanıcı Profilleri : Kişiselleştirilmiş deneyim. Kullanıcılar favori içeriklerini listeleyip, değerlendirebilir. \n" \
        "Teknik Özellikler : Frontend : React.js, Tailwind CSS. Backend : Flask, SQLAlchemy. API Entegrasyonu : TMDB API ve GEMINI ya da ChatGPT.",
        image_url = "/static/assets/project_images/CineFlow-Kapak.png",
        image_url2 = "/static/assets/project_images/CineFlow-2.png",
        github_url = "https://github.com/YENESDGN/CineFlow"
)

db.add(p1)
db.commit()
db.close()


p2 = Project(
        title = "StockMaster",
        description = "StockMaster, modern ve güvenilir bir stok yönetim sistemidir. FastAPI ve React teknolojileri ile geliştirilmiş bu web uygulaması, işletmelerin ürün yönetimi, stok takibi, kategori organizasyonu ve tedarikçi bilgilerini tek bir platform üzerinden yönetmesini sağlar. JWT tabanlı kimlik doğrulama ile güvenli erişim sunan sistem, PostgreSQL veritabanı kullanarak verileri güvenle depolar. Swagger UI aracılığıyla API dokümantasyonu da sunmaktadır.",
        description2 = "Python 3.11 ve FastAPI framework ile geliştirilmiş asenkron bir backend'e sahiptir. SQLModel ORM kullanılarak PostgreSQL veritabanına bağlanır ve Pydantic v2 ile veri doğrulama yapılır. Frontend, React 18 ve TypeScript ile inşa edilmiş olup Tailwind CSS 4 ile stillendirilmiştir. JWT tabanlı kimlik doğrulama, bcrypt şifreleme ve CORS güvenlik önlemleri uygulanmıştır. AWS Lambda/Azure Functions uyumlu serverless fonksiyonlar da içerir.",
        image_url = "/static/assets/project_images/StockMaster-1.png",
        image_url2 = "/static/assets/project_images/StockMaster-2.png",
        github_url = "https://github.com/YENESDGN/StockMaster"
)

db.add(p2)
db.commit()
db.close()

p3 = Project(
    title = "VisData",
    description = "VisData, kullanıcıların CSV ve Excel dosyalarını kolayca yükleyip analiz etmelerini sağlayan yapay zeka destekli modern bir veri görselleştirme platformudur. FastAPI ve React teknolojileriyle geliştirilen bu uygulama, OpenAI entegrasyonu sayesinde verileriniz için en uygun grafik türlerini otomatik olarak önerir. İnteraktif tablolar, akıllı sohbet asistanı ve güvenli kullanıcı yönetimiyle karmaşık veri setlerini hızlıca anlamlı görsel içgörülere dönüştürerek profesyonel analiz süreçlerini kolaylaştırmayı hedefler.",
    description2 = "VisData, modern bir teknoloji yığını üzerine inşa edilmiştir. Frontend tarafında React 18, TypeScript ve Vite kullanılarak yüksek performanslı ve tip güvenli bir kullanıcı deneyimi sunulur. Tailwind CSS ile şık bir glassmorphism arayüzü tasarlanmıştır. Backend'de FastAPI'nin asenkron gücü, Pandas'ın veri işleme yetenekleri ve OpenAI API'nin yapay zeka analizi birleşir. Veri güvenliği JWT ve Argon2 ile sağlanırken, SQLAlchemy veritabanı yönetimini optimize eder.",
    image_url = "/static/assets/project_images/VisData-1.png",
    image_url2 = "/static/assets/project_images/VisData-2.png",
    github_url = "https://github.com/YENESDGN/VisData"
)

db.add(p3)
db.commit()
db.close()

p4 = Project(
        title = "TicTacToe",
        description = "Modern ve şık arayüzüyle klasik X-O oyununu yeniden keşfedin. Avalonia UI ve .NET 9.0 ile geliştirilmiş bu uygulama, MVVM mimarisi sayesinde temiz kod yapısına sahip. CPU'ya karşı akıllıca hamle yapın, skorunuzu takip edin ve Fluent Design temasının sunduğu keyifli görsel deneyimin tadını çıkarın. Hem Windows, hem Linux, hem macOS'ta sorunsuz çalışır.",
        description2 = ".NET 9.0 ve Avalonia UI 11.3 ile geliştirilen cross-platform X-O oyunu. CommunityToolkit.Mvvm kütüphanesi ile güçlendirilmiş MVVM mimarisi, ObservableCollection tabanlı reaktif veri bağlama ve modern C# özellikleri kullanır. Fluent Design tema desteği, asenkron oyun akışı ve dinamik UI güncellemeleriyle profesyonel bir kod yapısı sunar. Linux, Windows ve macOS'ta native performans sağlar.",
        image_url = "/static/assets/project_images/TicTacToe-1.png",
        image_url2 = "/static/assets/project_images/TicTacToe-2.png",
        github_url = "https://github.com/YENESDGN/TicTacToe"
)

db.add(p4)
db.commit()     
db.close()

p5 = Project(
        title = "MineSweep",
        description = "Mayın Tarlası, Avalonia framework ile geliştirilmiş, modern ve cross-platform bir masaüstü oyunudur. Şık koyu teması, akıcı animasyonları ve responsive tasarımıyla Windows, Linux ve macOS üzerinde sorunsuz çalışır. 68 hücreli oyun alanında 15 mayını bularak strateji becerilerinizi test edin!",
        description2 = "Teknik Özellikler : Proje, Avalonia UI 11.2.1 ve .NET 8.0 ile C# dilinde geliştirilmiş cross-platform bir masaüstü uygulamasıdır. Windows, Linux ve macOS'ta çalışır. 68 hücreli oyun alanında 15 mayın rastgele yerleştirilir. Koyu tema, Fluent tasarım dili ve responsive WrapPanel yapısı kullanılmıştır. Oyun mantığı code-behind yaklaşımıyla 135 satırda implemente edilmiştir.",
        image_url = "/static/assets/project_images/MineSweep-1.png",
        image_url2 = "/static/assets/project_images/MineSweep-2.png",
        github_url = "https://github.com/YENESDGN/MineSweep"
)

db.add(p5)
db.commit()
db.close()


print("Veriler Başarıyla Eklendi.")

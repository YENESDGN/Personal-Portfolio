from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
import base64
import random

# Backend klasörünü path'e ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app.database import engine, Base, get_db
from backend.models.project import Project
from backend.routers import projects

#Database Oluşturma
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mevcut Dosya Yolu
current_path_file = os.path.dirname(os.path.abspath(__file__))

#Şifreleme Yolu
templates = Jinja2Templates(directory=os.path.join(current_path_file,"../../frontend"))

#Dinamik Şifreleme Fonksiyonu
def get_encrypted_email(email : str):
    key = random.randint(1,255)
    encrytped_bytes = bytes([ord(char) ^ key for char in email])
    encoded_email = base64.urlsafe_b64encode(encrytped_bytes).decode('utf-8')

    return encoded_email, key


# Klasör Yolu
frontend_path = os.path.join(current_path_file, "../../frontend")

#1 Cors Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"]
)

#Router Dahiliyeti
app.include_router(projects.router, prefix="/api", tags=["projects"])

#Statik Dosya Ayarları
app.mount("/static", StaticFiles(directory=os.path.join(frontend_path)), name="static")


@app.get("/")
async def read_index(request: Request): 
    
    mail_adresi = "mailto:yenesdogan@outlook.com.tr"
    sifreli_kod, anahtar = get_encrypted_email(mail_adresi)
    
    return templates.TemplateResponse("base.html", {
        "request": request,            
        "encrypted_mail": sifreli_kod, 
        "secret_key": anahtar         
    })


@app.get("/projects.html")  
async def read_projects():
    projects_path = os.path.join(frontend_path, "projects.html")
    return FileResponse(projects_path)
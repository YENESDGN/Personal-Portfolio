from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import sys

# Backend klasörünü path'e ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import engine, Base, get_db
from models.project import Project
from routers import projects

#Database Oluşturma
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mevcut Dosya Yolu
current_path_file = os.path.dirname(os.path.abspath(__file__))

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
async def read_index():
    index_path = os.path.join(frontend_path, "base.html")
    return FileResponse(index_path)

@app.get("/projects.html")  
async def read_projects():
    projects_path = os.path.join(frontend_path, "projects.html")
    return FileResponse(projects_path)
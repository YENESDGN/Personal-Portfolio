import os
import sys
import base64
import random
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO if os.getenv("APP_ENV") == "production" else logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Backend klasörünü path'e ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app.database import engine, Base, get_db
from backend.models.project import Project
from backend.routers import projects


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup/shutdown events."""
    # Startup
    logger.info("Application starting up...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created/verified")
    yield
    # Shutdown
    logger.info("Application shutting down...")


app = FastAPI(
    title="Kişisel Portfolyo API",
    description="Yağız Enes Doğan - Portfolyo Backend API",
    version="1.0.0",
    lifespan=lifespan
)

# Mevcut Dosya Yolu
current_path_file = os.path.dirname(os.path.abspath(__file__))

# Templates
templates = Jinja2Templates(directory=os.path.join(current_path_file, "../../frontend"))

# Klasör Yolu
frontend_path = os.path.join(current_path_file, "../../frontend")


# CORS Settings - Environment'tan oku
def get_allowed_origins():
    """Get CORS origins from environment variable."""
    origins = os.getenv("ALLOWED_ORIGINS", "*")
    if origins == "*":
        return ["*"]
    return [origin.strip() for origin in origins.split(",")]


app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)


# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Handle all unhandled exceptions."""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "path": str(request.url.path)
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions with logging."""
    logger.warning(f"HTTP {exc.status_code}: {exc.detail} - Path: {request.url.path}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


# Router Dahiliyeti
app.include_router(projects.router, prefix="/api", tags=["projects"])

# Statik Dosya Ayarları
app.mount("/static", StaticFiles(directory=frontend_path), name="static")


# Dinamik Şifreleme Fonksiyonu
def get_encrypted_email(email: str):
    key = random.randint(1, 255)
    encrypted_bytes = bytes([ord(char) ^ key for char in email])
    encoded_email = base64.urlsafe_b64encode(encrypted_bytes).decode('utf-8')
    return encoded_email, key


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "version": "1.0.0"}


@app.get("/")
async def read_index(request: Request):
    logger.debug("Serving index page")
    mail_adresi = "mailto:yenesdogan@outlook.com.tr"
    sifreli_kod, anahtar = get_encrypted_email(mail_adresi)
    
    return templates.TemplateResponse("base.html", {
        "request": request,
        "encrypted_mail": sifreli_kod,
        "secret_key": anahtar
    })


@app.get("/projects.html")
async def read_projects():
    logger.debug("Serving projects page")
    projects_path = os.path.join(frontend_path, "projects.html")
    return FileResponse(projects_path)
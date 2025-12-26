from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.project import ProjectBase
from backend.app.database import get_db
from backend.models.project import Project

router = APIRouter()

@router.get("/projects", response_model=List[ProjectBase])
async def read_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return projects

@router.get("/projects/{project_id}", response_model=ProjectBase)
async def read_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Proje bulunamadı")
    return project
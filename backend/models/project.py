from sqlalchemy import Column, Integer, String, Text
from backend.app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    description2 = Column(Text)
    image_url = Column(String)
    image_url2 = Column(String, nullable=True)
    github_url = Column(String, nullable=True)

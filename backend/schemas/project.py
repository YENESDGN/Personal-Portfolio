from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProjectBase(BaseModel):

    id: int
    title: str
    title_en: Optional[str] = None
    description: str
    description_en: Optional[str] = None
    description2: str 
    description2_en: Optional[str] = None
    image_url: str
    image_url2: Optional[str] = None
    github_url: Optional[str] = None

    model_config = ConfigDict(from_attributes = True)
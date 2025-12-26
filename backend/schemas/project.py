from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProjectBase(BaseModel):

    id: int
    title: str
    description: str
    description2: str 
    image_url: str
    image_url2: Optional[str] = None
    github_url: str

    model_config = ConfigDict(from_attributes = True)
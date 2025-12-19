from pydantic import BaseModel, ConfigDict

class ProjectBase(BaseModel):
    id:int
    title : str
    description : str
    description2 : str 
    image_url : str

    model_config = ConfigDict(from_attributes = True)
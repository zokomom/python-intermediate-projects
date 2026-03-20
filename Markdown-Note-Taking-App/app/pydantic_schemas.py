from pydantic import BaseModel

class GetNotes(BaseModel):
    id:int
    title:str
    markdown_content:str
    model_config={
        "from_attributes":True
    }

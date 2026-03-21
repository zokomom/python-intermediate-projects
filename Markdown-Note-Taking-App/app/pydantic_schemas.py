from pydantic import BaseModel
from datetime import datetime

class GetNotes(BaseModel):
    id:int
    title:str
    markdown_content:str
    created_at:datetime
    model_config={
        "from_attributes":True
    }

class CreateNote(BaseModel):
    title:str
    markdown_content:str

class GrammarCheck(BaseModel):
    title:str
    markdown_content:str
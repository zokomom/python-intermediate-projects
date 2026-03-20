from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.pydantic_schemas import GetNotes
from app.database import get_db


router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.get("",response_model=list[GetNotes])
def get_notes(db:Session=Depends(get_db)):
    return [
        GetNotes(id=1,title="First Note",markdown_content="This is the content of the first note."),
        GetNotes(id=2,title="Second Note",markdown_content="This is the content of the second note.")
    ]

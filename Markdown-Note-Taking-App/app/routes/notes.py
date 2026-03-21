from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.pydantic_schemas import GetNotes,CreateNote
from app.database import get_db
from app.models import Note

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.get("",response_model=list[GetNotes])
def get_notes(db:Session=Depends(get_db)):
    return db.query(Note).all()

@router.post("",response_model=GetNotes,status_code=201)
def create_note(note:CreateNote,db:Session=Depends(get_db)):
    new_note = Note(**note.model_dump())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note
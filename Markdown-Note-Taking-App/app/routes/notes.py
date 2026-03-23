from fastapi import APIRouter, Depends, UploadFile, HTTPException, Query
from sqlalchemy.orm import Session
from app.pydantic_schemas import GetNotes, CreateNote
from app.database import get_db
from app.models import Note
import markdown
import bleach
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.get("", response_model=list[GetNotes])
def get_notes(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    notes = db.query(Note).offset(skip).limit(limit).all()
    return notes


@router.post("", response_model=GetNotes, status_code=201)
def create_note(note: CreateNote, db: Session = Depends(get_db)):
    new_note = Note(**note.model_dump())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@router.get("/{note_id}/html", response_class=HTMLResponse)
def render_html(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    # Convert Markdown → HTML
    html = markdown.markdown(note.markdown_content)

    # Sanitize HTML
    safe_html = bleach.clean(
        html,
        tags=[
            "p", "h1", "h2", "h3", "h4",
            "ul", "ol", "li",
            "strong", "em",
            "a", "code", "pre", "blockquote", "hr"
        ],
        attributes={
            "a": ["href", "title"]
        },
        protocols=["http", "https", "mailto"],
        strip=True
    )

    return safe_html


@router.post("/upload-markdown", response_model=GetNotes, status_code=201)
async def upload_markdown(file: UploadFile, db: Session = Depends(get_db)):

    if not file.filename.endswith(".md"):
        raise HTTPException(status_code=400, detail="Only .md files allowed")

    content = await file.read()

    try:
        text = content.decode("utf-8")
    except:
        raise HTTPException(status_code=400, detail="Invalid file encoding")

    new_note = Note(
        title=file.filename,
        markdown_content=text
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

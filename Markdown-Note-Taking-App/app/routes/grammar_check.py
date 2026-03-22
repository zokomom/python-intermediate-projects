from fastapi import APIRouter, status
from spellchecker import SpellChecker
from ..pydantic_schemas import GrammarCheck

router = APIRouter(
    prefix="/grammar-check",
    tags=["Grammar Check"]
)

spell = SpellChecker()


@router.post("", status_code=status.HTTP_200_OK)
def check_grammar(note: GrammarCheck):
    full_text = note.title + " " + note.markdown_content
    words = full_text.split()
    misspelled = spell.unknown(words)
    corrections = {word: spell.correction(word) for word in misspelled}
    return {
        "original_title": note.title,
        "original_content": note.markdown_content,
        "mistakes": len(misspelled),
        "corrections": corrections
    }

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
    words = note.markdown_content.split()
    misspelled = spell.unknown(words)
    corrections = {word: spell.correction(word) for word in misspelled}
    return {
        "original": note.markdown_content,
        "mistakes": list(misspelled),
        "corrections": corrections
    }

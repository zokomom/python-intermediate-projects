from fastapi import APIRouter, status
from spellchecker import SpellChecker
from ..pydantic_schemas import GrammarCheck
import re

router = APIRouter(
    prefix="/grammar-check",
    tags=["Grammar Check"]
)

spell = SpellChecker()


@router.post("", status_code=status.HTTP_200_OK)
def check_grammar(note: GrammarCheck):

    # Combine text
    full_text = f"{note.title} {note.markdown_content}"

    # Remove markdown symbols and special chars
    clean_text = re.sub(r"[#*_`\-\[\]()]", " ", full_text)

    # Extract only valid words
    words = re.findall(r"\b[a-zA-Z']+\b", clean_text.lower())

    # Find misspelled words
    misspelled = spell.unknown(words)

    # Get corrections
    corrections = {
        word: spell.correction(word)
        for word in misspelled
    }

    return {
        "original_title": note.title,
        "original_content": note.markdown_content,
        "total_words": len(words),
        "mistakes": len(misspelled),
        "corrections": corrections
    }

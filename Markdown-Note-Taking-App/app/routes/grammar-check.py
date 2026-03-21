from fastapi import APIRouter
import language_tool_python
from ..pydantic_schemas import GrammarCheck

router = APIRouter(
    prefix="/grammar-check",
    tags=["Grammar Check"]
)

tool = language_tool_python.LanguageTool('en-US')


@router.post("", status_code=201)
def check_grammar(note: GrammarCheck):
    matches = tool.check(note.markdown_content)
    return {"mistakes": len(matches), "details": matches}

from fastapi import FastAPI
from app.routes import notes, grammar_check

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


app.include_router(notes.router)
app.include_router(grammar_check.router)

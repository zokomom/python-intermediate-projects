from fastapi import FastAPI
from app.routes import notes


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(notes.router)
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Server Imports.
from backend.score import compute_score


app = FastAPI()
templates = Jinja2Templates(directory="frontend/templates")

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", context={
        "request": request
    })


# Validating user input.
class UserInput(BaseModel):
    user_input: str


@app.post("/report")
def generate_report(user_input: UserInput):
    """
    Generate Readability Report.
    """
    user_input = user_input.user_input
    scores, stats = compute_score(user_input)

    return {
        "scores": scores,
        "stats": stats
    }

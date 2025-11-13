from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from .inference import predict, load_model_n_tokenizer
from contextlib import asynccontextmanager

app = FastAPI()
model, tokenizer = load_model_n_tokenizer()

BASE_DIR = Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


class CodeInput(BaseModel):
    code: str


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict_complexity(input_data: CodeInput):
    response = predict(input_data.code, tokenizer, model)
    return {"label": response}

from fastapi import FastAPI
from .inference import predict

app = FastAPI()

@app.get("/")
def root():
    return {"Health": "OK"}


@app.get("/predict")
def run(inputs: str):
    response = predict(inputs)
    return {"label": response}

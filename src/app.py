from flask import Flask, request
from typing import Optional, Any, Dict

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Server Works!"


@app.route("/predict_language", methods=["POST"])
def predict_language() -> str:
    content: Optional[Any] = request.json
    if content:
        body: Dict[str, Any] = content
        print(body["text"])
    return "Hello from Server"

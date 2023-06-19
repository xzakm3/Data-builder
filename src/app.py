from flask import Flask, request, Response
from typing import Optional, Any, Tuple

from src.models.responses.predict_language import PredictLanguage
from src.validation.validator import validate_data

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Server Works!"


@app.route("/predict_language", methods=["POST"])
def predict_language() -> Tuple[Response, int]:
    content: Optional[Any] = request.json
    if not content:
        status = 403
        return PredictLanguage("Missing JSON body", status).to_dict(), status  # type: ignore

    is_valid, msg = validate_data(content)
    if not is_valid:
        status = 403
        return PredictLanguage(msg, status).to_dict(), status  # type: ignore

    status = 200
    return PredictLanguage("Everything is OK", status).to_dict(), status  # type: ignore

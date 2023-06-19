from flask import Flask, request, Response
from typing import Optional, Any, Tuple


from src.predict import predict
from src.validation.validator import validate_data
from src.data_models.responses.predict_language_response import PredictLanguageResponse

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Server Works!"


@app.route("/predict_language", methods=["POST"])
def predict_language() -> Tuple[Response, int]:
    # check presence of data
    content: Optional[Any] = request.json
    if not content:
        status = 403
        return PredictLanguageResponse("Missing JSON body", status).to_dict(), status  # type: ignore

    # validate data
    is_valid, msg = validate_data(content)
    if not is_valid:
        status = 403
        return PredictLanguageResponse(msg, status).to_dict(), status  # type: ignore

    # do prediction
    predict(content)
    status = 200
    return PredictLanguageResponse("Everything is OK", status).to_dict(), status  # type: ignore

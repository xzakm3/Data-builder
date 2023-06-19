from flask import Flask, request, Response
from typing import Optional, Any, Tuple
from src import logger

from src.predict import predict
from src.validation.validator import validate_data
from src.data_models.predict_language_response_body import PredictLanguageResponseBody

app = Flask(__name__)
logger.init_logger()
log = logger.get_logger()


@app.route("/")
def index() -> str:
    return "Server Works!"


@app.route("/predict_language", methods=["POST"])
def predict_language() -> Tuple[Response, int]:
    # check presence of data
    content: Optional[Any] = request.json
    if not content:
        log.warn("JSON body for /predict_language endpoint is empty")
        status = 403
        return PredictLanguageResponseBody("Missing JSON body", status).to_dict(), status  # type: ignore

    # validate data
    is_valid, msg = validate_data(content)
    if not is_valid:
        log.warn("Data schema is invalid")
        status = 403
        return PredictLanguageResponseBody(msg, status).to_dict(), status  # type: ignore

    # do prediction
    results = predict(content)
    log.info(f"Response with prediction results = {results}")
    status = 200
    return PredictLanguageResponseBody("Everything is OK", status, results).to_json(), status  # type: ignore

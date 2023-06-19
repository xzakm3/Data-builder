import fasttext
import os
from typing import Dict, Any

from src.data_models.request_body.predict_language_request_body import PredictLanguageRequestBody

PATH_TO_THIS_FILE: str = os.path.dirname(os.path.abspath(__file__))
PRETRAINED_MODEL_PATH: str = os.path.join(PATH_TO_THIS_FILE, "bin", "lid.176.ftz")


class FastTextLanguagePredictionModel:
    def __init__(self) -> None:
        self._model = fasttext.load_model(PRETRAINED_MODEL_PATH)

    def predict(self, data: Dict[str, Any]) -> None:
        data_for_prediction: PredictLanguageRequestBody = PredictLanguageRequestBody.from_dict(data)  # type: ignore
        texts = data_for_prediction.text
        predictions = self._model.predict(texts)
        print(predictions)

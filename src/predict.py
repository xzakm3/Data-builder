from typing import Dict, Any, List

from src.data_models.responses.predict_language_response import SentencePrediction
from src.prediction_models.fast_text_language_prediction import FastTextLanguagePredictionModel

PREDICTIONS: str = "predictions"


def predict(data: Dict[str, Any]) -> Dict[str, List[SentencePrediction]]:
    model = FastTextLanguagePredictionModel()
    results = model.predict(data)
    return {PREDICTIONS: results}

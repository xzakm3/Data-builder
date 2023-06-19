from typing import Dict, Any, List

from src.prediction_models.fast_text_language_prediction import FastTextLanguagePredictionModel

PREDICTIONS: str = "predictions"


def predict(data: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    model = FastTextLanguagePredictionModel()
    results = model.predict(data)
    return {PREDICTIONS: results}

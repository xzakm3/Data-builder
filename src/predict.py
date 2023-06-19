from typing import Dict, Any

from src.prediction_models.fast_text_language_prediction import FastTextLanguagePredictionModel


def predict(data: Dict[str, Any]) -> None:
    model = FastTextLanguagePredictionModel()
    model.predict(data)

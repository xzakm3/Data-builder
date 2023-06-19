import fasttext
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import os
from typing import Dict, Any, List

from src.data_models.predict_language_request_body import PredictLanguageRequestBody

PATH_TO_THIS_FILE: str = os.path.dirname(os.path.abspath(__file__))
PRETRAINED_MODEL_PATH: str = os.path.join(PATH_TO_THIS_FILE, "bin", "lid.176.ftz")
LANG_PREDICT_PREFIX: str = "__label__"


@dataclass_json
@dataclass
class SentencePrediction:
    sentence: str
    language: str
    confidence: float
    is_confident: bool

    def __post_init__(self) -> None:
        if self.sentence is None:
            raise ValueError("Sentence for SentencePrediction is missing")
        if self.language is None:
            raise ValueError("Predicted Language abbreviation for SentencePrediction is missing")
        if self.confidence is None:
            raise ValueError("Confidence value for SentencePrediction is missing")
        if self.is_confident is None:
            raise ValueError("is_confident bool value for SentencePrediction is missing")


class FastTextLanguagePredictionModel:
    def __init__(self, confidence_threshold: float = 0.9) -> None:
        self._model = fasttext.load_model(PRETRAINED_MODEL_PATH)
        self._confidence_threshold = confidence_threshold

    def _parse_languages(self, languages: List[List[str]]) -> List[str]:
        return [lan[0].replace(LANG_PREDICT_PREFIX, "") for lan in languages]

    def _parse_confidence(self, confidences: List[List[float]]) -> List[float]:
        return [round(float(conf[0]), 4) for conf in confidences]

    def predict(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        data_for_prediction: PredictLanguageRequestBody = PredictLanguageRequestBody.from_dict(data)  # type: ignore
        texts = data_for_prediction.text
        languages, confidences = self._model.predict(texts)
        parsed_langs, parsed_confs = self._parse_languages(languages), self._parse_confidence(confidences)

        results = [
            SentencePrediction(
                text, lang, confidence, confidence >= self._confidence_threshold
            ).to_dict()  # type: ignore
            for (text, lang, confidence) in zip(texts, parsed_langs, parsed_confs)
        ]
        return results

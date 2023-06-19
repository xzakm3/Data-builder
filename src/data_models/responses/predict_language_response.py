from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Dict, Any


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


@dataclass_json
@dataclass
class PredictLanguageResponse:
    message: str
    status: int
    body: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.message is None:
            raise ValueError("Messaage for PredictLanguage response is missing")
        if self.status is None:
            raise ValueError("Status for PredictLanguage response is missing")

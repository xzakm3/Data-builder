from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List


@dataclass_json
@dataclass
class PredictLanguageRequestBody:
    text: List[str]

    def __post_init__(self) -> None:
        if self.text is None:
            raise ValueError("Text data for prediction are missing")

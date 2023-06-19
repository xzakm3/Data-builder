from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Dict, Any


@dataclass_json
@dataclass
class PredictLanguageResponseBody:
    message: str
    status: int
    body: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.message is None:
            raise ValueError("Messaage for PredictLanguage response is missing")
        if self.status is None:
            raise ValueError("Status for PredictLanguage response is missing")

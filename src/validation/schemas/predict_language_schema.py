from typing import Dict, Any


class PredictLanguageSchema:
    schema: Dict[str, Any] = {
        "type": "object",
        "required": ["text"],
        "properties": {"text": {"type": "array", "minItems": 1, "items": {"type": "string"}}},
    }

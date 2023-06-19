from typing import Dict, Any, Tuple
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from src.validation.schemas.predict_language_schema import PredictLanguageSchema


PREDICT_LANGUAGE_SCHEMA: Dict[str, Any] = PredictLanguageSchema.schema


def validate_data(data: Dict[str, Any]) -> Tuple[bool, str]:
    try:
        validate(instance=data, schema=PREDICT_LANGUAGE_SCHEMA)
        return True, ""
    except ValidationError as e:
        print("Validation error")
        return False, e.message

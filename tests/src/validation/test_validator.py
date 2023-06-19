import pytest
from typing import Dict, Any

from src.validation.validator import validate_data


def test_validator__correct_data_schema() -> None:
    data = {"text": ["text1", "text2"]}

    is_valid, msg = validate_data(data)

    assert is_valid is True
    assert msg == ""


@pytest.mark.parametrize("data, expected_is_valid_value", [({}, False), ({"sth": "hmm"}, False), ({"text": []}, False)])
def test_validator__wrong_data_schema(data: Dict[str, Any], expected_is_valid_value: bool) -> None:
    is_valid, _ = validate_data(data)

    assert is_valid is expected_is_valid_value

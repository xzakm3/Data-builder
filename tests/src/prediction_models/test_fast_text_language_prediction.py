from typing import List, Any
import numpy as np
from pytest_mock import MockerFixture

from src.prediction_models.fast_text_language_prediction import FastTextLanguagePredictionModel


def test_fast_text_language_pred__init_with_default_params() -> None:
    model = FastTextLanguagePredictionModel()

    assert hasattr(model, "_model") is True
    assert model._confidence_threshold == 0.8


def test_fast_text_language_pred__init_with_given_params() -> None:
    given_conf_thresh: float = 0.6
    model = FastTextLanguagePredictionModel(confidence_threshold=given_conf_thresh)

    assert hasattr(model, "_model") is True
    assert model._confidence_threshold == given_conf_thresh


def test_fast_text_language_pred__parse_languages() -> None:
    predicted_languages: List[List[str]] = [["__label__em"], ["__label__fk"]]
    model = FastTextLanguagePredictionModel()
    expected_languages = ["em", "fk"]

    result = model._parse_languages(predicted_languages)

    assert expected_languages == result


def test_fast_text_language_pred__parse_confidence_values() -> None:
    predicted_confidence_values: List[Any] = [np.array(["0.5612"]), np.array(["0.6322"])]
    model = FastTextLanguagePredictionModel()
    expected_confidence_values = [0.5612, 0.6322]

    result = model._parse_confidence(predicted_confidence_values)

    assert expected_confidence_values == result


def test_fast_text_language_pred__predict(mocker: MockerFixture) -> None:
    input_data = {"text": ["Hello how are you?", "Tell me what is your name?"]}
    model = FastTextLanguagePredictionModel()
    raw_languages = [["__label__en"], ["__label__en"]]
    raw_confidences = [["0.8554"], ["0.2643"]]
    model._model.predict = mocker.Mock(return_value=[raw_confidences, raw_languages])  # type: ignore
    model._parse_languages = mocker.Mock(return_value=["en", "en"])  # type: ignore
    model._parse_confidence = mocker.Mock(return_value=[0.8554, 0.2643])  # type: ignore
    expected_results = [
        {"sentence": "Hello how are you?", "language": "en", "confidence": 0.8554, "is_confident": True},
        {"sentence": "Tell me what is your name?", "language": "en", "confidence": 0.2643, "is_confident": False},
    ]

    result = model.predict(input_data)

    assert result == expected_results

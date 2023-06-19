from pathlib import Path
from typing_extensions import Final
from typing import List, Dict, Any
import os
import json
import argparse
import pandas as pd
import requests

from src import logger

log = logger.get_logger()

PROJECT_ROOT_PATH = f"{Path(__file__).parent}"
CSV_SUFFIX: Final = ".csv"
CSV_COMMA_SEP: Final = ","
CSV_DOTTED_LINE_SEP: Final = ";"
BASE_API: Final = "http://127.0.0.1:5000"

TEXT_DF_COLUMN_NAME: Final = "text"
SENTENCE_COLUMN_NAME: Final = "sentence"
LANGUAGE_COLUMN_NAME: Final = "language"
CONFIDENCE_COLUMN_NAME: Final = "confidence"
IS_CONFIDENT_COLUMN_NAME: Final = "is_confident"

RESULTS_CSV_FILE: Final = "result_predictions.csv"


def do_predictions(texts: List[str]) -> List[Dict[str, Any]]:
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_API}/predict_language", headers=headers, json=json.dumps({"text": texts}))
    res = response.json()
    if res["status"] == 200:
        return res["body"]["predictions"]
    else:
        raise Exception(f"There was some problem. Status: '{res['status']}', Message: '{res['message']}'")


def load_csv_data(csv_file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(csv_file_path, sep=CSV_COMMA_SEP)
        if df.columns.size <= 1:
            df = pd.read_csv(csv_file_path, sep=CSV_DOTTED_LINE_SEP)
    except pd.errors.ParserError:
        df = pd.read_csv(csv_file_path, sep=CSV_DOTTED_LINE_SEP)

    log.info(f"Data loaded from path: {csv_file_path}")
    return df


def preprocess_input_data(data: pd.DataFrame) -> List[str]:
    cp_data = data.copy()
    cp_data.dropna(inplace=True)
    cp_data.drop_duplicates(inplace=True)

    texts: List[str] = list(cp_data[TEXT_DF_COLUMN_NAME].values)
    return texts


def preprocess_response(predictions: List[Dict[str, Any]]) -> pd.DataFrame:
    feature_names = [SENTENCE_COLUMN_NAME, LANGUAGE_COLUMN_NAME, CONFIDENCE_COLUMN_NAME, IS_CONFIDENT_COLUMN_NAME]
    results = [
        [
            prediction[SENTENCE_COLUMN_NAME],
            prediction[LANGUAGE_COLUMN_NAME],
            prediction[CONFIDENCE_COLUMN_NAME],
            prediction[IS_CONFIDENT_COLUMN_NAME],
        ]
        for prediction in predictions
    ]
    df = pd.DataFrame(data=results, columns=feature_names)

    return df


def store_data(data: pd.DataFrame, output_file_path: str) -> None:
    full_output_path: str = os.path.join(output_file_path, RESULTS_CSV_FILE)
    data.to_csv(full_output_path, index=False, sep=CSV_COMMA_SEP)
    log.info(f"Data stored into: {full_output_path}")


def run(input_path: str, output_path: str) -> None:
    logger.init_logger()
    full_input_path: str = os.path.normpath(os.path.join(PROJECT_ROOT_PATH, input_path))
    full_output_path: str = os.path.normpath(os.path.join(PROJECT_ROOT_PATH, output_path))

    Path(full_output_path).mkdir(parents=True, exist_ok=True)

    df = load_csv_data(full_input_path)
    texts = preprocess_input_data(df)
    predictions = do_predictions(texts)
    predictions_df = preprocess_response(predictions)
    store_data(predictions_df, full_output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script  calling /predict_languages API for set of given texts stored in file with given path"
    )

    parser.add_argument(
        "-ip",
        "--input_path",
        type=str,
        help=("Input path for csv file. It should be relative with respect to root folder of this repository"),
        required=True,
    )
    parser.add_argument(
        "-op",
        "--output_path",
        type=str,
        help=(
            "Output path for results stored in results.csv file. It should be relative with"
            " respect to root folder of this repository"
        ),
        required=True,
    )
    cl_args = parser.parse_args()  # type: ignore
    input_path: str = cl_args.input_path
    output_path: str = cl_args.output_path

    if not input_path.endswith(CSV_SUFFIX):
        raise Exception("Input file path is not pointing to csv file")

    run(input_path=input_path, output_path=output_path)

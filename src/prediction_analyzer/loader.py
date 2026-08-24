import json
import logging


def load_predictions(file_path: str) -> list[dict] | None:
    """
    Load predictions from a JSON file.
    """
    try:
        with open(file_path, "r") as file:
            predictions = json.load(file)

        logging.info("Predictions loaded successfully.")
        return predictions

    except FileNotFoundError:
        logging.error("Prediction file not found.")
        return None

    except json.JSONDecodeError:
        logging.error("Invalid JSON file.")
        return None
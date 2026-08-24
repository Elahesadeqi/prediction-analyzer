import logging


def validate_prediction(prediction: dict) -> bool:
    """
    Validate a single prediction.
    """

    if "label" not in prediction or "confidence" not in prediction:
        return False

    if prediction["label"].strip() == "":
        return False

    if not 0 <= prediction["confidence"] <= 1:
        return False

    return True


def validate_predictions(predictions: list[dict]) -> list[dict]:
    """
    Return only valid predictions.
    """

    valid_predictions = []

    for prediction in predictions:

        if validate_prediction(prediction):
            valid_predictions.append(prediction)

        else:
            logging.warning(
                f"Invalid prediction removed: {prediction}"
            )

    return valid_predictions
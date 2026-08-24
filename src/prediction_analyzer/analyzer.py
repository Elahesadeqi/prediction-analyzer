def calculate_average_confidence(
    predictions: list[dict]
) -> float:
    """
    Calculate the average confidence score.
    """

    total_confidence = 0

    for prediction in predictions:
        total_confidence += prediction["confidence"]

    average = total_confidence / len(predictions)

    return round(average, 2)



def count_labels(
    predictions: list[dict]
) -> dict[str, int]:
    """
    Count the number of predictions for each label.
    """

    label_counts = {}

    for prediction in predictions:

        label = prediction["label"]

        if label in label_counts:
            label_counts[label] += 1

        else:
            label_counts[label] = 1

    return label_counts



def find_best_prediction(
    predictions: list[dict]
) -> dict:
    """
    Return the prediction with the highest confidence score.
    """

    if len(predictions) == 0:
        raise ValueError(
            "Predictions list cannot be empty."
        )

    best_prediction = predictions[0]

    for prediction in predictions:

        if (
            prediction["confidence"]
            > best_prediction["confidence"]
        ):
            best_prediction = prediction

    return best_prediction



def get_low_confidence_predictions(
    predictions: list[dict]
) -> list[dict]:
    """
    Return predictions with confidence below 0.90.
    """

    low_confidence_predictions = []

    for prediction in predictions:

        if prediction["confidence"] < 0.90:
            low_confidence_predictions.append(prediction)

    return low_confidence_predictions



def analyze_predictions(
    predictions: list[dict]
) -> dict:
    """
    Generate a complete analysis report.
    """

    total_predictions = len(predictions)

    average_confidence = calculate_average_confidence(
        predictions
    )

    label_counts = count_labels(
        predictions
    )

    best_prediction = find_best_prediction(
        predictions
    )

    low_confidence_predictions = (
        get_low_confidence_predictions(
            predictions
        )
    )


    report = {
        "total_predictions": total_predictions,
        "average_confidence": average_confidence,
        "label_counts": label_counts,
        "best_prediction": best_prediction,
        "low_confidence_predictions": low_confidence_predictions
    }

    return report
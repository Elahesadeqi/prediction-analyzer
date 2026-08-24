import json
import logging

from prediction_analyzer.loader import load_predictions
from prediction_analyzer.validator import validate_predictions
from prediction_analyzer.analyzer import analyze_predictions


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


def main():
    """
    Run the prediction analysis pipeline.
    """

    predictions = load_predictions(
        "data/prediction.json"
    )


    if predictions is None:
        return


    valid_predictions = validate_predictions(
        predictions
    )


    if len(valid_predictions) == 0:
        logging.warning(
            "No valid predictions found."
        )
        return


    report = analyze_predictions(
        valid_predictions
    )


    with open(
        "report.json",
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


    logging.info(
        "Report generated successfully."
    )


    print(report)



if __name__ == "__main__":
    main()
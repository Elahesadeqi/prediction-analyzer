from prediction_analyzer.analyzer import (
    calculate_average_confidence,
    count_labels,
    find_best_prediction
)


def test_calculate_average_confidence():
    predictions = [
        {"label": "cat", "confidence": 0.8},
        {"label": "dog", "confidence": 1.0}
    ]

    result = calculate_average_confidence(predictions)

    expected = 0.9

    assert result == expected



def test_count_labels():
    predictions = [
        {"label": "cat", "confidence": 0.9},
        {"label": "dog", "confidence": 0.8},
        {"label": "cat", "confidence": 0.7}
    ]

    result = count_labels(predictions)

    expected = {
        "cat": 2,
        "dog": 1
    }

    assert result == expected



def test_find_best_prediction():
    predictions = [
        {"label": "cat", "confidence": 0.82},
        {"label": "dog", "confidence": 0.96},
        {"label": "bird", "confidence": 0.91}
    ]

    result = find_best_prediction(predictions)

    expected = {
        "label": "dog",
        "confidence": 0.96
    }

    assert result == expected



def test_find_best_prediction_empty_list():

    try:
        find_best_prediction([])

        assert False

    except ValueError:
        assert True
# Prediction Analyzer

## Overview

Prediction Analyzer is a Python-based pipeline for processing and analyzing machine learning model outputs.

The project receives prediction results, validates prediction quality, analyzes confidence scores, identifies the best predictions, and generates structured analysis reports.

This project demonstrates a clean Python project structure with modular design, validation, error handling, and automated testing.

---

## Features

- Load prediction data from JSON files
- Validate prediction format and confidence scores
- Remove invalid predictions with missing keys or incorrect values
- Calculate average confidence score
- Count predictions by label
- Find the prediction with the highest confidence score
- Identify low-confidence predictions
- Handle file and data validation errors
- Generate structured analysis reports
- Include automated tests for core functions

---

## Project Structure

```text
prediction-analyzer/

├── src/
│   └── prediction_analyzer/
│       ├── __init__.py
│       ├── analyzer.py
│       ├── loader.py
│       ├── validator.py
│       └── main.py
│
├── tests/
│   └── test_analyzer.py
│
├── data/
│   └── prediction.json
│
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

## Components

- `loader.py`: Loads prediction data from JSON files.
- `validator.py`: Checks prediction format and removes invalid entries.
- `analyzer.py`: Performs confidence analysis and generates reports.
- `main.py`: Runs the complete prediction analysis pipeline.
- `tests/`: Contains automated tests for core functions.

---

# Installation

## Requirements

- Python 3.10+
- Conda (recommended) or any Python environment manager

## Create Environment

Create a new Conda environment:

```bash
conda create -n prediction-analyzer python=3.10
```

Activate the environment:

```bash
conda activate prediction-analyzer
```

## Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

## Install the Project

Install the package in editable mode:

```bash
pip install -e .
```

---

# Usage

Run the prediction analysis pipeline:

```bash
python src/prediction_analyzer/main.py
```

The pipeline will:

1. Load prediction data from `data/prediction.json`
2. Validate prediction inputs
3. Analyze confidence scores
4. Generate a structured analysis report

---

# Testing

This project uses `pytest` for automated testing.

Run tests with:

```bash
pytest
```

Expected result:

```text
4 passed
```

The tests cover:

- Average confidence calculation
- Label counting
- Finding the best prediction
- Handling empty prediction inputs
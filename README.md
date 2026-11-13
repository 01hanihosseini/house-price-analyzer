# House Price Analyzer

A command-line tool that reads a housing CSV file and reports the mean, min and max of its numeric columns, optionally grouped by a category and exportable to CSV or JSON.

## Features

- Detects numeric columns automatically
- Mean, min and max per column (missing values are ignored)
- --columns to analyze only selected columns
- --group-by to get statistics per category (e.g. per region)
- --output to save the result as .csv or .json
- Clear error messages for missing, empty or invalid files

## Installation

git clone https://github.com/01hanihosseini/house-price-analyzer.git
cd house-price-analyzer
python -m venv .venv
source .venv/bin/activate    # Windows (Git Bash): source .venv/Scripts/activate
pip install -r requirements.txt

## Usage

Download the dataset (see below) and put melb_data.csv in the data/ folder.

# all numeric columns
PYTHONPATH=src python -m analyzer.cli data/melb_data.csv

# selected columns
PYTHONPATH=src python -m analyzer.cli data/melb_data.csv --columns Price Rooms

# grouped by region
PYTHONPATH=src python -m analyzer.cli data/melb_data.csv --columns Price --group-by Regionname

# save the result
PYTHONPATH=src python -m analyzer.cli data/melb_data.csv --output result.json
## Example output

Summary statistics
------------------
              mean       min          max
Price 1,075,684.08 85,000.00 9,000,000.00
Rooms         2.94      1.00        10.

## Observations

- YearBuilt has a minimum of 1196, which is not plausible for this city.
- Landsize reaches 433,014 and pulls the mean up; its minimum is 0.
- Postcode, Lattitude and Longtitude are numeric, but their mean is meaningless. Use --columns to skip them.

## Running tests
pytest

## Project structure

src/analyzer/
    loader.py   # read and validate the CSV
    stats.py    # numeric columns and summary statistics
    report.py   # print and save results
    cli.py      # command-line interface
tests/          # pytest tests

## Dataset

Melbourne Housing Snapshot, derived from Tony Pino's dataset, via Kaggle:
https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot

Data license: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
The dataset file is not included in this repository.
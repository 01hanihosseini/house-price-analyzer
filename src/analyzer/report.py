from pathlib import Path
import pandas as pd


def print_report(summary):
    if isinstance(summary.columns, pd.MultiIndex):
        table = summary
    else:
        table = summary.T
    print("Summary statistics")
    print("-" * 18)
    print(table.to_string(float_format = "{:,.2f}".format))

def save_report(summary, path):
    suffix = Path(path).suffix.lower()
    if suffix not in (".csv", ".json"):
        raise ValueError(f"Unsupported output format '{suffix}' (use.csv or .json)")

    table = summary.copy()
    if isinstance(table.columns, pd.MultiIndex):
        table.columns= [f"{col}_{stat}" for col, stat in summary.columns]

    if suffix == ".csv":
        table.to_csv(path)
    else:
        table.to_json(path, indent=2)
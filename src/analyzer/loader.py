import pandas as pd
from pathlib import Path


def load_data(path):
    if not Path(path).exists():
        raise FileNotFoundError(f"File not found:{path}")

    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        raise ValueError(f"File is empty: {path}")

    if df.empty:
        raise ValueError(f"File has no data rows: {path}")

    return df
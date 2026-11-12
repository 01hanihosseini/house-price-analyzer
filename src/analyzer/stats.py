import pandas as pd

def get_numeric_columns(df):
    return list(df.select_dtypes(include="number").columns)

def summarize(df, column=None):
    if column is None:
        columns = get_numeric_columns(df)
    return df[columns].agg(["mean", "min", "max"])
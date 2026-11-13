import pandas as pd

def get_numeric_columns(df):
    return list(df.select_dtypes(include="number").columns)

def summarize(df, columns=None, group_by=None):
    if columns is None:
        columns = [c for c in get_numeric_columns(df) if c != group_by]
    if group_by is None:
            return df[columns].agg(["mean", "min", "max"])
    return df.groupby(group_by)[columns].agg(["mean", "min", "max"])


import pandas as pd


def print_report(summary):
    if isinstance(summary.columns, pd.MultiIndex):
        table = summary
    else:
        table = summary.T
    print("Summary statistics")
    print("-" * 18)
    print(table.to_string(float_format = "{:,.2f}".format))
    
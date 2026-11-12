import pandas as pd
from analyzer.stats import get_numeric_columns, summarize


def make_df():
    return pd.DataFrame(
        {
            "a":[1, 2, 3],
            "b":["x", "y", "z"],
            "c":[10.0, None, 30.0],
        }
    )

def test_get_numeric_columns_skips_text():
    assert get_numeric_columns(make_df()) == ["a", "c"]

def test_summarize_basic_value():
    result = summarize(make_df())
    assert result.loc["mean", "a"] == 2
    assert result.loc["min", "a"] == 1
    assert result.loc["max", "a"] == 3

def test_summarize_ignores_missing_values():
    result = summarize(make_df())
    assert result.loc["mean", "c"] == 20

def test_summarize_with_selected_columns():
    result = summarize(make_df(), columns=["a"])
    list(result.columns) == ["a"]
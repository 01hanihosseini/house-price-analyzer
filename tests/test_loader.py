import pytest 
from analyzer.loader import load_data



def test_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_data(tmp_path / "nothing.csv")

def test_header_only_file_raises(tmp_path):
    file = tmp_path / "header_only.csv"
    file.write_text("")
    with pytest.raises(ValueError):
        load_data(file)

def test_blank_file_raises(tmp_path):
    file = tmp_path / "blank.csv"
    file.write_text("")
    with pytest.raises(ValueError):
        load_data(file)

def test_valid_file_returns_dataframe(tmp_path):
    file = tmp_path / "valid.csv"
    file.write_text("a,b\n1,2\n3,4\n")
    df = load_data(file)
    assert df.shape == (2, 2)
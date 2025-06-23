import os
import pandas as pd
import pytest
from app.calculation import Calculator
from app.exceptions import DivideByZeroError

@pytest.fixture(autouse=True)
def cleanup(tmp_path, monkeypatch):
    # override history path
    monkeypatch.setenv("HISTORY_PATH", str(tmp_path/"hist.csv"))
    yield
    # tmpdir auto removed

def test_calculate_and_history(tmp_path):
    calc = Calculator()
    res = calc.calculate("+", 2, 3)
    assert res == 5
    df = calc.history.df
    assert df.iloc[-1]["expr"] == "2.0 + 3.0"
    assert df.iloc[-1]["result"] == 5

def test_undo_redo():
    calc = Calculator()
    calc.calculate("+", 1, 1)
    assert calc.undo() == None  # initial state has no last_result
    r = calc.calculate("*", 2, 3)
    assert r == 6
    prev = calc.undo()
    assert prev is None or isinstance(prev, float)
    redo = calc.redo()
    assert redo == 6

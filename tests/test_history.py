import pandas as pd
import os
import pytest
from app.history import HistoryManager

def test_history_add_and_save(tmp_path):
    p = tmp_path/"h.csv"
    h = HistoryManager(str(p))
    h.add("1 + 1", 2)
    h.save()
    df = pd.read_csv(str(p))
    assert df.iloc[0]["expr"] == "1 + 1"

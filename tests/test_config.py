import os
import pytest
from app.calculator_config import Config
from app.exceptions import ConfigError

def test_missing_history_path(monkeypatch):
    monkeypatch.delenv("HISTORY_PATH", raising=False)
    with pytest.raises(ConfigError):
        Config.validate()

def test_auto_save_default(monkeypatch):
    monkeypatch.setenv("HISTORY_PATH", "h.csv")
    # AUTO_SAVE defaults to true
    assert Config.AUTO_SAVE

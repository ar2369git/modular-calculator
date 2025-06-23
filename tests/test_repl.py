import subprocess
import sys
import os
import pytest

def test_repl_help(monkeypatch, capsys):
    import threading
    from app.calculator_repl import main
    # simulate user typing 'help' then 'exit'
    inputs = iter(["help\n", "exit\n"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Commands:" in captured.out

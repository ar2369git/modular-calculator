# tests/test_repl_commands.py

import pytest
from app.calculator_repl import main

def run_repl_sequence(inputs):
    """Helper: feed lines to the REPL and capture output."""
    from io import StringIO
    import sys

    it = iter(inputs)
    orig_in, orig_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("".join(inputs)), StringIO()
    try:
        main()
        return sys.stdout.getvalue()
    finally:
        sys.stdin, sys.stdout = orig_in, orig_out

def test_invalid_command_then_exit():
    out = run_repl_sequence(["foobar\n", "exit\n"])
    assert "Error:" in out

def test_calc_and_history_and_undo_redo_and_clear(tmp_path, monkeypatch):
    # ensure HISTORY_PATH is valid
    monkeypatch.setenv("HISTORY_PATH", str(tmp_path/"h.csv"))
    seq = [
        "1 + 2\n",
        "history\n",
        "undo\n",
        "redo\n",
        "save\n",
        "load\n",
        "clear\n",
        "exit\n",
    ]
    out = run_repl_sequence(seq)
    assert "3.0" in out
    assert "timestamp" in out  # printed by history
    assert "Reverted to:" in out
    assert "Redo result:" in out
    assert "History saved." in out
    assert "History reloaded." in out

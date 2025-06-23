import pytest
from app.calculator_repl import main
from io import StringIO
import sys

def run_sequence(inputs):
    orig_in, orig_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("".join(inputs)), StringIO()
    try:
        main()
        return sys.stdout.getvalue()
    finally:
        sys.stdin, sys.stdout = orig_in, orig_out

def test_history_not_configured_branch(monkeypatch):
    # unset HISTORY_PATH so calc=None
    monkeypatch.delenv("HISTORY_PATH", raising=False)
    out = run_sequence(["history\n", "exit\n"])
    assert "(no history available)" in out

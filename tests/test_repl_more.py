import pytest
from app.calculator_repl import main
from io import StringIO
import sys

def run_sequence(inputs):
    orig_stdin, orig_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("".join(inputs)), StringIO()
    try:
        main()
        return sys.stdout.getvalue()
    finally:
        sys.stdin, sys.stdout = orig_stdin, orig_stdout

@pytest.fixture(autouse=True)
def set_history_path(monkeypatch, tmp_path):
    # ensure a valid HISTORY_PATH for tests that need a Calculator
    monkeypatch.setenv("HISTORY_PATH", str(tmp_path / "hist.csv"))

def test_clear_escape_sequence():
    out = run_sequence(["clear\n", "exit\n"])
    assert "\x1b[2J\x1b[H" in out

def test_invalid_number_error_message():
    out = run_sequence(["abc + 1\n", "exit\n"])
    # parse_number should raise InvalidOperationError, caught and printed here
    assert "Error: Invalid number 'abc'" in out

def test_too_many_tokens_usage_error():
    out = run_sequence(["1 + 2 3\n", "exit\n"])
    assert "Error: Usage: <num> <op> <num>" in out

def test_quit_keyword_alias():
    # 'quit' should behave just like 'exit'
    out = run_sequence(["quit\n"])
    assert "Modular Calculator" in out

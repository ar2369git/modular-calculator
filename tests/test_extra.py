import pytest
from app.operations import Root, OperationFactory
from app.exceptions import DivideByZeroError, InvalidOperationError
from app.calculator_memento import Caretaker
from io import StringIO
import sys
from app.calculator_repl import main

def test_root_zero_raises():
    with pytest.raises(DivideByZeroError):
        Root().execute(4, 0)

def test_invalid_operation_raises():
    with pytest.raises(InvalidOperationError):
        OperationFactory.get("foobar")

def test_memento_legacy_undo_redo():
    ct = Caretaker()
    initial = {"a": 1}
    ct.save(initial)
    new_state = {"a": 2}
    # legacy undo
    assert ct.undo(new_state) == initial
    # legacy redo
    assert ct.redo(initial) == new_state

def test_calculation_invalid_operation(monkeypatch):
    from app.calculation import Calculator
    monkeypatch.setenv("HISTORY_PATH", "/tmp/hist.csv")
    calc = Calculator()
    with pytest.raises(InvalidOperationError):
        calc.calculate("nop", 1, 1)

def test_repl_calc_not_configured(monkeypatch):
    # ensure HISTORY_PATH is unset so calc=None
    monkeypatch.delenv("HISTORY_PATH", raising=False)
    inputs = ["1 + 1\n", "exit\n"]
    orig_in, orig_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("".join(inputs)), StringIO()
    try:
        main()
        output = sys.stdout.getvalue()
    finally:
        sys.stdin, sys.stdout = orig_in, orig_out
    assert "Error: Calculator not configured" in output

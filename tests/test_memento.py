import pytest
from app.calculator_memento import Caretaker

def test_undo_redo_empty():
    ct = Caretaker()
    state = {"x": 1}
    ct.save(state)
    assert ct.undo(state) == state
    assert ct.redo(state) == state

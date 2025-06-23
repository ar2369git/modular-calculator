import pytest
from app.operations import (
    OperationFactory,
    Add, Subtract, Multiply, Divide, Power, Root
)
from app.exceptions import DivideByZeroError

@pytest.mark.parametrize("symbol, cls", [
    ("+", Add),
    ("-", Subtract),
    ("*", Multiply),
    ("/", Divide),
    ("^", Power),
    ("root", Root),
])
def test_operation_factory_valid(symbol, cls):
    op = OperationFactory.get(symbol)
    assert isinstance(op, cls)

def test_divide_zero_through_factory():
    op = OperationFactory.get("/")
    with pytest.raises(DivideByZeroError):
        op.execute(5, 0)

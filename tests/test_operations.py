import pytest
from app.operations import Add, Subtract, Multiply, Divide, Power, Root
from app.exceptions import DivideByZeroError

@pytest.mark.parametrize("cls,a,b,expected", [
    (Add, 1, 2, 3),
    (Subtract, 5, 3, 2),
    (Multiply, 3, 4, 12),
    (Power, 2, 3, 8),
    (Root, 8, 3, 2),
])
def test_basic_ops(cls, a, b, expected):
    assert cls().execute(a, b) == pytest.approx(expected)

def test_divide_zero():
    with pytest.raises(DivideByZeroError):
        Divide().execute(5, 0)

import pytest
from app.exceptions import DivideByZeroError, InvalidOperationError

def test_exceptions_hierarchy():
    with pytest.raises(DivideByZeroError):
        raise DivideByZeroError()
    with pytest.raises(InvalidOperationError):
        raise InvalidOperationError()

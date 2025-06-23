import pytest
from app.operations import Operation

def test_base_operation_execute_raises():
    op = Operation()
    with pytest.raises(NotImplementedError):
        op.execute(1, 2)

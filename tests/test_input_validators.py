import pytest
from app.input_validators import parse_number
from app.exceptions import CalculatorError

def test_parse_number_valid():
    assert parse_number("3.5") == 3.5

def test_parse_number_invalid():
    with pytest.raises(CalculatorError):
        parse_number("abc")

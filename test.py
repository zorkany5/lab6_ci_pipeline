import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(3, 5) == 8
    assert calc.add(-1, 1) == 0

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(2, 5) == -3

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 3) == -6

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    with pytest.raises(ValueError):
        calc.divide(5, 0)

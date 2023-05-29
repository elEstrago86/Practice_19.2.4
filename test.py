import pytest

from calc.calculator import Calculator

# Позитивный тест для метода multiply()
def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(5, 10)
    assert result == 50

# Позитивный тест для метода division()
def test_division():
    calculator = Calculator()
    result = calculator.division(20, 5)
    assert result == 4.0

# Позитивный тест для метода subtraction()
def test_subtraction():
    calculator = Calculator()
    result = calculator.subtraction(15, 7)
    assert result == 8

# Позитивный тест для метода adding()
def test_adding():
    calculator = Calculator()
    result = calculator.adding(3, 9)
    assert result == 12
# tests/test_calculator.py

"""
This module contains unit tests for the calculator functions in the app.calculator module.
It tests the basic arithmetic operations: addition, subtraction, multiplication, and division.
"""

import pytest  # Required for testing exceptions
from app.calculator import add, subtract, multiply, divide  # Ensure 'app.calculator' exists and contains these functions

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3
    assert subtract(3, 3) == 0

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 3) == -3
    assert multiply(0, 5) == 0

def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(5, 0)

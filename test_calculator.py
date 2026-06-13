import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-4, -6) == -10


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_subtract_resulting_in_negative(self):
        assert subtract(3, 8) == -5


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 7) == 21

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_divide_resulting_in_float(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            divide(5, 0)

import pytest
from calculator import Calculator


def test_factorial_zero_and_edge_cases():
    calc = Calculator()
    assert calc.factorial(0) == 1
    assert calc.factorial(1) == 1


def test_power_negative_and_zero_exponent():
    calc = Calculator()
    assert calc.power(2, -1) == 0.5
    assert calc.power(5, 0) == 1


def test_square_root_zero():
    calc = Calculator()
    assert calc.square_root(0) == 0


def test_gcd_with_zero_values():
    calc = Calculator()
    assert calc.gcd(0, 5) == 5
    assert calc.gcd(0, 0) == 0


def test_modulo_with_negative_and_positive():
    calc = Calculator()
    assert calc.modulo(-10, 3) == (-10) % 3
    assert calc.modulo(10, -3) == 10 % -3


def test_is_even_negative_numbers():
    calc = Calculator()
    assert calc.is_even(-4) is True
    assert calc.is_even(-3) is False


def test_memory_store_overwrite_and_types():
    calc = Calculator()
    calc.memory_store(-3.5)
    assert calc.memory_recall() == -3.5
    calc.memory_store(42)
    assert calc.memory_recall() == 42


def test_divide_and_float_behaviour():
    calc = Calculator()
    assert calc.divide(3, 2) == 1.5
    assert calc.divide(9, 3) == 3.0


def test_add_and_subtract_with_floats():
    calc = Calculator()
    assert pytest.approx(calc.add(1.2, 2.3), rel=1e-9) == 3.5
    assert pytest.approx(calc.subtract(5.5, 2.0), rel=1e-9) == 3.5


def test_stack_contents_after_multiple_ops():
    calc = Calculator()
    calc.clear_stack()
    calc.add(1, 1)        # 2
    calc.multiply(2, 3)   # 6
    calc.power(2, 3)      # 8
    assert calc.get_stack()[-3:] == [2, 6, 8]

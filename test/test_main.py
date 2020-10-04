from currency_converter_cli.__main__ import *
import pytest


def test_calculate_rate():
    assert calculate_rate(1, 1, 1) == 1
    assert calculate_rate(1, 1, 10) == 10, 'Amount'
    assert calculate_rate(-1, -1, 10) == 10, 'Negative X and Y'
    assert calculate_rate(-1, 1, 10) == -10, 'Negative X'
    assert calculate_rate(1, -1, 10) == -10, 'Negative Y'
    assert pytest.approx(calculate_rate(1.5, 1, 10), 6.666), 'Fraction X'
    assert pytest.approx(calculate_rate(1, 1.5, 10), 15), 'Fraction Y'
    assert calculate_rate(0, 1, 1) == 0, 'Zero X'
    assert calculate_rate(1, 0, 1) == 0, 'Zero Y'

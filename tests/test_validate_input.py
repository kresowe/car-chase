import pytest
from validate_input import valid_input


def test_valid_input_is_valid():
    assert valid_input("1.0", 0.0, 2.0)


def test_invalid_input_is_invalid():
    assert not valid_input("aaa", 0.0, 2.0)


def test_input_out_of_range_is_invalid():
    assert not valid_input("3.0", 0.0, 2.0)
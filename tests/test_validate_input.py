import pytest
from validate_input import InputValidator


@pytest.fixture
def validator():
    return InputValidator()


def test_float_is_float(validator):
    assert validator.is_float("1.0")


def test_not_float_is_not_float(validator):
    assert not validator.is_float("aaa")


def test_in_range_is_in_range(validator):
    assert validator.is_in_range("1.0", 0.0, 2.0)


def test_out_of_range_is_not_in_range(validator):
    assert not validator.is_in_range("3.0", 0.0, 2.0)


def test_valid_input_is_valid(validator):
    assert validator.is_valid("1.0", 0.0, 2.0)


def test_invalid_input_is_invalid(validator):
    assert not validator.is_valid("aaa", 0.0, 2.0)


def test_input_out_of_range_is_invalid(validator):
    assert not validator.is_valid("3.0", 0.0, 2.0)


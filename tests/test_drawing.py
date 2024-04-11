import numpy as np
import pytest
from drawing import find_x_range


def test_find_x_range():
    car1_positions = np.concatenate((np.arange(1, 200, 0.5), np.arange(200, 180, -0.5)))
    car2_positions = np.arange(-5, 20, 0.3)
    x_min, x_max = find_x_range(car1_positions, car2_positions)
    diff = 200 + 5
    assert x_min == pytest.approx(-5 - 0.1 * diff)
    assert x_max == pytest.approx(200 + 0.1 * diff)
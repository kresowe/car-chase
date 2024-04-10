import pytest
from car import Car


def test_car_position():
    x0, v0, a = 0.0, 3.0, 0.0
    car = Car(x0, v0, a, 'red')
    t = 2.0
    assert car.position(t) == pytest.approx(v0 * t)
    assert car.position(t) == pytest.approx(6.0)

    x0, v0, a = 2.0, 3.0, 0.0
    car = Car(x0, v0, a, 'red')
    t = 2.0
    assert car.position(t) == pytest.approx(x0 + v0 * t)
    assert car.position(t) == pytest.approx(2 + 3 * 2)

    x0, v0, a = 10.0, -3.0, 0.0
    car = Car(x0, v0, a, 'red')
    t = 2.0
    assert car.position(t) == pytest.approx(x0 + v0 * t)
    assert car.position(t) == pytest.approx(10 - 3 * 2)

    x0, v0, a = 0.0, 3.0, 2.0
    car = Car(x0, v0, a, 'red')
    t = 2.0
    assert car.position(t) == pytest.approx(v0 * t + 0.5 * a * t**2)
    assert car.position(t) == pytest.approx(3.0 * 2.0 + 0.5 * 2.0 * 2**2)

    x0, v0, a = 4.0, 3.0, 2.0
    car = Car(x0, v0, a, 'red')
    t = 2.0
    assert car.position(t) == pytest.approx(x0 + v0 * t + 0.5 * a * t ** 2)
    assert car.position(t) == pytest.approx(4.0 + 3.0 * 2.0 + 0.5 * 2.0 * 2 ** 2)

    x0, v0, a = 10.0, -3.0, -2.0
    car = Car(x0, v0, a, 'red')
    t = 2.0
    assert car.position(t) == pytest.approx(x0 + v0 * t + 0.5 * a * t ** 2)
    assert car.position(t) == pytest.approx(10.0 - 3.0 * 2.0 - 0.5 * 2.0 * 2 ** 2)




from matplotlib import axes, lines
from numpy.typing import ArrayLike, NDArray


class Car:
    def __init__(self, x0: float, v0: float, a: float, marker_color: str, marker: str = 's') -> None:
        """
        :param x0: initial position [m]
        :param v0: initial speed [m/s]
        :param a: acceleration assumed to be constant [m/s**2]
        :param marker_color: color of a marker (color in plt.plot())
        :param marker: marker that shows a car's position (marker in plt.plot())
        """
        self._x0 = x0
        self._v0 = v0
        self._a = a
        self._marker_color = marker_color
        self._marker = marker

    @property
    def marker(self) -> str:
        return self._marker

    @property
    def marker_color(self) -> str:
        return self._marker_color

    def position(self, t: ArrayLike) -> NDArray:
        """If t is a single number, the function returns car's position at time t [s].
        If t is a list or numpy array, the function returns car's position at each time in t [s].
        It is assumed that a car is moving with uniformly accelerated motion (or constant speed)."""
        return self._x0 + self._v0 * t + 0.5 * self._a * t**2

    def plot_dummy(self, ax: axes.Axes) -> list[lines.Line2D]:
        """Makes a dummy plot of no points that will be updated by the cars markers during the animation."""
        return ax.plot([], [], color=self._marker_color, marker=self._marker, markersize=12)

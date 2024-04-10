class Car(object):
    def __init__(self, x0, v0, a, marker_color, marker='s'):
        self._x0 = x0  # initial position
        self._v0 = v0  # initial speed
        self._a = a  # constant acceleration
        self._marker = marker
        self._marker_color = marker_color

    def get_marker(self):
        return self._marker

    def get_marker_color(self):
        return self._marker_color

    def position(self, t):
        """Position at time t.
        Assume car is moving with uniformly accelerated motion (or constant speed)."""
        return self._x0 + self._v0 * t + 0.5 * self._a * t**2

    def plot_dummy(self, ax):
        return ax.plot([], [], color=self.get_marker_color(), marker=self.get_marker(), markersize=12)

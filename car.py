class Car(object):
    def __init__(self, x0, v0, a, marker_color, marker='s'):
        self.x0 = x0
        self.v0 = v0
        self.a = a
        self.marker = marker
        self.marker_color = marker_color

    def get_marker(self):
        return self.marker

    def get_marker_color(self):
        return self.marker_color

    def position(self, t):
        return self.x0 + self.v0 * t + 0.5 * self.a * t**2

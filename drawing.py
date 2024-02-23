import matplotlib.pyplot as plt
from car import Car


def drawing_settings(x_min, x_max):
    plt.rcParams['figure.figsize'] = [10, 3]
    plt.yticks([])
    plt.xlim(x_min, x_max)
    plt.ylim(0.3, 0.7)


def draw_road(low_y=0.4, high_y=0.6):
    plt.axhline(low_y, linewidth=2, color='black')
    plt.axhline(high_y, linewidth=2, color='black')


def draw_car(car: Car, t: float, y: float = 0.5):
    plt.plot(car.position(t), y, color=car.get_marker_color(), marker=car.get_marker(), markersize=12)
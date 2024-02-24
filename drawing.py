import matplotlib as mpl
import matplotlib.pyplot as plt
from car import Car


def drawing_settings(x_min, x_max, ax=None):
    plt.rcParams.update({'font.size': 20})
    if ax is None:
        plt.rcParams['figure.figsize'] = [10, 3]
        plt.yticks([])
        plt.xlim(x_min, x_max)
        plt.ylim(0.3, 0.7)
    else:
        ax.yaxis.set_ticks([])
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(0.3, 0.7)
        ax.tick_params(axis='x', which='major', labelsize=16)
        ax.set_xlabel('position', fontsize=16)


def draw_road(low_y=0.4, high_y=0.6, ax=None):
    if ax is None:
        plt.axhline(low_y, linewidth=2, color='black')
        plt.axhline(high_y, linewidth=2, color='black')
    else:
        ax.axhline(low_y, linewidth=2, color='black')
        ax.axhline(high_y, linewidth=2, color='black')


def draw_car(car: Car, t: float, y: float = 0.5):
    plt.plot(car.position(t), y, color=car.get_marker_color(), marker=car.get_marker(), markersize=12)
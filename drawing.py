import numpy as np
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

def find_x_range(car1_positions, car2_positions):
    car1_min_position, car2_min_position = np.min(car1_positions), np.min(car2_positions)
    car1_max_position, car2_max_position = np.max(car1_positions), np.max(car2_positions)
    pos_min = min(car1_min_position, car2_min_position)
    pos_max = max(car1_max_position, car2_max_position)
    pos_diff = pos_max - pos_min
    x_min = pos_min - 0.1 * pos_diff
    x_max = pos_max + 0.1 * pos_diff
    return x_min, x_max

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import axes, figure, text
from car import Car
from typing import Optional
from numpy.typing import ArrayLike


def drawing_settings(x_min: float, x_max: float,
                     ax: Optional[axes.Axes] = None,
                     fig: Optional[figure.Figure] = None) -> None:
    """Make settings for drawing, including font size, x-axis limits, axis labels."""
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
        ax.set_xlabel('position [m]', fontsize=16)
        fig.tight_layout()


def draw_road(low_y: float = 0.4, high_y: float = 0.6, ax: Optional[axes.Axes] = None) -> None:
    """Draws road, i.e., borders of road at y = low_y and at y = high_y."""
    if ax is None:
        plt.axhline(low_y, linewidth=2, color='black')
        plt.axhline(high_y, linewidth=2, color='black')
    else:
        ax.axhline(low_y, linewidth=2, color='black')
        ax.axhline(high_y, linewidth=2, color='black')


def draw_car(car: Car, t: float, y: float = 0.5) -> None:
    """Draws a car at its position at time t [s]."""
    plt.plot(car.position(t), y, color=car.marker_color, marker=car.marker, markersize=12)


def find_x_range(car1_positions: ArrayLike, car2_positions: ArrayLike) -> tuple[float, float]:
    """Finds range (x_min, x_max) for x-axis based on the min and max positions of two cars.
    There are some margins scaled by the range.

    Specifically,
    Let pos_diff be a difference between min and max from all car1_positions and car2_positions.
    Then:
    x_min = min from all car1_positions and car2_positions - 10% * pos_diff
    x_max = max from all car1_positions and car2_positions + 10% * pos_diff
    """
    car1_min_position, car2_min_position = np.min(car1_positions), np.min(car2_positions)
    car1_max_position, car2_max_position = np.max(car1_positions), np.max(car2_positions)
    pos_min = min(car1_min_position, car2_min_position)
    pos_max = max(car1_max_position, car2_max_position)
    pos_diff = pos_max - pos_min
    x_min = pos_min - 0.1 * pos_diff
    x_max = pos_max + 0.1 * pos_diff
    return x_min, x_max


def get_time_text(ax: axes.Axes) -> tuple[str, text.Text]:
    """Returns text to show current time in simulation and display to write it on a figure.
    Time and its display are then updated in animation.
    """
    return 'time = {:.1f} s', ax.text(0.05, 0.85, '', transform=ax.transAxes)

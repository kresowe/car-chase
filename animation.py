import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from drawing import drawing_settings, draw_road, find_x_range, get_time_text
from car import Car
from typing import Iterable
from matplotlib import artist


if __name__ == '__main__':
    car1 = Car(x0=0, v0=0, a=1.5, marker_color='red')
    car2 = Car(x0=0, v0=11.11, a=0.8, marker_color='green')
    T_START = 0.0
    T_END = 33.0
    DT = 0.04

    t_s = np.arange(T_START, T_END, DT)
    car1_positions = car1.position(t_s)
    car2_positions = car2.position(t_s)
    x_min, x_max = find_x_range(car1_positions, car2_positions)

    fig, ax = plt.subplots(figsize=(10, 3))
    drawing_settings(x_min, x_max, ax, fig)
    draw_road(ax=ax)
    car1_y, car2_y = 0.45, 0.55

    car1_pt, = car1.plot_dummy(ax)
    car2_pt, = car2.plot_dummy(ax)
    time_template, time_text = get_time_text(ax)

    def animate(i: int) -> Iterable[artist.Artist]:
        """Runs animation by updating positions of cars and displayed time"""
        car1_pt.set_data([car1_positions[i]], [car1_y])
        car2_pt.set_data([car2_positions[i]], [car2_y])
        time_text.set_text(time_template.format(i * DT))
        return car1_pt, car2_pt

    ani = FuncAnimation(fig, animate, frames=len(t_s), interval=DT)

    plt.show()

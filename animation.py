import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from drawing import drawing_settings, draw_road
from car import Car


# def find_x_range(car1_positions, car2_positions):
def find_x_range(car1_positions, car2_positions):
    car1_min_position, car2_min_position = np.min(car1_positions), np.min(car2_positions)
    car1_max_position, car2_max_position = np.max(car1_positions), np.max(car2_positions)
    pos_min = min(car1_min_position, car2_min_position)
    pos_max = max(car1_max_position, car2_max_position)
    pos_diff = pos_max - pos_min
    x_min = pos_min - 0.1 * pos_diff
    x_max = pos_max + 0.1 * pos_diff
    return x_min, x_max


if __name__ == '__main__':
    car1 = Car(x0=0, v0=0, a=1.5, marker_color='red')
    car2 = Car(x0=0, v0=11.11, a=0.8, marker_color='green')
    t_start = 0.0
    t_end = 33.0

    dt = 0.01
    t_s = np.arange(t_start, t_end, dt)
    car1_positions = car1.position(t_s)
    car2_positions = car2.position(t_s)
    x_min, x_max = find_x_range(car1_positions, car2_positions)

    fig, ax = plt.subplots(figsize=(10, 3))
    drawing_settings(x_min, x_max, ax)
    draw_road(ax=ax)
    car1_y, car2_y = 0.45, 0.55

    car1_pt, = ax.plot([], [], color=car1.get_marker_color(), marker=car1.get_marker(), markersize=12)
    car2_pt, = ax.plot([], [], color=car2.get_marker_color(), marker=car2.get_marker(), markersize=12)
    time_template = 'time = {:.1f}'
    time_text = ax.text(0.05, 0.88, '', transform=ax.transAxes)

    def animate(i):
        car1_pt.set_data([car1_positions[i]], [car1_y])
        car2_pt.set_data([car2_positions[i]], [car2_y])
        time_text.set_text(time_template.format(i * dt))
        return car1_pt, car2_pt,

    ani = FuncAnimation(fig, animate, frames=len(t_s), interval=dt*1000)

    plt.show()

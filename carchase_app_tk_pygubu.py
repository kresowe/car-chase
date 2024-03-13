import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import pathlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from car import Car
from drawing import find_x_range, drawing_settings, draw_road, get_time_text
from validate_input import validate_input

proj_path = pathlib.Path(__file__).parent
proj_ui = proj_path / "carchase.ui"


class CarChaseAppTkPyGubu:
    def __init__(self, master=None):
        self.builder = pygubu.Builder()
        self.builder.add_resource_path(proj_path)
        self.builder.add_from_file(proj_ui)
        self.mainwindow = self.builder.get_object('main_window', master)

        self.fig = Figure(figsize=(10, 3))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.builder.get_object('frameplot'))
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.c1_x0 = 0.0
        self.c1_v0 = 0.0
        self.c1_a = 0.0
        self.c2_x0 = 0.0
        self.c2_v0 = 0.0
        self.c2_a = 0.0
        self.t_start = 0.0
        self.t_end = 0.0

        self.dt = 0.04

        self.mini_dist = -1000
        self.maxi_dist = 1000
        self.mini_speed = -70  # [m/s] ~= -250 km/h
        self.maxi_speed = 70
        self.mini_acceleration = -10  # [m/s^2] ~= g
        self.maxi_acceleration = 10
        self.mini_time_start = -100  # [s]
        self.maxi_time_start = 0  # [s]
        self.mini_time_end = self.dt
        self.maxi_time_end = 1800

        self.car1, self.car2 = None, None
        self.x_min, self.x_max = 0., 0.
        self.car1_y, self.car2_y = 0.45, 0.55

        self.ani = None

        self.builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def on_start_clicked(self):
        self.ax.clear()
        self._read_values()
        self.builder.get_variable('err_msg').set(self.err_message)
        if not self.is_valid_all:
            return

        self.car1 = Car(self.c1_x0, self.c1_v0, self.c1_a, marker_color='red')
        self.car2 = Car(self.c2_x0, self.c2_v0, self.c2_a, marker_color='green')

        t_s = np.arange(self.t_start, self.t_end, self.dt)
        car1_positions = self.car1.position(t_s)
        car2_positions = self.car2.position(t_s)
        self.x_min, self.x_max = find_x_range(car1_positions, car2_positions)

        drawing_settings(self.x_min, self.x_max, self.ax, self.fig)
        draw_road(ax=self.ax)
        car1_pt, = self.car1.plot_dummy(self.ax)
        car2_pt, = self.car2.plot_dummy(self.ax)
        time_template, time_text = get_time_text(self.ax)
        self.canvas.draw()

        def animate(i):
            car1_pt.set_data([car1_positions[i]], [self.car1_y])
            car2_pt.set_data([car2_positions[i]], [self.car2_y])
            time_text.set_text(time_template.format(i * self.dt))
            return car1_pt, car2_pt,

        self.ani = FuncAnimation(self.fig, animate, frames=len(t_s), interval=self.dt * 1000, repeat=False)
        self.canvas.draw()

    def _read_values(self):
        self.err_message = ''
        self.is_valid_all = True

        self.c1_x0 = self._read_value('car1 x0', 'c1_x0', self.mini_dist, self.maxi_dist)
        self.c2_x0 = self._read_value('car2 x0', 'c2_x0', self.mini_dist, self.maxi_dist)
        self.c1_v0 = self._read_value('car1 v0', 'c1_v0', self.mini_speed, self.maxi_speed)
        self.c2_v0 = self._read_value('car2 v0', 'c2_v0', self.mini_speed, self.maxi_speed)
        self.c1_a = self._read_value('car1 a', 'c1_a', self.mini_acceleration, self.maxi_acceleration)
        self.c2_a = self._read_value('car2 a', 'c2_a', self.mini_acceleration, self.maxi_acceleration)
        self.t_start = self._read_value('time start', 't_start', self.mini_time_start, self.maxi_time_start)
        self.t_end = self._read_value('time end', 't_end', self.mini_time_end, self.maxi_time_end)

    def _read_value(self, field_name, input_name, mini, maxi):
        is_valid, text, res = validate_input(field_name,
                                                    self.builder.get_variable(input_name).get(),
                                                    mini, maxi)
        if not is_valid:
            self.is_valid_all = False
            self.err_message += text

        return res


if __name__ == '__main__':
    app = CarChaseAppTkPyGubu()
    app.run()
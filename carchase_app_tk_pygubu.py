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
from validate_input import valid_input

proj_path = pathlib.Path(__file__).parent
proj_ui = proj_path / "carchase.ui"


class CarChaseAppTkPyGubu:
    def __init__(self, master=None):
        self._builder = pygubu.Builder()
        self._builder.add_resource_path(proj_path)
        self._builder.add_from_file(proj_ui)
        self._mainwindow = self._builder.get_object('main_window', master)

        self._fig = Figure(figsize=(10, 3))
        self._ax = self._fig.add_subplot(111)
        self._canvas = FigureCanvasTkAgg(self._fig, master=self._builder.get_object('frameplot'))
        self._canvas.draw()
        self._canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self._c1_x0 = 0.0
        self._c1_v0 = 0.0
        self._c1_a = 0.0
        self._c2_x0 = 0.0
        self._c2_v0 = 0.0
        self._c2_a = 0.0
        self._t_start = 0.0
        self._t_end = 0.0

        self._dt = 0.04

        self._mini_dist = -1000
        self._maxi_dist = 1000
        self._mini_speed = -70  # [m/s] ~= -250 km/h
        self._maxi_speed = 70
        self._mini_acceleration = -10  # [m/s^2] ~= g
        self._maxi_acceleration = 10
        self._mini_time_start = -100  # [s]
        self._maxi_time_start = 0  # [s]
        self._mini_time_end = self._dt
        self._maxi_time_end = 1800

        self._car1, self._car2 = None, None
        self._x_min, self._x_max = 0., 0.
        self._car1_y, self._car2_y = 0.45, 0.55

        self._ani = None

        self._builder.connect_callbacks(self)

    def run(self):
        self._mainwindow.mainloop()

    def on_start_clicked(self):
        self._ax.clear()
        self._read_values()
        self._builder.get_variable('err_msg').set(self._err_message)
        if not self._is_valid_all:
            return

        self._car1 = Car(self._c1_x0, self._c1_v0, self._c1_a, marker_color='red')
        self._car2 = Car(self._c2_x0, self._c2_v0, self._c2_a, marker_color='green')

        t_s = np.arange(self._t_start, self._t_end, self._dt)
        car1_positions = self._car1.position(t_s)
        car2_positions = self._car2.position(t_s)
        self._x_min, self._x_max = find_x_range(car1_positions, car2_positions)

        drawing_settings(self._x_min, self._x_max, self._ax, self._fig)
        draw_road(ax=self._ax)
        car1_pt, = self._car1.plot_dummy(self._ax)
        car2_pt, = self._car2.plot_dummy(self._ax)
        time_template, time_text = get_time_text(self._ax)
        self._canvas.draw()

        def animate(i):
            car1_pt.set_data([car1_positions[i]], [self._car1_y])
            car2_pt.set_data([car2_positions[i]], [self._car2_y])
            time_text.set_text(time_template.format(i * self._dt))
            return car1_pt, car2_pt,

        self._ani = FuncAnimation(self._fig, animate, frames=len(t_s), interval=self._dt, repeat=False)
        self._canvas.draw()

    def _read_values(self):
        self._err_message = ''
        self._is_valid_all = True

        self._c1_x0 = self._read_value('car1 x0', 'c1_x0', self._mini_dist, self._maxi_dist)
        self._c2_x0 = self._read_value('car2 x0', 'c2_x0', self._mini_dist, self._maxi_dist)
        self._c1_v0 = self._read_value('car1 v0', 'c1_v0', self._mini_speed, self._maxi_speed)
        self._c2_v0 = self._read_value('car2 v0', 'c2_v0', self._mini_speed, self._maxi_speed)
        self._c1_a = self._read_value('car1 a', 'c1_a', self._mini_acceleration, self._maxi_acceleration)
        self._c2_a = self._read_value('car2 a', 'c2_a', self._mini_acceleration, self._maxi_acceleration)
        self._t_start = self._read_value('time start', 't_start', self._mini_time_start, self._maxi_time_start)
        self._t_end = self._read_value('time end', 't_end', self._mini_time_end, self._maxi_time_end)

    def _read_value(self, field_name, input_name, mini, maxi):
        inp = self._builder.get_variable(input_name).get()

        if not valid_input(inp, mini, maxi):
            self._is_valid_all = False
            self._err_message += f'{field_name} should be a number between {mini} and {maxi}. \n'
            return inp

        input_value = float(inp)
        return input_value


if __name__ == '__main__':
    app = CarChaseAppTkPyGubu()
    app.run()
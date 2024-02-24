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
from drawing import find_x_range, drawing_settings, draw_road

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

        self.dt = 0.01

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
        self.car1 = Car(self.c1_x0, self.c1_v0, self.c1_a, marker_color='red')
        self.car2 = Car(self.c2_x0, self.c2_v0, self.c2_a, marker_color='green')

        t_s = np.arange(self.t_start, self.t_end, self.dt)
        car1_positions = self.car1.position(t_s)
        car2_positions = self.car2.position(t_s)
        self.x_min, self.x_max = find_x_range(car1_positions, car2_positions)
        drawing_settings(self.x_min, self.x_max, self.ax)
        draw_road(ax=self.ax)
        car1_pt, = self.ax.plot([], [],
                                color=self.car1.get_marker_color(),
                                marker=self.car1.get_marker(), markersize=12)
        car2_pt, = self.ax.plot([], [],
                                color=self.car2.get_marker_color(),
                                marker=self.car2.get_marker(), markersize=12)
        time_template = 'time = {:.1f}'
        time_text = self.ax.text(0.05, 0.88, '', transform=self.ax.transAxes)
        self.canvas.draw()

        def animate(i):
            car1_pt.set_data([car1_positions[i]], [self.car1_y])
            car2_pt.set_data([car2_positions[i]], [self.car2_y])
            time_text.set_text(time_template.format(i * self.dt))
            return car1_pt, car2_pt,

        self.ani = FuncAnimation(self.fig, animate, frames=len(t_s), interval=self.dt * 1000, repeat=False)
        self.canvas.draw()

    def _read_values(self):
        self.c1_x0 = self.builder.get_variable('c1_x0').get()
        self.c2_x0 = self.builder.get_variable('c2_x0').get()
        self.c1_v0 = self.builder.get_variable('c1_v0').get()
        self.c2_v0 = self.builder.get_variable('c2_v0').get()
        self.c1_a = self.builder.get_variable('c1_a').get()
        self.c2_a = self.builder.get_variable('c2_a').get()
        self.t_start = self.builder.get_variable('t_start').get()
        self.t_end = self.builder.get_variable('t_end').get()


if __name__ == '__main__':
    app = CarChaseAppTkPyGubu()
    app.run()
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import artist
from matplotlib.animation import FuncAnimation
from simulation_settings import *
from car import Car
from drawing import find_x_range, drawing_settings, draw_road, get_time_text
from typing import Iterable


def user_input_values() -> dict:
    st.sidebar.subheader("Car 1:")
    c1_x0 = st.sidebar.slider('Initial position of car 1 [m]', MINI_DIST, MAXI_DIST, 0.0)
    c1_v0 = st.sidebar.slider('Initial speed of car 1 [m/s]', MINI_SPEED, MAXI_SPEED, 0.0)
    c1_a = st.sidebar.slider('Acceleration of car 1 [m/s'+r'$^2$'+']', MINI_ACCELERATION, MAXI_ACCELERATION, 1.5)
    st.sidebar.subheader("Car 2:")
    c2_x0 = st.sidebar.slider('Initial position of car 2 [m]', MINI_DIST, MAXI_DIST, 0.0)
    c2_v0 = st.sidebar.slider('Initial speed of car 2 [m/s]', MINI_SPEED, MAXI_SPEED, 11.11)
    c2_a = st.sidebar.slider('Acceleration of car 2 [m/s' + r'$^2$' + ']', MINI_ACCELERATION, MAXI_ACCELERATION, 0.8)
    st.sidebar.subheader('Time of simulation')
    t_start = st.sidebar.slider('Initial time [s]', MINI_TIME_START, MAXI_TIME_START, 0.0)
    t_end = st.sidebar.slider('Final time [s]', MINI_TIME_END, MAXI_TIME_END, 33.0)
    data = {'car1': {'x0': c1_x0, 'v0': c1_v0, 'a': c1_a},
            'car2': {'x0': c2_x0, 'v0': c2_v0, 'a': c2_a},
            'time': {'start': t_start, 'end': t_end}
            }
    return data


st.write("""
# Car Chase App

## Kinematic simulation
""")

st.sidebar.header("Set conditions:")

initial_data = user_input_values()

car1 = Car(initial_data['car1']['x0'], initial_data['car1']['v0'], initial_data['car1']['a'], marker_color='red')
car2 = Car(initial_data['car2']['x0'], initial_data['car2']['v0'], initial_data['car2']['a'], marker_color='green')

t_s = np.arange(initial_data['time']['start'], initial_data['time']['end'], DT)
car1_positions = car1.position(t_s)
car2_positions = car2.position(t_s)
x_min, x_max = find_x_range(car1_positions, car2_positions)

fig, ax = plt.subplots(figsize=(6, 3))

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


ani = FuncAnimation(fig, animate, frames=len(t_s), interval=DT*2, blit=True)

components.html(ani.to_jshtml(), height=400)

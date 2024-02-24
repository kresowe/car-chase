import matplotlib.pyplot as plt
from car import Car
from drawing import draw_road, draw_car, drawing_settings

if __name__ == '__main__':
    car1 = Car(x0=0, v0=0, a=1.5, marker_color='red')
    car2 = Car(x0=0, v0=11.11, a=0.8, marker_color='green')

    drawing_settings(-10, 800)
    draw_road()
    draw_car(car1, t=5, y=0.45)
    draw_car(car2, t=5, y=0.55)
    plt.show()

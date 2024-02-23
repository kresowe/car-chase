from car import Car

if __name__ == '__main__':
    car1 = Car(x0=0, v0=0, a=1.5, marker_color='red')
    car2 = Car(x0=0, v0=11.11, a=0.8, marker_color='green')

    print(car1.position(t=31.7))
    print(car2.position(t=31.7))
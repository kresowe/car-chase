import matplotlib.pyplot as plt


def draw_road(low_y=0.4, high_y=0.6):
    plt.axhline(low_y, linewidth=2, color='black')
    plt.axhline(high_y, linewidth=2, color='black')

import matplotlib.pyplot as plt
import numpy as np


def draw_pifagor_tree(ax, x, y, angle, length, level):
    if level == 0:
        return

    x_1 = x + length * np.cos(np.radians(angle))
    y_1 = y + length * np.sin(np.radians(angle))
    ax.plot([x, x_1], [y, y_1], color='brown')
    new_length = length * np.sin(np.radians(45))
    draw_pifagor_tree(ax, x_1, y_1, angle - 45, new_length, level - 1)
    draw_pifagor_tree(ax, x_1, y_1, angle + 45, new_length, level - 1)


def main():
    level = int(input("Введіть рівень рекурсії для фрактала 'Дерево Піфагора': "))
    length = 100
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()
    draw_pifagor_tree(ax, 0, 0, 90, length, level)
    plt.show()


if __name__ == "__main__":
    main()

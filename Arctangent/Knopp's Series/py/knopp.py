#TODO: deviation, tkinter integration

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import atan as arctan
import tkinter as tk

figure, axes = plt.subplots()
x: list[float] = []
y: list[float] = []
placeholder_name, = axes.plot(x, y)

def artists(): return placeholder_name # fixes the repitition of the ordered pair (0, y).

def next_value(k: int) -> float:
    if k == 1: return 4 * arctan(1/3)
    return 4 * arctan(1 / (pow(k, 2) + k + 1)) + y[-1]

def update_graph(frame):

    x.append(frame)
    y.append(next_value(frame + 1))
    placeholder_name.set_data(x, y)

    figure.gca().relim()
    figure.gca().autoscale_view()

plt.axhline(y=3.141592653589793238462643383279502884197169399375, color='r', linestyle='--', label="pi") # Adds a horizontal reference line at y = pi.

animation = FuncAnimation(figure, func=update_graph, interval=0, init_func=artists, repeat=False)
placeholder_name.set_label("approximation")

plt.legend()
plt.show()
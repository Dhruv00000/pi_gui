#TODO: deviation

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import atan as arctan
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

figure, axes = plt.subplots()
x: list[float] = []
y: list[float] = []
graph, = axes.plot(x, y)

def artists(): return graph # fixes the repitition of the ordered pair (0, y).

def next_value(k: int) -> float:
    if k == 1: return 4 * arctan(1/3)
    return 4 * arctan(1 / (pow(k, 2) + k + 1)) + y[-1]

def update_graph(frame):

    x.append(frame)
    y.append(next_value(frame + 1))
    graph.set_data(x, y)

    figure.gca().relim()
    figure.gca().autoscale_view()

plt.axhline(y=3.141592653589793238462643383279502884197169399375, color='r', linestyle='--', label="pi") # Adds a horizontal reference line at y = pi.

root = tk.Tk()
frame = tk.Frame(root)
canvas = FigureCanvasTkAgg(figure=figure, master=frame)
canvas.get_tk_widget().pack()

animation = FuncAnimation(figure, func=update_graph, interval=0, init_func=artists, repeat=False)

graph.set_label("approximation")
plt.legend()

frame.pack()
root.mainloop()
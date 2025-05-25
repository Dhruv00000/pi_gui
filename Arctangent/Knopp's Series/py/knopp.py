import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import atan as arctan
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import scrolledtext
from time import sleep

pi = 3.141592653589793238462643383279502884197169399375 # accurate value used for error calculation.

figure, axes = plt.subplots()
x: list[float] = []
y: list[float] = []
graph, = axes.plot(x, y)

def artists(): return graph # fixes the repitition of the ordered pair (0, y).

def approximation_function(k: int) -> float:
    if k == 1: return 4 * arctan(1/3)
    return 4 * arctan(1 / (pow(k, 2) + k + 1)) + y[-1]

root = tk.Tk()
root.geometry("1440x810")
root.title("Knopp's Arctangent Series")

log_area = scrolledtext.ScrolledText(root, wrap='none', width=43, height=20)
log_area.place(x=700, y=400)

def update_log():

    deviation = "undefined (first iteration)" if x[-1] == 0 else y[-1] - y[-2]

    log_area.configure(state="normal")
    log_area.insert(index=tk.END, chars = f"""
ITERATION {x[-1] + 1}-
approximation = {y[-1]}
deviation = {deviation}
error_percentage = {(y[-1] - pi) * 100 / pi}%
""")
    log_area.configure(state="disabled") # the state cannot be "disabled" permanently in order for the log text to actually be updated, so I enable and disable the log area rapidly enough where it is practically impossible to manually type inside the log, but the log text can still be updated as intended.

    log_area.see("end") # Temporary auto-scroll solution.

current_iteration_info_frame = tk.LabelFrame(master=root, text="CURRENT ITERATION-")
current_iteration_info_frame.place(x=700, y = 50, width="300", height="180")

def update_current_iteration_info():

    deviation = "undefined (first iteration)" if x[-1] == 0 else y[-1] - y[-2]

    current_iteration_info = tk.Label(master=current_iteration_info_frame, text=f"""
ITERATION {x[-1] + 1}-
approximation = {y[-1]}
deviation = {deviation}
error_percentage = {(y[-1] - pi) * 100 / pi}%
""")

    # The current iteration info text keeps flickering and sometimes even disappearing for some time because iterations go by too fast. I overlap the 2 latest iteration info labels (newer one on top) and delete all previous ones to minimize the flickering while also not overloading the label frame with thousands of labels corresponding to each iteration.
    current_iteration_info.place(x=20, y=20)
    for widget in current_iteration_info_frame.winfo_children():
        if len(current_iteration_info_frame.winfo_children()) > 2: widget.destroy()


def update_graph(frame):
    x.append(frame)
    y.append(approximation_function(frame + 1))
    graph.set_data(x, y)
    figure.gca().relim()
    figure.gca().autoscale_view()

def update_all_widgets(frame):

    update_graph(frame)

    update_current_iteration_info()
    update_log()

plt.axhline(y=pi, color='r', linestyle='--', label="pi") # Adds a horizontal line at y = pi as a reference.

# embed the plot into a tkinter window.
plot_frame = tk.Frame(root)
canvas = FigureCanvasTkAgg(figure=figure, master=plot_frame)
canvas.get_tk_widget().pack()

animation = FuncAnimation(figure, func=update_all_widgets, interval=0, init_func=artists, repeat=False)

graph.set_label("approximation")
plt.legend()

plot_frame.place(x=0, y=0)

root.mainloop()
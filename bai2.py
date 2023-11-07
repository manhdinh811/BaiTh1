import tkinter as tk
import sympy as sp
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Hàm tính đạo hàm
def compute_derivative():
    x = float(entry_x.get())
    expression = entry_function.get()
    f = sp.sympify(expression)
    df = sp.diff(f, sp.symbols('x'))
    result_label.config(text=f"Đạo hàm tại x={x}: {df.subs(sp.symbols('x'), x)}")

# Hàm tính tích phân
def compute_integral():
    a = float(entry_a.get())
    b = float(entry_b.get())
    expression = entry_function.get()
    f = sp.sympify(expression)
    integral = sp.integrate(f, (sp.symbols('x'), a, b))
    result_label.config(text=f"Tích phân từ {a} đến {b}: {integral}")

# Hàm vẽ biểu đồ
# Hàm vẽ biểu đồ
def plot_graph():
    expression = entry_function.get()
    f = sp.sympify(expression)
    x = sp.symbols('x')

    a = float(entry_a.get())
    b = float(entry_b.get())
    num_points = 400
    x_vals = np.linspace(a, b, num_points)
    y_vals = [f.subs(x, val) for val in x_vals]

    plt.clf()
    plt.plot(x_vals, y_vals)
    plt.title("Biểu đồ hàm số")
    plt.xlabel("x")
    plt.ylabel("y")
    canvas.draw()



# Tạo giao diện
app = tk.Tk()
app.title("Ứng dụng Giải tích")

frame = tk.Frame(app)
frame.pack()

tk.Label(frame, text="Hàm số:").grid(row=0, column=0)
entry_function = tk.Entry(frame)
entry_function.grid(row=0, column=1)

tk.Label(frame, text="a (Từ):").grid(row=1, column=0)
entry_a = tk.Entry(frame)
entry_a.grid(row=1, column=1)

tk.Label(frame, text="b (Đến):").grid(row=1, column=2)
entry_b = tk.Entry(frame)
entry_b.grid(row=1, column=3)

tk.Label(frame, text="x (Tại):").grid(row=2, column=0)
entry_x = tk.Entry(frame)
entry_x.grid(row=2, column=1)

compute_derivative_button = tk.Button(frame, text="Tính Đạo hàm", command=compute_derivative)
compute_derivative_button.grid(row=3, column=0)

compute_integral_button = tk.Button(frame, text="Tính Tích phân", command=compute_integral)
compute_integral_button.grid(row=3, column=1)

plot_graph_button = tk.Button(frame, text="Vẽ biểu đồ", command=plot_graph)
plot_graph_button.grid(row=3, column=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=4, columnspan=4)

# Tạo biểu đồ
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

app.mainloop()

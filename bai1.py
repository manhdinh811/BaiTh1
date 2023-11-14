import tkinter as tk
import numpy as np

def solve_linear_equations():
    # Kiểm tra xem tất cả ô nhập liệu đã được điền đủ giá trị
    if any("" in row for row in entries) or "" in constant_entries:
        result_label.config(text="Hãy điền đầy đủ giá trị ")
    else:
        matrix_a = []
        vector_b = []
        for i in range(n):
            equation = []
            for j in range(n):
                value = entries[i][j].get()
                if value == "":
                    result_label.config(text="Hãy điền đầy đủ giá trị ")
                    return
                try:
                    equation_value = float(value)
                    equation.append(equation_value)
                except ValueError:
                    result_label.config(text="Nhập giá trị hợp lệ cho a")
                    return
            if len(equation) != n:
                result_label.config(text="Số lượng phần tử trong ma trận a không đồng nhất")
                return
            matrix_a.append(equation)
            value = constant_entries[i].get()
            if value == "":
                result_label.config(text="Hãy điền đầy đủ giá trị ")
                return
            try:
                constant_value = float(value)
                vector_b.append(constant_value)
            except ValueError:
                result_label.config(text="Nhập giá trị hằng số hợp lệ cho b")
                return

        try:
            solution = np.linalg.solve(matrix_a, vector_b)
            result_label.config(text=f"Kết quả: {solution}")
        except np.linalg.LinAlgError:
            result_label.config(text="Hệ phương trình vô nghiệm hoặc vô số nghiệm.")

def get_number_of_equations():
    global n
    try:
        n = int(n_entry.get())
        if n > 0:
            n_label.config(text=f"Số phương trình và số ẩn (n = {n}):")
            create_entries()
        else:
            n_label.config(text="Nhập n > 0")
    except ValueError:
        n_label.config(text="Nhập n là số nguyên dương")

def create_entries():
    for widget in window.winfo_children():
        widget.grid_forget()

    entries.clear()
    constant_entries.clear()

    for i in range(n):
        row = []
        for j in range(n):
            tk.Label(window, text=f"a{i+1}{j+1} = ").grid(row=i, column=2*j)
            entry = tk.Entry(window)
            entry.grid(row=i, column=2*j+1)
            row.append(entry)
        entries.append(row)

    for i in range(n):
        tk.Label(window, text=f"b{i+1} = ").grid(row=i, column=2*n)
        entry = tk.Entry(window)
        entry.grid(row=i, column=2*n+1)
        constant_entries.append(entry)

    solve_button = tk.Button(window, text="Giải", command=solve_linear_equations)
    solve_button.grid(row=n, columnspan=2*n+2)

    global result_label
    result_label = tk.Label(window, text="")
    result_label.grid(row=n+1, columnspan=2*n+2)

window = tk.Tk()
window.title("Giải hệ phương trình tuyến tính")

n = 0  # Số phương trình và số ẩn

n_label = tk.Label(window, text="Nhập số phương trình (n):")
n_label.grid(row=0, column=0)

n_entry = tk.Entry(window)
n_entry.grid(row=0, column=1)

confirm_button = tk.Button(window, text="Xác nhận", command=get_number_of_equations)
confirm_button.grid(row=0, column=2)

entries = []
constant_entries = []

window.mainloop()

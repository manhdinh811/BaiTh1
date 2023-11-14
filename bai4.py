import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

def load_data():
    file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path, index_col=0, header=0)
        return df
    else:
        return None

def generate_report():
    df = load_data()
    if df is not None:
        in_data = array(df.iloc[:, :])
        print(in_data)
        print('Tong so sinh vien di thi:')
        tongsv = in_data[:, 1]
        print(np.sum(tongsv))
        diemA = in_data[:, 3]
        diemBc = in_data[:, 4]
        print('Tong sv:', tongsv)
        maxa = diemA.max()
        i, = np.where(diemA == maxa)
        print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i, 0], maxa))
        plt.plot(range(len(diemA)), diemA, 'r-', label="Diem A")
        plt.plot(range(len(diemBc)), diemBc, 'g-', label="Diem B +")
        plt.xlabel('Lơp')
        plt.ylabel(' So sv dat diem ')
        plt.legend(loc='upper right')
        plt.show()

# Giao diện đồ họa
root = tk.Tk()
root.title("Báo cáo học phần môn học")

load_button = tk.Button(root, text="Chọn file", command=load_data)
load_button.pack(pady=10)

generate_button = tk.Button(root, text="Tạo báo cáo", command=generate_report)
generate_button.pack(pady=10)

root.mainloop()

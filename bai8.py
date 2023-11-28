import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk

def detect_edges(image_path):
    # Đọc ảnh và chuyển sang ảnh xám
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng Gaussian Blur để làm mịn ảnh trước khi tìm biên
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Phát hiện biên bằng phương pháp Canny
    edges = cv2.Canny(blurred, 50, 150)

    return edges

def display_edges(edges):
    cv2.imshow("Edges", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        edges = detect_edges(file_path)
        display_edges(edges)

window = tk.Tk()
window.title("Image Edge Detection")

label = tk.Label(window, text="Image Edge Detection", font=("Helvetica", 16))
label.pack(pady=10)

open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack(pady=20)

window.mainloop()

import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        display_image(image)

def display_image(image):
    global panel
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (300, 300))  # Resize for display
    image = Image.fromarray(image)
    photo = ImageTk.PhotoImage(image=image)
    if panel is None:
        panel = tk.Label(window, image=photo)
        panel.image = photo
        panel.pack()
    else:
        panel.configure(image=photo)
        panel.image = photo

def smooth_image():
    global panel
    if panel is not None:
        img = cv2.cvtColor(cv2.imread("images.jpg"), cv2.COLOR_BGR2RGB)
        smoothed_img = cv2.bilateralFilter(img, 9, 75, 75)  # Apply bilateral filter
        display_image(smoothed_img)

def save_temp_image(image):
    cv2.imwrite("images.jpg", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

window = tk.Tk()
window.title("Image Smoothing App")

panel = None

open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()

smooth_button = tk.Button(window, text="Smooth Image", command=smooth_image)
smooth_button.pack()

window.mainloop()

import tkinter as tk
from tkinter import ttk
import numpy as np
class HocTapHinhHocApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng Dụng Học Tập Hình Học")

        self.create_widgets()

    def create_widgets(self):
        # Tạo Label và Combobox để chọn loại hình
        self.label_chon_hinh = ttk.Label(self.root, text="Chọn hình:")
        self.label_chon_hinh.grid(row=0, column=0, padx=10, pady=10)

        self.combobox_hinh = ttk.Combobox(self.root, values=["Hình Vuông", "Hình Chữ Nhật", "Hình Tròn", "Hình Tam Giác"])
        self.combobox_hinh.grid(row=0, column=1, padx=10, pady=10)

        # Tạo các Label và Entry để nhập thông số hình
        self.label_thong_so = ttk.Label(self.root, text="Nhập thông số:")
        self.label_thong_so.grid(row=1, column=0, padx=10, pady=10)

        self.label_kich_thuoc1 = ttk.Label(self.root, text="Kích thước 1:")
        self.label_kich_thuoc1.grid(row=1, column=1, padx=10, pady=10)

        self.entry_kich_thuoc1 = ttk.Entry(self.root)
        self.entry_kich_thuoc1.grid(row=1, column=2, padx=10, pady=10)

        self.label_kich_thuoc2 = ttk.Label(self.root, text="Kích thước 2:")
        self.label_kich_thuoc2.grid(row=1, column=3, padx=10, pady=10)

        self.entry_kich_thuoc2 = ttk.Entry(self.root)
        self.entry_kich_thuoc2.grid(row=1, column=4, padx=10, pady=10)

        self.label_kich_thuoc3 = ttk.Label(self.root, text="Kích thước 3:")
        self.label_kich_thuoc3.grid(row=1, column=5, padx=10, pady=10)

        self.entry_kich_thuoc3 = ttk.Entry(self.root)
        self.entry_kich_thuoc3.grid(row=1, column=6, padx=10, pady=10)

        # Tạo Button để tính diện tích và chu vi
        self.button_tinh_toan = ttk.Button(self.root, text="Tính Toán", command=self.tinh_toan)
        self.button_tinh_toan.grid(row=2, column=0, columnspan=7, pady=10)

        # Hiển thị kết quả
        self.label_ket_qua = ttk.Label(self.root, text="")
        self.label_ket_qua.grid(row=3, column=0, columnspan=7, pady=10)

    def tinh_toan(self):
        loai_hinh = self.combobox_hinh.get()

        kich_thuoc1_str = self.entry_kich_thuoc1.get()
        kich_thuoc2_str = self.entry_kich_thuoc2.get()
        kich_thuoc3_str = self.entry_kich_thuoc3.get()

        if not kich_thuoc1_str.replace('.', '', 1).isdigit() or not kich_thuoc2_str.replace('.', '', 1).isdigit() or not kich_thuoc3_str.replace('.', '', 1).isdigit():
            # Kiểm tra xem giá trị nhập vào có phải là số không
            ket_qua = "Vui lòng nhập số cho kích thước!"
            self.label_ket_qua.config(text=ket_qua)
            return

        kich_thuoc1 = float(kich_thuoc1_str)

        try:
            if loai_hinh == "Hình Vuông":
                dien_tich = kich_thuoc1 ** 2
                chu_vi = 4 * kich_thuoc1
            elif loai_hinh == "Hình Chữ Nhật":
                kich_thuoc2 = float(kich_thuoc2_str)
                dien_tich = kich_thuoc1 * kich_thuoc2
                chu_vi = 2 * (kich_thuoc1 + kich_thuoc2)
            elif loai_hinh == "Hình Tròn":
                dien_tich = np.pi * kich_thuoc1 ** 2
                chu_vi = 2 * np.pi * kich_thuoc1
            elif loai_hinh == "Hình Tam Giác":
                kich_thuoc2 = float(kich_thuoc2_str)
                kich_thuoc3 = float(kich_thuoc3_str)

                # Sử dụng công thức Heron
                s = (kich_thuoc1 + kich_thuoc2 + kich_thuoc3) / 2
                dien_tich = np.sqrt(s * (s - kich_thuoc1) * (s - kich_thuoc2) * (s - kich_thuoc3))
                chu_vi = kich_thuoc1 + kich_thuoc2 + kich_thuoc3

            ket_qua = f"Diện tích: {dien_tich:.2f}, Chu vi: {chu_vi:.2f}"
            self.label_ket_qua.config(text=ket_qua)

        except ValueError:
            # Xử lý nếu có lỗi khi chuyển đổi sang số
            ket_qua = "Vui lòng nhập số cho kích thước!"
            self.label_ket_qua.config(text=ket_qua)
        except ValueError:
            # Xử lý nếu có lỗi khi chuyển đổi sang số
            ket_qua = "Vui lòng nhập số cho kích thước!"
            self.label_ket_qua.config(text=ket_qua)

if __name__ == "__main__":
    root = tk.Tk()
    app = HocTapHinhHocApp(root)
    root.mainloop()

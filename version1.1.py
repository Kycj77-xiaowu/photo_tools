# import os
# import shutil
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk  # pip install pillow

# class PhotoOrganizerSequence:
#     def __init__(self, master):
#         self.master = master
#         master.title("照片整理工具（顺序处理版）")
#         master.geometry("1200x800")  # 固定窗口大小

#         self.folder_path = ""
#         self.image_list = []
#         self.current_index = 0

#         # 主布局：左右两区
#         self.left_frame = tk.Frame(master, width=800, height=800)
#         self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

#         self.right_frame = tk.Frame(master, width=400, height=800, padx=20, pady=20)
#         self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)

#         # 图片显示（左侧）
#         self.image_label = tk.Label(self.left_frame, bg="gray")
#         self.image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

#         # 右侧标题
#         tk.Label(self.right_frame, text="照片重命名与分类", font=("Arial", 16, "bold")).pack(pady=10)

#         # 第一部分
#         tk.Label(self.right_frame, text="第一部分（D001-1）:", font=("Arial", 12)).pack(anchor="w", pady=5)
#         self.part1 = tk.Entry(self.right_frame, font=("Arial", 12), width=25)
#         self.part1.pack(pady=5)

#         # 第二部分
#         tk.Label(self.right_frame, text="第二部分JX（镜像）:", font=("Arial", 12)).pack(anchor="w", pady=5)
#         self.part2 = tk.Entry(self.right_frame, font=("Arial", 12), width=25)
#         self.part2.pack(pady=5)

#         # 第三部分
#         tk.Label(self.right_frame, text="第三部分（编号）:", font=("Arial", 12)).pack(anchor="w", pady=5)
#         self.part3 = tk.Entry(self.right_frame, font=("Arial", 12), width=25)
#         self.part3.pack(pady=5)

#         # 按钮区
#         tk.Button(self.right_frame, text="选择文件夹", font=("Arial", 12), width=20, height=2,
#                   command=self.choose_folder).pack(pady=15)
#         tk.Button(self.right_frame, text="下一张", font=("Arial", 12), width=20, height=2,
#                   command=self.process_next).pack(pady=15)

#     def choose_folder(self):
#         folder = filedialog.askdirectory(title="选择图片文件夹")
#         if folder:
#             self.folder_path = folder
#             self.image_list = sorted([
#                 f for f in os.listdir(folder)
#                 if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tif'))
#             ])
#             self.current_index = 0

#             if not self.image_list:
#                 messagebox.showerror("错误", "该文件夹没有图片")
#                 return

#             self.show_image()

#     def show_image(self):
#         """显示当前图片"""
#         if 0 <= self.current_index < len(self.image_list):
#             img_path = os.path.join(self.folder_path, self.image_list[self.current_index])
#             try:
#                 img = Image.open(img_path)
#                 img.thumbnail((780, 780))  # 左侧最大显示
#                 img_tk = ImageTk.PhotoImage(img)
#                 self.image_label.config(image=img_tk)
#                 self.image_label.image = img_tk
#             except Exception as e:
#                 messagebox.showerror("错误", f"无法打开图片: {e}")
#         else:
#             messagebox.showinfo("完成", "全部照片已处理")
#             self.image_label.config(image="", text="")

#     def process_next(self):
#         """处理当前图片并进入下一张"""
#         if not self.image_list:
#             messagebox.showerror("错误", "请先选择文件夹")
#             return

#         part1 = self.part1.get().strip()  # 可能是 D001-1 或 D002-5
#         part2 = self.part2.get().strip()
#         part3 = self.part3.get().strip()

#         if not part1 or not part2 or not part3:
#             messagebox.showerror("错误", "请填写完整三个部分")
#             return

#         old_name = self.image_list[self.current_index]
#         old_path = os.path.join(self.folder_path, old_name)
#         ext = os.path.splitext(old_name)[1]

#         # 新文件名
#         new_name = f"{part1}-{part2}{part3}{ext}"

#         # 文件夹名取调查点编号（-前部分）
#         folder_name = part1.split('-')[0]  # "D001-1" → "D001"
#         folder_path = os.path.join(self.folder_path, folder_name)
#         os.makedirs(folder_path, exist_ok=True)

#         # 移动并改名
#         new_path = os.path.join(folder_path, new_name)
#         try:
#             shutil.move(old_path, new_path)
#         except Exception as e:
#             messagebox.showerror("错误", f"移动文件出错: {e}")
#             return

#         # 下一张
#         self.current_index += 1
#         if self.current_index < len(self.image_list):
#             self.show_image()
#             self.part3.delete(0, tk.END)  # 只清空编号，方便同一调查点快速录入
#         else:
#             messagebox.showinfo("完成", "已处理完所有图片")
#             self.image_label.config(image="", text="")
#             self.image_list = []

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PhotoOrganizerSequence(root)
#     root.mainloop()








    # def next_image(self):
    #     if not self.current_image_path:
    #         return

    #     # Build new file name
    #     part1 = f"{self.part1_1_var.get()}-{self.part1_2_var.get()}"
    #     part2 = self.part2_var.get()
    #     part3 = self.part3_var.get()

    #     if not part1 or not part2 or not part3:
    #         messagebox.showerror("Error", "All fields must be filled before proceeding.")
    #         return

    #     new_name = f"{part1}-{part2}{part3}{os.path.splitext(self.current_image_path)[1]}"
    #     folder_name = self.part1_1_var.get()  # Folder is based on Part1.1 only

    #     # Create folder if not exists
    #     base_dir = os.path.dirname(self.current_image_path)
    #     target_folder = os.path.join(base_dir, folder_name)
    #     os.makedirs(target_folder, exist_ok=True)

    #     # Move and rename
    #     target_path = os.path.join(target_folder, new_name)
    #     shutil.move(self.current_image_path, target_path)

    #     # Go to next image
    #     self.current_index += 1
    #     if self.current_index >= len(self.photo_list):
    #         messagebox.showinfo("Info", "All images processed.")
    #         self.photo_list = []
    #         self.current_image_path = None
    #         self.image_label.config(image="", text="No image")
    #         return

    #     self.show_image()

    #     # Reset input fields sequence
    #     self.part1_2_var.set("")
    #     self.part3_var.set("")
    #     self.entry_part1_1.focus_set()


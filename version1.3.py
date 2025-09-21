import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  # pip install pillow


class PhotoRenamer:
    def __init__(self, root):
        self.root = root
        self.root.title("照片重命名与分类工具")
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)

        # Variables
        self.photo_list = []
        self.current_index = 0
        self.current_image_path = None

        self.part1_1_var = tk.StringVar()  # e.g., D001
        self.part1_2_var = tk.StringVar()  # e.g., 1
        self.part2_var = tk.StringVar()    # optional
        self.part3_var = tk.StringVar()    # optional

        # UI
        self.create_widgets()

    def create_widgets(self):
        # Top control frame
        ctrl_frame = tk.Frame(self.root)
        ctrl_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        btn_select = tk.Button(ctrl_frame, text="选择文件夹", command=self.select_folder)
        btn_select.pack(side=tk.LEFT, padx=5)

        btn_next = tk.Button(ctrl_frame, text="下一张(保存)", command=self.next_image)
        btn_next.pack(side=tk.LEFT, padx=5)

        # Input fields frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        tk.Label(input_frame, text="点编号").grid(row=0, column=0)
        self.entry_part1_1 = tk.Entry(input_frame, textvariable=self.part1_1_var, width=8)
        self.entry_part1_1.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="照片编号").grid(row=0, column=2)
        self.entry_part1_2 = tk.Entry(input_frame, textvariable=self.part1_2_var, width=5)
        self.entry_part1_2.grid(row=0, column=3, padx=5)

        tk.Label(input_frame, text="镜像（可选）").grid(row=0, column=4)
        self.entry_part2 = tk.Entry(input_frame, textvariable=self.part2_var, width=8)
        self.entry_part2.grid(row=0, column=5, padx=5)

        tk.Label(input_frame, text="镜像角度（可选）").grid(row=0, column=6)
        self.entry_part3 = tk.Entry(input_frame, textvariable=self.part3_var, width=8)
        self.entry_part3.grid(row=0, column=7, padx=5)

        # Store entries for navigation
        self.entries = [
            self.entry_part1_1,
            self.entry_part1_2,
            self.entry_part2,
            self.entry_part3
        ]

        def navigate(event, direction):
            current = self.entries.index(event.widget)
            new_index = (current + direction) % len(self.entries)
            self.entries[new_index].focus_set()

        # Bind Up/Down/Enter for all entries
        for entry in self.entries:
            entry.bind("<Up>", lambda e, d=-1: navigate(e, d))
            entry.bind("<Down>", lambda e, d=1: navigate(e, d))
            # Enter moves forward, last entry triggers save
            if entry != self.entry_part3:
                entry.bind("<Return>", lambda e, d=1: navigate(e, d))
            else:
                entry.bind("<Return>", lambda e: self.next_image())

        # Image display
        self.image_label = tk.Label(self.root, bg="gray")
        self.image_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.image_label.bind("<Configure>", self.resize_image)

        # Bind Left/Right for image browsing without saving
        self.root.bind("<Left>", lambda e: self.prev_image())
        self.root.bind("<Right>", lambda e: self.skip_next_image())

    def select_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return
        self.photo_list = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
        ]
        self.photo_list.sort()
        self.current_index = 0
        if not self.photo_list:
            messagebox.showwarning("Warning", "No images found in the folder.")
            return
        self.show_image()

    def show_image(self):
        if not self.photo_list:
            return
        self.current_image_path = self.photo_list[self.current_index]
        self.load_and_display_image()

    def load_and_display_image(self, width=None, height=None):
        if not self.current_image_path:
            return
        img = Image.open(self.current_image_path)
        if width and height:
            img.thumbnail((width, height))
        else:
            img.thumbnail((self.image_label.winfo_width(), self.image_label.winfo_height()))
        self.tk_img = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.tk_img)

    def resize_image(self, event):
        self.load_and_display_image(event.width, event.height)

    def prev_image(self):
        """Go to previous image without saving."""
        if not self.photo_list:
            return
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()

    def skip_next_image(self):
        """Go to next image without saving."""
        if not self.photo_list:
            return
        if self.current_index < len(self.photo_list) - 1:
            self.current_index += 1
            self.show_image()

    def next_image(self):
        if not self.current_image_path:
            return

        # Required fields
        p1_1 = self.part1_1_var.get().strip()
        p1_2 = self.part1_2_var.get().strip()
        p2 = self.part2_var.get().strip()
        p3 = self.part3_var.get().strip()

        if not p1_1 or not p1_2:
            messagebox.showerror("Error", "Point ID and Photo No. must be filled.")
            return

        # Build file name
        file_name = f"{p1_1}-{p1_2}"
        if p2 or p3:
            file_name += f"-{p2}{p3}"

        ext = os.path.splitext(self.current_image_path)[1]
        new_name = f"{file_name}{ext}"

        # Create folder and move file
        base_dir = os.path.dirname(self.current_image_path)
        target_folder = os.path.join(base_dir, p1_1)
        os.makedirs(target_folder, exist_ok=True)

        target_path = os.path.join(target_folder, new_name)
        shutil.move(self.current_image_path, target_path)

        # Next image
        self.current_index += 1
        if self.current_index >= len(self.photo_list):
            messagebox.showinfo("Info", "All images processed.")
            self.photo_list = []
            self.current_image_path = None
            self.image_label.config(image="", text="No image")
            return

        self.show_image()
      # Reset only p1_2, p2, p3
        self.part1_2_var.set("")
        # self.part2_var.set("")
        self.part3_var.set("")
        self.entry_part1_1.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoRenamer(root)
    root.mainloop()
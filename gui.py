import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from predict_script import detection_script

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.current_file_path = None

        self.label = tk.Label(root)
        self.label.pack()

        self.button = tk.Button(root, text="Choose an image", command=self.choose_image)
        self.button.pack()

        # Label for displaying the image
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Button to process the image
        self.process_button = tk.Button(root, text="Start", command=self.process_image)
        self.process_button.pack(pady=10)

        # Label for displaying the result text
        self.result_text = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.result_text)
        self.result_label.pack(pady=10)

    def choose_image(self):
        file_path = filedialog.askopenfilename(title="Choose an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.current_file_path = file_path
            self.display_image()
            self.result_text.set("")

    def display_image(self):
        image = Image.open(self.current_file_path)
        image = image.resize((300, 300), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        self.label.config(image=image)
        self.label.image = image

    def process_image(self):
        if self.current_file_path:
            result = detection_script(self.current_file_path)
            self.result_text.set(result)
        else:
            self.result_text.set("No image selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()

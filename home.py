# home.py

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from image_encryption import ImageEncryptionApp
from text_encryption import TextEncryptionApp

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Encryption Standard App")
        self.root.geometry("660x525")

        # Header
        self.header_label = ctk.CTkLabel(self.root, text="DATA ENCRYPTION STANDARD APP", font=("Helvetica", 30, "bold"))
        self.header_label.pack(pady=(10, 20))

        # Text button
        self.text_button = ctk.CTkButton(self.root, text="Text", command=self.open_text_page, width=300, height=70)
        self.text_button.pack(pady=10)

        # File button
        self.file_button = ctk.CTkButton(self.root, text="Files", command=self.open_file_page, width=300, height=70)
        self.file_button.pack(pady=10)

        # Image button
        self.image_button = ctk.CTkButton(self.root, text="Image", command=self.open_image_page, width=300, height=70)
        self.image_button.pack(pady=10)

        # Video button
        self.video_button = ctk.CTkButton(self.root, text="Video", command=self.open_video_page, width=300, height=70)
        self.video_button.pack(pady=10)

        # Audio button
        self.audio_button = ctk.CTkButton(self.root, text="Audio", command=self.open_audio_page, width=300, height=70)
        self.audio_button.pack(pady=10)

    def open_image_page(self):
        self.new_window = ctk.CTkToplevel(self.root)
        self.app = ImageEncryptionApp(self.new_window)

    def open_video_page(self):
        # Implement open video page
        pass

    def open_text_page(self):
        self.new_window = ctk.CTkToplevel(self.root)
        self.app = TextEncryptionApp(self.new_window)

    def open_file_page(self):
        # Implement open file page
        pass

    def open_audio_page(self):
        # Implement open audio page
        pass

if __name__ == "__main__":
    ctk.set_default_color_theme("/Users/sultanazizul/Documents/CODE/PYTHON/Keamanan Informasi/TUBES/DES ENCRYPTION APP/assets/MoonLitSky.json")

    root = ctk.CTk()
    app = HomePage(root)
    root.mainloop()

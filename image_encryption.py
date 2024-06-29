# image_encryption.py

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from utils.encryption_utils import *

class ImageEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Decryption Using DES Algorithm")
        self.root.geometry("660x525")

        # User interface elements
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=10, padx=5)

        self.browse_button = ctk.CTkButton(self.frame, text="( + ) Browse Image", command=self.browse_image, width=626, height=70)
        self.browse_button.grid(row=1, column=0, columnspan=3, padx=6, pady=5, sticky='ew')

        self.image_frame = ctk.CTkFrame(self.root)
        self.image_frame.pack(padx=5)

        self.input_image_label = ctk.CTkLabel(self.image_frame, text="Input Image")
        self.input_image_label.grid(row=0, column=0, padx=10)
        self.input_image_label_image = ctk.CTkLabel(self.image_frame, width=300, height=300, text='')
        self.input_image_label_image.grid(row=1, column=0, padx=10)

        self.decrypted_image_label = ctk.CTkLabel(self.image_frame, text="Decrypted")
        self.decrypted_image_label.grid(row=0, column=1, padx=10)
        self.decrypted_image_label_image = ctk.CTkLabel(self.image_frame, width=300, height=300, text='')
        self.decrypted_image_label_image.grid(row=1, column=1, padx=10)

        self.button_frame = ctk.CTkFrame(self.root)
        self.button_frame.pack(pady=10, padx=10)

        self.key_label = ctk.CTkLabel(self.button_frame, text="Key (8 characters):")
        self.key_label.grid(row=0, column=0, columnspan=1, padx=5, pady=5)
        self.key_entry = ctk.CTkEntry(self.button_frame)
        self.key_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky='ew')

        self.encryption_button = ctk.CTkButton(self.button_frame, text="Encryption", command=self.encrypt_image, width=256)
        self.encryption_button.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.decryption_button = ctk.CTkButton(self.button_frame, text="Decryption", command=self.decrypt_image, width=256)
        self.decryption_button.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        self.reset_button = ctk.CTkButton(self.button_frame, text="Reset", command=self.reset_images, fg_color="#D03F2C", hover_color="lightcoral", width=100)
        self.reset_button.grid(row=1, column=2, padx=5, pady=5)

        self.input_image_path = ""

    def load_image(self, path, size):
        img = Image.open(path)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def encrypt_image(self):
        key = self.key_entry.get()
        if len(key) != 8:
            messagebox.showerror("Error", "Key must be 8 characters long!")
            return
        if not self.input_image_path:
            messagebox.showerror("Error", "Please choose an image first!")
            return
        try:
            with open(self.input_image_path, 'rb') as file:
                plaintext = file.read()

            start_time = time.time()

            encrypted_text = encrypt_data(key, plaintext)

            output_path = self.input_image_path.split('.')[0] + '_encrypt.bin'
            with open(output_path, 'wb') as file:
                file.write(encrypted_text)

            encrypted_size_kb = get_file_size_kb(output_path)
            duration = measure_execution_time(start_time)

            messagebox.showinfo("Success", f"Encrypted image saved as {output_path}\n\nTime: {duration:.4f} seconds\nSize: {encrypted_size_kb:.2f} KB")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def decrypt_image(self):
        key = self.key_entry.get()
        if len(key) != 8:
            messagebox.showerror("Error", "Key must be 8 characters long!")
            return
        if not self.input_image_path:
            messagebox.showerror("Error", "Please choose an image first!")
            return
        try:
            with open(self.input_image_path, 'rb') as file:
                encrypted_text = file.read()

            start_time = time.time()

            plaintext = decrypt_data(key, encrypted_text)

            output_path = self.input_image_path.split('.')[0] + '_decrypt.jpg'
            with open(output_path, 'wb') as file:
                file.write(plaintext)

            decrypted_size_kb = get_file_size_kb(output_path)
            duration = measure_execution_time(start_time)

            messagebox.showinfo("Success", f"Decrypted image saved as {output_path}\n\nTime: {duration:.4f} seconds\nSize: {decrypted_size_kb:.2f} KB")

            decrypted_img = self.load_image(output_path, (300, 300))
            self.decrypted_image_label_image.configure(image=decrypted_img)
            self.decrypted_image_label_image.image = decrypted_img

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def browse_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.input_image_path = file_path
            input_img = self.load_image(self.input_image_path, (300, 300))
            self.input_image_label_image.configure(image=input_img)
            self.input_image_label_image.image = input_img
            self.decrypted_image_label_image.configure(image='', text='')

    def reset_images(self):
        self.input_image_label_image.configure(image='')
        self.decrypted_image_label_image.configure(image='')

# Uncomment this section if running as a standalone application
# if __name__ == "__main__":
#     ctk.set_default_color_theme("/Users/sultanazizul/Documents/CODE/PYTHON/Keamanan Informasi/TUBES/MoonLitSky.json")
#     root = ctk.CTk()
#     app = ImageEncryptionApp(root)
#     root.mainloop()

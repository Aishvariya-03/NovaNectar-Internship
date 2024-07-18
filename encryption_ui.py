import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_text():
    key = key_entry.get().encode()
    plain_text = text_entry.get().encode()
    try:
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(plain_text)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, cipher_text.decode())
    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))

def decrypt_text():
    key = key_entry.get().encode()
    cipher_text = text_entry.get()
    try:
        cipher_suite = Fernet(key)
        decrypted_text = cipher_suite.decrypt(cipher_text.encode())
        result_entry.delete(0, tk.END)
        result_entry.insert(0, decrypted_text.decode())
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))

def generate_new_key():
    new_key = generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, new_key.decode())

# Create the main window
root = tk.Tk()
root.title("Text Encryption and Decryption")

# Create and place the widgets
tk.Label(root, text="Text:").grid(row=0, column=0, padx=10, pady=10)
text_entry = tk.Entry(root, width=50)
text_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Key:").grid(row=1, column=0, padx=10, pady=10)
key_entry = tk.Entry(root, width=50)
key_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Generate New Key", command=generate_new_key).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Encrypt", command=encrypt_text).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Decrypt", command=decrypt_text).grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=10)
result_entry = tk.Entry(root, width=50)
result_entry.grid(row=3, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()

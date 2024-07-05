import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    length = password_length.get()
    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid length (positive integer).")
        return
    
    length = int(length)
    characters = ''
    if use_lowercase.get():
        characters += string.ascii_lowercase
    if use_uppercase.get():
        characters += string.ascii_uppercase
    if use_digits.get():
        characters += string.digits
    if use_special.get():
        characters += string.punctuation
    
    if not characters:
        messagebox.showerror("No Character Set Selected", "Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy the password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Password Copied", "Password has been copied to clipboard.")

# Setting up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Password length label and entry
tk.Label(root, text="Password Length:").pack(pady=10)
password_length = tk.Entry(root)
password_length.pack(pady=5)

# Character sets checkboxes
use_lowercase = tk.BooleanVar()
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=use_lowercase).pack(anchor='w', padx=20)

use_uppercase = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=use_uppercase).pack(anchor='w', padx=20)

use_digits = tk.BooleanVar()
tk.Checkbutton(root, text="Include Digits (0-9)", variable=use_digits).pack(anchor='w', padx=20)

use_special = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters (!@#$%^&*)", variable=use_special).pack(anchor='w', padx=20)

# Generate and Copy buttons
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

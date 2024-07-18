import tkinter as tk
from tkinter import messagebox

# Caesar Cipher functions
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

# Tkinter functions
def perform_encryption():
    try:
        text = text_entry.get("1.0", "end-1c")
        shift = int(shift_entry.get())
        encrypted_text = encrypt(text, shift)
        result_text.set(encrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def perform_decryption():
    try:
        text = text_entry.get("1.0", "end-1c")
        shift = int(shift_entry.get())
        decrypted_text = decrypt(text, shift)
        result_text.set(decrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

# Tkinter GUI setup
app = tk.Tk()
app.title("Caesar Cipher Tool")

# Text input
tk.Label(app, text="Enter Text:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
text_entry = tk.Text(app, height=3, width=50)
text_entry.grid(row=0, column=1, padx=10, pady=5)

# Shift input
tk.Label(app, text="Shift Value:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
shift_entry = tk.Entry(app)
shift_entry.grid(row=1, column=1, padx=10, pady=5)

# Buttons
button_frame = tk.Frame(app)
button_frame.grid(row=2, column=1, pady=5)

encrypt_button = tk.Button(button_frame, text="Encrypt", command=perform_encryption)
encrypt_button.pack(side="left", padx=5)

decrypt_button = tk.Button(button_frame, text="Decrypt", command=perform_decryption)
decrypt_button.pack(side="left", padx=5)

# Result display
tk.Label(app, text="Result:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, wraplength=400)
result_label.grid(row=3, column=1, padx=10, pady=5)

# Start the GUI loop
app.mainloop()
